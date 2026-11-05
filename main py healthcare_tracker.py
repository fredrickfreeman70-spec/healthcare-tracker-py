"""
HealthCare Patient Record and Vaccination Tracker
Course: PROG211 - Object-Oriented Programming 1

Educational demonstration only. Uses sample data and is not intended
for storing real patient or medical information.
"""

class Patient:
    """Represents one patient and their vaccination record."""

    patient_count = 0  # Class attribute shared by all Patient objects

    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.vaccinations = []
        Patient.patient_count += 1

    def add_vaccination(self, vaccine_name, vaccination_date):
        """Add a vaccination entry to this patient's record."""
        vaccination = {
            "vaccine": vaccine_name,
            "date": vaccination_date
        }
        self.vaccinations.append(vaccination)

    def display_info(self):
        """Display patient details and vaccination history."""
        print("\n--- Patient Record ---")
        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        if not self.vaccinations:
            print("Vaccinations: No vaccinations recorded.")
        else:
            print("Vaccinations:")
            for item in self.vaccinations:
                print(f"  - {item['vaccine']} | Date: {item['date']}")

    @classmethod
    def get_patient_count(cls):
        """Return the number of Patient objects created in this run."""
        return cls.patient_count


class HealthTracker:
    """Manages patient objects in a list."""

    def __init__(self):
        self.patients = []  # Required Python data structure: list

    def add_patient(self, patient):
        """Add a patient if the ID is not already registered."""
        if self.find_patient(patient.patient_id) is not None:
            print("Error: A patient with that ID already exists.")
            return False
        self.patients.append(patient)
        print("Patient registered successfully.")
        return True

    def find_patient(self, patient_id):
        """Find a patient by their unique ID."""
        for patient in self.patients:
            if patient.patient_id.lower() == patient_id.lower():
                return patient
        return None

    def display_all_patients(self):
        """Display every patient in the list."""
        if not self.patients:
            print("No patient records have been registered.")
            return
        for patient in self.patients:
            patient.display_info()

    def record_vaccination(self, patient_id, vaccine_name, vaccination_date):
        """Find a patient and record a vaccination."""
        patient = self.find_patient(patient_id)
        if patient is None:
            print("Patient ID not found.")
            return False
        patient.add_vaccination(vaccine_name, vaccination_date)
        print("Vaccination recorded successfully.")
        return True

    @staticmethod
    def display_system_name():
        """A static method that does not require an object or class state."""
        print("\n=== HealthCare Patient Record and Vaccination Tracker ===")


def get_non_empty(prompt):
    """Keep asking until the user enters non-empty text."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def get_age():
    """Validate that age is a non-negative whole number."""
    while True:
        try:
            age = int(input("Enter age: "))
            if age < 0:
                print("Age cannot be negative.")
            else:
                return age
        except ValueError:
            print("Please enter a whole number for age.")


def main():
    tracker = HealthTracker()

    # Sample records demonstrate the program without using sensitive data.
    tracker.add_patient(Patient("P001", "Sample Patient One", 24))
    tracker.add_patient(Patient("P002", "Sample Patient Two", 31))
    tracker.record_vaccination("P001", "Sample Vaccine A", "2026-10-01")

    while True:
        HealthTracker.display_system_name()
        print("1. Register patient")
        print("2. Display all patients")
        print("3. Search for patient")
        print("4. Record vaccination")
        print("5. Show patient count")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            patient_id = get_non_empty("Enter unique patient ID: ")
            name = get_non_empty("Enter patient name (use sample data): ")
            age = get_age()
            tracker.add_patient(Patient(patient_id, name, age))

        elif choice == "2":
            tracker.display_all_patients()

        elif choice == "3":
            patient_id = get_non_empty("Enter patient ID to search: ")
            patient = tracker.find_patient(patient_id)
            if patient:
                patient.display_info()
            else:
                print("Patient ID not found.")

        elif choice == "4":
            patient_id = get_non_empty("Enter patient ID: ")
            vaccine = get_non_empty("Enter vaccine name: ")
            date = get_non_empty("Enter vaccination date (YYYY-MM-DD): ")
            tracker.record_vaccination(patient_id, vaccine, date)

        elif choice == "5":
            print(f"Patient objects created this run: {Patient.get_patient_count()}")
            print(f"Patients currently registered: {len(tracker.patients)}")

        elif choice == "0":
            print("Thank you for using the HealthCare Tracker.")
            break

        else:
            print("Invalid choice. Please select a listed option.")


if __name__ == "__main__":
    main()
