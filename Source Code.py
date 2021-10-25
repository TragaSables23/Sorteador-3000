from tkinter import *
import random
import string

def clicked():

    vs = [plyr1.get(), plyr2.get(), plyr3.get(), plyr4.get(),plyr5.get(), plyr6.get(), plyr7.get(),plyr8.get()]

    for x in range(0,45):
        random.shuffle(vs)

    sorteo_1 = vs[0] + " VS " + vs[1]
    vs.pop(0)
    vs.pop(0)
    sorteo_2 = vs[0] + " VS " + vs[1]
    vs.pop(0)
    vs.pop(0)
    sorteo_3 = vs[0] + " VS " + vs[1]
    vs.pop(0)
    vs.pop(0)
    sorteo_4 = vs[0] + " VS " + vs[1]
    vs.pop(0)
    vs.pop(0)


    lb1.configure(text=sorteo_1)
    lb2.configure(text=sorteo_2)
    lb3.configure(text=sorteo_3)
    lb4.configure(text=sorteo_4)

window = Tk()

window.title("Sorteo")

window.geometry('500x200')

lb1 = Label(window, text="Made By Kanata")
lb2 = Label(window, text="Made By Kanata")
lb3 = Label(window, text="Made By Kanata")
lb4 = Label(window, text="Made By Kanata")

lb5 = Label(window, text="      ||      ")
lb6 = Label(window, text="      ||      ")
lb7 = Label(window, text="      ||      ")
lb8 = Label(window, text="      ||      ")

plyr1txt = Label(window, text="Jugador 1: ")
plyr2txt = Label(window, text="Jugador 2: ")
plyr3txt = Label(window, text="Jugador 3: ")
plyr4txt = Label(window, text="Jugador 4: ")
plyr5txt = Label(window, text="Jugador 5: ")
plyr6txt = Label(window, text="Jugador 6: ")
plyr7txt = Label(window, text="Jugador 7: ")
plyr8txt = Label(window, text="Jugador 8: ")

btn = Button(window, text="Sortear", command=clicked)

plyr1 = Entry(window,width=20)
plyr2 = Entry(window,width=20)
plyr3 = Entry(window,width=20)
plyr4 = Entry(window,width=20)
plyr5 = Entry(window,width=20)
plyr6 = Entry(window,width=20)
plyr7 = Entry(window,width=20)
plyr8 = Entry(window,width=20)

lb1.grid(column=0, row=0, sticky='w')
lb2.grid(column=0, row=1, sticky='w')
lb3.grid(column=0, row=2, sticky='w')
lb4.grid(column=0, row=3, sticky='w')

lb5.grid(column=1, row=0, sticky='w')
lb6.grid(column=1, row=1, sticky='w')
lb7.grid(column=1, row=2, sticky='w')
lb8.grid(column=1, row=3, sticky='w')

plyr1txt.grid(column=2, row=0, sticky='w')
plyr2txt.grid(column=2, row=1, sticky='w')
plyr3txt.grid(column=2, row=2, sticky='w')
plyr4txt.grid(column=2, row=3, sticky='w')
plyr5txt.grid(column=2, row=4, sticky='w')
plyr6txt.grid(column=2, row=5, sticky='w')
plyr7txt.grid(column=2, row=6, sticky='w')
plyr8txt.grid(column=2, row=7, sticky='w')

plyr1.grid(column=3, row=0, sticky='w')
plyr2.grid(column=3, row=1, sticky='w')
plyr3.grid(column=3, row=2, sticky='w')
plyr4.grid(column=3, row=3, sticky='w')
plyr5.grid(column=3, row=4, sticky='w')
plyr6.grid(column=3, row=5, sticky='w')
plyr7.grid(column=3, row=6, sticky='w')
plyr8.grid(column=3, row=7, sticky='w')

btn.grid(column=6, row=4)

window.mainloop()
