from datetime import datetime
from datetime import date
from datetime import timedelta


def compute_prev_date(dates_list: list):
    yesterdays_date = []
    for i in dates_list:
        date_in_list = date.fromisoformat(i)
        new_format = date_in_list.strftime('%d-%b-%Y')
        prev = date_in_list - timedelta(days = 1)
        
        yesterdays_date.append(prev.strftime('%d-%b-%Y'))
    return [yesterdays_date]


dates_list = ['2022-11-01', '2022-11-02']
#for i in dates_list:
 #   date_in_list = date.fromisoformat(i)
  #  new_format = date_in_list.strftime('%d-%b-%Y')
   # print(new_format)

yesterday_list = []
yesterday_list = compute_prev_date(dates_list)
print(yesterday_list)

