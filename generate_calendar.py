from datetime import datetime
from ics import Calendar, Event

cal = Calendar()

e = Event()
e.name = "Teste Premier Padel"
e.begin = datetime.now()
e.end = datetime.now()

cal.events.add(e)

with open("premier_padel_live.ics", "w") as f:
    f.writelines(cal)

print("Calendário criado!")
