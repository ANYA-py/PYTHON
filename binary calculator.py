def b_t_d():
    a = int(input("enter a binary num\n"))
    b = len(str(a))
    f  =0
    for i in range(b):
        d = a%10
        e = d*(pow(2,i))
        a = a//10
        f = f+e
    print(f)
def d_t_b():
    a = int(input("enter a decimal num\n"))
    i = a
    c = ""
    while i >= 1:
        b = str(a % 2)
        a = int(a // 2)
        c = c + b
        i = a
    d = c[::-1]
    print(d)
k = int(input("for converting decimal to binary ,press 1\n"
          "for converting binary to decimal to binary,press 2\n"))
if k == 1:
    d_t_b()
elif k == 2:
    b_t_d()
else:
    print("wrong number")
