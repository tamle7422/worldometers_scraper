from datetime import datetime

def printTime():
    now = datetime.now()
    currentDate = now.strftime("%m_%d_%y")
    return currentDate




def checkEmpty(data):
    if (data == None or len(data) == 0):
        data = "None"
        return data
    else:
        return data