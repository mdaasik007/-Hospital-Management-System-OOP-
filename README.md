# 🏥 Hospital Management System

A structured **Object-Oriented Programming (OOP)** project built in Python that simulates core hospital operations using clean architecture and real-world modeling concepts.

---
## 👨‍💻 Author

**Mohammed Aasik.A**  
🔗 GitHub: [mdaasik007](https://github.com/mdaasik007)
---

## 🐍 Tech Stack

- **Language:** Python 3  
- **Paradigm:** Object-Oriented Programming (OOP)  
- **Concepts:** Inheritance, Composition, Encapsulation, File Handling  

---

## 📖 Overview

The Hospital Management System models a real-world hospital environment by managing:

- 👨‍⚕️ Doctors  
- 🧑 Patients  
- 🛏️ Rooms  
- 📄 Medical Records  
- 🏥 Admissions & Discharges  

The system demonstrates practical implementation of OOP principles while maintaining a clean and scalable architecture.

---

## 🧠 OOP Concepts Implemented

### 🔹 Inheritance
`Doctor` and `Patient` inherit from the base `Person` class to promote reusability and reduce redundancy.

### 🔹 Composition
Each `Patient` maintains multiple `MedicalRecord` objects, representing a real-world **has-a** relationship.

### 🔹 Encapsulation
Data and behavior are organized within classes to ensure modular and maintainable code.

---

## 🏗️ System Architecture


Person
├── Doctor
└── Patient
└── MedicalRecord (Composition)

Room
Hospital (Main Controller)


The `Hospital` class manages:

- Patient registration  
- Doctor management  
- Room handling  
- Admissions & discharges  
- File output generation  

---

## 📂 Output

After running the program, a file named:


hospital.txt


is generated containing structured hospital data.

---

## ▶️ Installation & Execution

1. Install Python 3  
2. Clone the repository  

```bash
git clone https://github.com/mdaasik007/hospital-management-system.git

Navigate to the folder

cd hospital-management-system

Run the program

python hospital_management.py
🚀 Future Enhancements

Database Integration (SQLite / MySQL)

Automatic Room Allocation

Billing System

Authentication & Role Management

GUI or Web-Based Interface

REST API Support

📜 License

Developed for educational purposes.

⭐ If you found this project useful, consider giving it a star!



