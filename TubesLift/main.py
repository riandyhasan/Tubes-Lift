import eel
import time

lantai = 1
lift = 1

@eel.expose
def naik():
    global lantai
    lantai += 1
    if (lantai >= 6):
        lantai = 6
    eel.update_text(str(lantai))

@eel.expose
def turun():
    global lantai
    lantai -= 1
    if (lantai <= 0):
        lantai = 1
    eel.update_text(str(lantai))

@eel.expose
def liftnaik ():
    global lantai
    global lift
    while (lift < lantai):
        lift += 1
        time.sleep(1)
        eel.update_lift(str(lift))

@eel.expose
def liftturun ():
    global lantai
    global lift
    while (lift > lantai):
        lift -= 1
        time.sleep(1)
        eel.update_lift(str(lift))



eel.init('lift')
eel.start('index.html', size=(320,520))