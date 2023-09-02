from telebot import TeleBot
from ultralytics import YOLO
import cvzone
import cv2
import math
import numpy as np
from PIL import ImageGrab
import threading

modelFire = YOLO('fire.pt')
modelSmoke = YOLO('smoke.pt')

fireName = ['fire']
smokeName = ['smoke']

bot = TeleBot("5929775332:AAH-wiOg471WCJbYzsWsLnXfW4NgKTNBsf4")

bot_stopped = False

def send_telegram_message(message):
    if not bot_stopped:
        bot.send_message("573795843", message)

@bot.message_handler(commands=['stop'])
def stop_bot(message):
    global bot_stopped
    bot_stopped = True
    bot.send_message(message.chat.id, "Бот приостановлен. Для возобновления отправки сообщений используйте /start")

@bot.message_handler(commands=['start'])
def start_bot(message):
    global bot_stopped
    bot_stopped = False
    bot.send_message(message.chat.id, "Бот возобновил работу.")

def start_telegram_bot():
    bot.polling()

telegram_bot_thread = threading.Thread(target=start_telegram_bot)
telegram_bot_thread.start()

while True:
    if not bot_stopped:
        screenshot = ImageGrab.grab(bbox=(0, 0, 1920 // 2, 1080))
        frame = np.array(screenshot)

        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame = cv2.resize(frame, (640, 480))

        resultFire = modelFire(frame, stream=True)
        resultSmoke = modelSmoke(frame, stream=True)

        for info in resultFire:
            boxes = info.boxes
            for box in boxes:
                confidence = box.conf[0]
                confidence = math.ceil(confidence * 100)
                Class = int(box.cls[0])
                if confidence > 50:
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
                    cvzone.putTextRect(frame, f'{fireName[Class]} {confidence}%', [x1 + 8, y1 + 100],
                                       scale=1.5, thickness=2)

                    send_telegram_message(f"Обнаружен огонь: {fireName[Class]} с вероятностью {confidence}%")

        for info in resultSmoke:
            boxes = info.boxes
            for box in boxes:
                confidence = box.conf[0]
                confidence = math.ceil(confidence * 100)
                Class = int(box.cls[0])
                if confidence > 50:
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
                    cvzone.putTextRect(frame, f'{smokeName[Class]} {confidence}%', [x1 + 8, y1 + 100],
                                       scale=1.5, thickness=2)

                    send_telegram_message(f"Обнаружен дым: {smokeName[Class]} с вероятностью {confidence}%")

        cv2.imshow('frame', frame)
        cv2.waitKey(1)

        if cv2.waitKey(1) == 27:
            break

cv2.destroyAllWindows()