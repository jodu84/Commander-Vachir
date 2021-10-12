import serial
from serial.tools import list_ports
from serial import SerialException
import time
import sys

def main():
    port = list_ports.comports()
    print(port)
    
if __name__ == '__main__':
    main()