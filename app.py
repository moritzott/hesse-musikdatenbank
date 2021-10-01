#!/usr/bin/env python
# -*- coding: utf-8 -*-

#----------------------------------------------------------
#
#----------------------------------------------------------
from tkinter import *
import sqlite3
from sqlite3 import Error

# funktionen des button vielleicht in anderer Datei? -> import

def show_version_info():
    version_info_window = Toplevel()
    version_info_window.title("Über das Projekt")
    version_info_window.geometry("240x120")
    info_text = Label(version_info_window, text = "Autor: Moritz Ott\nLizenz: MIT\nVersion: 0.0.1")
    info_text.pack(pady = 10)
    close_version_window = Button(version_info_window, text = "OK", command = version_info_window.destroy)
    close_version_window.pack()

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

def show_results_info(res):
    # open new window and show results (res) info:
    result_window = Toplevel()
    result_window.title("Ergebnisse")
    result_window.geometry("400x200")
    your_results_label = Label(result_window, text = "Ihre Ergebnisse:")
    your_results_label.pack(pady = 10)
    results_counter = len(res)
    results_counter_label = Label(result_window, text = f"{results_counter} Ergebniss(e) gefunden")
    results_counter_label.pack()
    # Nur in eine Datei schreiben, wenn auch Ergebnisse vorhanden sind! Option zum Öffnen der Ergebnisse einfügen
    save_destination_label = Label(result_window, text = "Die Resultate wurden in die\n 'ergebnisse.txt'-Datei geschrieben.\n Sie befindet sich im selben Verzeichnis wie die Datenbank.")
    save_destination_label.pack()
    confirm_button = Button(result_window, text = "OK", command = result_window.destroy)
    confirm_button.pack(pady = 15)

def write_results_to_file(res):
    # schreibe Resultate (res) in eine txt-Datei
    # wichtig hier: Überschreibe-Modus!
    # Nutzer noch darauf hinweisen!!
    
    # given parameter res (results) is a list of tuples
    results_list = res
    
    
    # create or overwrite file
    results_file = open("ergebnisse.txt", "w")
    
    results_file.write(f"Ihre Suchergebnisse ({len(results_list)}):\n========================\n\n\n\n")

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

        # text content is on the first position of the tuple:
        #results_file.write(item[0])
        # to get the strings inside the tuple, we need to iterate through
        # that tuple:
        #for string in item:
         #   results_file.write(string) # no need to convert!
            
            
        # Alternative item[x] -> then write someting like Year: iitem[2]
        
        #results_file.write(str(type(item)))
        #results_file.write("\n")
        
        #results_file.write(str(item))
#         results_file.write("\n")
#         results_file.write("WERK:\n------\n")
#         results_file.write(item[1])
#         results_file.write("\n")        
#         results_file.write("ART:\n------\n")
#         results_file.write(item[2])
#         results_file.write("\n")
#         results_file.write("DATIERUNG:\n------\n")
#         results_file.write(str(item[3]))
#         results_file.write("\n")
#         results_file.write("AUSGABE:\n------\n")
#         results_file.write(item[4])
#         results_file.write("\n")
#         results_file.write("SCHLAGWORTE:\n------\n")
#         results_file.write(item[5])
#         results_file.write("\n")
#         results_file.write("===========")
#         results_file.write("\n\n")
        
    
    
    # close the file
    results_file.close()

def query_database(searched_words):
    try:
        sql_query_base = "SELECT DISTINCT Text, Werk, Art, Datierung, Ausgabe, Schlagworte FROM Textstellen WHERE Text "
        # complete sql query base with LKE patterns and wildcards ?
        for word in searched_words:
            sql_query_base += "LIKE ? AND Text "
        # letztes überschüssiges 'AND Text' entfernen:
        sql_query = sql_query_base[:-9]

        # semikolon am Ende hinzufügen
        sql_query += ";"
        print(f"SQL-Query: {sql_query}")

        sql_values = []

        # change list for sql-query-pattern (add %word%, %word2%, %word3%)
        for word in searched_words:
            word_value = "%" + word + "%"
            sql_values.append(word_value)

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
    write_results_to_file(results)
    
    # Info der Anzahl der Ergebnisse in separatem Fenster:
    show_results_info(results)




# function start search:
def start_search(words):
    #test
    print("Die Suche geht los...")
    #sql_input = ""
    # lese Wörter aus Eingabefeld
    #words = words_input.get()
    words_array = words.split() # nach Leerzeichen getrennt in einen Array gschrieben
    print(f"Wir suchen nachen den Wörtern: {words}") # nur für debugging
    #print(words_array) # only for debugging

    # Hier, abfangen, falls keine Parameter übergeben worden sind!!
    if len(words) == 0:
        # Fenster mit Warnung geben, dass keine Parameter ausgegeben worden sind!
        create_warning_window()
    else:
        query_database(words_array)
