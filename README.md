# Hermann Hesse und die Musik
Dieses Repositorium enthält eine Musikdatenbank mit Texten von Hermann Hesse über die Musik (eigene Aussagen und von fiktiven Erzählpersonen).
![Beispiel](https://github.com/moritzott/hesse-musikdatenbank/blob/main/img/hesse-beispiel.png)

**Wichtig**: Die Datenbank befindet sich erst im Aufbau, genauso wie das dazugehörige Python-Programm, mit der die Datenbank komfortabel befragt werden kann.

## Beschreibung


* Export in 'ergebnisse.txt'-Datei

## Technische Informationen
* Die Datenbank "hesse-musik.db" ist eine SQLite3-Datenbank.
* Die graphische Nutzeroberfläche zur Befragung der Datenbank ist in Python (mit tkinter) erstellt worden.
* Die Anwendung besteht aus drei Dateien: der Datenbank (hesse-musik.db), der index.py-Datei und der app.py-Datei. Die index.py-Datei enthält die grundlegenden Elemente für die graphische Nutzeroberfläche und den Start des Programms. In der app.py-Datei sind die Funktionen und Unterprogramme ausgelagert (eventuell werde ich bei entstprechender Größe die zwei Python-Dateien doch wieder zusammenlegen).


## Ziele
* eine Datebank mit Musiktextstellen von Hermann Hesse erstellen
* ein Programm zum druchförsten der Datenbank erstellen
* besseres Verständnis kriegen: Wie speichert man Daten, damit diese auch in 20-30 Jahren noch auslesbar sind? Stichwort: Forschungsdatenmanagement
* Anregungen für ähnliche Projekte erhalten
* sicherstellen, dass die Datenbank und die Anwendung auch noch in ferner Zukunft läuft und einfach zu installieren bzw. zu bedienen ist
* meine Python/tkinter/SQLite-Kenntnisse am Köcheln halten

## Noch zu machen:
* verständliche Bedienungsanleitung schreiben (LaTeX)
* Datenbank befüllen mit weiteren Textstellen (Buchliste abarbeiten)
* Suchwörter auch in Schlagwörter suchen (SQL-Query erweitern)
* weitere Filteroption: Nur in bestimmten Werken suchen (Werkliste erstellen und als SQL-Query hinzufügen)
* Datierungssuche (von ... bis ...) funktioniert noch nicht
* nach Erstellen einer 'ergebnisse.txt'-Datei einen Schalter anbieten, zum einfachen Öffnen des Verzeichnisses
* automatische Umbenennung der 'ergebnisse.txt'-Datei, falls schon eine existiert; momentan wird überschrieben
* zum Abschluss des Python-Programmes: einfache Installationsdateien für Windows- MacOS- und Linux-Nutzer erstellen
