'''Part A'''
total_cost = float(input("Enter total cost of your dream home : "))
pdp = total_cost * 0.25
annual_salary = float(input("Enter your annual salary : "))
a = float(input("percentage to be saved from your salary : "))
pts = (annual_salary/12)*(a/100)
cs=0
i=0
while cs <= pdp :
    cs = cs + pts + ((cs*0.04)/12)
    i += 1
b = str(i)
print("months to be needed : " + b )









