first_name = str(input("Enter your first name: ")).strip()
last_name = str(input("Enter your last name: ")).strip()
section = str(input("Enter your section: ")).strip()
event_title = str(input("Enter event title: ")).strip()

full_name = first_name + last_name

print("Name:", full_name.title())
print("Name code:", full_name.upper())
print("Section:", section.upper())
print("Event:", event_title.title())