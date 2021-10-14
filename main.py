from serial.tools import list_ports

from CoboltLaser import CoboltLaser

def main():
    
    # Mock test code
    ports = list_ports.comports()
    
    for port in ports:
        laser = CoboltLaser(port=port.device)
        print(laser.serialnumber)
        laser.disconnect()

    laser = CoboltLaser(serialnumber=16811)
    print(laser.port.device)
    laser.disconnect()
    
if __name__ == '__main__':
    main()