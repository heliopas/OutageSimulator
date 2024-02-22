import datetime
import time

import io
import serial
import errno
from colorama import Fore, Back, Style
from time import sleep
import logging
import csv

#comm ports var
comRelayBox = 'COM118'
#global vars
global comportRelayBox

def openportRelayBox():
    global comportRelayBox
    try:
        comportRelayBox = serial.Serial(port=comRelayBox, baudrate=9600, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE
                                        , timeout= 5, rtscts=False, xonxoff=False, bytesize=serial.EIGHTBITS)
    except serial.SerialException as e:
        logging.error("Error during open port RelayBox: %s" % e)

def closeportRelayBox():
    global comportRelayBox
    comportRelayBox.close()

def openRelayBox_rele_1():
    global comportRelayBox
    try:
        comportRelayBox.write(b"1\r")
    except serial.SerialException as e:
        logging.error("Error during open RelayBox_ch1: %s" % e)

def openRelayBox_rele_2():
    global comportRelayBox
    try:
        comportRelayBox.write(b"2\r")
        logging.info("Rele open")
    except serial.SerialException as e:
        logging.error("Error during open RelayBox_ch1: %s" % e)

def openRelayBox_rele_3():
    global comportRelayBox
    try:
        comportRelayBox.write(b"3\r")
        logging.info("Rele open")
    except serial.SerialException as e:
        logging.error("Error during open RelayBox_ch1: %s" % e)

def openRelayBox_rele_4():
    global comportRelayBox
    try:
        comportRelayBox.write(b"4\r")
        logging.info("Rele open")
    except serial.SerialException as e:
        logging.error("Error during open RelayBox_ch1: %s" % e)