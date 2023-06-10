import time
from grove.factory import Factory

buzzer = Factory.getGpioWrapper("Buzzer", 12)
while True:
    buzzer.on()
    time.sleep(1)
    buzzer.off()
    time.sleep(3)
