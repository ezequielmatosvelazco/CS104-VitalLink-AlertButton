import time
import RPi.GPIO as GPIO
import requests
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print("Alert button monitoring system is now active. Press Ctrl+C to stop.")


button_pressed = False
try:
	while True:
		if GPIO.input(7) == GPIO.HIGH:
			print("Someone pressed the alert button!")
			requests.post("https://api.telegram.org/bot8697763524:AAHEJaJIIlfgCRUdnSEHuM9X-v2i3zn71T8/sendMessage", json={"chat_id": "8378412767", "text": "Someone pressed the alert button!"})
			button_pressed = True
		elif GPIO.input(7) == GPIO.LOW:
			button_pressed = False
		time.sleep(0.1)

except KeyboardInterrupt:
	print("\nMonitoring stopped.")
	GPIO.cleanup()
