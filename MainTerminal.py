#!/usr/bin/env python

# Diego Fernando
# "Pico y Placa" terminal
# 14/06/2022

from PicoYPlacaService import PicoYPlacaService

# Request input from user
_plate = input('Please, enter the license plate without a hyphen: ').lower()
_date = str(input('Please, enter the date (yyyy-mm-dd): '))
_time = input('Please, enter the time in 24 hours format (hh:mm): ')

# create some instances
service = PicoYPlacaService
message = service.be_on_road(_plate, _date, _time)
print(message)
