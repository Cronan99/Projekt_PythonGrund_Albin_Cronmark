import boatinfo
import file_module
import race_module
from tkinter import *
from tkinter import messagebox

boatlist = [] #List of Boats
racelist = [] #List of Races

try:
    racelist = file_module.loadfile("Racelist.txt") #If the file exist, opens otherwise pass
except:
    pass

try:
    boatlist = file_module.loadfile("Boatlist.txt") #If the file exist, opens otherwise pass
except:
    pass


class GUI():
    """Creates the main GUI"""
    def __init__(self):
        """Creates Main Window"""
        self.root = Tk()
        self.root.geometry("1000x500")
        self.root.title("RaceTracker")

    def boatlist(self):
        """Creates scrollbar displaying BOATLIST"""
        scroll = Scrollbar(self.root)
        scroll.grid(column=1, row= 1, sticky=NS)
        t = Label(self.root, text="Boat List")
        t.grid(column=0, row=0)
        self.list = Listbox(self.root, yscrollcommand=scroll.set, width=30, height=15)
        scroll.config(command=self.list.yview)

        self.update_boatlist()

        self.list.grid(column=0, row=1)

    def delete_boat(self):
        """Takes selected boat from boatlist and deletes it"""

        cursor = self.list.curselection()
        delete_boat = boatlist[int(cursor[0]/5)]
        boatlist.remove(delete_boat)

        self.update_boatlist()

    def addboat(self):
        """Takes userinput to create a new boat object"""

        Label(self.root, text="Add New Boat").grid(column=2, row=0, sticky=N)

        self.update_boatinput()

    def update_boatinput(self):
        """Takes userinput to create a new boat object"""

        addboat_layout = Frame(self.root) #Creates a layout for the boatinfo entry
        addboat_layout.rowconfigure(0, weight=1)
        addboat_layout.rowconfigure(1, weight=1)
        addboat_layout.rowconfigure(2, weight=1)

        Label(addboat_layout, text="Boat:").grid(column=0, row=0, sticky=NW) #Boat info labels
        Label(addboat_layout, text="SailNr:").grid(column=0, row=1, sticky=NW)
        Label(addboat_layout, text="SRS:").grid(column=0, row=2, sticky=NW)
        Label(addboat_layout, text="Crew:").grid(column=0, row=3, sticky=NW)

        self.name = Entry(addboat_layout)               #Boatinfo Entries
        self.name.grid(column=1 ,row=0, sticky=NW)

        self.sail = Entry(addboat_layout)
        self.sail.grid(column=1, row=1, sticky=NW)

        self.srs = Entry(addboat_layout)
        self.srs.grid(column=1, row=2, sticky=NW)

        self.crew = Entry(addboat_layout)
        self.crew.grid(column=1, row=3, sticky=NW)

        btn = Button(addboat_layout, text="Add Boat", command=lambda: self.refresh_boats()) #Addboat button
        btn.grid(column=1, row=4, sticky=EW)

        delete_button = Button(addboat_layout, text="Delete Selected Boat", command=lambda: self.delete_boat()) #Deleteboat button
        delete_button.grid(column=1, row=5, sticky=EW)

        create_race = Button(addboat_layout, text="Create Race", command=lambda: self.create_race()) #Button to create a race
        create_race.grid(column=1, row=6, sticky=EW)

        addboat_layout.grid(column=2, row=1, sticky=N)

    def refresh_boats(self):
        """Gets entrys when the button is pressed in update_boatinput"""

        state = True #If no error happens state will remain true and add boat
        try:          #Test if sail and srs is numbers
            int(self.sail.get())
            float(self.srs.get())
        except:
            self.error_msg("Error: Sailnumber and SRS must be numbers!")
            state = False

        if state:
            boatinfo.new_boat(boatlist, self.name.get(), self.sail.get(), self.srs.get(), self.crew.get()) #get() from update_boatinfo()
            self.update_boatlist()
            self.update_boatinput()

    def update_boatlist(self):
        """Deletes the old boatlist to insert it again including any new boats"""

        self.list.delete(0, END)

        for i in boatlist:
            self.list.insert(END, f"Boat: {i.name}")
            self.list.insert(END, f"Sailnumber: {i.sail}")
            self.list.insert(END, f"SRS: {i.srs}")
            self.list.insert(END, f"Crewmembers: {i.crew}")
            self.list.insert(END, "")

    def racelist(self):
        """Creates Scrollbar displaying RACELIST"""
        scroll2 = Scrollbar(self.root)
        scroll2.grid(column=5, row=1,sticky=NS)
        race = Label(self.root, text="Race List")
        race.grid(column=4, row=0, sticky=NSEW)
        self.races = Listbox(self.root, yscrollcommand=scroll2.set, width=30, height=15)
        scroll2.config(command=self.races.yview)

        self.update_racelist()

        self.races.grid(column=4, row=1)

    def create_race(self):
        """Creates a race window"""
        self.race_widget = Tk()
        self.race_widget.geometry("200x500")
        self.race_widget.title("Race")





        self.race_widget.mainloop()

    def update_racelist(self):
        """Delete old racelist to insert new races from racelist"""
        self.races.delete(0, END)

        for i in racelist:
            self.races.insert(END, f"{i.name}")

    def error_msg(self, error):
        """Display any error that occours"""
        messagebox.showerror("ERROR", f"{error}")


    def updateUI(self):
        self.root.mainloop()


myGUI=GUI() #Creating and running the main GUI
myGUI.boatlist()
myGUI.racelist()
myGUI.addboat()
myGUI.updateUI()


file_module.savefile(boatlist, "Boatlist.txt") #Saving the lists of object to files before closing down.
file_module.savefile(racelist, "Racelist.txt")