n = int(input("Enter the length of the sequence: ")) # Do not change this line

num1 = 1
num2 = 2
num3 = 3

if n >= 1:
    print(num1)
if n >= 2:    
    print(num2)
if n >= 3:    
    print(num3)

for i in range(3, n):
    max_num = num1 + num2 + num3
    print(max_num)
    num1 = num2
    num2 = num3
    num3 = max_num
  
