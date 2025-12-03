@echo off
setlocal enabledelayedexpansion

:: Check if day-parameter was passed
if "%1"=="" (
    echo Usage: runDay ^<day-number^> [-c] [-j] [-p]
    echo.
    echo Flags:
    echo   -c    Execute C-implementation
    echo   -j    Execute Java-implementation
    echo   -p    Execute Python-implementation
    echo.
    echo Default: Python-implementation
    exit /b 1
)

:: Format day number with leading zero
set DAY_NUM=%1
if %DAY_NUM% LSS 10 (
    set DAY=Day0%DAY_NUM%
) else (
    set DAY=Day%DAY_NUM%
)

set RUN_C=false
set RUN_JAVA=false
set RUN_PYTHON=false
set INPUTFILE=in.txt

:: Parse flags
shift
:parse_flags
if "%1"=="" goto end_parse
if "%1"=="-c" (
    set RUN_C=true
    shift
    goto parse_flags
)
if "%1"=="-j" (
    set RUN_JAVA=true
    shift
    goto parse_flags
)
if "%1"=="-p" (
    set RUN_PYTHON=true
    shift
    goto parse_flags
)
echo Unknown flag: %1
exit /b 1

:end_parse

:: Default: Execute Python
if "%RUN_C%"=="false" if "%RUN_JAVA%"=="false" if "%RUN_PYTHON%"=="false" (
    set RUN_PYTHON=true
)

:: Check whether the directory exists
if not exist "%DAY%" (
    echo Error: directory "%DAY%" does not exist!
    exit /b 1
)

:: Check whether the input file exists
if not exist "%DAY%\%INPUTFILE%" (
    echo Error: file "%DAY%\%INPUTFILE%" does not exist!
    exit /b 1
)

if not exist "out" mkdir out

:: Execute C if enabled
if "%RUN_C%"=="true" (
    echo ****************************************
    echo *            C Implementation          *
    echo ****************************************
    
    if not exist "%DAY%\Solver.c" (
        echo Error: file "%DAY%\Solver.c" does not exist!
    ) else (
        gcc -o out\solver.exe helper\FileReader.c "%DAY%\Solver.c"
        
        if !errorlevel! neq 0 (
            echo Compilation failed!
        ) else (
            set START_TIME=!time!
            out\solver.exe "%DAY%\%INPUTFILE%"
            set END_TIME=!time!

            call :calculate_duration "!START_TIME!" "!END_TIME!"
            echo Duration: !DURATION!ms
            echo ========================================
        )
        echo.
    )
)

:: Execute Java if enabled
if "%RUN_JAVA%"=="true" (
    echo ****************************************
    echo *          Java Implementation         *
    echo ****************************************
    
    if not exist "%DAY%\Solver.java" (
        echo Error: file "%DAY%\Solver.java" does not exist!
    ) else (
        javac -d out helper\FileReader.java "%DAY%\Solver.java"
        
        if !errorlevel! neq 0 (
            echo Compilation failed!
        ) else (
            set START_TIME=!time!
            java -cp out "%DAY%.Solver" "%DAY%\%INPUTFILE%"
            set END_TIME=!time!

            call :calculate_duration "!START_TIME!" "!END_TIME!"
            echo Duration: !DURATION!ms
            echo ========================================
        )
        echo.
    )
)

:: Execute Python if enabled
if "%RUN_PYTHON%"=="true" (
    echo ****************************************
    echo *        Python Implementation         *
    echo ****************************************
    
    if not exist "%DAY%\Solver.py" (
        echo Error: file "%DAY%\Solver.py" does not exist!
    ) else (
        set START_TIME=!time!
        python "%DAY%\Solver.py" "%DAY%\%INPUTFILE%"
        set END_TIME=!time!

        call :calculate_duration "!START_TIME!" "!END_TIME!"
        echo Duration: !DURATION!ms
        echo ========================================
        echo.
    )
)

rmdir /s /q out
goto :eof

:calculate_duration
set START=%~1
set END=%~2

:: Remove leading zeros and spaces
set START=%START: =%
set END=%END: =%

:: Convert time to hundredths of a second
for /f "tokens=1-4 delims=:,." %%a in ("%START%") do (
    set /a "H=1%%a-100"
    set /a "M=1%%b-100"
    set /a "S=1%%c-100"
    set /a "CS=1%%d-100"
    set /a START_CS=^(^(H*60+M^)*60+S^)*100+CS
)
for /f "tokens=1-4 delims=:,." %%a in ("%END%") do (
    set /a "H=1%%a-100"
    set /a "M=1%%b-100"
    set /a "S=1%%c-100"
    set /a "CS=1%%d-100"
    set /a END_CS=^(^(H*60+M^)*60+S^)*100+CS
)

:: Calculate time difference
set /a DIFF_CS=END_CS-START_CS

:: If negative (past midnight), add 24 hours
if !DIFF_CS! lss 0 set /a DIFF_CS+=8640000

:: Convert to milliseconds
set /a DURATION=DIFF_CS*10

goto :eof

endlocal