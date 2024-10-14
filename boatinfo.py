class Boat:
    """Creates boat object with a shipname, handicap(srs) and a crew"""
    def __init__(self, name, sail, srs, crew):
        self.name = name
        self.sail = sail
        self.srs = srs
        self.crew = crew
        pass
    
    def info(self):
        return f"Boat: {self.name}   Sailnumber: {self.sail}   SRS: {self.srs}   Crew: {self.crew}"
    
def new_boat(list, name, sail, srs, crew):
    """Creates a new ship and adds it to the boatlist"""
    boat = Boat(name, sail, srs, crew)
    list.insert(0, boat)

def delete_boat(list, boat):
    """Deletes the boat from the boatlist if it exists, takes the list as an argument"""
    removed = False
    for i in list:
        """i[0] = NAME"""
        if i.name == boat:
            list.remove(i)
            removed = True
    if removed == False:
        print(f"Couldn't find: {boat}")

def find_boat(list, search):
    """Finds and returns the specified boat by name"""
    for i in list:
        if search == i.name:
            return i