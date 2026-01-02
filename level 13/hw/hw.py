# 1)გამოიტანეთ კენტი რიცხვები 0-დან 50-მდე

for i in range(1,50,2):
    print(i)

# 2)მომხმარებელს შემოატანინეთ მისი გვარი და გამოიტანეთ ამ გვარის თითოეული ასო ცალცალკე

surname = input("Please enter your surname: ")
for f in surname:
    print(f)

# 3)შექმენით for ციკლი 150ის დიაპაზონში და შეამოწმეთ თითოეული რიცხვი, თუ ეს რიცხვი არის ლუწი, მაშინ დაბეჭდეთ "even" ხოლო თუ იქნება კენტი, დაბეჭდეთ "odd".

for x in range(0,150):
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")

# 4) გამოიტანეთ რიცხვები 20-იდან 0-მდე, for ციკლით

for a in range(20,0,-1):
    print(a)

# 5)შექმენით ცვლადი სადაც შეინახავთ ორიგინალ აქაუნთის პაროლს, და while ციკლის მეშვეობით მომხმარებელს შეეკითხეთ აქაუნთის პაროლი იქამდე სანამ სწორედ არ გამოიცნობს.

name = "alexandre"
password = "something"
email = "sandrogabidzashvili98@gmail.com"
Name = input("Please enter name: ")
Password = input("Please enter password: ")
Email = input("Please enter Email: ")

while Name != name and Password != password and Email != email:
    Name = input("Please enter name: ")
    Password = input("Please enter password: ")
    Email = input("Please enter Email: ")