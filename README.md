# Proyecto
Pico y Placa predictor developed in Python

This project was developed in python with fastapi and Vue.js.

1. In order to run this code, you need to open the MainTerminal.py file for terminal input.

2. If you have fastapi installed, you can use the following command in the terminal:

uvicorn main_api:app --reload

and then open the index.html file.



Description:

Pico y Placa predictor is an API developed to check whether a car can be on the road based on the "Pico y Placa" rules of Quito city in Ecuador.

The license plate restriction is two digits per day based on:

Day         Plates that do not circulate
Monday      Plates ending in 1 and 2
Tuesday     Plates ending in 3 and 4
Wednesday   Plates ending in 5 and 6
Thursday    Plates ending in 7 and 8
Friday      Plates ending in 9 and 0
Saturday    Free circulation 24 hours
Sunday      Free circulation 24 hours

The API works in the following way:

First, the user has to enter the license plate, the date, and the time in order to check if the car can be on the road. Therefore, first, it was developed a class named Licence_plate.py where the plate, date, and time objects can be checked for correct input from the user.

Second, the algorithm developed to determine if the car can be on the road is available in PicoYPlacaService.py based on the license plate restrictions for Quito.

Third, MainTerminal.py is the code where the user can call PicoYPlacaService.py and Licence_plate.py objects in order to check the plate number in the terminal.

Finally, main_api.py uses the fastapi framework to call PicoYPlacaService and present in an HTML page the app "Pico y Placa checker", where the user can enter the plate, date, and time to check if the car can be on the road or not.
