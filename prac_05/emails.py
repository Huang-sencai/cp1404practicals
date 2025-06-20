email_to_name = {}

email = input("Email: ").strip()
while email != "":
    user_name= email.title().split('@')[0].replace('.', ' ').replace('_', ' ')
    whether = input(f"Is your name {user_name}? (Y/n) ").strip().lower()
    if whether == 'n' or whether == 'no':
        name = input("Name: ").strip()
    else:
        name = user_name
    email_to_name[email] = name.title()
    email = input("Email: ").strip()
print()
for email, name in email_to_name.items():
    print(f"{name} ({email})")