emplist=[]
while True:
    #print("welcome to emp list:")              This is just a welcome message
    #print("1. Add employe : ")                 CHOICE 1 This is to add the employee to the list
    #print("2. show all employes :")            CHOICE 2 THIS IS TO SHOW THE COMPLETE LIST OF THE EMPLOYESS
    #print("3. Details of the employes :")      CHOICE 3 THIS IS TO SHOW THE DEAILS OF THE EMPLOYESS INDIVIDUALLY
    #print(" update employe :")                 CHOICE 4 THIS IS TO UPDATE A EMPLOYEE DATA
    #print("Delete the employee :")             CHOICE 5 THIS IS TO DELETE/REMOVE A EMPLOYEE DATA
    #print("6. Exit")                           CHOICE 4 TO EXIT THE PROGRAM
    print()

    choice =int(input("enter your choice : "))
    print()
    

    if choice== 6:
       print("EXIT End of Program")


    if choice == 1:
        name = input("Enter the Employee name :")
        designation = input("Enter designation : ")
        sal = input("Enter salary :")
        dict = {"name":name, "designation":designation, "sal":sal}
        emplist.append(dict)
    #  print()

    if choice == 2:
        print("print list of employess below : ")
        for emp in emplist:
            for k in emp.keys():
                print (k,":",emp[k])
                print()

    if choice == 3:
        empname = input("Enter Employee Name :")
        isFound = False
        for emp in emplist:
            if emp['name'] == empname:
                isFound=True
                print("\n name", emp['name'], "\n designation", emp['designation'], "\n sal", emp['sal'] )
                #print("designation", emp['designation'])
                #print("sal", emp['sal'])
                break
                if isFound==False:
                        print("employee not found : ")

    if choice == 4:
        empname = input("enter employee name :")
        isFound=False
        for emp in emplist:
            if emp['name'] == empname:
                isFound=True
                designation=input("enter nre designation name :")
                salary=input("enter new salary : ")
                emp['designation']=designation
                emp['sal']=salary
                print("Update Sucessfully")
                break
        isFound=False
        print ("employee not found")

    if choice == 5:
        empname = input("enter employee name :")
        isFound = False
        for emp in emplist:
            if emp['name'] == empname:
                isFound = True
                emplist.remove(emp) #or you can use del code instead of remove CODE
                #del emp
                print("Deleted Sucessfully")
                print()
                break
            if isFound==False:
                print("employee not found")
        print()

