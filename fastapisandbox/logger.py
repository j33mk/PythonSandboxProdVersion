from datetime import datetime
import os

def Log(log_text,file_name):
    try:
        today = datetime.now()
        currentDate = today.strftime("%d%b%Y")
        #check if logs folder exists else create it
        folder_path = os.path.join(os.getcwd(),'Logs')
        if os.path.isdir(folder_path) == False:
            os.mkdir(folder_path)
        file_path = folder_path+'/'+currentDate+'.log'
        if os.path.isfile(file_path) == False:
            f = open(file_path,'w+')
            f.close()
        f = open(file_path,'a+')
        currentDateTime = today.strftime("%d/%m/%Y %H:%M:%S")
        f.write('------------------------------------------------------------------------------------------------------------------\n')
        f.write('Error/Issue occured in file '+file_name+' on '+str(currentDateTime)+'\n')
        f.write('Exception: '+str(log_text)+'\n')
        f.write('------------------------------------------------------------------------------------------------------------------\n')    
        f.close()
    except Exception as e:
        print(e)