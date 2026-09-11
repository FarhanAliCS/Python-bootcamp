# 🎓 Student Management System

A Python-based **Student Management System** developed as my **Day 30 Python Final Integration Project**.

This project combines the major Python concepts I learned throughout my first 30 days into one practical, multi-file application. It supports student management, validation, GPA calculation, JSON data persistence, logging, and automated unit testing.

---

## ✨ Features

* ➕ Add student records
* 🔍 Search students
* ✏️ Update student information
* 🗑️ Delete student records
* 📋 Display student information
* 📊 Calculate GPA and grade points
* 💾 Store data permanently using JSON
* 🛡️ Validate user input
* 📝 Record application events using logging
* 🧪 Automated unit testing
* 📦 Virtual environment and dependency management

---

## 📁 Project Structure

```text
Student Management System/
│
├── main.py
├── Student.py
├── Manage.py
├── validate_function.py
├── Test_manager.py
├── students.json
├── Student.log
├── requirements.txt
└── README.md
```

### Student.py

Contains the `Student` dataclass and the main student data structure.

### Manage.py

Contains the `StudentManager` class and the core student management operations.

### validate_function.py

Contains input validation, GPA/grade-point calculation, student display functions, and logging configuration.

### Test_manager.py

Contains automated unit tests for testing the main functionality of the application.

###  students.json

Stores student records so that data remains available after the program is closed.

---

## 💾 Data Storage

Student information is stored permanently in a JSON file:

```text
students.json
```

The application loads existing records when it starts and saves updated data back to the file.

---

## 🧮 GPA Calculation

The system converts subject marks into grade points and calculates the student's GPA based on the average grade points.

Example:

```text
85 marks → 4.0
80 marks → 3.5
75 marks → 3.0
```

The final GPA is calculated from the average of the student's subject grade points.

---

## 🛡️ Input Validation

The application validates important student information before saving it.

Examples:

* Name must contain valid characters
* Roll number must contain exactly 4 digits
* Roll number must be unique
* Age must be between 16 and 25
* Semester must be between 1 and 8
* Marks must be between 0 and 100
* GPA must be between 0 and 4

This helps prevent invalid or inconsistent student records.

---

## 📝 Logging

The project uses Python's built-in `logging` module to record important application events, warnings, and errors.

Logs are stored in:

```text
Student.log
```

This makes it easier to track what happens inside the application and troubleshoot errors.

---

## 🧪 Testing

The project uses Python's built-in `unittest` framework.

Run the automated tests with:

```bash
python -m unittest Test_manager.py -v
```

The project currently contains **22 automated tests** covering major functionality.

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <project-folder>
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment on Windows

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python main.py
```

---

## 🎯 Learning Objectives

The main goal of this project was to bring together the Python concepts I learned during my first 30 days into a single practical application.

Through this project, I practiced:

* Structuring a multi-file Python project
* Object-Oriented Programming
* Dataclasses and Type Hints
* Functions and modular programming
* File handling and JSON
* Exception handling
* Input validation
* Logging
* Automated unit testing
* Virtual environments
* Dependency management with `pip`
* Git and GitHub workflow

---

## 📈 My Python Learning Journey

```text
Python Fundamentals
        ↓
Data Structures
        ↓
Functions
        ↓
File Handling & JSON
        ↓
Object-Oriented Programming
        ↓
Exception Handling
        ↓
Logging
        ↓
Dataclasses & Type Hints
        ↓
Unit Testing
        ↓
Virtual Environment & pip
        ↓
Final Integration Project ✅
```

This project represents the transition from learning individual Python concepts to combining them into a complete application.

---

## 🔮 Future Improvements

Possible future improvements include:

* 🖥️ GUI interface
* 🗄️ SQLite database
* 🔐 User authentication
* 📄 CSV import/export
* 📊 Advanced statistics and reports
* 🔎 Advanced search and filtering
* 🌐 REST API
* 🌍 Web interface

---

## 👨‍💻 Developer

**Farhan Ali**

BS Computer Science Student
Aspiring AI/ML Engineer

**GitHub:**
https://github.com/FarhanAliCS

---

## ✅ Project Status

**Completed — Day 30 Python Final Integration Project 🎉**

This project marks an important milestone in my Python learning journey and gives me a foundation to move toward more advanced topics such as **Pandas, Data Analysis, APIs, and AI/ML**.

