# 🎄 Advent of Code 2025
In this directory, you will find my solutions for the [Advent of Code 2025](https://adventofcode.com/2025) challenges. For this edition, only **12 days** of puzzles are available. I primarily solve the challenges in **Python**, but I also implement each solution in **Java** and **C** to practice these languages again.
### Table of Contents
1. 🗂️ [Structure](#%EF%B8%8F-structure)
2. 🚀 [Running the Solutions](-running-the-solutions)
3. 📅 [Progress Tracker](#-progress-tracker)
---


## 🗂️ Structure 
Each day has its own folder named `DayXX`, where `XX` is the day number (01 to 12). Inside each folder, you will find the solution files for that day's challenge in Python (`Solver.py`), Java (`Solver.java`), and C (`Solver.C`).
```yaml
2025/
├── Day01/
│   ├── Solver.py
│   ├── Solver.java
│   └── Solver.C
├── Day02/
├── Day03/
├── ...
├── Day12/
├── helper/
├── runDay.bat
├── runDay.sh
└── README.md
```

## 🚀 Running the Solutions 
To run the solutions for a specific day, you can use the provided scripts:
- `runDay.bat` for Windows
- `runDay.sh` for Unix-based systems

### Prerequisites
Create a file named input.txt inside the respective DayXX folder containing the puzzle input for that day. Additionally, ensure you have Python, the Java JDK, and/or a C compiler installed.

### Instructions
```
Usage:
  runDay <day_number> [-j] [-c] [-p]

Options:
  <day_number>   The day number (1 to 12) to run the solution
  -j             Run the Java solution
  -c             Run the C solution
  -p             Run the Python solution
  
If no language option is provided, the Python solution will be executed by default.
```

### Example
Run the Python and Java solutions for Day 3:
```bash
  runDay 3 -j -p 
```

### Note
You can also run the solutions directly using the respective language interpreters 
```bash
# Python
cd DayXX
python Solver.py [optional_input_file]

# Java
mkdir -p out
javac -d out helper\FileReader.java DayXX\Solver.java
java  -cp out DayXX.Solver [input_file]

# C
gcc -o Solver DayXX\Solver.c helper\FileReader.c
./Solver [input_file]
```

## 📅 Progress Tracker
I will update this table as I complete each day's challenge, including which languages I have implemented.

|   Day   | Part1 | Part2 | Java  |   C   |
|---------|:-----:|:-----:|:-----:|:-----:|
| **01**  | ⭐    | ⭐   | ✅   | ✅   |
| **02**  | ⭐    | ⭐   | ✅   | ✅   |
| **03**  | ⭐    | ⭐   | ✅   | ✅   |
| **04**  | ⭐    | ⭐   | ✅   | ✅   |
| **05**  | ⭐    | ⭐   | ✅   | ✅   |
| **06**  | ⭐    | ⭐   | ✅   | ✅   |
| **07**  | ⭐    | ⭐   | ✅   | ✅   |
| **08**  | ⭐    | ⭐   |    |    |
| **09**  | ⭐    | ⭐   |    |    |
| **10**  |     |    |    |    |
| **11**  |     |    |    |    |
| **12**  |     |    |    |    |

---
Legend: ⭐ = Solved ✅ = Implemented

---

*@2025 Jakub Kliemann*