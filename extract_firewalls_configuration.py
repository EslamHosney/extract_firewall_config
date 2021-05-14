#import texttable
#import netmiko
from netmiko import ConnectHandler
##from texttable import Texttable
##import paramiko
#import os
#import getpass
#import sys
#import telnetlib

def ReadFile(inFile):
    with open(inFile, "r") as f:
        content = f.readlines()   
    content = [x.strip() for x in content]
    return (content)

def Parse_FW_configuration(FW):
    
    FW_name     = FW[0]
    FW_IP       = FW[1]
    FW_Platform = FW[2]
    FW_Username = FW[3]
    FW_Password = FW[4]    
    
    #To be Tested
    if(FW_Platform == 'Fortinet'):
            device = ConnectHandler(device_type='fortinet', ip= FW_IP , username=FW_Username, password=FW_Password)
            device.send_command_timing('cli',2,1500)#to decide where to start(2,1500 ) used for delay and waiting time
            configLines = device.send_command_timing('show full-configuration',2,1500)
            routeLines = device.send_command_timing('get router info routing-table details',2,1500)
            configLines = str(configLines)
            configFile = open(FW_name+".txt" , "w")#"c:\\Users\\User\\Desktop\\Policy\\CIH_file\\get FWs Conf\\Config Files\\"+
            configFile.write(configLines)
            routeFile = open(FW_name+"_routes.txt" , "w")#"c:\\Users\\User\\Desktop\\Policy\\CIH_file\\get FWs Conf\\Route Files\\"+
            routeFile.write(routeLines)
            configFile.close()
            routeFile.close()
            device.disconnect()
    
    if(FW_Platform == 'Juniper Junos'):
            device = ConnectHandler(device_type='juniper', ip= FW_IP , username=FW_Username, password=FW_Password)
            device.send_command_timing('cli',2,1500)#to decide where to start(2,1500 ) used for delay and waiting time
            configLines = device.send_command_timing('show configuration | display set | no-more',2,1500)
            routeLines = device.send_command_timing('show route | no-more',2,1500)
            configLines = str(configLines)
            configFile = open(FW_name+".txt" , "w")#"c:\\Users\\User\\Desktop\\Policy\\CIH_file\\get FWs Conf\\Config Files\\"+
            configFile.write(configLines)
            routeFile = open(FW_name+"_routes.txt" , "w")#"c:\\Users\\User\\Desktop\\Policy\\CIH_file\\get FWs Conf\\Route Files\\"+
            routeFile.write(routeLines)
            configFile.close()
            routeFile.close()
            device.disconnect()

    if(FW_Platform == 'Juniper ScreenOS'):
            device = ConnectHandler(device_type='juniper', ip= FW_IP , username=FW_Username, password=FW_Password)
            configLines = device.send_command_timing('get config',2,1500)
            configLines = str(configLines)
            routeLines = device.send_command_timing('get route',2,1500)
            routeLines = str(routeLines)
            configFile = open(FW_name+".txt" , "w")#"c:\\Users\\User\\Desktop\\Policy\\CIH_file\\get FWs Conf\\Config Files\\"+
            configFile.write(configLines)
            routeFile = open(FW_name+"_routes.txt" , "w")#"c:\\Users\\User\\Desktop\\Policy\\CIH_file\\get FWs Conf\\Route Files\\"+
            routeFile.write(routeLines)
            configFile.close()
            routeFile.close()
            device.disconnect()
      
    


#extract configuration and routes from the FW :


firewallsData = ReadFile("FirewallsData.csv")
FWsDic = {}
unParsedFW = []
#print firewallsData
for line in firewallsData[1:]: #start from 1 to neglect the header line 
    name, ip, platform, UserName, Password = line.split(',')
    FWsDic[name+"_"+ip] = [name+"_"+ip, ip, platform, UserName, Password] #created FW dictionary with all needed Data 
    unParsedFW.append(name+"_"+ip)

for FW in FWsDic.values():
    print FW

#raw_input("FW Date read")


while len(unParsedFW) != 0:# for the code to retry till all the FW configuration is completed
    for fw in unParsedFW:
        try:
            print("try ",fw)
#            Parse_FW_configuration(FWsDic[fw][0],fw,FWsDic[fw][1])
            Parse_FW_configuration(FWsDic[fw])
            
            unParsedFW.remove(fw)
            print(fw,"Done")
            print "Remaining FWs List:"
            print unParsedFW
        except Exception as error: 
            print(error)
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>error "+str(fw))
            continue

