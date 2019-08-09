#calculator
print("1 for integral caluclator 2 for float calci")
type=int(input("enter the type of claci"))

if (type==1):
    a=int(input("enter 1st no"))
    b=int(input("enter 2nd no"))

elif(type==2):
    a=float(input("enter 1st no"))
    b=float(input("enter 2nd no"))

def addition():

    add=a+b
    return add


def subtraction():
    sub=a-b
    return sub


def multiplication():
    mult=a*b
    return mult


def division():
    div=a/b
    return div


print("1 for addition  2 for subtraction  3 for multiplication  4 for division ")
choice=int(input("enter the choice"))

if(choice==1):
    add=addition()
    print("addition=",add)
elif(choice==2):
    sub=subtraction()
    print("subtraction=",sub)  
elif(choice==3):
    mult=multiplication()
    print("multiplication=",mult)
elif(choice==4):
    div=division()
    print("division=",div)


