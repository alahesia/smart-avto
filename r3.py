#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import time

red = 40

card_01 = '1662448133'

GPIO.setmode(GPIO.BOARD) # Это значит, что считаем пины по порядку с левого верхнего (3v3 - первый)
GPIO.setwarnings(False)
GPIO.setup(red, GPIO.OUT)
continue_reading = True

MIFAREReader = MFRC522.MFRC522()

while continue_reading:

# Сканируем карты - считываем их UID
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    if status == MIFAREReader.MI_OK:
        print "Card detected"

    # Read UID
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # Если считали UID, то идем дальше
    if status == MIFAREReader.MI_OK:
        # показ UID
        UIDcode = str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])
        print UIDcode

        if UIDcode == card_01:

                GPIO.output(red, 0)
                print "Door open"

        # А если карты в списке нет, то моргаем и пищим
        else:
                GPIO.output(red, 1)
                time.sleep(0.05)

                print "Unrecognised Card"
GPIO.cleanup()