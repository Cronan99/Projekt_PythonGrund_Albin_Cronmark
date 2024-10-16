from datetime import datetime

class Race:
    """Creates a race object that has functions to give boats finishing times and sort them in order by time"""
    def __init__(self, name):
        self.name = name
        self.finish_times = {}
        pass

    def result(self, list):
        """Calculates the recounted times with the realtimes from the race"""
        self.recounted = {}
        for i in self.finish_times:
            newtime = float(i.srs)*self.finish_times[i]
            self.recounted.update({i:newtime})
        self.recounted = {k: v for k, v in sorted(self.recounted.items(), key=lambda item: item[1])}
        list.append(self)

    def race(self, boat, start):
        """Runs the race and saves each boats time delta to start time in a key:value dict"""
        finish = datetime.now()
        racetime = finish-start
        self.finish_times.update({boat:racetime})