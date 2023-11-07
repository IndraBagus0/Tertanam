import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

# Konfigurasi pin untuk motor servo
servo_pin = 18  # Ganti dengan pin yang sesuai

# Inisialisasi GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Inisialisasi pembaca RFID
reader = SimpleMFRC522()

try:
    while True:
        text = input('New data: ')
        print("Tempelkan kartu untuk menggerakkan motor servo")
        id, _ = reader.read()

        if text == str(id):
            print("Kartu cocok. Motor servo bergerak.")
            # Posisikan motor servo (misalnya, 90 derajat)
            GPIO.output(servo_pin, GPIO.HIGH)
            time.sleep(1)  # Waktu servo bergerak
            GPIO.output(servo_pin, GPIO.LOW)
        else:
            print("Kartu tidak cocok. Tidak ada aksi yang diambil.")

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
