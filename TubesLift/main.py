import eel

lantai = 1

@eel.expose
def naik():
    global lantai
    lantai += 1
    eel.update_text(str(lantai))
    if (lantai == 4):
        eel.init('lift')
        eel.start('dalam.html', size=(320,520))
    
def turun():
    global lantai
    lantai -= 1
    eel.update_text(str(lantai))


eel.init('lift')
eel.start('index.html', size=(320,520))