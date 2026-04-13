import threading
import Bras, Camera, IR_Sensor, Moteur

def main():
    try:
        thread_bras = threading.Thread(target=Bras.main)
        thread_cam = threading.Thread(target=Camera.main)
        thread_ir = threading.Thread(target=IR_Sensor.main)
        thread_moteur = threading.Thread(target=Moteur.main)

        thread_bras.start()
        thread_cam.start()
        thread_ir.start()
        thread_moteur.start()
    except KeyboardInterrupt:
        print("Main Program stopped by User")


if __name__ == "__main__":
    main()
else:
    raise RuntimeError("Main file cannot be run as module!")