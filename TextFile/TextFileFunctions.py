from time import sleep
from FileManagement import DateTimeFunctions as DTF

def create(txtFileName: str):
    """Creates a txt file with filename and format: Date    Time    GPS Data    Speed"""
    f = open(txtFileName, "w")
    f.write(txtFileName + "\n")
    f.write("Date        Time        GPS Co-ords    Speed [km/h]\n")
    f.close
    print("New File created: " + txtFileName)

def propogate_file(txtFile: str):
    f = open(txtFile, "a")
    for i in range(4):
        info = DTF.get_date_and_time(True)
        #gpsData = return_GPS_data()
        f.write(info + "     GPS Data\n")
        sleep(1)
    f.close
    print("File propogation completed")
    return True

# def new(txtFile: str, condition: bool): 
#    create_file(txtFile)
#    #while condition:
#        check = propogate_file(txtFile)
#    if check == True:
#        return True
#        print("New textfile completed")
#    else:
#        print("Error propogating txtFile")
