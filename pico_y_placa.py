#!/usr/bin/env python

# Diego Fernando
# "Pico y Placa" predictor
# 14/06/2022

from dataclasses import dataclass
from re import compile
from datetime import datetime, time


@dataclass
class License_plate:
    plate: str
    date: str
    time: datetime

    # Check license plate method
    def check_plate(self):
        if len(self.plate) == 6:
            plate_format = compile('^[a-zA-Z]{3}[0-9]{3}$')

            if plate_format.match(self.plate) is not None:
                # print('Correct plate format')
                return True
            else:
                # print('Invalid plate format')
                return False

        elif len(self.plate) == 7:
            plate_format = compile('^[a-zA-Z]{3}[0-9]{4}$')

            if plate_format.match(self.plate) is not None:
                # print('Correct plate format')
                return True
            else:
                # print('Invalid plate format')
                return False

        else:
            # print('Invalid plate format')
            return False

    def check_date(self):
        if len(self.date) == 10:
            date_format = compile('^[0-9]{4}-[0-9]{2}-[0-9]{2}$')

            if date_format.match(self.date) is not None:
                # print('Correct date format')
                return True
            else:
                # print('Invalid date format')
                return False

        else:
            # print('Invalid date format')
            return False

    def check_time(self):
        if len(self.time) == 5:
            time_format = compile('^[0-9]{2}:[0-9]{2}$')

            if time_format.match(self.time) is not None:
                # print('Correct time format')
                return True
            else:
                # print('Invalid time format')
                return False

        else:
            print('Invalid date format')
            return False

    # Car can be on road method
    def be_on_road(self):

        plate_correct = self.check_plate()
        date_correct = self.check_date()
        time_correct = self.check_time()

        if plate_correct and date_correct and time_correct:

            last_digit = int(self.plate.strip()[-1])
            my_date = datetime.strptime(self.date, "%Y-%m-%d")
            my_time = datetime.strptime(self.time, "%H:%M")

            t1 = datetime.strptime('07:00', '%H:%M').time()
            t2 = datetime.strptime('09:30', '%H:%M').time()
            t3 = datetime.strptime('16:00', '%H:%M').time()
            t4 = datetime.strptime('19:30', '%H:%M').time()

            message = "Your car can't be on road"

            if my_time.time() >= t1 and my_time.time() <= t2 or my_time.time() >= t3 and my_time.time() <= t4:
                if my_date.weekday() == 0 and (last_digit == 1 or last_digit == 2):
                    print(message)
                elif my_date.weekday() == 1 and (last_digit == 3 or last_digit == 4):
                    print(message)
                elif my_date.weekday() == 2 and (last_digit == 5 or last_digit == 6):
                    print(message)
                elif my_date.weekday() == 3 and (last_digit == 7 or last_digit == 8):
                    print(message)
                elif my_date.weekday() == 4 and (last_digit == 9 or last_digit == 0):
                    print(message)
                else:
                    print("Your car can be on road")
            else:
                print("Your car can be on road")
        else:
            print("Incorrect input format")


# Request input from user
plate = input('Please, enter the license plate without a hyphen: ').lower()
date_ = str(input('Please, enter the date (yyyy-mm-dd): '))
time_ = input('Please, enter the time in 24 hours format (hh:mm): ')

# create some instances
car = License_plate(plate, date_, time_)

car.be_on_road()
