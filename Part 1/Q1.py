import datetime


def is_date_format_correct(date:str)->bool:

#This function takes in a date in string format
#and returns true if the date matches the format
#YYYY-MM-DD and false if it doesnt
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        print(True)
    except:
        print(False)
    

    
date = input("Please enter date")
is_date_format_correct(date)