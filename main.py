
from tkinter import *
from page_manager import PageManager




# ----------UI SETUP---------

window = Tk()
window.title("Airbus A320-200 FMS")
window.config(padx=100, pady=5)
window.geometry("1200x800")
window.resizable(False, False)
LOGO_img=PhotoImage(file="./images/plane_logo.png")
window.iconphoto(False, LOGO_img)

COCKPIT_img = PhotoImage(file="./images/cockpit.png")
canvas = Canvas(window,width= COCKPIT_img.width(),height= COCKPIT_img.height())
canvas.create_image(COCKPIT_img.width()/2,COCKPIT_img.height()/2,image=COCKPIT_img)
canvas.grid(row=0,column=0,columnspan=4)
canvas.config(bg="black")


# ----------PAGES----------

my_page_manager = PageManager(window,canvas)

my_page_manager.create_labels()
my_page_manager.create_entries()


window.mainloop()