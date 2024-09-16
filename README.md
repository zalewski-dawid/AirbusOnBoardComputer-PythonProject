Aircraft On-Board Computer for Airbus A320-200 FMS
This program serves as a tool for performing calculations and generating a flight plan report
based on the data provided by the pilot. It allows the pilot to input key information about the
flight, such as the flight number, airports, flight level, number of passengers, and takeoff
conditions. Based on these inputs, the program performs calculations, such as fuel mass,
aircraft weights, takeoff speeds, and other essential parameters, and then generates a
detailed flight plan report.
Features


● Geographical Coordinates Lookup: The program reads airport data, including
geographical coordinates, from JSON files. This data is then analyzed to determine
the coordinates for departure, arrival, and alternate airports.


● Distance Calculation: Using the geographical data from the JSON files, the program
calculates the great-circle distance between airports.


● Fuel Calculation: Calculates the required fuel mass for the trip and includes
additional fuel considerations, such as contingency fuel and reserves.


● Airline Identification: Identifies the airline based on the flight number prefix.


● Takeoff Performance Calculation: Calculates the necessary takeoff speeds (V1,
VR, V2) based on the aircraft's weight and atmospheric parameters.


● Flight Plan Generation: Generates a comprehensive flight plan report, including fuel
requirements, wind conditions, and other critical information.


● Modular Architecture: The program is designed with a modular architecture, where
several collaborating modules handle different aspects of the data processing. These
modules read data from JSON files and perform specific tasks, such as fuel
calculation, geographical data handling, or performance computation, working
together to generate a complete and accurate flight plan.


This modular approach ensures that each part of the program can be easily maintained and
updated while providing a reliable and accurate flight planning tool.
