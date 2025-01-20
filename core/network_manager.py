from datetime import datetime
from config import Config
from time import sleep
import threading
import socket

class NetworkHandler:
    def __init__(self, receives_path=""):
        self.config = Config(log_header="network_manager.py")
        self.receive_path = receives_path
        self.logger = self.config.logger

    def broadcast_ip(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        server_address = ('', 9434)
        sock.bind(server_address)

        response = 'pfg_ip_response_serv'

        try:
            self.logger.info("[SERVER] Server is waiting for a single broadcast message...")

            data, address = sock.recvfrom(4096)
            data = data.decode('UTF-8')

            if data == 'pfg_ip_broadcast_cl':
                self.logger.info(f"[SERVER] Received broadcast from {address}")

                sock.sendto(response.encode(), address)
                self.logger.info(f"[SERVER] Response sent to {address}")

                sock.settimeout(5)
                ack, ack_address = sock.recvfrom(4096)
                ack = ack.decode('UTF-8')

                if ack == 'pfg_ack_cl':
                    self.logger.info(f"[SERVER] Acknowledgment received from {ack_address}. Server is stopping.")
                else:
                    self.logger.error("[SERVER] Unexpected acknowledgment message. Server is stopping.")
        except socket.timeout:
            self.logger.error("[SERVER] Timeout: No acknowledgment received. Server is stopping.")
        except Exception as e:
            self.logger.error(f"[SERVER] Error occurred: {e}")
        finally:
            sock.close()
            self.logger.info("[SERVER] Server has stopped.")

    def send_file(self, filename):
        conn = None
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind(("0.0.0.0", 5000))
            server_socket.listen(1)
            self.logger.info("[SERVER] Waiting for connection...")

            threading.Thread(target=self.broadcast_ip, daemon=True).start()

            conn, addr = server_socket.accept()
            self.logger.info(f"[SERVER] Connection established with {addr}")

            with open(filename, "rb") as file:
                while chunk := file.read(1024):
                    conn.send(chunk)

            self.logger.info("[SERVER] File sent successfully.")
        except Exception as e:
            self.logger.error(f"[SERVER] Error: {e}")
        finally:
            if conn:
                conn.close()
            server_socket.close()
            self.logger.info("[SERVER] Connection closed.")

    def discover_server(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.settimeout(5)

        server_address = ('255.255.255.255', 9434)
        message = 'pfg_ip_broadcast_cl'

        try:
            while True:
                self.logger.info(f"[CLIENT] Sending broadcast message: {message}")
                sock.sendto(message.encode(), server_address)

                self.logger.info("[CLIENT] Waiting for a response...")
                try:
                    data, server = sock.recvfrom(4096)
                    if data.decode('UTF-8') == 'pfg_ip_response_serv':
                        self.logger.info("[CLIENT] Received response from server.")
                        self.logger.info(f"[CLIENT] Server IP: {server[0]}")
                        return server
                except socket.timeout:
                    self.logger.warning("[CLIENT] No response received. Retrying...")
        finally:
            self.logger.info("[CLIENT] Closing socket...")
            sock.close()

    def receive_file(self):
        client_socket = None
        try:
            server_ip = self.discover_server()
            self.logger.info(f"[CLIENT] Server IP discovered: {server_ip}")

            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((server_ip[0], 5000))

            timestamp = datetime.now().strftime("%Y-%m-%d(%H_%M_%S,%f)")[:-3]
            filename = f"receives\\received_{timestamp}.png"

            with open(filename, "wb") as file:
                while chunk := client_socket.recv(1024):
                    file.write(chunk)

            self.logger.info("[CLIENT] File received successfully.")
        except Exception as e:
            self.logger.error(f"[CLIENT] Error: {e}")
        finally:
            if client_socket:
                client_socket.close()
                self.logger.info("[CLIENT] Connection closed.")
