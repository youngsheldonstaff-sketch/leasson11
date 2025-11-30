

number_str = input("Enter an integer: ")


num = abs(int(number_str)) 

count = 0


if num == 0:
    count = 1
else:
    
    temp_num = num
    while temp_num > 0:
        temp_num //= 10 
        count += 1      

# Print the result
print(f"The total number of digits in {number_str} is: {count}")





    
   