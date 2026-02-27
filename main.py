# Project - Hospital Management System (OOP)

# Inheritance + Composition 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f"{self.name}, Age: {self.age} y/o"
    
class Doctor(Person):
    def __init__(self, name, age, doctor_id, specialization):
        super().__init__(name, age)
        self.doctor_id = doctor_id
        self.specialization = specialization
        
    def __repr__(self):
        return f"{super().__repr__()} | ID: {self.doctor_id}, Specialization: {self.specialization}"

    #Composition
class MedicalRecord:
    def __init__(self, record_id, diagnosis, treatement):
        self.record_id = record_id
        self.diagnosis = diagnosis
        self.treatement = treatement
        
    def __repr__(self):
        return f"Record ID: {self.record_id}\nDiagnosis: {self.diagnosis}\nTreatement: {self.treatement}"
    

class Patient(Person):
    def __init__(self, name, age, patient_id, disease):
        super().__init__(name, age)
        self.patient_id = patient_id
        self.disease = disease
        self.medical_record = []    # composition
        
    def add_medical_record(self,record_id, diagnosis, treatement):
        mdrecord = MedicalRecord(record_id, diagnosis, treatement)
        self.medical_record.append(mdrecord)
        
    def __repr__(self):
        return f"Name: {self.name}\nAge: {self.age}\nMedical Record: {self.medical_record} Disease: {self.disease}"
    
    
class Room:
    def __init__(self, room_number, type):
        self.room_number = room_number
        self.type = type
        self.occupied = False
        
    def __repr__(self):
        status = "Occupied" if self.occupied else "Free"
        return f"Room NO: {self.room_number}, Room:{self.type} - {status}"
    

class Hospital:
    def __init__(self, hospital_name, location):
        self.hospital_name = hospital_name
        self.location =location
        self.patients = []  # all registered patients
        self.admit_patients = []
        self.doctors = []
        self.rooms = []
        
        #adding Patients
    def add_patient(self, patients):
        self.patients.append(patients)
        print(f"Registered: {patients}")
        
        #Adding rooms
    def add_rooms(self, room_number, type):
        room = Room(room_number, type)
        self.rooms.append(room)
        
        #adding Doctors
    def add_doctors(self,doctor):
        self.doctors.append(doctor)
        
    def admit_patient(self,patients):
        self.admit_patients.append(patients)
        
    def discharge_patients(self, patient):
        if patient in self.admit_patients:
            self.admit_patients.remove(patient)
            
            
    def display(self):
        with open("hospital.txt", "a") as f:
            f.write("Hospital:" + str(self.hospital_name) + "\n")
            f.write("Hospital Location:" + str(self.location) + "\n")
            f.write("Patients: ")
            
            for pat in self.patients:
                f.write(str(pat) + "\n")
                
            f.write("Room: ")
            
            for rm in self.rooms:
                f.write(str(rm) + "\n")
                
            f.write("Doctor: ")
            
            for doc in self.doctors:
                f.write(str(doc) + "\n")
                
            f.write("Admit Patients: ")
            
            for ad_patitents in self.admit_patients:
                f.write(str(ad_patitents) + "\n")
                
            f.write("---------------------------------------------------------\n")
            
        print("Fle Created")
        
        
# ────────────────────────────────────────────────
#          DEMO / TEST DATA
# ────────────────────────────────────────────────

# Create hospital
kmch = Hospital("KMCH", "Coimbatore")

# Doctors
doc1 = Doctor("Dr. Arun", 48, "D001", "Cardiology")
doc2 = Doctor("Dr. Priya", 39, "D002", "Ophthalmology")
doc3 = Doctor("Dr. Karthik", 45, "D003", "Orthopedics")

#adding doc
kmch.add_doctors(doc1)
kmch.add_doctors(doc2)
kmch.add_doctors(doc3)


# Rooms
kmch.add_rooms(101, "General")
kmch.add_rooms(205, "ICU")
kmch.add_rooms(310, "Private")
kmch.add_rooms(108, "General")

# Patients
p1 = Patient("Sanjay", 34, "P1001", "Heart Attack")
p2 = Patient("Adhira", 19, "P1002", "Eye Infection")
p3 = Patient("Hari", 27, "P1003", "Fractured Leg")

#adding Patients
kmch.add_patient(p1)
kmch.add_patient(p2)
kmch.add_patient(p3)

# Add some medical records
p1.add_medical_record(501, "Acute Myocardial Infarction", "Angioplasty + Stent")
p2.add_medical_record(502, "Conjunctivitis", "Antibiotic drops")
p3.add_medical_record(503, "Tibia Fracture", "Open reduction + internal fixation")

## Admissions
kmch.admit_patient(p1) # ICU
kmch.admit_patient(p3)   # Private

# Show everything
kmch.display()

# Example discharge
kmch.discharge_patients(p3)