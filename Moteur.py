import RPi.GPIO as GPIO
import time

#todo: tester et personaliser
# Utilisation de la numérotation BCM (mode GPIO number plutôt que PIN number)
GPIO.setmode(GPIO.BCM)

# Choisir les GPIO pour les signaux
PIN_DIR_D = 17 # Bleu
PIN_VIT_G = 22 # Jaune
PIN_VIT_D = 23 # Brun
PIN_DIR_G = 27 # Mauve
GPIO.setup(PIN_DIR_D, GPIO.OUT)
GPIO.setup(PIN_VIT_G, GPIO.OUT)
GPIO.setup(PIN_VIT_D, GPIO.OUT)
GPIO.setup(PIN_DIR_G, GPIO.OUT)

def stop():
    GPIO.output(PIN_VIT_G, GPIO.LOW)
    GPIO.output(PIN_VIT_D, GPIO.LOW)
    GPIO.output(PIN_DIR_G, GPIO.LOW)
    GPIO.output(PIN_DIR_D, GPIO.LOW)

def gauche():
    print('Gauche!')
    GPIO.output(PIN_VIT_G, GPIO.HIGH)
    GPIO.output(PIN_VIT_D, GPIO.HIGH)
    GPIO.output(PIN_DIR_G, GPIO.LOW)
    GPIO.output(PIN_DIR_D, GPIO.LOW)
    time.sleep(0.01)

def droite():
    print('Droite!')
    GPIO.output(PIN_VIT_G, GPIO.HIGH)
    GPIO.output(PIN_VIT_D, GPIO.HIGH)
    GPIO.output(PIN_DIR_G, GPIO.HIGH)
    GPIO.output(PIN_DIR_D, GPIO.HIGH)
    time.sleep(0.01)

def enAvant():
    print('En avant!')
    GPIO.output(PIN_VIT_G, GPIO.HIGH)
    GPIO.output(PIN_VIT_D, GPIO.LOW)
    GPIO.output(PIN_DIR_G, GPIO.HIGH)
    GPIO.output(PIN_DIR_D, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(PIN_VIT_G, GPIO.HIGH)
    GPIO.output(PIN_VIT_D, GPIO.HIGH)
    GPIO.output(PIN_DIR_G, GPIO.HIGH)
    GPIO.output(PIN_DIR_D, GPIO.LOW)
    time.sleep(0.4)
    GPIO.output(PIN_VIT_G, GPIO.HIGH)
    GPIO.output(PIN_VIT_D, GPIO.LOW)
    GPIO.output(PIN_DIR_G, GPIO.HIGH)
    GPIO.output(PIN_DIR_D, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(PIN_VIT_G, GPIO.HIGH)
    GPIO.output(PIN_VIT_D, GPIO.HIGH)
    GPIO.output(PIN_DIR_G, GPIO.HIGH)
    GPIO.output(PIN_DIR_D, GPIO.LOW)
    time.sleep(0.4)
    GPIO.output(PIN_VIT_G, GPIO.HIGH)
    GPIO.output(PIN_VIT_D, GPIO.LOW)
    GPIO.output(PIN_DIR_G, GPIO.HIGH)
    GPIO.output(PIN_DIR_D, GPIO.LOW)
    time.sleep(0.1)

def enArriere():
    print('En arriere!')
    GPIO.output(PIN_VIT_G, GPIO.HIGH)
    GPIO.output(PIN_VIT_D, GPIO.HIGH)
    GPIO.output(PIN_DIR_G, GPIO.LOW)
    GPIO.output(PIN_DIR_D, GPIO.HIGH)
    time.sleep(1)

try:
    while True:
        gauche()
        stop()
except KeyboardInterrupt:
    pass

GPIO.cleanup() # Défaire le setup des GPIO