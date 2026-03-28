
# 🎓 Student Performance Analyzer

## 🚀 Overview

The **Student Performance Analyzer** is a Python-based mini project that collects student data, calculates average scores, assigns grades, and displays a structured performance report.

This project demonstrates core Python concepts including:

* Data structures (lists & dictionaries)
* Functions and modular programming
* Loops and conditional logic
* User input handling

---

## 📌 Problem Statement

Create a program that takes student data, stores it using appropriate data structures, applies logic through functions, and generates meaningful output reports.

---

## ✨ Features

* Collects data for multiple students
* Stores data using lists of dictionaries
* Calculates average marks
* Assigns grades based on performance
* Displays a clean and formatted report

---

## 🔹 Requirements

### 1️⃣ Input & Data Handling

* Ask the user for the number of students

* For each student, collect:

  * `name` (string)
  * `marks` in 3 subjects (integers)

* Store the data in this format:

```python
students = [
    {
        "name": "Aurex",
        "marks": [78, 85, 90]
    }
]
```

---

### 2️⃣ Functions (Mandatory)

* `get_average(marks)`
  Calculates the average of marks

* `get_grade(avg)`
  Returns the grade based on average score

* `display_report(students)`
  Displays the final formatted report

---

### 3️⃣ Grading Logic

| Average Score | Grade |
| ------------- | ----- |
| ≥ 85          | A     |
| ≥ 70          | B     |
| ≥ 50          | C     |
| < 50          | Fail  |

---

## 📊 Sample Output

```text
Name: Aurex
Marks: [78, 85, 90]
Average: 84.33
Grade: B
------------------
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/004_student_performance.git
```

2. Navigate to the project folder:

```bash
cd 004_student_performance
```

3. Run the program:

```bash
python stu_maks_avg_grad.py
```

---

## 📁 Project Structure

```
004_student_performance/
│
├── 001input.py
├── stu_marks_avg_grade.py
├── README.md
└── .gitignore
```

---

## 🧠 Learning Outcomes

This project covers most foundational Python concepts, including:

* Variables and data types
* Lists and dictionaries
* Functions
* Loops and conditionals
* Basic program structure

---

## 📌 Notes

* Ensure Python is installed before running the program
* This project is designed for learning and practice purposes

---
