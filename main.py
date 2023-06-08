import pymodbus
from pymodbus.pdu import ModbusRequest
from pymodbus.client.serial import ModbusSerialClient as ModbusClient
#initialize a serial RTU client instance
from pymodbus.transaction import ModbusRtuFramer

client = ModbusClient(method = 'rtu', port='COM3', stopbits = 1, bytesize = 8, parity = 'E' , baudrate= 19200)

#Connect to the serial modbus server
connection = client.connect()
print(connection)

read_mls=client.read_input_registers(address=192,count=11,slave=10)
print(read_mls.registers)