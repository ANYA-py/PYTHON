a = int(input("enter a number\n"))
e = a
b = 0
for i in range(len(str(a))):
    b = b+1
c = 0
for i in range(len(str(a))):
    d = a%10
    c = pow(d,b)+c
    a = a//10
if e in range(1, 10):
    print("It is an Armstrong number")
elif e == c:
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")
