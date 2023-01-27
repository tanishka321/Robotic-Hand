from gpiozero import AngularServo
from time import sleep

from gpiozero.pins.pigpio import PiGPIOFactory
factory=PiGPIOFactory()

s1 = AngularServo(4, min_pulse_width=0.0006, max_pulse_width=0.0023,pin_factory=factory)

s2 = AngularServo(17, min_pulse_width=0.0006, max_pulse_width=0.0023,pin_factory=factory)

s3 = AngularServo(22, min_pulse_width=0.0006, max_pulse_width=0.0023,pin_factory=factory)

s4 = AngularServo(23, min_pulse_width=0.0006, max_pulse_width=0.0023,pin_factory=factory)

s5 = AngularServo(24, min_pulse_width=0.0006, max_pulse_width=0.0023,pin_factory=factory)



while True:
    
    if r1 < 1:
        s1.angle = -90
    else:
        s1.angle = 90


    if r2 < 1:
        s2.angle = -90
    else:
        s2.angle = 90


    if r3 < 1:
        s3.angle = -90
    else:
        s3.angle = 90


    if r4 < 1.4:
        s4.angle = -90
    else:
        s4.angle = 90


    if r5 < 1.4:
        s5.angle = -90
    else:
        s5.angle = 90



