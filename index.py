#!/usr/bin/env python
# -*- coding: utf-8 -*-

#----------------------------------------------------------
#
#----------------------------------------------------------

from tkinter import *
from utils import app

def start():
    # get words from input and call the function start_search with those words
    worte = words_input.get()
    start_date = duration_start_input.get()
    end_date = duration_end_input.get()
    
    app.start_search(worte, start_date, end_date)


# ------------------
# create main window
# ------------------

window = Tk()
window.title("Hermann Hesse und die Musik")
window.geometry("600x200")

# Titellabel:
title_label = Label(window, text = "Hesse-Musikdatenbank", font=("Arial", 12, "bold"))
title_label.place(x = 10, y = 10)

# Wörter-Suche-Label:
words_label = Label(window, text = "Suche nach ")
words_label.place(x = 10, y = 50)

# Wörter-Suche-Eingabe-Feld:
words_input = Entry(window, width = 40)
words_input.place(x = 120, y = 48)

#Wörter-Suche-Hinweis-Button:
words_tip_button = Button(window, text = "Info", width = 4, command = app.show_info_word_search)
words_tip_button.place(x = 460, y = 44)

# Werke-Label
#works_label = Label(window, text = "in den folgenden Werken:")
#works_label.place(x = 10, y = 100)

# zeitraum von-Label
duration_start_label = Label(window, text = "Zeitraum von")
duration_start_label.place(x = 10, y = 100)

# zeitraum - Start - Input
duration_start_input = Entry(window, width = 10)
duration_start_input.place(x = 120, y = 98)

# zeitraum bis-Label
duration_end_label = Label(window, text = "bis")
duration_end_label.place(x = 240, y = 100)

# zeitraum bis-Input:
duration_end_input = Entry(window, width = 10)
duration_end_input.place(x = 300, y = 98)

#Zeitraum-Hinweis-Button:
duration_tip_button = Button(window, text = "Info", width = 4, command = app.show_info_date_search)
duration_tip_button.place(x = 460, y = 94)

# Such-Schaltfläche:
start_search_button = Button(window, text = "Starte Suche", width = 18, command = start)
start_search_button.place(x = 220, y = 150)

# Projekt-Info:
project_info_button = Button(window, text = "?", width = 2, command = app.show_version_info)
project_info_button.place(x = 530, y = 150)


# start program (main loop):
if __name__ == "__main__":
    window.mainloop()
