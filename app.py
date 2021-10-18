#!/usr/bin/env python
# -*- coding: utf-8 -*-

#----------------------------------------------------------
#
#----------------------------------------------------------
import os
from tkinter import *
import sqlite3
from sqlite3 import Error
# import datetime
import webbrowser



def show_version_info():

    version_info_window = Toplevel()
    version_info_window.title("Über das Projekt")
    version_info_window.geometry("380x160")
    
    info_text = Label(version_info_window, text = "Autor: Moritz Ott\nLizenz: MIT\nVersion: 0.0.1")
    info_text.pack(pady = 10)
    visit_website = "Projektseite besuchen"
    open_website_project = Button(version_info_window, text=visit_website, command=lambda: webbrowser.open_new_tab("https://github.com/moritzott/hesse-musikdatenbank"))
    open_website_project.pack(pady=5)
    
    
    close_version_window = Button(version_info_window, text = "OK", command = version_info_window.destroy)
    close_version_window.pack(pady=5)

def show_info_word_search():
    # new window to show info:
    word_info_window = Toplevel()
    word_info_window.title("Wörtersuche")
    word_info_window.geometry("260x160")
    info_text = Label(word_info_window,
                      text = "Geben Sie die Wörter\nmit einem Leerzeichen voneinander\ngetrennt ein, z. B.: Musik Klavier ...\nGroß- oder Kleinschreibung\nspielt keine Rolle.")
    info_text.pack(pady = 10)
    info_close_button = Button(word_info_window, text = "OK", command = word_info_window.destroy)
    info_close_button.pack()

def show_info_date_search():
    # new window to show date info:
    date_info_window = Toplevel()
    date_info_window.title("Jahresangaben")
    date_info_window.geometry("260x130")
    info_text = Label(date_info_window, text = "Diese Angaben sind optional.\n Geben Sie bitte nur vierstellige Jahres-\nzahlen ein, z. B. 1923, ...")
    info_text.pack(pady = 10)
    info_close_button = Button(date_info_window, text = "OK", command = date_info_window.destroy)
    info_close_button.pack()

def create_warning_window():
    warning_window = Toplevel()
    warning_window.title("Hoppla...")
    warning_window.geometry("350x100")
    info_text = Label(warning_window, text = "Sie haben keine Suchbegriffe eingegeben!")
    info_text.pack(pady = 10)
    warning_window_close_button = Button(warning_window, text = "OK", command = warning_window.destroy)
    warning_window_close_button.pack()
    
def create_date_error_window():
    warning_window = Toplevel()
    warning_window.title("Ja, ja ... die Jahresangaben")
    warning_window.geometry("350x100")
    info_text = Label(warning_window, text = "Ihre Jahresangaben sind fehlerhaft!")
    info_text.pack(pady = 10)
    warning_window_close_button = Button(warning_window, text = "OK", command = warning_window.destroy)
    warning_window_close_button.pack()

def show_results_info(res, search_words):

    # to open the right file with a webbrowser: reconstructing the name of the file...
    searched_words_string = "-".join(search_words)


    # open new window and show results (res) info:
    result_window = Toplevel()
    result_window.title("Ergebnisse")
    result_window.geometry("400x200")
    your_results_label = Label(result_window, text = "Ihre Ergebnisse:")
    your_results_label.pack(pady = 10)
    results_counter = len(res)
    results_counter_label = Label(result_window, text = f"{results_counter} Ergebnis(se) gefunden")
    results_counter_label.pack()
    # Nur in eine Datei schreiben, wenn auch Ergebnisse vorhanden sind! Option zum Öffnen der Ergebnisse einfügen
    save_destination_label = Label(result_window, text = "Die Resultate wurden in den\n 'ergebnisse'-Ordner geschrieben.")
    save_destination_label.pack()
    open_results_button = Button(result_window, text="Ergebnis öffnen", command=lambda: webbrowser.open(f"./ergebnisse/ergebnis-{searched_words_string}.txt"))
    open_results_button.pack(pady=1)
    confirm_button = Button(result_window, text = "OK", command = result_window.destroy)
    confirm_button.pack(pady = 15)

def write_results_to_file(res, words, start, end):
    # schreibe Resultate (res) in eine txt-Datei im Ordner "ergbnisse":

    # überprüfe, ob der Ordner schon existiert; wenn nicht, erstelle ihn, ansonsten fahre fort
    if not os.path.isdir("./ergebnisse"):
        os.mkdir("ergebnisse")

    # wechsle in den Ordner "ergebnisse":
    os.chdir("./ergebnisse")

    #print(f"Aktuelles Arbeitsverzeicnis: {os.getcwd()}")
    
    # Dateiname soll aus dem Wort "ergebnis-" und den Suchwörtern mit "-" getrent als Textdatei gespeichert werden
    searched_words_string = "-".join(words)
    filename = f"ergebnis-{searched_words_string}.txt"
    
    
    # given parameter res (results) is a list of tuples
    results_list = res
    
    
    # create or overwrite file
    results_file = open(filename, "w")
    
    results_file.write(f"Ihre Suchergebnisse ({len(results_list)}):\n===================================================\n")
    results_file.write(f"Sie suchten nach den Wörtern: ")
    for word in words:
        results_file.write(f"{word} ")
    results_file.write(f"\nin Werken Hesses im Zeitraum zwischen {start} und {end}.\n")
    results_file.write("\n")
    results_file.write("====================================================\n")
    results_file.write("====================================================\n")
    results_file.write("\n\n\n")

    # write results (res) to the file
    # but it is an list, so we have to iterate throuh the list
    for item in results_list:
        
        # now we get a tuple for each result in the result list
        
        # create list with item names which
        # match the position of results_list:
        item_names = ["Text", "Werk/Titel", "Art", "Datierung", "Ausgabe", "Schlagworte"]
        
        # print like: Werk/Titel: Der Steppenwolf (19XX)
        results_file.write(f"{item_names[1]}: {item[1]} ({str(item[3])})\n")
        # print type of source (poem, roman, ...)
        results_file.write(f"{item_names[2]}: {item[2]}\n")
        # print key words:
        results_file.write(f"{item_names[5]}: {item[5]}\n\n\n")
        
        # print text content
        results_file.write(item[0])
        results_file.write("\n\n\n")
        # print Ausgabe: in: Mueller, S. 34...
        results_file.write(item[4])
        
        # marker: next item
        results_file.write("\n\n\n\n")
        results_file.write("-------------------------------------------------\n")
        results_file.write("\n\n\n\n")

    # close the file
    results_file.close()

    # wechsel wieder ein Verzeichnis nach oben
    os.chdir("..")

    # gibt das aktuelle Arbeitsverzeichnis aus:
    #print(f"Aktuelles Arbeitsverzeichnis: {os.getcwd()}")
    
    
    

def query_database(searched_words, start_date, end_date):
    try:
        sql_query_base = "SELECT DISTINCT Text, Werk, Art, Datierung, Ausgabe, Schlagworte FROM Textstellen WHERE ( Text "
        # complete sql query base with LKE patterns and wildcards ?
        for word in searched_words:
            sql_query_base += "LIKE ? AND Text "
        # letztes überschüssiges 'AND Text' entfernen:
        sql_query = sql_query_base[:-9]
        
        # Klammer schließen bei WHERE-Klausel:
        sql_query += ")"
        
        # OR-Klausel hinzufügen und Anfang der Schlagwörter:
        sql_query += " OR (Schlagworte "
        
        # for-Schleife wie oben: nur jetzt wird eben nach Schlagwörtern
        # gesucht:
        for word in searched_words:
            sql_query += "LIKE ? AND Schlagworte "
        
        # letztes überschüssiges 'AND Schlagworte' entfernen:
        sql_query = sql_query[:-16]
        
        # schließende Klammer setzen
        sql_query += ")"
        
        # Datierungseinschränkung:
        sql_query += " AND Datierung BETWEEN ? AND ?"

        # Ausgabe nach Werken ordnen (alphabetisch): // vielleicht besser nach Jahreszahlen ordnen?? Nutzer entscheiden lassen?
        sql_query += " ORDER BY Werk ASC "

        # semikolon am Ende hinzufügen
        sql_query += " ;"
        print(f"SQL-Query: {sql_query}")

        # SQL Searching values        
        sql_values = []

        # change list for sql-query-pattern (add %word%, %word2%, %word3% then repeat: %word%, %word2%)
        # important: 2 times!! because every word will be searched in
        # 'Text' and 'Schlagworte'
        for times in range(2):
            for word in searched_words:
                word_value = "%" + word + "%"
                sql_values.append(word_value)
        
        # finally append the start and end date:
        sql_values.append(start_date)
        sql_values.append(end_date)

        print(f"SQL-Values: {sql_values}")

        # Verbindung zur Datenbank und Cursor setzen
        db = sqlite3.connect("hesse-musik.db")
        cursor = db.cursor()

        # execute sql-query with the searched patterns (sql_values)
        cursor.execute(sql_query, (sql_values))
        results = cursor.fetchall()
        
        # results seems to be list of tuples:
        print(type(results))
        
        #print(f"Gefunden: {results}")
        #for item in results:
            #print(str(item))

    except Error as e:
        # falls Fehler da, ausgaben:
        print(e)
    finally:
        # Datenbank zum Schluss immer schließen!
        db.close()

    # schreibe die Ergebnisse in eine txt-Datei:
    # muss ein string sein!
    write_results_to_file(results, searched_words, start_date, end_date)
    
    # Info der Anzahl der Ergebnisse in separatem Fenster:
    show_results_info(results, searched_words)




# function start search:
def start_search(words, start_date, end_date):
    #test
    print("Die Suche geht los...")
    #print(start_date)
    #print(end_date)
    #sql_input = ""
    # lese Wörter aus Eingabefeld
    #words = words_input.get()
    words_array = words.split() # nach Leerzeichen getrennt in einen Array gschrieben
    print(f"Wir suchen nachen den Wörtern: {words}") # nur für debugging
    #print(words_array) # only for debugging
    print(f"Im Zeitraum von {start_date} bis {end_date}")
    print(type(start_date))
    #print(int(start_date))
    

    # Hier, abfangen, falls keine Suchwörter-Parameter übergeben worden sind!!
    if len(words) == 0:
        # Fenster mit Warnung geben, dass keine Parameter ausgegeben worden sind!
        create_warning_window()
    else:
        # ist eine Zeit angegeben? und richtig? wenn beide leer sind?
        # dann als standard wert für start_date sein Geburtsjahr und
        # für end_date das aktuelle Jahr nehmen
        try:
            # wenn keine Zahl angegeben: dann setze als
            # start-Datum Hesses Geburtsjahr
            if start_date == "":
                start_date = int(1877)
            # wenn kein End-Datum: setze das aktuelle Jahr
            if end_date == "":
                end_date = int(2021)
            
            # Typkonvertiereung:
            start_date = int(start_date)
            end_date = int(end_date)
            
            # Ausgabe des Start- und Endejahr mitsamt des Typs
            print(start_date, type(start_date))
            print(end_date, type(end_date))
            
            query_database(words_array, start_date, end_date)
            
        except ValueError:
            create_date_error_window()
        