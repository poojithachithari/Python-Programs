stu ={"varsha": 90, "Padma": 100, "Sanjana": 95}
name = input("Enter the student's name: ")

if name in stu:
    print(f"{name}'s marks: {stu[name]}")
else:
    print("Student Not Found")