email=input("enter the email")
place=email.index("@")
username=email[:place]
Domain=email[(place+1):]
print("username",username)
print("Domain",Domain)