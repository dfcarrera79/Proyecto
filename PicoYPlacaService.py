#!/usr/bin/env python

# Diego Fernando
# "Pico y Placa" Services
# 14/06/2022

from datetime import datetime, time
from re import compile
from License_plate import License_plate


class PicoYPlacaService:

    def be_on_road(plate, _date, _time):
        car = License_plate(plate, _date, _time)
        plate_correct = car.check_plate()
        date_correct = car.check_date()
        time_correct = car.check_time()

        if plate_correct and date_correct and time_correct:

            last_digit = int(car.plate.strip()[-1])
            my_date = datetime.strptime(car.date, "%Y-%m-%d")
            my_time = datetime.strptime(car.time, "%H:%M")

            t1 = datetime.strptime('07:00', '%H:%M').time()
            t2 = datetime.strptime('09:30', '%H:%M').time()
            t3 = datetime.strptime('16:00', '%H:%M').time()
            t4 = datetime.strptime('19:30', '%H:%M').time()

            message = "Your car can't be on road"

            if my_time.time() >= t1 and my_time.time() <= t2 or my_time.time() >= t3 and my_time.time() <= t4:
                if my_date.weekday() == 0 and (last_digit == 1 or last_digit == 2):
                    return message
                elif my_date.weekday() == 1 and (last_digit == 3 or last_digit == 4):
                    return message
                elif my_date.weekday() == 2 and (last_digit == 5 or last_digit == 6):
                    return message
                elif my_date.weekday() == 3 and (last_digit == 7 or last_digit == 8):
                    return message
                elif my_date.weekday() == 4 and (last_digit == 9 or last_digit == 0):
                    return message
                else:
                    return "Your car can be on road"
            else:
                return "Your car can be on road"
        else:
            return "Incorrect input format"
