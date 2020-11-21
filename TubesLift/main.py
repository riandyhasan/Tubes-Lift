import eel
import time


user = 1
lift = 1
lantai = [1, 2, 3, 4, 5, 6]


@eel.expose
def display():
    global lift
    eel.display(lift)

@eel.expose
def userdis():
    global user
    eel.update_user(user)

@eel.expose
def naik():
    global user
    user += 1
    if (user >= 6):
        user = 6
    eel.update_text(user)

@eel.expose
def turun():
    global user
    user -= 1
    if (user <= 0):
        user = 1
    eel.update_text(user)

@eel.expose
def liftnaik ():
    global user
    global lift
    if (lift < user):
        while (lift != user):
            lift += 1
            time.sleep(1)
            eel.update_lift(lift)
        time.sleep(1)
    elif (lift > user):
        while (lift != user):
            lift -= 1
            time.sleep(1)
            eel.update_lift(lift)
        time.sleep(1)


@eel.expose
def liftturun ():
    global user
    global lift
    if (lift > user):
        while (lift != user):
            lift -= 1
            time.sleep(1)
            eel.update_lift(lift)
        time.sleep(1)
    elif (lift < user):
        while (lift != user):
            lift += 1
            time.sleep(1)
            eel.update_lift(lift)
        time.sleep(1)



@eel.expose
def satu ():
    global lift
    global lantai
    if (lantai[0] < lift):
        while (lantai[0] != lift):
            lift -= 1
            time.sleep(1)
            eel.update_lift(lift)
        time.sleep(1)

@eel.expose
def dua ():
    global lift
    global lantai
    if (lantai[1] > lift):
        while (lantai[1] != lift):
            lift += 1
            time.sleep(1)
            eel.update_lift(lift)
        time.sleep(1)
        
    elif (lantai[1] < lift):
        while (lantai[1] != lift):
            lift -= 1
            time.sleep(1)
            eel.update_lift(lift)
        time.sleep(1)


@eel.expose
def tiga ():
    global lift
    global lantai
    if (lantai[2] > lift):
        while (lantai[2] != lift):
            lift += 1
            time.sleep(1)
            eel.update_lift(lift)
        time.sleep(1)
        
    elif (lantai[2] < lift):
        while (lantai[2] != lift):
            lift -= 1
            time.sleep(1)
            eel.update_lift(lift)
        time.sleep(1)


@eel.expose
def empat ():
    global lift
    global lantai
    if (lantai[3] > lift):
        while (lantai[3] != lift):
            lift += 1
            time.sleep(1)
            eel.update_lift(lift)
        time.sleep(1)
        
    elif (lantai[3] < lift):
        while (lantai[3] != lift):
            lift -= 1
            time.sleep(1)
            eel.update_lift(lift)
        time.sleep(1)


@eel.expose
def lima ():
    global lift
    global lantai
    if (lantai[4] > lift):
        while (lantai[4] != lift):
            lift += 1
            time.sleep(1)
            eel.update_lift(lift)
        time.sleep(1)
        
    elif (lantai[4] < lift):
        while (lantai[4] != lift):
            lift -= 1
            time.sleep(1)
            eel.update_lift(lift)
        time.sleep(1)

@eel.expose
def enam ():
    global lift
    global lantai
    if (lantai[5] > lift):
        while (lantai[5] != lift):
            lift += 1
            time.sleep(1)
            eel.update_lift(lift)
        time.sleep(1)

eel.init('lift')
eel.start('luar.html', size=(320,520))