from core.network_manager import NetworkHandler
from core.hand_detector import HandTracker
from datetime import datetime
from config import Config
import pyautogui
import threading
import time
import cv2
import os

class FistBump():
    def __init__(self, cam=0):
        self.state, self.state2, self.time_flag = True, True, None
        self.config = Config(log_header="main.py")
        self.network = NetworkHandler()
        self.logger = self.config.logger
        self.cam = cam
        if not os.path.isdir("screenshots"):
            os.mkdir("screenshots")
        if not os.path.isdir("receives"):
            os.mkdir("receives")

    def start(self):
        tracker = HandTracker()
        cap = cv2.VideoCapture(self.cam)

        while True:
            success, img = cap.read()
            if not success:
                break

            img = tracker.find_hands(img)

            landmark_list = tracker.find_position(img)

            if landmark_list:
                is_open = tracker.is_hand_open(landmark_list)
                status_r = True if is_open else False

                decision = self.status_checker(status_r)

                if decision == "send":
                    timestamp = datetime.now().strftime("%Y-%m-%d(%H_%M_%S,%f)")[:-3]
                    filename = f"{self.screenshots_path}\\screenshots\\screenshot_{timestamp}.png"
                    self.save_screenshot(filename)
                    try:
                        send_thread = threading.Thread(target=self.network.send_file, args=(filename, ))
                        send_thread.start()
                    except Exception as e:
                        self.logger.error(f"There was an error while sending. | Error: {e}")
                        # print(f"There was an error while sending. | Error: {e}")

                elif decision == "receive":
                    try:
                        receive_thread = threading.Thread(target=self.network.receive_file)
                        receive_thread.start()
                    except Exception as e:
                        self.logger.error(f"There was an error while receiving. | Error: {e}")
                        # print(f"There was an error while receiving. | Error: {e}")

                cv2.putText(img, f"El Durumu: {decision}", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow("El Takibi", img)
            if cv2.waitKey(1) & 0xFF == 27:
                break

        cap.release()
        cv2.destroyAllWindows()

    def status_checker(self, status_r):
        if status_r == True and self.state == True:
            if self.time_flag is None:
                self.time_flag = time.time()
            if time.time() - self.time_flag >= 1:
                self.state = False

        elif status_r == False and self.state == False:
            self.time_flag = None
            self.state = True
            return "send"

        if status_r == True and self.state2 == False:
            self.state2 = True
            return "receive"

        elif status_r == False and self.state2 == True:
            self.state2 = False

    def save_screenshot(self, filename):
        try:
            screenshot = pyautogui.screenshot()
            screenshot.save(filename)
            self.logger.info(f"[SCREENSHOT] Screenshot saved as '{filename}'")
            # print(f"[SCREENSHOT] Screenshot saved as '{filename}'")
        except Exception as e:
            self.logger.error(f"[SCREENSHOT] Error saving screenshot: {e}")
            # print(f"[SCREENSHOT] Error saving screenshot: {e}")

if __name__ == "__main__":
    shake_hand = FistBump(0)
    shake_hand.start()