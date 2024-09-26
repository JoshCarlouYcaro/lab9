salary = float(input("Enter montly salary: "))
loan = float(input("Enter loan amount: "))
max_loan = salary * 10
interest = loan * 1.
if(salary>=30000):
    if(loan <= max_loan):
        print("You are eligible for a loan")
        month = int(input("How many months to pay?: "))
        monthly = interest / month
        print(f"Your total loan amount with 10 interest is {interest:.1f}")
        print(f"Your monthly payment over {month} months is {monthly:.1f}")
    else:
        print("You are not eligible for a loan: HIGH LOAN")
else:
    print("You are not eligible for a loan: LOW SALARY")