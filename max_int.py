max_int = 0

while True:
    num_int = int(input("Input a number: "))
    if num_int < 0:
        break
    else:
        max_int = max(max_int, num_int)

        #this is a commant

print("The maximum is", max_int)         

