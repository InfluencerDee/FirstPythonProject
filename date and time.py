import datetime
#Get the current day, month, year, hour, minute and timestamp from datetime module

now = datetime.datetime.now()
print(now)

#Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
format_current_datetime = now.strftime("%m/%d/%Y %H:%M:%S")
print(format_current_datetime)

#Today is 5 December, 2019. Change this time string to time.
datetime_string = "5 December, 2019"
print("date and time:", datetime_string)
datetime_object = datetime.datetime.strptime(datetime_string, "%d %B, %Y")
print("date and time object", datetime_object)


#Calculate the time difference between now and new year.
today = datetime.datetime.today()
new_year = datetime.datetime(year = 2026, month = 1, day = 1)
time_difference = new_year - today
print(time_difference)

#Calculate the time difference between 1 January 1970 and now.
previous_datetime_string = "1 January 1970"
previous_datetime = datetime.datetime.strptime(previous_datetime_string, "%d %B %Y")
current_datetime = datetime.datetime.today()
time_difference1 = current_datetime - previous_datetime
print(time_difference1)




