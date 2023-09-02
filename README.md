# AI_Fire_Detector

This Python script integrates the use of YOLO (You Only Look Once) object detection models for detecting fire and smoke in the screen capture. It utilizes the `telebot` library to send notifications about fire and smoke detection via Telegram.

---

<img width="1434" alt="Screenshot 2023-09-02 at 23 42 40" src="https://github.com/Zhanserkenov/AI_Fire_Detector/assets/73212575/0947c594-def2-4d6f-ba69-11290ae517a5">

--- 

<img width="1430" alt="Screenshot 2023-09-02 at 23 48 00" src="https://github.com/Zhanserkenov/AI_Fire_Detector/assets/73212575/795307da-52ab-4b0b-bd46-3bc8192b656d"> 

---

Here's a breakdown of what this script does:

1. **Import Libraries**: The script starts by importing necessary libraries such as `telebot` for working with Telegram, `YOLO` for object detection, `cv2` for image processing, `numpy` for numerical operations, `Pillow` for image handling, and `threading` for creating a separate thread to run the Telegram bot.

2. **Initialize YOLO Models**: The script initializes two YOLO models, `modelFire` and `modelSmoke`, for detecting fire and smoke, respectively. The model files are loaded from `'fire.pt'` and `'smoke.pt'`.

3. **Define Class Names**: The script defines class names for fire and smoke objects.

4. **Initialize Telegram Bot**: It initializes the Telegram bot using your bot's API token.

5. **Bot Control Flags**: There's a `bot_stopped` flag to control whether the bot should send messages or not.

6. **Telegram Message Functions**: There are functions for sending messages to Telegram. `send_telegram_message` is used to send messages to your chat ID.

7. **Command Handlers**: The script defines command handlers for `/start` and `/stop` commands. `/start` resumes the bot, and `/stop` pauses it.

8. **Telegram Bot Thread**: It creates a separate thread (`telegram_bot_thread`) for running the Telegram bot. This allows the bot to continue running while the main part of the script captures the screen and processes images.

9. **Screen Capture and Object Detection Loop**: The main loop continuously captures the screen using `ImageGrab.grab()`, converts the screenshot to a NumPy array, and resizes it to a smaller size for faster processing.

10. **Object Detection**: It runs object detection for both fire and smoke on the captured frame using the YOLO models. If objects are detected with confidence above 50%, their bounding boxes are drawn on the frame.

11. **Telegram Notifications**: When fire or smoke is detected, a message is sent to your Telegram chat using `send_telegram_message`.

12. **Display Image**: The script displays the processed image with bounding boxes using `cv2.imshow()`.

13. **Exit Condition**: Pressing the "Esc" key (`27` in OpenCV) breaks the main loop and exits the program.

14. **Cleanup**: Finally, the script cleans up by closing the OpenCV windows.

To use this script, you need to replace `"your telegram id"` with your actual Telegram chat ID and make sure you have the required Python libraries and YOLO model weights (`'fire.pt'` and `'smoke.pt'`) available.

Remember to run this script in an environment where you have the necessary libraries installed and the required permissions to capture the screen and send Telegram messages.

![Снимок экрана 2023-09-02 234339](https://github.com/Zhanserkenov/AI_Fire_Detector/assets/73212575/f1e43097-bfc1-4b00-9b65-8feeb5c365d1)



