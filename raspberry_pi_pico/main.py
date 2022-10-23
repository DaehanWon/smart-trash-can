from machine import Pin, PWM
import time
import utime

is_opened = False

trig1 = Pin(4, Pin.OUT)
echo1 = Pin(5, Pin.IN)
trig2 = Pin(6, Pin.OUT)
echo2 = Pin(7, Pin.IN)

r = Pin(0, Pin.OUT)
y = Pin(1, Pin.OUT)
g = Pin(2, Pin.OUT)

servo = PWM(Pin(3))
servo.freq(50)

def openlid():
    servo.duty_u16(2800)
    
def closelid():
    servo.duty_u16(1420)

def ultra1():
   trig1.low()
   utime.sleep_us(2)
   trig1.high()
   utime.sleep_us(5)
   trig1.low()
   while echo1.value() == 0:
       signaloff = utime.ticks_us()
   while echo1.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   return distance
   
def ultra2():
   trig2.low()
   utime.sleep_us(2)
   trig2.high()
   utime.sleep_us(5)
   trig2.low()
   while echo2.value() == 0:
       signaloff = utime.ticks_us()
   while echo2.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   return distance
   
closelid()

while True:
    d1 = ultra1()
    #print(d1)
    if d1 < 10:
        if not is_opened:
            is_opened = True
            openlid()
        for i in range(2):
            r.on()
            y.off()
            g.off()
            time.sleep(0.25)
            r.off()
            y.on()
            g.off()
            time.sleep(0.25)
            r.off()
            y.off()
            g.on()
            time.sleep(0.25)
        r.off()
        y.off()
        g.off()
    else:
        if is_opened:
            is_opened = False
            closelid()
            time.sleep(0.5)
        d2 = ultra2()
        print(d2)
        time.sleep(0.5)
        if d2 < 8:
            r.off()
            y.off()
            g.on()
        elif d2 < 10 :
            r.off()
            y.on()
            g.off()
        else:
            r.on()
            y.off()
            g.off()
