import file_module
from datetime import datetime


class Race:
    """Creates a race object that has functions to make a list of contestants and calculate a result"""
    def __init__(self, name):
        self.name = name
        pass

    def contestants(self):
        """Checks if contesants are in the list of available boats and then appends them to the contestants list"""
        list = file_module.loadfile("Boatlist.txt")
        self.cont_list = []
        number = int(input("Number of contestants: "))
        count = 1
        for i in range(number):
            contestant = input(f"Contestant nr{count}: ")
            for x in list:
                print(x)
                if x.name == contestant:
                    self.cont_list.append(x)
            count += 1

    def result(self, list):
        """Calculates the recounted times with the realtimes from the race"""
        self.recounted = {}
        for i in self.finish_times:
            newtime = i.srs*self.finish_times[i]
            self.recounted.update({i:newtime})
        self.recounted = {k: v for k, v in sorted(self.recounted.items(), key=lambda item: item[1])}
        list.append(self)

    def show_result(self):
        counter = 1
        for i in self.recounted:
            print(f"Placement: {counter} \nBoat: {i.name}\nTime: {self.recounted[i]}")
            counter += 1

    def race(self):
        """Runs the race and saves each boats time delta to start time in a key:value dict"""
        self.finish_times = {}
        start = datetime.now()
        count = 0
        while count < len(self.cont_list):
            print("To finish race, press representing key")
            for i in self.cont_list:
                print(f"{i.name}: {i.sail}")
            
            finish = input(": ")
            for i in self.cont_list:
                if finish == i.sail:
                    racetime = datetime.now()-start
                    self.finish_times.update({i:racetime})
                    count += 1