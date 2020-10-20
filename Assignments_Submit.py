num = (1, 2, 3, 4, 5)
print(type(num))
print(max(num))
print()

num1=int(input('Enter the Number:'))
for i in range(2,num1):
    if num1 % i ==0:
        print(num1,'It is a not a  Prime Number')
        break
else:
    print(num1,'It is a prime Number')
print()


num2=int(input('Enter a number:'))
if num2 % 2 ==0:
    print('This is a Even Number')
else:
    print('This is Odd Number')
