num = int(input("Enter a number for the multiplication table: "))

print(f"Multiplication table for {num}:")

for a in range(1, 11):
    print(f"{num} x {a} = {num * a}")