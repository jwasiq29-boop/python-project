n1 = int(input("enter the first number: "))
n2 = int(input("enter the second number: "))
print(n1, '+' ,n2 ,'=' , n1 + n2)
print(n1, '-' ,n2 ,'=' , n1 - n2)
print(n1, '*' ,n2 ,'=' , n1 * n2)
print(n1, '/' ,n2 ,'=' , n1 / n2)
print(n1, '%' ,n2 ,'=' , n1 % n2)
print(n1, '**' ,n2 ,'=' , n1 ** n2)
print(n1, '//' ,n2 ,'=' , n1 // n2)



n1 = int(input("enter the 3gread number: "))
x = n1 % 10
x1 = n1 // 10
x2 = x1 % 10
x3 = x1 // 10
x4 = x3 % 10
c1 = x4 + x2 + x
print( 'result' ,x4 ,  '\n' , x2 ,  '\n' , x ,'\n' , c1 , sep ="")




all = float(input("al money 'value' " ))  # موجودی حساب 

m1 = float(input("enter the 'cost value 1': "))  # هزینه اولیه
m2 = float(input("enter the 'cost value 2': "))  # هزینه دومی
cost = m1 + m2   # مجموع هزینه ها 

print("all costs :" , cost)




x = all - cost   # موجودی بعد از کات هزینه ها 
print("acc balance after cuting costs :" , x)


recive = float(input("enter the 'recive value ' "))

acc = recive + x #موجودی حساب بعد دریافت پول 
print("the balnce after money recives :" , acc)





name = input("enter your name : ")
f_name = input("enter your last name : ")
user_name = input("enter your user name : ")
city = input("enter the name of your city that you live : ")

print(name.strip(" "))
print('@' + user_name)
print(user_name.upper())
print(len(name))


mark = int(input("number: "))

if mark <= 20 and mark >= 15:
    print("accepted!" ,"'A' grade")
elif mark <= 10 and mark < 15:
    print("accepted!" , "'B'grade")
elif mark < 10 and mark >= 0:
    print("rejected!","'C' grade")
else:
    print("no")