princle=float(input("enter the princle amount"))
time=float(input("enter the time of periods"))
age=int(input("enter the customer age"))

if age>= 60:
   rate_of_interest=12
else:
   rate_of_interest=10
simple_interest=(princle*rate_of_interest*time)/100
print(f"the simple interest:{simple_interest:2f}")
