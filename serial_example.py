import serial
import serial.tools.list_ports
import struct

# Mac ports, for windows you have to find the ports yourself
frdm_port = "COM3"

Start = b'\x16'
SYNC = b'\x22'
Fn_set = b'\x55'
ATR_AMP = struct.pack("B", 1)
ATR_PW = struct.pack("B", 1)
MODE = struct.pack("B", 2)
VENT_AMP = struct.pack("B", 1)
VENT_PW = struct.pack("B", 1)
ARP = struct.pack("B", 1)
VRP = struct.pack("B", 1)
LRL =struct.pack("B", 1)
Activity_Threshold =struct.pack("B", 1)
Response_Factor =struct.pack("B", 1)
Recovery_Time = struct.pack("B", 1)
Max_Sensor_Rate =struct.pack("B",1)
Reaction_Time = struct.pack("B",1)

Signal_Set = Start + Fn_set + ATR_AMP + ATR_PW + MODE + VENT_AMP+VENT_PW+ARP+VRP+LRL+Activity_Threshold+Response_Factor+Recovery_Time+Max_Sensor_Rate+Reaction_Time
Signal_echo = Start + SYNC + ATR_AMP +ATR_PW+MODE+VENT_AMP+VENT_PW+ARP+VRP+LRL+Activity_Threshold+Response_Factor+Recovery_Time+Max_Sensor_Rate+Reaction_Time

with serial.Serial(frdm_port, 115200) as pacemaker:
    pacemaker.write(Signal_Set)

with serial.Serial(frdm_port, 115200) as pacemaker:
    pacemaker.write(Signal_echo)
    data = pacemaker.read(13)
    RATR_AMP = data[0]
    RATR_PW = data[1]
    RMODE = data[2]
    RVENT_AMP = data[3]
    RVENT_PW = data[4]
    RARP = data[5]
    RVRP = data[6]
    RLRL =data[7]
    RActivity_Threshold =data[8]
    RResponse_Factor =data[9]
    RRecovery_Time = data[10]
    RMax_Sensor_Rate =data[11]
    RReaction_Time = data[12]

print("From the board:")
print("ATR_AMP = ", RATR_AMP)
print("ATR_PW = ", RATR_PW)
print("MODE = ", RMODE)
print("VENT_AMP = ",  RVENT_AMP)
print("VENT_PW = ", RVENT_PW)
print("ARP = ", RARP)
print("VRP = ",  RVRP)
print("LRL = ", RLRL)
print("ACTIVITY_THRESHOLD = ", RActivity_Threshold)
print("RESPONSE_FACTOR = ",  RResponse_Factor)
print("Recovery_TIME = ", RRecovery_Time)
print("Max_Sensor_Rate = ",  RMax_Sensor_Rate)
print("Reaction_Time = ", RReaction_Time)
