"""
1. Add the current date to the text file today.txt as a string.

ANSWER..

To add the current date to the text file today.txt as a string, we can use the datetime module in Python as follows:

import datetime

# get the current date
now = datetime.datetime.now()

# open the file in append mode and write the date
with open("today.txt", "a") as f:
    f.write(now.strftime("%Y-%m-%d"))

-----------------------------------------------------------------------------------------------


2. Read the text file today.txt into the string today_string

ANSWER..

To read the text file today.txt into the string today_string, we can use the following code:

with open("today.txt", "r") as f:
    today_string = f.read()


-----------------------------------------------------------------------------------------------


3. Parse the date from today_string.

ANSWER..

To parse the date from today_string, assuming that the date is in the format "YYYY-MM-DD", we can use the datetime module in Python as follows:

import datetime

date = datetime.datetime.strptime(today_string, "%Y-%m-%d")


-----------------------------------------------------------------------------------------------


4. List the files in your current directory

ANSWER..

To list the files in your current directory, you can use the os module in Python as follows:

import os

files = os.listdir(".")
for file in files:
    print(file)


-----------------------------------------------------------------------------------------------


5. Create a list of all of the files in your parent directory (minimum five files should be available).

ANSWER..

To create a list of all of the files in your parent directory, we can use the os module in Python as follows:

import os

parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
files = os.listdir(parent_dir)
for file in files:
    print(file)


-----------------------------------------------------------------------------------------------


6. Use multiprocessing to create three separate processes. Make each one wait a random number of
seconds between one and five, print the current time, and then exit.

ANSWER..

To use multiprocessing to create three separate processes that wait a random number of seconds between one and five, print the current time, and then exit, we can use the multiprocessing module in Python as follows:

import multiprocessing
import random
import time
import datetime

def worker():
    wait_time = random.randint(1, 5)
    time.sleep(wait_time)
    print(f"{datetime.datetime.now()}: Process {multiprocessing.current_process().name} waited {wait_time} seconds and finished.")

if __name__ == "__main__":
    for i in range(3):
        p = multiprocessing.Process(target=worker, name=f"Worker-{i}")
        p.start()


-----------------------------------------------------------------------------------------------


7. Create a date object of your day of birth.

ANSWER..

To create a date object of your day of birth, we can use the datetime module in Python as follows:

import datetime

birthday = datetime.date(year=1990, month=10, day=15)


-----------------------------------------------------------------------------------------------


8. What day of the week was your day of birth?

ANSWER..

To determine the day of the week of your day of birth, we can use the strftime() method of the datetime object in Python as follows:

import datetime

birthday = datetime.date(year=1990, month=10, day=15)
weekday = birthday.strftime("%A")
print(weekday)

-----------------------------------------------------------------------------------------------


9. When will you be (or when were you) 10,000 days old?

ANSWER..

To determine when you will be (or when you were) 10,000 days old, we can use the datetime module in Python as follows:

import datetime

birthday = datetime.date(year=1990, month=10, day=15)
ten_thousand_days = datetime.timedelta(days=10000)
future_date = birthday + ten_thousand_days
print(future_date)

-----------------------------------------------------------------------------------------------

"""