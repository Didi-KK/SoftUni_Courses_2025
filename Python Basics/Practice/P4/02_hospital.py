period = int(input())

doctors_qty = 7
treated_patients_count = 0
untreated_patients_count = 0


for day in range(1, period+1):
    if day % 3 == 0:
        if untreated_patients_count >treated_patients_count:
            doctors_qty += 1
    patients = int(input())
    
    if patients <=doctors_qty:
        treated_patients_count += patients
    else:
        treated_patients_count += doctors_qty
        untreated_patients_count += patients - doctors_qty

print(f'Treated patients: {treated_patients_count}.'
      f'\nUntreated patients: {untreated_patients_count}.')