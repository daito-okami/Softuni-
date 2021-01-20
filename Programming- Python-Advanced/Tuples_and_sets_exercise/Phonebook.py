phonebook = {}
a = input()
while True:
    if a[0].isdigit():
        break
    else:
        name, number = a.split("-")
        phonebook[name] = number
    a = input()


n = int(a)
for i in range(n):
    contact = input()
    if contact in phonebook:
        for key, value in phonebook.items():
            if contact == key:
                print(f"{contact} -> {phonebook[contact]}")
    else:
        print(f"Contact {contact} does not exist.")
