#question No 2 
#  extract the username form a give email

email=input("enter your email: ")
a= email.split('@')
username=a[0]
print("Your username is :",username)
