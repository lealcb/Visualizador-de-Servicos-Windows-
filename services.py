from __future__ import print_function
import psutil
import win32serviceutil  as servico
import time
import os

def get_service(name):
    service = None
    try:
        service = psutil.win_service_get(name)
        service = service.as_dict()
        if service:
            print("Service found: ", service)
        else:
            print("Service not found")

        if service and service['status'] == 'running':
            print("Service is running")
            os.chdir("C:/ZettaBrasil/ZettaNFCe")                             
            os.startfile("ZettaNFCe.exe")
        else: 
            print("Service is not running")
            print("Starting server")
            servico.StartService("PostgreSQL_10_Zetta")
            time.sleep(10)
            print("Done")
            os.chdir("C:/ZettaBrasil/ZettaNFCe")                             
            os.startfile("ZettaNFCe.exe")                      
            time.sleep(10)
            
    

    except Exception as ex:
        # raise psutil.NoSuchProcess if no service with such name exists
        print(str(ex))
    
service = get_service('PostgreSQL_10_Zetta')


