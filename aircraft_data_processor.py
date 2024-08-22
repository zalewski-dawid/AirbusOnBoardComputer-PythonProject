import json
import math
from geopy.distance import great_circle
from tkinter import *
from datetime import datetime
import random
import page_manager
from page_manager import *
from validator import *




class Processor:
    def __init__(self):
        self.TRIP_FUEL = 0
        self.ALT_FUEL = 0
        self.MIN_T_OFF_FUEL = 0
        self.T_OFF_FUEL = 0
        self.distance=0
        self.alt_distance=0
        self.TOW = 0

        self.NBR=str(page_manager.ENTRY_1)
        self.FROM = str(page_manager.ENTRY_2).upper()
        self.TO = str(page_manager.ENTRY_3).upper()
        self.ALT = str(page_manager.ENTRY_4).upper()
        self.CRZ_FL = int(page_manager.ENTRY_5)
        self.PAX = int(page_manager.ENTRY_7)
        self.EXTRA = int(page_manager.ENTRY_8)
        self.TAXI = int(page_manager.ENTRY_9)
        self.FLAPS = str(page_manager.ENTRY_10)
        self.RNW_L = int(page_manager.ENTRY_11)
        self.RNW_COND = str(page_manager.ENTRY_12)
        self.PIC = str(page_manager.ENTRY_13).upper()
        self.v1 = 0
        self.vr = 0
        self.v2 = 0
        self.PASSENGERS_WEIGHT = self.PAX * 84


    def reading_airport_codes(self):

        # AIRPORT CODES DATA PROCESSING
        airport_departure = self.FROM
        airport_arrival = self.TO
        airport_alt = self.ALT

        with open("airports.json", "r", encoding="utf-8") as file:
            data = json.load(file)


        if airport_departure and airport_arrival and airport_alt in data:
            coord_airport_departure = (data[airport_departure]["latitude"], data[airport_departure]["longitude"])
            coord_airport_arrival = (data[airport_arrival]["latitude"], data[airport_arrival]["longitude"])
            coord_airport_alt = (data[airport_alt]["latitude"], data[airport_alt]["longitude"])



            # calculating the distance between airports
            distance = great_circle(coord_airport_departure, coord_airport_arrival).kilometers
            alt_distance = great_circle(coord_airport_arrival, coord_airport_alt).kilometers

            #calculate
            self.TRIP_FUEL=self.fuel_mass(distance)
            self.ALT_FUEL=self.fuel_mass(alt_distance)
            self.MIN_T_OFF_FUEL=self.TRIP_FUEL+605.0+self.ALT_FUEL
            #######
            self.T_OFF_FUEL=self.MIN_T_OFF_FUEL+self.EXTRA+self.TAXI
            self.TOW=45700+self.T_OFF_FUEL+self.PASSENGERS_WEIGHT

            self.distance=distance
            self.alt_distance=alt_distance
            self.speeds(self.TOW,self.FLAPS,self.RNW_COND,self.RNW_L)



    def fuel_mass(self,distance):
        #func that allows to calculate the mass of fuel
        # fuel_consumption_per_km=3.8
        litres_of_fuel = distance * 3.8
        mass_of_fuel = litres_of_fuel * 0.8

        return mass_of_fuel

    def speeds(self,TOW,flaps,cond,leng):
        #depends on value of TOW there are different speeds for aircraft

        if TOW < 47850:
            self.v1 = 122
            self.vr = 122
            self.v2 = 127

        elif 47850 <= TOW < 52500:
            self.v1 = 122

            self.vr = 122
            self.v2 = 132


        elif 52500 <= TOW < 57500:
            self.v1 = 126
            self.vr = 126
            self.v2 = 137


        elif 57500 <= TOW < 62500:
            self.v1 = 130
            self.vr = 131
            self.v2 = 142

        elif 62500 <= TOW < 67500:
            self.v1 = 134
            self.vr = 135
            self.v2 = 148

        else:  # TOW >= 67500
            self.v1 = 138
            self.vr = 140
            self.v2 = 153

        # if flaps == 2 , we have to change speeds
        if (flaps== "2"):
            self.v1 = 0.9 * self.v1
            self.vr = 0.97 * self.vr
            self.v2 = 0.92 * self.v2
        # depends if runway is WET or DRY
        if (cond == "WET"):
            self.v1 = 0.9 * self.v1
            self.vr = 0.96 * self.vr
            self.v2 = 0.92 * self.v2

        # depends on length of runway we have to change speeds

        if leng < 2250:
            self.v1 = self.v1 - 1
            self.vr = self.vr - 1

        elif 2750 <= leng < 3250:
            self.v1 = self.v1 + 1
            self.vr = self.vr + 1

        elif 3250 <= leng < 3750:
            self.v1 = self.v1 + 2
            self.vr = self.vr + 2

        elif 3750 <= leng < 4250:
            self.v1 = self.v1 + 3
            self.vr = self.vr + 3

        elif 4250 <= leng < 4750:
            self.v1 = self.v1 + 4
            self.vr = self.vr + 4

        elif 4750 <= leng < 5250:
            self.v1 = self.v1 + 5
            self.vr = self.vr + 5

        elif 5250 <= leng < 5750:
            self.v1 = self.v1 + 6
            self.vr = self.vr + 6

        elif 5750 <= leng <= 6250:
            self.v1 = self.v1 + 7
            self.vr = self.vr + 7

    def calculate_everything(self):
        self.reading_airport_codes()


    def generate_report(self):
        first_3_char = self.NBR[:3].upper()
        with open("airlines.JSON", "r", encoding="utf-8") as file:
            data = json.load(file)
            airline_name=data[first_3_char]

        current_time = datetime.now()
        random_runway1 = random.randint(1,10)
        random_runway2 = random.randint(1,10)
        # formatted time
        formatted_time=current_time.strftime("%Y-%m-%d %H:%M:%S")



        report_text = Text(wrap="word",background="white",foreground="black",font=("Arial",12,"bold"))

        report_text.grid(column=0,row=0,sticky="nsew")

        #Create scrollbar
        scrollbar=Scrollbar(command=report_text.yview)
        report_text.config(yscrollcommand=scrollbar.set)

        scrollbar.grid(column=1,row=0,sticky="ns")


        report_content = f"""
            ----------AIRBUS A320 A320-200 FMS----------
            
            
            FLIGHT PLAN
            ---------------------------------
            REPORT GENERATED: {formatted_time}
            ---------------------------------
            
            {self.NBR}  {self.FROM}  {self.TO} 
            {airline_name}
            A320-200 / CFM56-5B4  
            
            MAXIMUM TOW 78000 LAW 66000 ZFW 62500
            ESTIMATED TOW {int(self.TOW)} LAW {int(self.TOW-self.TRIP_FUEL)} ZFW {int(self.PASSENGERS_WEIGHT+45700)}
            ---------------------------------
            ---------------------------------
            AVG WIND: {random.randint(40,250)}/{random.randint(20,70)}
            -----------
            PLANNED FUEL
            ---------------------------------
            FUEL/TIME
            ---------------------------------
            TRIP: {int(self.TRIP_FUEL+self.ALT_FUEL)}/{int(self.distance/14)}
            -----------
            CONT 15 MIN: 605/0015
            ---------------------------------
            MINIMUM T/OFF FUEL: {int(605+self.TRIP_FUEL+self.ALT_FUEL)}  {int(15+int(self.distance/14))+int(self.alt_distance/14)}   
            ---------------------------------
            EXTRA: {self.EXTRA}
            T/OFF FUEL: {int(self.EXTRA+605+self.TRIP_FUEL+self.ALT_FUEL)}
            ---------------------------------
            TAXI: {int(self.TAXI)}
            ---------------------------------
            BLOCK FUEL: {int(self.TAXI+self.EXTRA+605+self.TRIP_FUEL+self.ALT_FUEL)}
            ---------------------------------
            ROUTING
            ---------------------------------
            {self.FROM}/{random_runway1} FL {self.CRZ_FL} {self.TO}/{random_runway2}      
            -----------
            DEPARTURE
            ---------------------------------
            {self.FROM}/{random_runway1} RNW {self.RNW_COND}
            ---------------------------------
            WIND: {random.randint(40,250)}/{random.randint(20,70)}
            ---------------------------------
            ARRIVAL
            ---------------------------------
            {self.TO}/{random_runway2} RNW {self.RNW_COND} 
            ---------------------------------
            T/OFF SPEEDS
            ---------------------------------
            V1: {round(self.v1,2)}
            VR: {round(self.vr,2)}
            V2: {round(self.v2,2)}
            ---------------------------------
            I HEREWITH CONFIRM THAT I HAVE PERFORMED A
            THOROUGH SELF BRIEFING ABOUT THE DESTINATION
            AND ALTERNATE AIRPORTS OF THIS FLIGHT
            INCLUDING THE APPLICABLE INSTRUMENT APPROACH
            PROCEDURES, AIRPORT FACILITIES, NOTAMS AND
            ALL OTHER RELEVANT PARTICULAR INFORMATION.
            PIC NAME: {self.PIC}
            ---------------------------------
            HAVE A SAFE FLIGHT !
            ---------------------------------
            
        """
        report_text.insert(END,report_content)
        report_text.config(state="disabled")





