from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from BusSchedule_getter import BUS_GET
from datetime import datetime

__version__ = '0.1.2'

app = Flask(__name__)
nowtime=datetime.now()
print(nowtime)
@app.route('/')
def home():
    bus_schedule_JR_S = BUS_GET("JR_station")
    bus_schedule_JR_C = BUS_GET("JR_campus")
    bus_schedule_TOBU_S = BUS_GET("TOBU_station")
    bus_schedule_TOBU_C = BUS_GET("TOBU_campus")

    next_bus_JR_S = bus_schedule_JR_S.next_bus()
    next_bus_JR_C = bus_schedule_JR_C.next_bus()
    next_bus_TOBU_S = bus_schedule_TOBU_S.next_bus()
    next_bus_TOBU_C = bus_schedule_TOBU_C.next_bus()

    next_next_bus_JR_S = bus_schedule_JR_S.next_next_bus()
    next_next_bus_JR_C = bus_schedule_JR_C.next_next_bus()
    next_next_bus_TOBU_S = bus_schedule_TOBU_S.next_next_bus()
    next_next_bus_TOBU_C = bus_schedule_TOBU_C.next_next_bus()
    
    

    return render_template('index.html', 
                           next_bus_JR_S=next_bus_JR_S, 
                           next_bus_JR_C=next_bus_JR_C,
                           next_bus_TOBU_S=next_bus_TOBU_S, 
                           next_bus_TOBU_C=next_bus_TOBU_C,
                           next_next_bus_JR_S=next_next_bus_JR_S,
                           next_next_bus_JR_C=next_next_bus_JR_C,
                           next_next_bus_TOBU_S=next_next_bus_TOBU_S,
                           next_next_bus_TOBU_C=next_next_bus_TOBU_C,)

if __name__ == '__main__':
    app.run(debug=True)
