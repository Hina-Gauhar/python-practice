# Problem 3: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
# Salary(Lakhs) : Tax(%)

# Below 5 : 0%
# 5-10 : 10%
# 10-20 : 20%
# aboove 20 : 30%
ctc=int(input("enter ur ctc"))
print("After tax eduction ur salary is: ")
HRA=(ctc*10)/100
DA= (ctc*5)/100
PF= (ctc*3)/100
salary=ctc-(HRA + DA +PF)

if(salary<5):
  print(salary)
elif(salary>5 and salary<10):
  ten=(salary*10)/100
  salary=salary-ten
  print(salary)
elif(salary>10 and salary<20):
  twenty=(salary*20)/100
  salary=salary-twenty
  print(salary)
else:
  thirty=(salary*30)/100
  salary=salary-thirty
  print(salary)
