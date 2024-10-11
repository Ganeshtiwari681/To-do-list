task=[]

def add():
    x=int(input("How many task you want to add : "))
    for i in range(x):
        t=input("ENTER TASK: ")
        task.append(t)
    print("All task added to list...")

def update():
    t=input("ENTER TASK WHICH YOU WANT TO UPDATE : ")
    if t in task:
        up=input("ENTER NEW TASK : ")
        task[task.index(t)]=up
        print("Task updated...")
    else:
        print("Task not Persent !")

def delete():
    t=input("ENTER TASK WHICH YOU WANT TO DELETE : ")
    if t in task:
        task.remove(t)
        print("Task Deleted...")
    else:
        print("Task not Persent !")

def view():
    print("-------TODAY TASKS-------")
    for i in range(len(task)):
        print(i+1,"\t",task[i])
    print("-------------------------")
    
while True:
    print("-------MENU-------")
    print("1.   ADD\n2.   UPDATE\n3.   DELETE\n4.   VIEW\n5.   EXIT\n")
    ch=int(input("ENTER YOUR CHOISE : "))
    if ch==5:
        print("EXITING FROM THE PROGRAM....")
        break
    elif ch==1:
        add()
    elif ch==2:
        update()
    elif ch==3:
        delete()
    elif ch==4:
        view()
    else:
        print("Invalid Choise..")