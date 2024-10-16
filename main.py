import boatinfo
import file_module
import race_module
from datetime import datetime
from tkinter import *
from tkinter import messagebox

"""This is the mainfile of the Racetracker
Here most of the app is running from
It uses two types of objects (Boats and Races)
with the objects it can create lists of boats and races and displays them in listboxes
with the functions in the race-class a race can be created where it tracks the time of
all contestants and when one finishes their time is recounted by their srs(handicap)
each race gets saved in a list and can later be displayed"""

boatlist = [] #List of Boats
racelist = [] #List of Races

"""Try to load previusly saved files"""
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
        self.root.geometry("1100x280")
        self.root.title("RaceTracker")

    def boatlist(self):
        """Creates scrollbar displaying BOATLIST"""
        scroll = Scrollbar(self.root)
        scroll.grid(column=1, row= 1, sticky=NS)
        t = Label(self.root, text="Boat List")
        t.grid(column=0, row=0)
        self.list = Listbox(self.root, yscrollcommand=scroll.set, width=30, height=15)
        scroll.config(command=self.list.yview)

        self.update_boatlist() #Updates the boatlist in the window using the boatlist

        self.list.grid(column=0, row=1)

    def delete_boat(self):
        """Takes selected boat from boatlist and deletes it"""
        try:    #If no boat is selected it tells the user
            cursor = self.list.curselection()
            delete_boat = boatlist[int(cursor[0]/5)]
            boatlist.remove(delete_boat)

            self.update_boatlist()
        except IndexError:
            self.error_msg("Please select a boat for deletion!")

    def addboat(self):
        """Takes userinput to create a new boat object or other actions"""

        Label(self.root, text="Add New Boat").grid(column=2, row=0, sticky=N)

        self.update_boatinput() #Updates buttons and user entries in the boatinfo boxes

    def update_boatinput(self):
        """Most of userinput is created here, buttons and entries"""

        addboat_layout = Frame(self.root) #Creates a layout for the boatinfo entry
        addboat_layout.rowconfigure(0, weight=1)
        addboat_layout.rowconfigure(1, weight=1)
        addboat_layout.rowconfigure(2, weight=1)

        Label(addboat_layout, text="Boat:").grid(column=0, row=0, sticky=NW) #Boat info labels
        Label(addboat_layout, text="SailNr:").grid(column=0, row=1, sticky=NW)
        Label(addboat_layout, text="SRS:").grid(column=0, row=2, sticky=NW)
        Label(addboat_layout, text="Crew:").grid(column=0, row=3, sticky=NW)

        self.name = Entry(addboat_layout)                                               #Boatinfo Entries
        self.name.grid(column=1 ,row=0, sticky=NW)
        self.sail = Entry(addboat_layout)
        self.sail.grid(column=1, row=1, sticky=NW)
        self.srs = Entry(addboat_layout)
        self.srs.grid(column=1, row=2, sticky=NW)
        self.crew = Entry(addboat_layout)
        self.crew.grid(column=1, row=3, sticky=NW)

        btn = Button(addboat_layout, text="Add Boat", command=lambda: self.refresh_boats())                          #Addboat button
        btn.grid(column=1, row=4, sticky=EW)

        delete_button = Button(addboat_layout, text="Delete Selected Boat", command=lambda: self.delete_boat())     #Deleteboat button
        delete_button.grid(column=1, row=5, sticky=EW)

        create_race = Button(addboat_layout, text="Create Race", command=lambda: self.create_race())                #Button to create a race
        create_race.grid(column=1, row=6, sticky=EW)

        add_to_race = Button(addboat_layout, text="Add to Race", command=lambda: self.boat_to_race())               #Button to send a boat to a race
        add_to_race.grid(column=1, row=7, sticky=EW)
        
        displayrace = Button(addboat_layout, text="Display Race", command=lambda: self.display_race())              #Button to display a race
        displayrace.grid(column=1, row=8, sticky=EW)

        delete_race = Button(addboat_layout, text="Delete Selected Race", command=lambda: self.delete_race())        #Deletes selected race
        delete_race.grid(column=1, row=9)

        addboat_layout.grid(column=2, row=1, sticky=N)                                                               #<<<<<LAYOUT GRID PLACEMENT

    def refresh_boats(self):
        """Gets entries when the button is pressed in update_boatinput"""

        state = True #If no error happens state will remain true and add boat
        try:
            if not self.name.get() or not self.sail.get() or not self.srs.get() or not self.crew.get():
                raise TypeError("Please fill in all of the boxes above!")

            for i in boatlist:
                if self.name.get() == i.name and self.sail.get() == i.sail:
                    raise TypeError(f"The boat: {self.name.get()} {self.sail.get()}, is already in the list!")

            int(self.sail.get())
            float(self.srs.get())
            
        except ValueError:
            self.error_msg("Error: Sailnumber and SRS must be numbers!")
            state = False

        except TypeError as e:
            self.error_msg(f"{e}")
            state = False
    
        if state:
            boatinfo.new_boat(boatlist, self.name.get(), self.sail.get(), self.srs.get(), self.crew.get()) #Getting info from entries in update_boatinfo()
            self.update_boatlist()                                                                         #Updating list aswell as removes previus userinput from entries
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

        self.contestant_list = []
        self.contestant_buttons = []
        self.race_widget = Tk()
        self.race_widget.geometry("300x500")
        self.race_widget.title("Race")

        enter_name = Label(self.race_widget, text="Race Name:")
        enter_name.grid(column=0, row=0, sticky=E)

        self.race_name = Entry(self.race_widget)
        self.race_name.grid(column=1, row=0, sticky=EW)

        self.refresh_race()

        self.race_widget.mainloop()

    def refresh_race(self):
        """refreshes boatlist when creating a race"""
        self.count=0
        for boat in self.contestant_list:
            boat_button = Button(self.race_widget, text=f"{boat.name} {boat.sail}", state=DISABLED)
            boat_button.config(command=lambda b_button=boat_button, b=boat: self.race_button_press(b_button, b))
            boat_button.grid(column=1, row=self.count+2, sticky=EW)
            self.contestant_buttons.append(boat_button)
            self.count +=1
        self.start_button = Button(self.race_widget, text="Start Race", command=lambda: self.start_race(self.start_button))
        self.start_button.grid(column=1, row=self.count+2, sticky=EW)

    def race_time(self):
        """Displays race duration during the race"""
        time = datetime.now()-self.start
        time_label = Label(self.race_widget, text=f"Race Duration: {time}")
        time_label.grid(column=1, row=1)
        time_label.after(1000, self.race_time)

    def race_button_press(self, button, boat):
        """When the button is pressed the boat has finnished the race and the button becomes DISABLED"""
        button.config(state=DISABLED)
        self.race.race(boat, self.start)
        self.counter += 1
        if self.counter == self.count:
            self.race.result(racelist)
            self.race_widget.destroy()
            self.update_racelist()
            
    def start_race(self, startbutton):
        """When start button is pressed checks if there are atleast two boats and a name entered and otherwise starts the race"""
        try:
            if len(self.contestant_list) < 2:
                raise ValueError("Race need atleast 2 boats to start!")
            if not self.race_name.get():
                raise ValueError("Please enter a name for the race!")
            startbutton.config(state=DISABLED)
            self.start = datetime.now()
            self.race_time()
            for button in self.contestant_buttons:
                button.config(state=ACTIVE)
            self.race = race_module.Race(self.race_name.get())
            self.counter = 0
        except ValueError as e:
            self.error_msg(e)
        
    def boat_to_race(self):
        """Adds selected boat to active race creation"""
        try:
            cursor = self.list.curselection()
            selected_boat = boatlist[int(cursor[0]/5)]

            state = True
        except IndexError:
            self.error_msg("START a race and SELECT a boat from the list to add!")
            state = False

        try:
            for i in self.contestant_list:
                if selected_boat == i:
                    raise TypeError(f"{selected_boat.name} is already in the race! Please select another one.")
        except TypeError as e:
            self.error_msg(e)    
            state = False   

        if state:
            self.contestant_list.append(selected_boat)
            self.refresh_race()

    def delete_race(self):
        """Deletes the selected race"""
        try:
            cursor = self.races.curselection()
            selected_race = racelist[int(cursor[0])]
            racelist.remove(selected_race)
            self.update_racelist()
        except IndexError:
            self.error_msg("Please select a race for deletion!")

    def update_racelist(self):
        """Delete old racelist to insert new races from racelist"""
        self.races.delete(0, END)

        for i in racelist:
            self.races.insert(END, f"{i.name}")
            
    def leaderboard(self):
        """Creates a leaderboard where the result of a race is going to be displayed"""
        scroll = Scrollbar(self.root)
        scroll.grid(column=8, row=1,sticky=NS)
        label = Label(self.root, text="Leaderboard")
        label.grid(column=7, row=0, sticky=NSEW)
        self.board = Listbox(self.root, yscrollcommand=scroll.set, width=30, height=15)
        scroll.config(command=self.board.yview)

        self.board.grid(column=7, row=1)
        
    def display_race(self):
        """Displaying selected race on the leaderboard widget"""
        try:
            self.board.delete(0, END)
            cursor = self.races.curselection()
            selected_race = racelist[int(cursor[0])]
            count = 1
            for i in selected_race.recounted:
                self.board.insert(END, f"Placement: {count}")
                self.board.insert(END, f"{i.name}")
                self.board.insert(END, f"{selected_race.recounted[i]}")
                self.board.insert(END, "")
                count+=1
        except IndexError:
            self.error_msg("Please select a race to display!")

    def error_msg(self, error):
        """Display any error that occours"""
        messagebox.showerror("ERROR", f"{error}")

    def updateUI(self):
        self.root.mainloop()

myGUI=GUI() #Creating and running the main GUI
myGUI.boatlist()
myGUI.racelist()
myGUI.addboat()
myGUI.leaderboard()
myGUI.updateUI()

file_module.savefile(boatlist, "Boatlist.txt") #Saving the lists of object to files before closing down.
file_module.savefile(racelist, "Racelist.txt")