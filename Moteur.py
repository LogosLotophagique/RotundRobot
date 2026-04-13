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

DIR_HIGH = GPIO.LOW
DIR_LOW = GPIO.HIGH

def stop():
    GPIO.output(PIN_VIT_G, GPIO.LOW)
    GPIO.output(PIN_VIT_D, GPIO.LOW)
    GPIO.output(PIN_DIR_G, DIR_LOW)
    GPIO.output(PIN_DIR_D, DIR_LOW)

def gauche():
    print('Gauche!')
    GPIO.output(PIN_VIT_G, GPIO.HIGH)
    GPIO.output(PIN_VIT_D, GPIO.HIGH)
    GPIO.output(PIN_DIR_G, DIR_LOW)
    GPIO.output(PIN_DIR_D, DIR_LOW)
    time.sleep(0.01)

def droite():
    print('Droite!')
    GPIO.output(PIN_VIT_G, GPIO.HIGH)
    GPIO.output(PIN_VIT_D, GPIO.HIGH)
    GPIO.output(PIN_DIR_G, DIR_HIGH)
    GPIO.output(PIN_DIR_D, DIR_HIGH)
    time.sleep(0.01)

def sleep_angle(angle: int):
    time.sleep((angle*1.6)/360) # 90o = 0.4

def avant():
    print('En avant!')
    GPIO.output(PIN_VIT_G, GPIO.HIGH)
    GPIO.output(PIN_VIT_D, GPIO.HIGH)
    GPIO.output(PIN_DIR_G, DIR_HIGH)
    GPIO.output(PIN_DIR_D, DIR_LOW)
    time.sleep(0.01)

def arriere():
    print('En arriere!')
    GPIO.output(PIN_VIT_G, GPIO.HIGH)
    GPIO.output(PIN_VIT_D, GPIO.HIGH)
    GPIO.output(PIN_DIR_G, DIR_LOW)
    GPIO.output(PIN_DIR_D, DIR_HIGH)
    time.sleep(0.01)

def main():
    try:
        while True:
            command = input().split(",")
            isComandTime = len(command) > 1
            commandTime = float(command[1]) if isComandTime else None
            if command[0] == "u":
                avant()
                time.sleep(commandTime if commandTime else 1)
            elif command[0] == "d":
                arriere()
                time.sleep(commandTime if commandTime else 1)
            if command[0] == "l":
                gauche()
                sleep_angle(commandTime if commandTime else 45)
            elif command[0] == "r":
                droite()
                sleep_angle(commandTime if commandTime else 45)
            stop()
    except KeyboardInterrupt:
        stop()
        pass
    except Exception as e:
        stop() # empêcher le robot d'avancer à l'infini
        GPIO.cleanup()
        raise e
    GPIO.cleanup() # Défaire le setup des GPIO

if __name__ == "__main__":
    main()