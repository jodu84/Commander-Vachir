import serial
from serial.tools import list_ports
from serial import SerialException
import time

class CoboltLaser():
    
    def __init__(self, port=None, serialnumber=None, baudrate=11500):
        self.serialnumber = serialnumber
        self.status = None
        self.port = port
        self.modelnumber = None
        self.baudrate=baudrate
        self.address=None
        self.connect()

    def connect(self):
       
        if self.port != None:
            print('Port known!')
            try:
                self.address = serial.Serial(self.port, self.baudrate, timeout=1)
                self.serialnumber = self.send_cmd('sn?')
            except Exception as error:
                self.address = None
                raise SerialException (f'{self.port}, not accessible. Error {error}')
        
        elif self.serialnumber != None:
            print('Serialnumber known!')
            
            ports = list_ports.comports()
            for port in ports:
                
                self.port = port.device
                
                try:
                    self.address = serial.Serial(self.port,baudrate=self.baudrate)
                    sn = self.send_cmd('sn?')
                    self.address.close()
                    
                    print([sn, self.serialnumber])
                    
                    if sn == self.serialnumber:
                        self.address = serial.Serial(self.port,baudrate=self.baudrate)
                        self.status = 'Connected'
                        break
                    else:
                        self.port = None
                        
                except:
                    pass
                
            if self.port == None:
                self.status = 'disconnected'
                                
        return
    
    def _timeDiff(self, time_start):
        
        time_diff = (time.perf_counter() - time_start)
        return(time_diff)
    
    def send_cmd(self, msg, timeout=1):
        
        time_start = time.perf_counter()
        msg += '\r'
        
        try:
            self.address.write(msg.encode())
            print(f'{msg.encode()} sent!')
        except:
            return 'Syntax ERROR: write failed'
            
        time_stamp = 0
        
        while (time_stamp < timeout):
            try:
                rec_str = self.address.readline().decode().replace('\r\n', '')
                return rec_str
            except:
                time_stamp = self._timeDiff(time_start)
                
        return 'Syntax ERROR: no message recieved'
    
    def disconnect(self):
        
        if self.address != None:
                self.address.close()
                self.serialnumber = None
                self.modelnumber = None
                
                print(f'Connection at {self.port} closed')