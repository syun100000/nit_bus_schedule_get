import requests
from bs4 import BeautifulSoup
import pytz
from datetime import datetime,timedelta

class BUS_GET:
    def __init__(self, type):
        self.type = type
        url = 'https://www.nit.ac.jp/campus/access/bus-schedule'
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        if type=="JR_station":
            elems = soup.select("#main > div > div.split-contents__main.bg-white.order-2 > div.bus_main > div.jr > table:nth-child(1)")
        elif type=="JR_campus":
            elems = soup.select("#main > div > div.split-contents__main.bg-white.order-2 > div.bus_main > div.jr > table:nth-child(2)")
        elif type=="TOBU_station":
            elems = soup.select("#main > div > div.split-contents__main.bg-white.order-2 > div.bus_main > div.tobu > table:nth-child(1)")
        elif type=="TOBU_campus":
            elems = soup.select("#main > div > div.split-contents__main.bg-white.order-2 > div.bus_main > div.tobu > table:nth-child(2)")
        self.bus_schedule = {}

        # We start at index 1 to skip the first column with the title
        for i, header in enumerate(elems[0].find_all('th')[1:], start=1):
            self.bus_schedule[f'{header.text}'] = []
            departure_times = elems[0].find_all('td')[i].find_all('li')
            for time in departure_times:
                self.bus_schedule[f'{header.text}'].append(time.text)

        self.timezone = pytz.timezone('Asia/Tokyo')
        self.bus_schedule_list = []
        for hour, minutes in self.bus_schedule.items():
            for minute in minutes:
                self.bus_schedule_list.append(datetime.strptime(f'{hour}:{minute}', '%H:%M'))
        self.bus_schedule_list.sort()

    def print(self):
        # Print the bus schedule
        for time, schedule in self.bus_schedule.items():
            print(f'{time}: {schedule}')
    
    def next_bus(self):
        now = datetime.now(self.timezone).time()  # We only care about the time
        for bus_time in self.bus_schedule_list:
            if bus_time.time() > now:
                return bus_time.strftime('%H:%M')
        return '本日の運行は終了しました。'

    def next_next_bus(self):
        now = datetime.now(self.timezone).time()  # We only care about the time
        bus_times_after_now = [bus_time for bus_time in self.bus_schedule_list if bus_time.time() > now]
        
        if len(bus_times_after_now) > 1:
            return bus_times_after_now[1].strftime('%H:%M')
        return '本日の運行は終了しました。'
 


