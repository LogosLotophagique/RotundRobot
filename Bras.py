import RPi.GPIO as GPIO
import time

#todo: tester et personaliser
# Utilisation de la numérotation BCM (mode GPIO number plutôt que PIN number)
GPIO.setmode(GPIO.BCM)

# Choisir les GPIO pour les signaux
SERVO_PINC = 5 # coude
SERVO_PINT = 6 # torse
SERVO_PINB = 13 # bras
MAGNET_PIN = 12
THRESHOLD_TURN = 25

GPIO.setup(SERVO_PINC, GPIO.OUT)
GPIO.setup(SERVO_PINT, GPIO.OUT)
GPIO.setup(SERVO_PINB, GPIO.OUT)
GPIO.setup(MAGNET_PIN, GPIO.OUT)

# Création des PWM à 50 Hz (standard servo)
pwmC = GPIO.PWM(SERVO_PINC, 50)
pwmC.start(0)
pwmT = GPIO.PWM(SERVO_PINT, 50)
pwmT.start(0)
pwmB = GPIO.PWM(SERVO_PINB, 50)
pwmB.start(0)

def set_angle(*args: list):
    """
    args: lists of [angle_target, angle_init, steps, pwm] OR [angle_target, pwm]
    """
    for arg in args:
        print(*arg)
        if len(arg) == 4:
            angle_target, angle_init, steps, pwm = arg
            for i in range(angle_init, angle_target, (angle_target-angle_init)/steps):
                # Conversion angle → DutyCycle
                duty = 2 + (i / 18)  # approx pour SG90 (0°=2%, 90°=7%, 180°=12%)
                pwm.ChangeDutyCycle(duty)
                time.sleep(0.01)
        else: 
            angle_target, pwm = arg
        duty = 2 + (angle_target / 18)  # approx pour SG90 (0°=2%, 90°=7%, 180°=12%)
        pwm.ChangeDutyCycle(duty)
        time.sleep(0.01)
    time.sleep(0.7)  # temps pour que le(s) servo(s) bouge(nt)
    for arg in args:
        pwm.ChangeDutyCycle(0)  # éviter vibrations
    time.sleep(0.01)

def idle():
    set_angle([0, pwmC])
    set_angle([90, pwmT])
    set_angle([0, pwmB])

def left():
    set_angle([180-THRESHOLD_TURN, pwmT])
    time.sleep(0.1) # 100ms juste pour dire qu'on ne recommence pas tout de suite

def right():
    set_angle([0+THRESHOLD_TURN, pwmT])
    time.sleep(0.1)

def take(up_angle:int=0, release=False):
    set_angle([180-up_angle, 0, 10, pwmB], [85+up_angle//45, 0, 10, pwmC])
    GPIO.output(MAGNET_PIN, GPIO.LOW if release else GPIO.HIGH) # aimant ON/OFF
    time.sleep(0.1)
    set_angle([0, 180-up_angle, 10, pwmB])
    time.sleep(0.1)

def main():
    try:
        while True:
            idle()
            time.sleep(2) 
            take()
            left()
            take(release=True)
            right()
            take()
    except KeyboardInterrupt:
        pass

    pwmC.stop()
    pwmT.stop()
    pwmB.stop()
    GPIO.cleanup() # Défaire le setup des GPIO

if __name__ == "__main__":
    main()