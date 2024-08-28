
def add_name(my_dict):
    name = input("Enter the name: ")
    class_name = input("Enter the class: ")
    print("Enter 2 the grades")
    grades =[]
    x = int(input("Grade 1: "))
    grades.append(x)
    y = int(input("Grade 2: "))
    grades.append(y)
    
    
    n = len(my_dict)
    my_dict[n+1] = [name, class_name, grades]

def print_dict(my_dict):
    print("student ID", "   name   ", "   class   ", "   list of grades")
    for key, val in my_dict.items():
        print(key,"           ",val[0], " ",val[1],"           ", val[2])


def upgrade_grades(my_dict):
    print_dict(my_dict)
    stud_id = int(input("Enter the id of the student: "))
    for key, val in my_dict.items():
        if key == stud_id:
            name = val[0]
            class_name = val[1]
    print("Enter the updates grades :")
    new_grades =[]
    x = int(input("Grade 1: "))
    new_grades.append(x)
    y = int(input("Grade 2: "))
    new_grades.append(y)
    
    my_dict[stud_id] =[name, class_name, new_grades] 

def calc_avg(stud_id):
    for key, val in my_dict.items():
        if key == stud_id:
             total =  sum(val[2])
             avg = float(total/ len(val[2]))
        
    return avg

def generate_top(my_dict):
    x = int(input("Enter the class :"))
    max_grade = 0
    stud_id = 0
    for key, val in my_dict.items():
        if val[1]==x:
            if max_grade > calc_avg(key):
               max_grade = calc_avg(key)
               stud_id = key
        print("The maximum grade is of", stud_id)
    

my_dict = {1:["Sushweta",12,[10,9]]}
print("Hello user")
men = 1
while men ==1:
    print(''' 1. Add a student''')
    print(''' 2. Update grades''')
    print(''' 3. Calculate the average''')
    print(''' 4. Generate Top Students''')
    print(''' 5. Print''')
    print(''' 6. Exit''')
    choice = int(input("Enter  a number:"))
    if choice == 1:
        add_name(my_dict)
    elif choice == 2:
        upgrade_grades(my_dict)
    elif choice == 3:
        print_dict(my_dict)
        stud_id = int(input("Enter the id of the student: "))
        #calc_avg(stud_id)
        print("Average of student with id = ", calc_avg(stud_id))
    elif choice == 4:
        generate_top(my_dict)

    elif choice == 5:
        print_dict(my_dict)
    else:
        men=0
        
