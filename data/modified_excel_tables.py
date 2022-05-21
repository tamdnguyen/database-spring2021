import pandas as pd
# Reading all data frames:

df_vaccine_type = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="VaccineType")
df_manufacturer = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="Manufacturer")
df_vaccine_batch = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="VaccineBatch")
df_vaccination_stations = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="VaccinationStations")
df_transportation_log = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="Transportation log")
df_staff_members = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="StaffMembers")
df_shifts = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="Shifts")
df_vaccinations = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="Vaccinations")
df_patients = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="Patients")
df_vaccine_patients = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="VaccinePatients")
df_symptoms = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="Symptoms")
df_diagnosis = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="Diagnosis")

# Creating corresponding data frames:


## VaccineData
vaccine_data = df_vaccine_type[[col for col in df_vaccine_type if not col.startswith('Unnamed:')]]
vaccine_data.columns = ['vaccineID', 'name', 'nrOfDoses', 'tempMin', 'tempMax']
print('VaccineData: ')
print(vaccine_data.head())
vaccine_data.to_csv('data/VaccineData.csv', index = False)

## Manufacturer
manufacturer = df_manufacturer[[col for col in df_manufacturer if not col.startswith('Unnamed:')]]
manufacturer.columns = ['ID', 'origin', 'phone', 'vaccineID']
print('Manufacturer: ')
print(manufacturer.head())
manufacturer.to_csv('data/Manufacturer.csv', index = False)

## Vaccinationbatch
vaccinationBatch = df_vaccine_batch[[col for col in df_vaccine_batch if not col.startswith('Unnamed:')]]
vaccinationBatch.columns = ['batchID', 'amount', 'vaccineID', 'manufID', 'manufDate', 'expDate', 'initialReceiver']
vaccinationBatch = vaccinationBatch.reindex(columns = ['batchID', 'amount', 'manufDate', 'expDate', 'manufID', 'vaccineID', 'initialReceiver'])
vaccinationBatch['manufDate'] = pd.to_datetime(vaccinationBatch['manufDate'])
vaccinationBatch['expDate'] = pd.to_datetime(vaccinationBatch['expDate'])
vaccinationBatch = vaccinationBatch.dropna(axis = 0, subset=['manufDate', 'expDate'])
print('VaccinationBatch: ')
print(vaccinationBatch.head())
vaccinationBatch.to_csv('data/VaccinationBatch.csv', index=False)

## MedicalFacility
medicalFacility = df_vaccination_stations[[col for col in df_vaccination_stations if not col.startswith('Unnamed:')]]
medicalFacility.columns = ['name', 'address', 'phone']
print('MedicalFacility:')
print(medicalFacility)
medicalFacility.to_csv('data/MedicalFacility.csv', index = False)

## TransportationLog
transportationLog = df_transportation_log[[col for col in df_transportation_log if not col.startswith('Unnamed:')]]
transportationLog.columns = ['batchID', 'receiverName', 'senderName',  'arrivalDate', 'departureDate']
transportationLog['ID'] = transportationLog.index
transportationLog = transportationLog.reindex(columns = ['ID', 'departureDate', 'arrivalDate', 'batchID', 'senderName', 'receiverName'])
transportationLog['departureDate'] = pd.to_datetime(transportationLog['departureDate'])
transportationLog['arrivalDate'] = pd.to_datetime(transportationLog['arrivalDate'])
transportationLog = transportationLog.dropna(axis=0, subset=['departureDate', 'arrivalDate'])
print('TransportationLog: ')
print(transportationLog.head())
transportationLog.to_csv('TransportationLog.csv', index = False)

## StaffMembers
staffMember = df_staff_members[[col for col in df_staff_members if not col.startswith('Unnamed:')]]
staffMember.columns = ['ssNo', 'name', 'birthday', 'phone', 'role', 'vaccinationStatus', 'employer']
staffMember = staffMember.reindex(columns = ['ssNo', 'name', 'phone', 'birthday', 'vaccinationStatus', 'role', 'employer'])
print('StaffMember: ')
print(staffMember.head())
staffMember.to_csv('data/StaffMember.csv', index = False)

## VaccinationShift
vaccination_shifts = df_shifts[[col for col in df_shifts if not col.startswith('Unnamed:')]]
print('VaccinationShitfs: ')
print(vaccination_shifts.head())
vaccination_shifts.to_csv('data/VaccinationShift.csv', index = False)

## VaccinationEvent
vaccination_event = df_vaccinations[[col for col in df_vaccinations if not col.startswith('Unnamed:')]]
vaccination_event['date'] = pd.to_datetime(vaccination_event['date'],errors='coerce')
vaccination_event = vaccination_event.dropna(axis=0, subset=['date'])
vaccination_event['weekday'] = pd.Series(vaccination_event['date']).dt.day_name()
print('VaccinationEvent: ')
print(vaccination_event.head())
vaccination_event.to_csv('data/VaccinationEvent.csv', index=False)

## Patient 
patient = df_patients[[col for col in df_patients if not col.startswith('Unnamed:')]]
patient = patient.rename(columns={'date of birth': 'birthday'})
print('Patient: ')
print(patient.head())
patient.to_csv('data/Patient.csv', index = False)

## Attend
attend = df_vaccine_patients[[col for col in df_vaccine_patients if not col.startswith('Unnamed:')]]
attend = attend.rename(columns={'patientSsNo': 'patient'})
attend['date'] = pd.to_datetime(attend['date'], errors='coerce')
attend = attend.dropna(axis=0, subset=['date'])
print('Attend: ')
print(attend.head())
attend.to_csv('data/Attend.csv', index = False)

## Symptom
symptom = df_symptoms[[col for col in df_symptoms if not col.startswith('Unnamed:')]]
symptom = symptom.rename(columns = {'criticality':'critical'})
print('Symptom:')
print(symptom.head())
symptom.to_csv('data/Symptom.csv', index = False)

## Diagnosed

diagnosed = df_diagnosis[[col for col in df_diagnosis if not col.startswith('Unnamed:')]]
diagnosed['date'] = pd.to_datetime(diagnosed['date'], errors='coerce')
diagnosed = diagnosed.dropna(axis=0, subset=['date'])
print('Diagnosed')
print(diagnosed)
diagnosed.to_csv('data/Diagnosed.csv', index = False)