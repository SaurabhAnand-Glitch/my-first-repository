print("WELCOME TO IT COMPANY")
mgr=[]     #list for manager
prhd=[]    #list for project head
jreg=[]    #list for junior engineers
emp=[]     #common list for all the employees
print("choose designation  manager , projecthead , juniorengineer")
count=0
bcount=0
ccount=0
for j in range(1,5):
    name=input("enter your name")
    desg=input("your designation")
    if(desg=='manager'):
        
        count=count+1
        a="77"+"01"+str(count) #id for manager
        mgr.append(a)
        mgr.append(name)
        mgr.append(desg)
    elif(desg=='projecthead'):
        
        
        bcount=bcount+1
        b='77'+'02'+str(bcount) #id for project head
        prhd.append(b)
        prhd.append(name)
        prhd.append(desg)
    elif(desg=='juniorengineer'):
        
        ccount=ccount+1
        c='77'+'03'+str(ccount) #id for junior engineer
        jreg.append(c)
        jreg.append(name)
        jreg.append(desg)
    else:
        print("wrong choice")

print(mgr)
print(prhd)
print(jreg)

                              
