from sys import argv
import csv
import random

# Still unfinished. Will be reworked...

# Step 1
students = {}
def read_csv(filename):
    global students
    try:
        with open("Technical Basics I_2025 - Sheet1.csv") as my_file:
            reader = csv.DictReader(my_file)
            for row in reader:
                if not row["Name"]:
                    break
                name = row["Name"]
                stream = row["Stream"]
                grades = {}
                for i in range(1,14):
                    if i == 6:
                        continue
                    key = f"week{i}"
                    if key not in row:
                        grades[key] = None
                    else:
                        value = row[key]
                        if value == "-":
                            grades[key] = 0
                        elif value == "":
                            grades[key] = None
                        else:
                            grades[key] = int(value)
                students[name] = {"stream": stream, "grades": grades}
    except FileNotFoundError:
        print("File not found")
    return students
    # load csv to variables in your program
    # handle file exceptions here
    pass

# Step 2
def populate_scores():
    global students
    for student in students.values():
        for week, value in student["grades"].items():
            if value is None:
                student["grades"][week] = random.randint(0,3)
    pass

# Step 3
def calculate_all():
    global students
    for student in students.values():
        total_grades = list(student["grades"].values())
        best_10 = sorted(total_grades)[:10]
        student["total"] = sum(best_10)
    print(students)



    # loop through all the students and calculate grades
    pass

def calculate_total(scores):
    total = 0
    return total

def calculate_average(scores):
    average =  0
    return average

# After the update let's save the data as a new csv file

def write_csv(filename):
    pass

# Bonus

def print_analysis():
    # print average scores for stream A, B and every week
    pass

if __name__ == "__main__":
    script, filename = argv

    print("Open file:", filename)

    read_csv(filename)

    populate_scores()
    calculate_all()

    user_name = "[your_name]"

    newname = filename.split(".")[0] + "_calculated_by_" + user_name + ".csv"
    write_csv(newname)
    print("New file written:", newname)

    print_analysis()

# Run the file with `python grade_calculator.py sheet.csv`