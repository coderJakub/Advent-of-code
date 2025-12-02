#!/bin/bash

# Prüfen ob Tag-Parameter übergeben wurde
if [ -z "$1" ]; then
    echo "Verwendung: ./run.sh <Tag>"
    echo "Beispiel: ./run.sh Day1"
    exit 1
fi

TAG="$1"
INPUTFILE="in.txt"

# Prüfen ob -t Flag gesetzt ist
if [ "$2" = "-t" ]; then
    INPUTFILE="test.txt"
fi

# Prüfen ob das Verzeichnis existiert
if [ ! -d "$TAG" ]; then
    echo "Fehler: Verzeichnis \"$TAG\" existiert nicht!"
    exit 1
fi

# Prüfen ob die Input-Datei existiert
if [ ! -f "$TAG/$INPUTFILE" ]; then
    echo "Fehler: Datei \"$TAG/$INPUTFILE\" existiert nicht!"
    exit 1
fi

# Out-Verzeichnis erstellen falls nicht vorhanden
if [ ! -d "out" ]; then
    mkdir out
fi

# Kompilieren
javac -d out helper/FileReader.java "$TAG/Solver.java"

# Prüfen ob Kompilierung erfolgreich war
if [ $? -ne 0 ]; then
    echo "Kompilierung fehlgeschlagen!"
    rm -rf out
    exit 1
fi

echo "Kompilierung erfolgreich!"
# Ausführen
java -cp out "$TAG.Solver" "$TAG/$INPUTFILE"

# Out-Verzeichnis löschen
rm -rf out