import datetime
import time

import io
import serial
import errno
from colorama import Fore, Back, Style
from time import sleep
import logging
import csv

import serialLayer as boxFunctions


boxFunctions.openportRelayBox()
boxFunctions.openRelayBox_rele_1()
sleep(1)
for aud in range(10):
    boxFunctions.openRelayBox_rele_1()
    boxFunctions.openRelayBox_rele_2()
    sleep(1)


serial.closeportRelayBox()




