from gpiozero import PWMLED, DistanceSensor
import time

LED = PWMLED(18)
ultrasonic = DistanceSensor(
    echo=13, trigger=19, max_distance=0.50)

try:
    LED.off()
    while True:
        distance = ultrasonic.value * 0.50
        print(f"Distance is{distance: 1.2f} units")
        dutycycle = round(1.0 - distance/0.50, 1)
        if dutycycle < 0:
            dutycycle = 0.0
        LED.value = dutycycle
        time.sleep(1.5)
except KeyboardInterrupt as key_pressed:
        LED.off()
        ultrasonic.close()
