@echo off
setlocal

:: Prüfen ob Tag-Parameter übergeben wurde
if "%1"=="" (
    echo Verwendung: run.bat ^<Tag^>
    echo Beispiel: run.bat Day1
    exit /b 1
)

set TAG=%1
set INPUTFILE=in.txt

:: Prüfen ob -t Flag gesetzt ist
if "%2"=="-t" set INPUTFILE=test.txt

:: Prüfen ob das Verzeichnis existiert
if not exist "%TAG%" (
    echo Fehler: Verzeichnis "%TAG%" existiert nicht!
    exit /b 1
)

:: Prüfen ob die Input-Datei existiert
if not exist "%TAG%\%INPUTFILE%" (
    echo Fehler: Datei "%TAG%\%INPUTFILE%" existiert nicht!
    exit /b 1
)

:: Out-Verzeichnis erstellen falls nicht vorhanden
if not exist "out" mkdir out

:: Kompilieren
javac -d out helper/FileReader.java %TAG%/Solver.java

:: Prüfen ob Kompilierung erfolgreich war
if %errorlevel% neq 0 (
    echo Kompilierung fehlgeschlagen!
    rmdir /s /q out
    exit /b 1
)

echo Kompilierung erfolgreich!
:: Ausführen
java -cp out %TAG%.Solver %TAG%/%INPUTFILE%

:: Out-Verzeichnis löschen
rmdir /s /q out

endlocal