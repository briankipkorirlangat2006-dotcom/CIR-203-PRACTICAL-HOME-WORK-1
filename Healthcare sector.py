
patient = ("John Doe", 35, "120/80", 72)
print("Age:", patient[1])
print("Heart Rate:", patient[3])
print("Reason: Tuples are immutable, so patient records remain unchanged by mistake.")
patient_list = list(patient)
patient_list[3] = 80
patient_updated = tuple(patient_list)
print("Updated Patient Tuple:", patient_updated)
patients = [
    ("Alice", 28, "110/70", 65),
    ("Bob", 40, "130/85", 75),
    ("Charlie", 50, "140/90", 80),
    ("Diana", 32, "115/75", 68),
    ("Eve", 45, "135/88", 77)
]

names = [p[0] for p in patients]
print("Patient Names:", names)