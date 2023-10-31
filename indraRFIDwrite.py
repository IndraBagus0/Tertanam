import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
try:
    text = input('New data: ')
    print("Letakkan kartu untuk isi")
    reader.write(text)
    print("Terisi")
finally:
    GPIO.cleanup()
