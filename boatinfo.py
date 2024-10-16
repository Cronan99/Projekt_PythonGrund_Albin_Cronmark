class Boat:
    """Creates boat object with a shipname, handicap(srs) and a crew"""
    def __init__(self, name, sail, srs, crew):
        self.name = name
        self.sail = sail
        self.srs = srs
        self.crew = crew
        pass
    
def new_boat(list, name, sail, srs, crew):
    """Creates a new ship and adds it to the boatlist"""
    boat = Boat(name, sail, srs, crew)
    list.insert(0, boat)