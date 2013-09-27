from time import sleep
from board import Board
from led import Led
from arm import Arm
from ring import Ring

def test(str):
    sleep(2)
    print "Testing" + str
    pg.off()

LOW_BRIGHTNESS = 1
BRIGHTNESS = 100
BLIND = 255
pg = Board()

test("all")
pg.all(BRIGHTNESS)

test("led")
for i in range(Led.NUMBER):
    pg.off()
    pg.led(i+1, BRIGHTNESS)
    sleep(2)
test("arm")
for i in range(Arm.NUMBER):
    pg.off()
    pg.arm(i+1, BRIGHTNESS)
    sleep(2)

test("color")
for i in range(Ring.NUMBER):
    pg.off()
    pg.color(i+1, BRIGHTNESS)
    sleep(2)

test("buffer...update")
pg.buffer([1,2,3,5,8,13], LOW_BRIGHTNESS)
pg.buffer([4,6,7,9,10,11,12,15,16,17,18], BRIGHTNESS)

test("light")
pg.ledset([1,3,7,11,18], BRIGHTNESS)

test("buffer...update")
sleep(2)
pg.update()

test("dump...restore")
pg.ledset([1, 5, 2, 8, 13], BRIGHTNESS)
pg.buffer([3, 1, 18], BRIGHTNESS)
backup = pg.dump()
sleep(2)
pg.off()
sleep(2)
pg.ledset([1,2,3], BRIGHTNESS)
sleep(2)
pg.restore(backup)
sleep(2)

print "Exit..."
sleep(2)
pg.off()
