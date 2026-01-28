# This is Student DataBase Program


import json # Importing json

FILENAME = "studentsDB.json" # asigning this students.json file to this FILENAME variable

def load_students():
    try:
        with open(FILENAME, 'r')as f: # opeing the studentsDB.json file and reading that file
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


# This function will save the students data
def save_student(students):
    with open(FILENAME, 'w') as f: # opening the studentDB.file and writing in that file
        json.dump(students,f,indent=4)


# This function will add the students
def add_student(students):
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    marks = input("Enter marks: ")
    students.append({
        "id":sid,
        "name":name,
        "age":age,
        "course":course,
        "marks":marks 
    })
    save_student(students)
    print("Student added successfully")

# This function will display the students
def display_students(students):
    if not students:
        print("No Students records found")
        return # Returning to the main function 
    print("\n----- STUDENTS RECORDS -----")
    for s in students:
        print(f'ID: {s["id"]}, Name: {s["name"]}, Age: {s["age"]}, Course: {s["course"]}, Marks: {s["marks"]}')

# This function will search for student
def search_students(students):
    sid = input("Enter student ID to search: ")

    for s in students:
        if s['id'] == sid:
            print(f'Found -> {s}')
            return # Returning to the main function 
    print("Student Record Not Found")

# This function will update the studet
def update_student(students):
    sid = input("Enter Student ID to update: ")

    for s in students:
        if s["id"] == sid:
            s["name"] = input("Enter New Name: ").strip() # Updating the student
            s["age"] = input("Enter New Age: ").strip() # Updating the student
            s["course"] = input("Enter New Course Name: ").strip() # Updating the student
            s["marks"] = input("Enter New Marks: ").strip() # Updating the student

            save_student(students)
            print('Student Updated Successfully')
            return # Returning to the main function 
    print("Student Not Found")
        
# This function will delete the student
def delete_student(students):
    sid = input("Enter Student ID to delete: ")

    for s in students:
        if s["id"] == sid:
            students.remove(s) #Deleting the student from the list
            save_student(students)
            print(f'Student deleted Successfully')
            return # Returning to the main function 
    print("Student Not Found")




def main(): # This is the main funciton

    students = load_students() # calling the load_students() function

    while True: # This is the loop which is always true
        # These are the menu which will be shown to user
        print("\n====== StudentDB Menu =======")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Save & Exit")

        # Taking input from the user without leading and tralling spaces or anything with the help of strip
        choice = input("Enter your choice: ").strip() 

        # The TRUE condition will exicute 
        if choice == "1":
            add_student(students) # Calling the funciton 
        elif choice == "2":
            display_students(students) # Calling the funciton 
        elif choice == "3":
            search_students(students) # Calling the funciton 
        elif choice == "4":
            update_student(students) # Calling the funciton 
        elif choice == "5":
            delete_student(students) # Calling the funciton 
        elif choice == "6":
            save_student(students)
            print("Data saved. Existing program.")
            break # This will 'break' the loop
        else: # If the choice is not an one of this then the else will be exicuted 
            print("Invalid choice! Try again.")


main() # calling the main function in globally