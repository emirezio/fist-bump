# Fist-Bump

Fist-Bump is a Python-based implementation inspired by Huawei's hand-gesture file-sharing feature. The goal of this project is to enable users to share files via hand gestures detected by a webcam or video feed. The latest updates include enhanced directory management, improved modularity, and a more robust implementation of multithreading for sending and receiving files. Your contributions and ideas are highly welcomed to enhance this project further.

---

## Features

- **Hand Gesture Detection**: Uses OpenCV and MediaPipe to detect whether a hand is open or closed.
- **File Sharing**:
  - **Send Files**: Automatically takes a screenshot and sends it when a specific gesture (closed fist) is detected.
  - **Receive Files**: Listens for incoming files when another gesture (open hand) is detected.
- **Directory Management**: Automatically creates directories for saving screenshots and received files.
- **Multithreaded Design**: Sending and receiving operations run in separate threads for efficiency.
- **Logging**: Configurable logging to track application behavior and errors.

---

## Requirements

- Python 3.7+
- OpenCV
- PyAutoGUI
- MediaPipe

### Install Dependencies
To install the required dependencies, run the following command:
```bash
pip install -r requirements.txt
```

---

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-github-username>/fist-bump.git
   cd fist-bump
   ```

2. Run the main script:
   ```bash
   python main.py
   ```

3. By default, the script uses your primary webcam. You can modify the `cam` parameter in the `FistBump` class to use a different video source.

---

## How It Works

- The program uses a `HandTracker` class to identify hand landmarks and detect the openness or closedness of the hand.
- Based on the detected gestures:
  - A **closed fist** triggers the program to take a screenshot and send it to a predefined recipient.
  - An **open hand** triggers the program to listen for incoming files.
- The `NetworkHandler` handles the sending and receiving of files over a local network.
- Logging and directory management are handled using the `Config` class for better modularity and debugging.

---

## Challenges & Future Goals

While the basic functionality is in place, there are areas where this project can be improved:

### Security
- **Encryption**: Currently, file transfers lack encryption. Implementing secure protocols (e.g., TLS or file encryption) is crucial.
- **Authentication**: Add mechanisms to ensure that files are only shared between trusted parties.

### Reliability
- **Error Handling**: Improve exception handling for network issues, file system errors, etc.
- **Robust Gesture Detection**: Enhance accuracy to reduce false positives.

### Expandability
- **New Features**: Explore additional gestures or extend functionality to include voice commands.
- **Cross-Platform Compatibility**: Ensure smooth operation on different operating systems and hardware configurations.

---

## Contributing

Contributions are highly encouraged! Here’s how you can help:

1. Fork the repository.
2. Create a branch for your feature or fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a detailed explanation of your changes.

---

## Contact

If you have any questions or ideas, feel free to open an issue or contact me directly. Let’s make Fist-Bump better together!

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Acknowledgments

Special thanks to the open-source community and everyone who inspired this project by contributing to gesture recognition and file-sharing technologies. Your input is invaluable!

