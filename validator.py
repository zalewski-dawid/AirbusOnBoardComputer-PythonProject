from tkinter import *
from aircraft_data_processor import *
from tkinter import messagebox
import json



class Validator:


    def __init__(self):
        self.VALIDATOR_SCORE=0


    def check_flight_nbr(self,nbr):

        first_3_char=nbr[:3]

        #validate format


        if len(nbr)==7 and nbr[3].isdigit() and nbr[4].isdigit and nbr[5].isdigit() and nbr[6].isdigit():

            # validate with JSON file
            with open("airlines.JSON", "r", encoding="utf-8") as file:
                data = json.load(file)
            if first_3_char in data:
                return True
            else:
                messagebox.showinfo("ERROR", "FLIGHT NBR-> WRONG AIRLINE CODE (first 3 letters)")
                return False


        else:
            messagebox.showinfo("ERROR"," WRONG FORMAT of FLIGHT NBR-> length 7, first 3 chars are letters, next 4 chars are digits e.g.WZZ1234")
            return False



    def check_airport_codes(self,airport_departure,airport_arrival,airport_alt):

        with open("airports.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            if airport_departure and airport_arrival and airport_alt in data:
                return True
            else:
                messagebox.showinfo("ERROR","WRONG AIRPORT CODE")
                return False


    def check_flight_level(self,FL):

        if FL == 300 or FL == 320 or FL == 340 or FL == 360 or FL == 380 or FL == 400:
            return True
        else:
            messagebox.showinfo("ERROR","POSSIBLE FLIGHT LEVEL VALUES: 300,320,340,360,380,400")
            return False


    def check_PAX(self,PAX):
        if PAX >= 20 and PAX <= 180:
            return True
        else:
            messagebox.showinfo("ERROR","PAX-> MIN-20 MAX-180")
            return False


    def check_flaps(self,flaps):
        if flaps=="1+F" or flaps=="2":
            return True
        else:
            messagebox.showinfo("ERROR","FLAPS-> 1+F or 2")
            return False


    def check_RNW_L(self,length):
        if length>=1000 and length<=6250:
            return True
        else:
            messagebox.showinfo("ERROR","RNW/L-> MIN-1000 MAX-6250")


    def check_RNW_COND(self,cond):
        if cond=="DRY" or cond=="WET":
            return True
        else:
            messagebox.showinfo("ERROR","RNW/COND-> DRY or WET")
            return False

