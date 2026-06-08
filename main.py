import mysql.connector as m
import datetime
import time
import os
import sys
from tabulate import tabulate
import sqlite3

# Connect to MySQL server
mydb = m.connect(host='localhost', user='root', passwd='root')
c = mydb.cursor()

# Create the EMP_RECRUIT database
c.execute("CREATE DATABASE IF NOT EXISTS CODERED")
mydb.close()

# Connect to the EMP_RECRUIT database
d = m.connect(host='localhost', user='root', passwd='root', database='CODERED')
C = d.cursor()

# Create Symptoms Table
create_table_template = """
CREATE TABLE IF NOT EXISTS {table_name} (
    diseaseID VARCHAR(255) PRIMARY KEY,
    diseasename VARCHAR(255) NOT NULL,
    symptoms1 VARCHAR(255) NOT NULL,
    symptoms2 VARCHAR(255) NOT NULL,
    symptoms3 VARCHAR(255) NOT NULL,
    symptoms4 VARCHAR(255) NOT NULL,
    symptoms5 VARCHAR(255) NOT NULL
);
"""
categories = [
    'FeverColdDiseases',
    'SkinDiseases',
    'MentalDiseases',
    'StomachDiseases',
    'BoneDiseases',
    'EyeDiseases',
    'EarNoseDiseases'
]

for category in categories:
    query = create_table_template.format(table_name=category)
    C.execute(query)
for table in categories:
    C.execute(f"DELETE FROM {table}")


diseases1 = [
    ('D001', 'Malaria', 'Fever', 'Chills', 'Headache', 'Sweating', 'Nausea'),
    ('D002', 'Dengue', 'Fever', 'Rash', 'Joint Pain', 'Nausea', 'Bleeding'),
    ('D003', 'COVID-19', 'Fever', 'Cough', 'Breathing Difficulty', 'Loss of Taste', 'Fatigue'),
    ('D004', 'Typhoid', 'Fever', 'Weakness', 'Stomach Pain', 'Headache', 'Loss of Appetite'),
    ('D005', 'Flu', 'Fever', 'Cough', 'Sore Throat', 'Muscle Pain', 'Fatigue'),
    ('D006', 'Tuberculosis', 'Cough', 'Chest Pain', 'Weight Loss', 'Fever', 'Night Sweats'),
    ('D007', 'Cholera', 'Watery Diarrhea', 'Dehydration', 'Vomiting', 'Leg Cramps', 'Dry Mouth'),
    ('D008', 'Pneumonia', 'Fever', 'Cough', 'Chest Pain', 'Fatigue', 'Shortness of Breath'),
    ('D009', 'Measles', 'Fever', 'Cough', 'Runny Nose', 'Rash', 'Red Eyes'),
    ('D010', 'Chickenpox', 'Fever', 'Itchy Rash', 'Fatigue', 'Loss of Appetite', 'Headache'),
    ('D011', 'Meningitis', 'Fever', 'Stiff Neck', 'Nausea', 'Sensitivity to Light', 'Confusion'),
    ('D012', 'Hepatitis A', 'Fatigue', 'Nausea', 'Abdominal Pain', 'Jaundice', 'Loss of Appetite'),
    ('D013', 'Hepatitis B', 'Dark Urine', 'Joint Pain', 'Jaundice', 'Fatigue', 'Abdominal Discomfort'),
    ('D014', 'Zika Virus', 'Fever', 'Rash', 'Joint Pain', 'Red Eyes', 'Muscle Pain'),
    ('D015', 'Rabies', 'Fever', 'Agitation', 'Hallucinations', 'Fear of Water', 'Excess Saliva'),
    ('D016', 'Ebola', 'Fever', 'Vomiting', 'Diarrhea', 'Bleeding', 'Muscle Pain'),
    ('D017', 'Polio', 'Fever', 'Sore Throat', 'Headache', 'Stiff Neck', 'Paralysis'),
    ('D018', 'Leptospirosis', 'Fever', 'Muscle Pain', 'Red Eyes', 'Vomiting', 'Jaundice'),
    ('D019', 'H1N1 (Swine Flu)', 'Fever', 'Cough', 'Sore Throat', 'Body Ache', 'Fatigue'),
    ('D020', 'Scarlet Fever', 'Fever', 'Red Rash', 'Sore Throat', 'Flushed Face', 'Strawberry Tongue')
]

C.executemany("""
    INSERT INTO FeverColdDiseases (diseaseID, diseasename, symptoms1, symptoms2, symptoms3, symptoms4, symptoms5)
    VALUES (%s, %s, %s, %s, %s, %s, %s)""", diseases1)

d.commit()

diseases2 = [
    ('SK001', 'Eczema', 'Itchy Skin', 'Redness', 'Dryness', 'Inflammation', 'Cracked Skin'),
    ('SK002', 'Psoriasis', 'Scaly Skin', 'Red Patches', 'Dry Skin', 'Itching', 'Burning'),
    ('SK003', 'Acne', 'Pimples', 'Blackheads', 'Oily Skin', 'Redness', 'Swelling'),
    ('SK004', 'Rosacea', 'Facial Redness', 'Swollen Bumps', 'Eye Irritation', 'Visible Blood Vessels', 'Burning'),
    ('SK005', 'Ringworm', 'Circular Rash', 'Scaly Skin', 'Itching', 'Red Patches', 'Hair Loss'),
    ('SK006', 'Contact Dermatitis', 'Rash', 'Itching', 'Redness', 'Blisters', 'Burning'),
    ('SK007', 'Vitiligo', 'White Patches', 'Skin Discoloration', 'Photosensitivity', 'Premature Graying', 'Eye Discoloration'),
    ('SK008', 'Hives', 'Raised Welts', 'Itching', 'Redness', 'Swelling', 'Burning Sensation'),
    ('SK009', 'Melasma', 'Brown Patches', 'Skin Discoloration', 'Facial Pigmentation', 'Symmetrical Spots', 'No Itch'),
    ('SK010', 'Warts', 'Rough Skin Growth', 'Pain', 'Small Lumps', 'Hard Texture', 'Itching')
]

# Insert data
C.executemany("""
    INSERT INTO SkinDiseases (diseaseID, diseasename, symptoms1, symptoms2, symptoms3, symptoms4, symptoms5)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
""", diseases2)

d.commit()

mental_diseases = [
    ('M001', 'Depression', 'Sadness', 'Fatigue', 'Sleep Issues', 'Loss of Interest', 'Weight Changes'),
    ('M002', 'Anxiety', 'Restlessness', 'Tense Muscles', 'Sweating', 'Irritability', 'Racing Heart'),
    ('M003', 'Bipolar Disorder', 'Mood Swings', 'Depression', 'Mania', 'Impulsiveness', 'Sleep Disturbance'),
    ('M004', 'Schizophrenia', 'Delusions', 'Hallucinations', 'Disorganized Speech', 'Social Withdrawal', 'Flat Affect'),
    ('M005', 'OCD', 'Repetitive Behavior', 'Obsessions', 'Anxiety', 'Compulsions', 'Fear of Contamination')
]

bone_diseases = [
    ('B001', 'Osteoporosis', 'Bone Pain', 'Fractures', 'Back Pain', 'Height Loss', 'Weak Bones'),
    ('B002', 'Arthritis', 'Joint Pain', 'Swelling', 'Stiffness', 'Redness', 'Reduced Motion'),
    ('B003', 'Rickets', 'Bone Softening', 'Delayed Growth', 'Pain', 'Muscle Weakness', 'Skeletal Deformities'),
    ('B004', 'Osteomyelitis', 'Fever', 'Swelling', 'Pain', 'Fatigue', 'Redness'),
    ('B005', 'Paget\'s Disease', 'Bone Pain', 'Joint Pain', 'Deformity', 'Nerve Compression', 'Headaches')
]

eye_diseases = [
    ('E001', 'Conjunctivitis', 'Redness', 'Itching', 'Tearing', 'Discharge', 'Swollen Eyelids'),
    ('E002', 'Cataract', 'Blurry Vision', 'Glare Sensitivity', 'Faded Colors', 'Poor Night Vision', 'Halos'),
    ('E003', 'Glaucoma', 'Eye Pain', 'Tunnel Vision', 'Redness', 'Nausea', 'Blurred Vision'),
    ('E004', 'Dry Eye', 'Burning', 'Itching', 'Gritty Feeling', 'Redness', 'Watery Eyes'),
    ('E005', 'Macular Degeneration', 'Blurred Vision', 'Dark Spots', 'Visual Distortion', 'Color Fading', 'Central Vision Loss')
]

stomach_diseases = [
    ('S001', 'Gastritis', 'Stomach Pain', 'Nausea', 'Vomiting', 'Bloating', 'Loss of Appetite'),
    ('S002', 'Ulcer', 'Burning Pain', 'Nausea', 'Indigestion', 'Weight Loss', 'Vomiting'),
    ('S003', 'Acid Reflux', 'Heartburn', 'Regurgitation', 'Chest Pain', 'Sour Taste', 'Bloating'),
    ('S004', 'IBS', 'Abdominal Pain', 'Cramps', 'Bloating', 'Gas', 'Constipation/Diarrhea'),
    ('S005', 'Appendicitis', 'Abdominal Pain', 'Fever', 'Nausea', 'Vomiting', 'Loss of Appetite')
]

earnose_diseases = [
    ('EN001', 'Sinusitis', 'Facial Pain', 'Congestion', 'Runny Nose', 'Headache', 'Postnasal Drip'),
    ('EN002', 'Otitis Media', 'Ear Pain', 'Hearing Loss', 'Fever', 'Irritability', 'Fluid Drainage'),
    ('EN003', 'Tonsillitis', 'Sore Throat', 'Difficulty Swallowing', 'Fever', 'Bad Breath', 'Swollen Glands'),
    ('EN004', 'Tinnitus', 'Ringing Ears', 'Buzzing Sound', 'Hearing Loss', 'Anxiety', 'Ear Fullness'),
    ('EN005', 'Nasal Polyps', 'Congestion', 'Runny Nose', 'Loss of Smell', 'Facial Pressure', 'Sneezing')
]


C.executemany("""
    INSERT INTO MentalDiseases (diseaseID, diseasename, symptoms1, symptoms2, symptoms3, symptoms4, symptoms5)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
""", mental_diseases)

C.executemany("""
    INSERT INTO BoneDiseases (diseaseID, diseasename, symptoms1, symptoms2, symptoms3, symptoms4, symptoms5)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
""", bone_diseases)

C.executemany("""
    INSERT INTO EyeDiseases (diseaseID, diseasename, symptoms1, symptoms2, symptoms3, symptoms4, symptoms5)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
""", eye_diseases)

C.executemany("""
    INSERT INTO StomachDiseases (diseaseID, diseasename, symptoms1, symptoms2, symptoms3, symptoms4, symptoms5)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
""", stomach_diseases)

C.executemany("""
    INSERT INTO EarNoseDiseases (diseaseID, diseasename, symptoms1, symptoms2, symptoms3, symptoms4, symptoms5)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
""", earnose_diseases)


d.commit()

#Create Epedemic Check Table
C.execute("""CREATE TABLE IF NOT EXISTS epedemiccheck (
diseaseID VARCHAR(255) PRIMARY KEY,
diseasename VARCHAR(255) NOT NULL,
cases INT NOT NULL,
location VARCHAR(50) NOT NULL)""")

# Clear screen function
def clear_screen():
    time.sleep(2)  # Pause for 3 seconds before clearing the screen
    os.system('cls' if os.name == 'nt' else 'clear')




#Symptoms Scanner Function
def scansym():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    gender = input("Enter your gender: ")

    print("\nWhat issue are you facing? Kindly choose one from below by entering the number:")
    print("1) Fever, Cold or Cough related")
    print("2) Pregnancy related problems")
    print("3) Skin issues or allergies")
    print("4) Mental health concerns (anxiety, depression, etc.)")
    print("5) Stomach problems (pain, indigestion, diarrhea)")
    print("6) Bone or joint pain")
    print("7) Eye or vision problems")
    print("8) Ear, nose or throat problems")
    print("9) Injury or wounds")
    print("10) Other: (experiencing chest pain or other symptoms)") 

    choice = input("Enter your choice (1–9): ")

    severity = None
    alert = ""

    if choice == "2":
        pregnancy_details = {}

        pregnancy_details['weeks'] = input("How many weeks pregnant are you (or enter 'unknown')? ")

        print("\nAre you experiencing any of these symptoms? Enter yes or no.")
        pregnancy_details['nausea'] = input("Nausea or vomiting? ")
        pregnancy_details['pain'] = input("Abdominal pain? ")
        pregnancy_details['bleeding'] = input("Spotting or bleeding? ")
        pregnancy_details['swelling'] = input("Swelling in hands, feet or face? ")
        pregnancy_details['high_bp'] = input("High blood pressure? ")
        pregnancy_details['fetal_movement'] = input("Reduced fetal movement? (if applicable): ")

    # Store the answers in lowercase to prevent case issues
        symptoms_to_watch = [
            pregnancy_details['nausea'].lower(),
            pregnancy_details['pain'].lower(),
            pregnancy_details['bleeding'].lower(),
            pregnancy_details['swelling'].lower(),
            pregnancy_details['high_bp'].lower(),
            pregnancy_details['fetal_movement'].lower()
        ]

    # Check if any of the answers were "yes"
        if "yes" in symptoms_to_watch:
            print("\n⚠️ If you are experiencing any of the following symptoms, kindly contact your doctor and remain calm 🙏\n"
                  "- Nausea or vomiting\n"
                  "- Abdominal pain\n"
                  "- Spotting or bleeding\n"
                  "- Swelling in hands, feet, or face\n"
                  "- High blood pressure\n"
                  "- Reduced fetal movement (if late-stage)\n")
            time.sleep(3)
            main_program()
        else:
            print("No severe symptoms detected, but monitor your health and consult a doctor if needed.")
            time.sleep(3)
            main_program()
            
                    
    if choice == "9":
        print("\nPlease categorize the injury based on its severity:")
        print("1) Minor – small cuts, bruises, or scrapes")
        print("2) Moderate – swelling, mild bleeding, or deeper wounds")
        print("3) Severe – heavy bleeding, broken bones, burns, or head injury")

        severity_choice = input("Enter the severity level (1–3): ")

        severity_levels = {
            "1": "Minor",
            "2": "Moderate",
            "3": "Severe"
        }

        severity = severity_levels.get(severity_choice, "Unknown")

        # Add appropriate alerts
        if severity_choice == "3":
            alert = "\n🚨 ALERT: This may be a medical emergency. Please visit the Emergency Room (ER) immediately."
        if severity_choice == "2":
            alert = "\n⚠️ Note: If the issue continues or worsens, please visit the Emergency Room (ER)."
        if severity_choice=="1":
            alert="Keep monitoring the injury. If it worsens, go to the Emergency Room (ER)."
        if severity:
            print("Injury Severity:", severity)
            print(alert)
            time.sleep(4)
            main_program()
    if choice=="10":
        print("Go to the Emergency Room Immediately!!!")
        time.sleep(4)
        main_program()


    # Final Output
    if choice!="2" and choice!="9" and choice!="10":
        clear_screen()
        print("\nThank you,", name + ".")
        print("Age:", age)
        print("Gender:", gender)
        sym1=input("Enter Symptom 1:").lower()
        sym2=input("Enter Symptom 2:").lower()
        sym3=input("Enter Symptom 3:").lower()
        if choice=="1":
            C.execute("Select * from FeverColdDiseases")
            result=C.fetchall()
            found=False
            for i in result:
                symptom_fields = [s.lower() for s in i[2:7]]
                if sym1 in symptom_fields and sym2 in symptom_fields and sym3 in symptom_fields:
                    print("You may have...")
                    print("Disease ID:",i[0])
                    print("Disease Name:",i[1])
                    found=True
                    time.sleep(4)
                    main_program()
            if found==False:
                print("Please visit the doctor.")
        elif choice=="3":
            C.execute("Select * from SkinDiseases")
            result=C.fetchall()
            found=False
            for i in result:
                symptom_fields = [s.lower() for s in i[2:7]]
                if sym1 in symptom_fields and sym2 in symptom_fields and sym3 in symptom_fields:
                    print("You may have...")
                    print("Disease ID:",i[0])
                    print("Disease Name:",i[1])
                    found=True
                    time.sleep(4)
                    main_program()
            if found==False:
                print("Please visit the doctor.")
                time.sleep(4)
                main_program()
        elif choice=="4":
            C.execute("Select * from MentalDiseases")
            result=C.fetchall()
            found=False
            for i in result:
                symptom_fields = [s.lower() for s in i[2:7]]
                if sym1 in symptom_fields and sym2 in symptom_fields and sym3 in symptom_fields:
                    print("You may have...")
                    print("Disease ID:",i[0])
                    print("Disease Name:",i[1])
                    found=True
                    time.sleep(4)
                    main_program()
            if found==False:
                print("Please visit the doctor.")
                time.sleep(4)
                main_program()
        elif choice=="5":
            result=C.fetchall()
            found=False
            for i in result:
                symptom_fields = [s.lower() for s in i[2:7]]
                if sym1 in symptom_fields and sym2 in symptom_fields and sym3 in symptom_fields:
                    print("You may have...")
                    print("Disease ID:",i[0])
                    print("Disease Name:",i[1])
                    found=True
                    time.sleep(4)
                    main_program()
            if found==False:
                print("Please visit the doctor.")
                time.sleep(4)
                main_program()
        elif choice=="6":
            C.execute("Select * from BoneDiseases")
            result=C.fetchall()
            found=False
            for i in result:
                symptom_fields = [s.lower() for s in i[2:7]]
                if sym1 in symptom_fields and sym2 in symptom_fields and sym3 in symptom_fields:
                    print("You may have...")
                    print("Disease ID:",i[0])
                    print("Disease Name:",i[1])
                    found=True
                    time.sleep(4)
                    main_program()
            if found==False:
                print("Please visit the doctor.")
                time.sleep(4)
                main_program()
        elif choice=="7":
            C.execute("Select * from EyeDiseases")
            result=C.fetchall()
            found=False
            for i in result:
                symptom_fields = [s.lower() for s in i[2:7]]
                if sym1 in symptom_fields and sym2 in symptom_fields and sym3 in symptom_fields:
                    print("You may have...")
                    print("Disease ID:",i[0])
                    print("Disease Name:",i[1])
                    found=True
                    time.sleep(4)
                    main_program()
            if found==False:
                print("Please visit the doctor.")
                time.sleep(4)
                main_program()
        elif choice=="8":
            C.execute("Select * from EarNoseDiseases")
            result=C.fetchall()
            found=False
            for i in result:
                symptom_fields = [s.lower() for s in i[2:7]]
                if sym1 in symptom_fields and sym2 in symptom_fields and sym3 in symptom_fields:
                    print("You may have...")
                    print("Disease ID:",i[0])
                    print("Disease Name:",i[1])
                    found=True
                    time.sleep(4)
                    main_program()
            if found==False:
                print("Please visit the doctor.")
                time.sleep(4)
                main_program()
        else:
            print("Invalid Choice. Please Try Again.")
            clear_screen()
            scansym()
        



#Local Disease Portfolio
def setup_disease_table():
    print("checking for local communicable diseases...")
    x=input("What state are you from?")
    x=x.title()
    print("it is advisable to first rule out the following diseases based on your region")
    state_diseases = {
        "Delhi": ["Dengue", "Chikungunya", "Tuberculosis", "Hepatitis A"],
        "Maharashtra": ["Malaria", "Dengue", "Leptospirosis", "Swine Flu"],
        "Uttar Pradesh": ["Cholera", "Typhoid", "Tuberculosis", "Hepatitis E"],
        "Tamil Nadu": ["COVID-19", "Dengue", "Tuberculosis", "Leptospirosis"],
        "Karnataka": ["Tuberculosis", "Dengue", "Chikungunya", "Hepatitis A"],
        "West Bengal": ["Cholera", "Dengue", "Encephalitis", "Malaria"],
        "Telangana": ["Dengue", "Chikungunya", "Hepatitis A", "Typhoid"],
        "Rajasthan": ["Malaria", "Dengue", "Typhoid", "Cholera"],
        "Gujarat": ["Chikungunya", "Hepatitis E", "Malaria", "Leptospirosis"],
        "Kerala": ["Nipah Virus", "Leptospirosis", "Dengue", "Hepatitis A"],
        "Punjab": ["Tuberculosis", "Swine Flu", "Hepatitis C", "Dengue"],
        "Haryana": ["Tuberculosis", "Hepatitis A", "Typhoid", "Swine Flu"],
        "Madhya Pradesh": ["Malaria", "Cholera", "Dengue", "Tuberculosis"],
        "Bihar": ["Cholera", "Japanese Encephalitis", "Typhoid", "Tuberculosis"],
        "Assam": ["Japanese Encephalitis", "Malaria", "Dengue", "Tuberculosis"],
        "Odisha": ["Cholera", "Malaria", "Dengue", "Hepatitis A"],
        "Jharkhand": ["Malaria", "Dengue", "Cholera", "Tuberculosis"],
        "Chhattisgarh": ["Malaria", "Tuberculosis", "Dengue", "Leptospirosis"],
        "Himachal Pradesh": ["Swine Flu", "Tuberculosis", "Typhoid", "Hepatitis A"],
        "Goa": ["Leptospirosis", "Dengue", "Malaria", "Hepatitis A"]
}
    if x in state_diseases.keys():
        print(state_diseases[x])
        time.sleep(5)
        main_program()
    else:
        print("Not an Indian State")
        time.sleep(4)
        main_program()
#Main Screen
def main_program():
    clear_screen()
    print("{:>60}".format("-->>SCANALYZE<<--"))
    print("{:>68}".format("What can we do for you today?"))
    ops=int(input("""1. Scan your symptoms
2. Disease Lookup
3. Exit
Enter your option:"""))
    if ops==1:
        clear_screen()
        scansym()
    elif ops==2:
        clear_screen()
        setup_disease_table()
    elif ops==3:
        print("Thank you for using Scanalyze. Visit Again!!!")
        tables=[
    'FeverColdDiseases',
    'SkinDiseases',
    'MentalDiseases',
    'StomachDiseases',
    'BoneDiseases',
    'EyeDiseases',
    'EarNoseDiseases'
]
        for table in tables:
            C.execute(f"DROP TABLE IF EXISTS {table}")
        d.close()
        time.sleep(3)
        sys.exit()
    else:
        print("Invalid Choice. Please Try Again.")
        main_program()
main_program()        
        
        
    
