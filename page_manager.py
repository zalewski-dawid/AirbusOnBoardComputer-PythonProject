from tkinter import *

from aircraft_data_processor import Processor
from validator import Validator
from PIL import Image, ImageTk


CURRENT_PAGE=1
ENTRY_1 = 0
ENTRY_2 = 0
ENTRY_3 = 0
ENTRY_4 = 0
ENTRY_5 = 0
ENTRY_6 = 0
ENTRY_7 = 0
ENTRY_8 = 0
ENTRY_9 = 0
ENTRY_10 = 0
ENTRY_11 = 0
ENTRY_12 = 0
ENTRY_13=0


class PageManager:
    def __init__(self,win,canv):
        self.pages_titles=["--FLIGHT INIT--", "--PAYLOAD--", "--TAKE OFF PERFORMANCE--"]
        self.container_widgets=[]
        self.my_validator=Validator()
        self.window=win
        self.canv=canv

        self_ref_img=None



    def clear_widgets(self):
        for widget in self.container_widgets:
            widget.destroy()



    def final_animation(self):
        self.clear_widgets()
        self.delete_margins()
        self.ref_img = PhotoImage(file="./images/plane_take_off.png")
        canvas = Canvas(self.window, width=self.ref_img.width(), height=self.ref_img.height())
        canvas.create_image(self.ref_img.width() / 2, self.ref_img.height() / 2, image=self.ref_img)
        canvas.grid(row=0, column=0)


    def delete_margins(self):
        self.window.config(padx=0, pady=0)





    def report(self):
        self.clear_widgets()
        self.delete_cockpit_img()
        my_processor = Processor()
        my_processor.calculate_everything()
        my_processor.generate_report()
        saving_button = Button(text="FLY", width=20, command=self.final_animation)
        saving_button.grid(column=2, row=8)
        self.container_widgets.append(saving_button)

    def delete_cockpit_img(self):
        self.canv.destroy()
    #labels
    def create_labels(self):

        self.clear_widgets()


        if CURRENT_PAGE==1:
            page_nbr_label=Label(text=f"PAGE {CURRENT_PAGE}",font=("Halvetica,20"))
            page_nbr_label.grid(column=0,row=1)
            self.container_widgets.append(page_nbr_label)
            page_title_label = Label(text=f"{self.pages_titles[CURRENT_PAGE-1]}",font=("Halvetica,20"))
            page_title_label.grid(column=0,row=2)
            self.container_widgets.append(page_title_label)
            page_flight_nbr_label=Label(text="FLIGHT NBR: ",font=("Halvetica,20"))
            page_flight_nbr_label.grid(column=0,row=3)
            self.container_widgets.append(page_flight_nbr_label)
            page_from_label=Label(text="FROM: ",font=("Halvetica,20"))
            page_from_label.grid(column=0,row=4)
            self.container_widgets.append(page_from_label)
            page_to_label=Label(text="TO: ",font=("Halvetica,20"))
            page_to_label.grid(column=0,row=5)
            self.container_widgets.append(page_to_label)
            page_alt_label=Label(text="ALT: ",font=("Halvetica,20"))
            page_alt_label.grid(column=0,row=6)
            self.container_widgets.append(page_alt_label)
            page_crz_fl_label=Label(text="CRZ/FL: ",font=("Halvetica,20"))
            page_crz_fl_label.grid(column=0,row=7)
            self.container_widgets.append(page_crz_fl_label)
            page_temp_label=Label(text="TEMP: ",font=("Halvetica,20"))
            page_temp_label.grid(column=0,row=8)
            self.container_widgets.append(page_temp_label)

        if CURRENT_PAGE == 2:

            page_nbr_label = Label(text=f"PAGE {CURRENT_PAGE}",font=("Halvetica,20"))
            page_nbr_label.grid(column=0, row=1)
            self.container_widgets.append(page_nbr_label)
            page_title_label = Label(text=f"{self.pages_titles[CURRENT_PAGE - 1]}",font=("Halvetica,20"))
            page_title_label.grid(column=0, row=2)
            self.container_widgets.append(page_title_label)
            page_flight_pax_label = Label(text="PAX: ",font=("Halvetica,20"))
            page_flight_pax_label.grid(column=0, row=3)
            self.container_widgets.append(page_flight_pax_label)
            page_extra_label = Label(text="EXTRA: ",font=("Halvetica,20"))
            page_extra_label.grid(column=0, row=4)
            self.container_widgets.append(page_extra_label)
            page_taxi_label = Label(text="TAXI: ",font=("Halvetica,20"))
            page_taxi_label.grid(column=0, row=5)
            self.container_widgets.append(page_taxi_label)

        if CURRENT_PAGE == 3:
            page_nbr_label = Label(text=f"PAGE {CURRENT_PAGE}",font=("Halvetica,20"))
            page_nbr_label.grid(column=0, row=1)
            self.container_widgets.append(page_nbr_label)
            page_title_label = Label(text=f"{self.pages_titles[CURRENT_PAGE - 1]}",font=("Halvetica,20"))
            page_title_label.grid(column=0, row=2)
            self.container_widgets.append(page_title_label)
            page_flaps_label=Label(text="FLAPS(1+F/2): ",font=("Halvetica,20"))
            page_flaps_label.grid(column=0,row=3)
            self.container_widgets.append(page_flaps_label)
            page_rnw_L_label=Label(text="RNW/L: ",font=("Halvetica,20"))
            page_rnw_L_label.grid(column=0,row=4)
            self.container_widgets.append(page_rnw_L_label)
            page_rnw_cond_label=Label(text="RNW/COND: ",font=("Halvetica,20"))
            page_rnw_cond_label.grid(column=0,row=5)
            self.container_widgets.append(page_rnw_cond_label)
            page_pic_name_label=Label(text="PIC (PILOT IN COMMAND) NAME: ",font=("Halvetica,20"))
            page_pic_name_label.grid(column=0,row=6)
            self.container_widgets.append(page_pic_name_label)



    def create_entries(self):
        global CURRENT_PAGE
        if CURRENT_PAGE == 1:
            page_flight_nbr_entry = Entry(width=35,font=("Halvetica,20"))
            page_flight_nbr_entry.grid(column=1, row=3)
            self.container_widgets.append(page_flight_nbr_entry)
            page_from_entry = Entry(width=35,font=("Halvetica,20"))
            page_from_entry.grid(column=1, row=4)
            self.container_widgets.append(page_from_entry)
            page_to_entry = Entry(width=35,font=("Halvetica,20"))
            page_to_entry.grid(column=1, row=5)
            self.container_widgets.append(page_to_entry)
            page_alt_entry = Entry(width=35,font=("Halvetica,20"))
            page_alt_entry.grid(column=1, row=6)
            self.container_widgets.append(page_alt_entry)
            page_crz_fl_entry = Entry(width=35,font=("Halvetica,20"))
            page_crz_fl_entry.grid(column=1, row=7)
            self.container_widgets.append(page_crz_fl_entry)
            page_temp_entry = Entry(width=35,font=("Halvetica,20"))
            page_temp_entry.grid(column=1, row=8)
            self.container_widgets.append(page_temp_entry)

            def save_page_1_entries():
                global ENTRY_1, ENTRY_2, ENTRY_3, ENTRY_4, ENTRY_5, ENTRY_6,CURRENT_PAGE
                ENTRY_1 = page_flight_nbr_entry.get()
                ENTRY_2 = page_from_entry.get()
                ENTRY_3 = page_to_entry.get()
                ENTRY_4 = page_alt_entry.get()
                ENTRY_5 = int(page_crz_fl_entry.get())
                ENTRY_6 = int(page_temp_entry.get())
                if self.my_validator.check_flight_nbr(ENTRY_1)==True and self.my_validator.check_airport_codes(ENTRY_2,ENTRY_3,ENTRY_4)==True and self.my_validator.check_flight_level(ENTRY_5)==True:
                    #VALIDATE ALL PAGE 1 ENTRIES
                    CURRENT_PAGE += 1
                self.create_labels()
                self.create_entries()



            #Create button to save info
            saving_button = Button(text="NEXT", width=20, command=save_page_1_entries)
            saving_button.grid(column=2, row=8)
            self.container_widgets.append(saving_button)




        if CURRENT_PAGE==2:

            page_flight_pax_entry = Entry(width=35,font=("Halvetica,20"))
            page_flight_pax_entry.grid(column=1, row=3)
            self.container_widgets.append(page_flight_pax_entry)
            page_extra_entry = Entry(width=35,font=("Halvetica,20"))
            page_extra_entry.grid(column=1, row=4)
            self.container_widgets.append(page_extra_entry)
            page_taxi_entry = Entry(width=35,font=("Halvetica,20"))
            page_taxi_entry.grid(column=1, row=5)
            self.container_widgets.append(page_taxi_entry)

            def save_page_2_entries():
                global ENTRY_7, ENTRY_8, ENTRY_9,CURRENT_PAGE
                ENTRY_7 = int(page_flight_pax_entry.get())
                ENTRY_8 = page_extra_entry.get()
                ENTRY_9 = page_taxi_entry.get()
                if self.my_validator.check_PAX(ENTRY_7):
                    CURRENT_PAGE +=1
                self.create_labels()
                self.create_entries()

            # Create button to save info
            saving_button = Button(text="NEXT", width=20, command=save_page_2_entries)
            saving_button.grid(column=2, row=8)
            self.container_widgets.append(saving_button)

        if CURRENT_PAGE==3:
            page_flaps_entry=Entry(width=35,font=("Halvetica,20"))
            page_flaps_entry.grid(column=1, row=3)
            self.container_widgets.append(page_flaps_entry)
            page_rnw_L_entry=Entry(width=35,font=("Halvetica,20"))
            page_rnw_L_entry.grid(column=1, row=4)
            self.container_widgets.append(page_rnw_L_entry)
            page_rnw_cond_entry=Entry(width=35,font=("Halvetica,20"))
            page_rnw_cond_entry.grid(column=1, row=5)
            self.container_widgets.append(page_rnw_cond_entry)
            page_pic_name_entry=Entry(width=35,font=("Halvetica,20"))
            page_pic_name_entry.grid(column=1, row=6)
            self.container_widgets.append(page_pic_name_entry)

            def save_page_3_entries():
                global ENTRY_10,ENTRY_11,ENTRY_12,ENTRY_13,CURRENT_PAGE

                ENTRY_10=str(page_flaps_entry.get())
                ENTRY_11=int(page_rnw_L_entry.get())
                ENTRY_12=str(page_rnw_cond_entry.get())
                ENTRY_13=str(page_pic_name_entry.get())
                if self.my_validator.check_flaps(ENTRY_10)==True and self.my_validator.check_RNW_L(ENTRY_11)==True and self.my_validator.check_RNW_COND(ENTRY_12)==True:
                    CURRENT_PAGE += 1
                    self.report()

            # Create button to save info
            saving_button = Button(text="CONFIRM", width=20, command=save_page_3_entries)
            saving_button.grid(column=2, row=8)
            self.container_widgets.append(saving_button)

            if CURRENT_PAGE==4:
                # Create button to save info
                saving_button = Button(text="CONFIRM", width=20, command=self.final_animation)
                saving_button.grid(column=2, row=8)
                self.container_widgets.append(saving_button)














