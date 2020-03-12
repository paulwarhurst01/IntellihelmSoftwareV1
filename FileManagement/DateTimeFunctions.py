import datetime

def get_time():                                                 # Returns the time in the format: 08h37m45s
    dateTime = datetime.datetime.now()
    theHour = str(dateTime.hour)
    theMinute = str(dateTime.minute)
    theSecond = str(dateTime.second)
    tm = theHour + "h" + theMinute + "m" + theSecond + "s"
    return tm

def get_date():                                                 # Returns the date in the format: 03d04m20y
    dateTime = datetime.datetime.now()
    theYear = str(dateTime.year)
    theMonth = str(dateTime.month)
    theDay = str(dateTime.day)
    dt = theYear + "y" + theMonth +"m" + theDay + "d"
    return dt

def get_date_and_time(separatedByTab: bool):                    # If bool is true, returns the sting with a tab
    if(separatedByTab == True):                                      # Otherwise returns the strings with an underscore
        return get_date() + "    " + get_time()
    else:
        return get_date() + "_" + get_time()