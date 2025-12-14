#Calculator
def add(s,r):
    #this function is used for addding two numbers
    return s + r 

def subtract(s,r):
    #this function is used for subtracting two numbers
    return s - r 

def multiply(s,r):
    #this function is used for multiplying two numbers
    return s * r 

def division(s,r):
    #this function is used for dividing two numbers
    return s / r 

print("Please select the operation")
print("a.Add")
print("b.subtract")
print("c.multiply")
print("d.divide")

choice = input("Please enter the choice(a/b/c/d)")

num_1 = int(input("please enter the first number"))
num_2 = int(input("please enter the second number"))

if choice =='a':
    print(num_1,'+',num_2,'=',add(num_1,num_2))
elif choice =='b':
    print(num_1,'-',num_2,'=',subtract(num_1,num_2))
elif choice =='c':
    print(num_1,'*',num_2,'=',multiply(num_1,num_2))
elif choice =='d':
    print(num_1,'/',num_2,'=',division(num_1,num_2))

else:
    print('its invaild choice')