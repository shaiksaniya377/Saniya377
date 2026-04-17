file = open("Emails.py", "r")

Emails = []

for line in file:
    Emails.append(line.strip())

file.close()

result = ";".join(Emails)
print(result)
