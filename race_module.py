import file_module
from datetime import datetime


class Race:
    """Creates a race object that has functions to make a list of contestants and calculate a result"""
    def __init__(self, name):
        self.name = name
        pass

    def result(self, list):
        """Calculates the recounted times with the realtimes from the race"""
        self.recounted = {}
        for i in self.finish_times:
            newtime = i.srs*self.finish_times[i]
            self.recounted.update({i:newtime})
        self.recounted = {k: v for k, v in sorted(self.recounted.items(), key=lambda item: item[1])}
        list.append(self)

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