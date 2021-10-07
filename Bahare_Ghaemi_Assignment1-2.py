a = int(input("enter first side : "))
b = int(input("enter second side : "))
c = int(input("enter third side : "))

if(a+b>c):
    if a+c>b:
        if b+c>a:
            print("YES!  You can make a triangle with these sides...")
        else:
            print("ERROR!  You can NOT make a triangle with these sides...")
    else:
        print("ERROR!  You can NOT make a triangle with these sides...")
else :
    print("ERROR!  You can NOT make a triangle with these sides...")