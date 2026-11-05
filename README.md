# HealthCare Patient Record and Vaccination Tracker

## Overview
A small, menu-driven Python console program demonstrating Object-Oriented Programming (OOP).
It uses sample data for educational purposes only and must not be used to store real patient data.

## Requirements
- Python 3.8 or newer
- No third-party packages required

## Run
1. Save `healthcare_tracker.py`.
2. Open a terminal in the same folder.
3. Run: `python healthcare_tracker.py`

## Features
- Register a patient with a unique ID, name, and age
- List patient records
- Search by patient ID
- Record vaccination name and date
- Show patient-object count

## OOP concepts
- `Patient` and `HealthTracker` are classes.
- `Patient(...)` creates patient objects.
- Attributes include `patient_id`, `name`, `age`, and `vaccinations`.
- Instance methods include `display_info`, `add_patient`, `find_patient`, and `record_vaccination`.
- `Patient.get_patient_count` is a class method.
- `HealthTracker.display_system_name` is a static method.
- A list (`self.patients`) stores multiple Patient objects. Each patient's vaccination entries are represented as dictionaries.

## Digital Public Goods (DPG) alignment
- Open-source: source code can be published in a public GitHub repository.
- Inclusive/accessibility: simple text menu, clear prompts, and readable output.
- Privacy-respecting: built-in examples use fictional sample data; do not enter real sensitive health information.
- Modular/reusable: patient management and user-interface functions are separated into classes and functions.

This is a classroom demonstration, not a clinically validated system. It does not provide medical advice,
authentication, encryption, backups, or legal compliance for handling health data.

## Example test plan
1. Start the program and choose option 2: two sample patients should appear.
2. Choose option 3 and search for `P001`: the record and sample vaccination should appear.
3. Choose option 4 and add a vaccination to `P002`; search for `P002` to verify it.
4. Try registering `P001` again: the program should reject the duplicate ID.
5. Search for `P999`: the program should report that the ID was not found.
6. Choose option 5: the object count and currently registered count should be displayed.
7. Choose option 0: the program should exit.

## GitHub submission checklist
- i Created a public repository named `healthcare-patient-vaccination-tracker`.
- i Upload `healthcare_tracker.py` and this README.
- i Add my lecturer as a collaborator.
- i Include screenshots of the program running in the hardcopy report.
