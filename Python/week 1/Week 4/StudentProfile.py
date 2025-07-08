student = {}

studentName =input("Enter your student's name: ")
student["Name"] = studentName

print(student)

student = {}

studentAge = input("Enter your age: ")
student["Age"] = studentAge

print(student)

student = {}

studentGrade = input("Enter your grade level: ")
student["Grade"] = studentGrade

print(student)


hobbies = []
hobby = input("Enter your student's hobby:Type 'Done' when done:").lower()
hobbies.append(hobby)

while hobby != "done":
    hobby = input("Enter your student's hobby:Type 'Done' when done:").lower()    
    hobbies.append(hobby)
   
student["Hobbies"] = hobbies

