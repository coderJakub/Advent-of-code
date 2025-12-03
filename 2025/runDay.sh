#!/bin/bash

# Check if day-parameter was passed
if [ -z "$1" ]; then
    echo "Usage: runDay ^<day-number^> [-c] [-j] [-p]"
    echo ""
    echo "Flags:"
    echo "  -c    Execute C-implementation"
    echo "  -j    Execute Java-implementation"
    echo "  -p    Execute Python-implementation"
    echo ""
    echo "Default: Python-implementation"
    exit 1
fi

# Format day number with leading zero
DAY_NUM=$1
DAY=$(printf "Day%02d" $DAY_NUM)

RUN_C=false
RUN_JAVA=false
RUN_PYTHON=false
INPUTFILE="in.txt"

# Parse flags
shift  # Skip first parameter (day number)
while [ $# -gt 0 ]; do
    case "$1" in
        -c)
            RUN_C=true
            ;;
        -j)
            RUN_JAVA=true
            ;;
        -p)
            RUN_PYTHON=true
            ;;
        *)
            echo "Unknown flag: $1"
            exit 1
            ;;
    esac
    shift
done

# Default: Execute Python
if [ "$RUN_C" = false ] && [ "$RUN_JAVA" = false ]; then
    RUN_PYTHON=true
fi

# Check whether the directory exists
if [ ! -d "$DAY" ]; then
    echo "Error: directory '$DAY' does not exist!"
    exit 1
fi

# Check whether the input file exists
if [ ! -f "$DAY/$INPUTFILE" ]; then
    echo "Error: file '$DAY/$INPUTFILE' does not exist!"
    exit 1
fi

mkdir -p out
# Execute C if enabled
if [ "$RUN_C" = true ]; then
    echo "****************************************"
    echo "*            C Implementation          *"
    echo "****************************************"
    echo ""
    
    if [ ! -f "$DAY/solver.c" ]; then
        echo "Error: file '$DAY/solver.c' does not exist!"
    else
        gcc -o out/solver helper/FileReader.c "$DAY/solver.c"
        
        if [ $? -ne 0 ]; then
            echo "Compilation failed!"
        else            
            START_TIME=$(date +%s%N)
            ./out/solver "$DAY/$INPUTFILE"
            END_TIME=$(date +%s%N)
            
            ELAPSED=$((($END_TIME - $START_TIME) / 1000000))
            echo "Duration: ${ELAPSED}ms"
            echo "========================================"
        fi
        
        echo ""
    fi
fi

# Execute Java if enabled
if [ "$RUN_JAVA" = true ]; then
    echo "****************************************"
    echo "*          Java Implementation         *"
    echo "****************************************"
    echo ""
    
    if [ ! -f "$DAY/Solver.java" ]; then
        echo "Error: file '$DAY/Solver.java' does not exist"
    else
        javac -d out helper/FileReader.java "$DAY/Solver.java"
        
        if [ $? -ne 0 ]; then
            echo "Compilation failed!"
        else
            START_TIME=$(date +%s%N)
            java -cp out "$DAY.Solver" "$DAY/$INPUTFILE"
            END_TIME=$(date +%s%N)
            
            ELAPSED=$((($END_TIME - $START_TIME) / 1000000))
            echo "Duration: ${ELAPSED}ms"
            echo "========================================"
        fi
        
        echo ""
    fi
fi

# Execute Python if enabled
if [ "$RUN_PYTHON" = true ]; then
    echo "****************************************"
    echo "*          Python Implementation         *"
    echo "****************************************"
    echo ""
    
    if [ ! -f "$DAY/Solver.py" ]; then
        echo "Error: file '$DAY/Solver.py' does not exist!"
    else
        START_TIME=$(date +%s%N)
        python "$DAY/Solver.py" 
        END_TIME=$(date +%s%N)
        
        ELAPSED=$((($END_TIME - $START_TIME) / 1000000))
        echo "Duration: ${ELAPSED}ms" "$DAY/$INPUTFILE"
        echo "========================================"
        fi
        
        echo ""
    fi
fi

rm -rf out