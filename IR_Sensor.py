import RPi.GPIO as GPIO
import time

# Use BCM numbering
GPIO.setmode(GPIO.BCM)

# Sensor pins
IR_SENSOR_1 = 17
IR_SENSOR_2 = 23

# Setup pins
GPIO.setup(IR_SENSOR_1, GPIO.IN)
GPIO.setup(IR_SENSOR_2, GPIO.IN)

# Cooldown time in seconds
COOLDOWN = 5

def main():
    # Store last trigger times
    last_trigger_1 = 0
    last_trigger_2 = 0
    print("IR Sensor Monitoring with 5s Cooldown (CTRL+C to exit)")

    try:
        while True:
            current_time = time.time()

            sensor1_state = GPIO.input(IR_SENSOR_1)
            sensor2_state = GPIO.input(IR_SENSOR_2)

            # Sensor 1 detection (LOW = detected)
            if sensor1_state == 0 and (current_time - last_trigger_1) > COOLDOWN:
                print("Object detected on Sensor 1 (GPIO 17)")
                last_trigger_1 = current_time

            # Sensor 2 detection (LOW = detected)
            if sensor2_state == 0 and (current_time - last_trigger_2) > COOLDOWN:
                print("Object detected on Sensor 2 (GPIO 23)")
                last_trigger_2 = current_time

            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Program stopped by User")

    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()