from serial.tools.list_ports import comports

def get_com_port():
    ports = comports()
    for port in ports:
        if 'USB' in port.description:
            return port.device 

if __name__ == '__main__':
    print(get_com_port())