import socket 
import binascii
from datetime import datetime
from datetime import timedelta


client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client1.connect(('129.6.15.27',37)) #start connection with server1 at port 37
time1 = client1.recv(32)
client1.close()
time1 = bin(int(binascii.hexlify(time1),16))[2:] #convert into binary string
time1 = int(time1,2) #convert string into intiger decimal which gives us number of seconds

client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client2.connect(('132.163.97.7',37)) #start connection with server1 at port 37
time2 = client2.recv(32)
client2.close()
time2 = bin(int(binascii.hexlify(time2),16))[2:] #convert into binary string
time2 = int(time2,2)

x = datetime(1900,1,1,0,0,0)  #set a date time at 1900 january 1 at 12AM
x1 = x + timedelta(seconds=time1) #add number of seconds to the date to get current time
x2 = x + timedelta(seconds=time2)

print("Server 1\n","IP address: 129.6.15.27\n","Server time:", x1, "UTC")
print("Server 2\n","IP address: 128.138.140.44\n","Server time:", x2,"UTC")
print("Time difference between the two servers is:",abs(time2-time1))