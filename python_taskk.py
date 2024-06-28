row=int(input("enter the row"))
col=int(input("enter the colum"))
for i in range(row):
    if i == 0:
        for j in range(col):
            if j % 2==0:
                print(" ___",end=" ")
            else: 
                print("   ",end="")
    print() 
    if col % 2 ==0:
        if i==0:
            for l in range(col):
                if  l % 2 == 0:
                    print("/  ",end=" ") 
                else:
                    print("\\___",end="")
            print()
            for h in range(col+1):
                    if  h %2 ==0 :
                        print("\\",end="")
                    else:
                         print("___/",end="   ")
        else:
            if i != row-1 :
                for l in range(col+1):
                    if  l % 2 == 0 :
                        print("/  ",end=" ") 
                    else:
                        print("\\___",end="")
                print()
                for h in range(col+1):
                        if  h %2 ==0 :
                            print("\\",end="")
                        else:
                            print("___/",end="   ")
            else:
                for l in range(col+1):
                    if   l % 2 == 0 :
                        print("/  ",end=" ") 
                
                    else:
                        print("\\___",end="")
                print()
                for h in range(col):
                      if h %2==0:
                            print("\\___/",end="   ")
    else:
        for l in range(col+1):
            if  l % 2 == 0:
                print("/  ",end=" ") 
            elif l==col:
                print("\\",end="")
            else:
                print("\\___",end="")
        print()
        for h in range(col+1):
                if h%2==0:
                  print("\\___/",end="   ")
                
print()





