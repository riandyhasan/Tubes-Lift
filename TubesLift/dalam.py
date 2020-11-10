import eel

lantai = 1

@eel.expose
def naik():
    global lantai
    lantai += 1
    eel.update_text(str(lantai))

def turun():
    global lantai
    lantai -= 1
    eel.update_text(str(lantai))


eel.init('lift')
eel.start('dalam.html', size=(320,520))