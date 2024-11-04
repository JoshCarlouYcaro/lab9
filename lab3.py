name = str(input("Enter Name"))
first = float(input("Enter 1st Grade"))
second = float(input("Enter 2nd Grade"))
third = float(input("Enter 3rd Grade"))
average = first + second + third 
new_average = average/3
print(new_average)

if new_average>=95:
    print("Highest Honor")
if new_average>=85:
    print("Average Honor")
else:
    print("Congrats")    
