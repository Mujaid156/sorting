usernames = ["Zaid", "Aaliyah", "Lithe", "Thabo", "Zoe"]
passwords = ["1000", "5566", "7700", "1244", "4953"]

name = input("Enter username: ")
pword = input("Enter password: ")
found = False
for x1 in range(len(usernames)):
    if name == usernames[x1] and pword == passwords[x1]:
        found = True
if found == True:
        print("Access granted")
else:
    print("Access denied")






