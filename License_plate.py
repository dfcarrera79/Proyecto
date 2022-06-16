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


