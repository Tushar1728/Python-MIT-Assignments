total_cost = float(input("Enter total cost of your dream home : "))
pdp = total_cost * 0.25
annual_salary = float(input("Enter your annual salary : "))
a = float(input("percentage to be saved from your salary : "))
b = float(input("enter percentage semi annual salary raise : "))
sar = b/100
pts = (annual_salary/12)*(a/100)
cs=0
i=0
while cs <= pdp :
    cs = cs + pts + ((cs*0.04)/12)
    if i%6==0 and i!=0 :
        annual_salary = annual_salary + annual_salary*sar
        pts = (annual_salary/12)*(a/100)
    i += 1
c = str(i)
print("months to be needed : " + c )
