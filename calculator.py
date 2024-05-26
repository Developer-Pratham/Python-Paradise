print("Do you want to use the calculator?")
use=input("\n Enter y for yes and n for no: ")
while (use=='y'):
    global x,y
    print("Simple Calculator program using python")
    x=int(input("Enter the first number: "))
    y=int(input("Enter the second number: "))
    print("\n Choose from the following choices : ")
    print(''' press + to add
        \n press - to substract
        \n press * to multiply
        \n press / to divide
        \n press % for modulo''')
    choice=str(input("Enter your choice: "))

    def add():
        print("\n The addition will be: ",x+y)

    def sub():
        print("\n The substraction will be: ",x-y)

    def mult():
        print("\n The multiplication will be: ",x*y)

    def div():
        print("\n The division will be: ",x/y)

    def rem():
        print("\n The remainder will be: ",x%y)

    if (choice== '+'):
        add()
    elif(choice== '-'):
        sub()
    elif(choice== '*'):
        mult()
    elif(choice== '/'):
        div()
    elif(choice== '%'):
        rem()
    else:
        print("Invalid choice!!")

    print("Do you want to use the calculator again?")
    use=input("\n Enter y for yes and n for no: ")
    

    
    
