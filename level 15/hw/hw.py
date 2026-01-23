# 1)მომხმარებელს შემოატანინეთ მისი სახელი და თუ ეს სახელი უდრის თქვენს სახელს, დაბეჭდეთ "Hello" სხვა შემთხვევაში "Bye".

name = input("Please enter your name: ")
if name == "alexandre":
    print("Hello")
else:
    print("Bye Bye")

# 2)ცვლადში შეინახეთ თქვენი საყვარელი რიცხვი და მომხმარებელს შემოატანინეთ ასევე მისი საყვარელი რიცხვი, თუ თქვენი რიცხვები ემთხვევა მაშინ დაბეჭდეთ "Perfect" თუ მისი რიცხვი მეტია, დაბეჭდეთ "More", სხვა შემთხვევაში "Less".

my_fav = 7
your_fav = int(input("Enter your fav number: "))
if my_fav == your_fav:
    print("Perfect")
elif my_fav > your_fav:
    print("More")
else:
    print("Less")

# 3)მომხმარებელს შემოატანინეთ მისი ასაკი და ასევე მისი სახელი, თუ მომხმარებლის სახელი ემთხვევა თქვენს სახელს და ასევე მისი ასაკი ემთხვევა თქვენს სახელს, დაბეჭდეთ "Twins" სხვა შემთხვევაში "Not Twins".

name = input("Please enter your name again: ")
age = int(input("please enter your age again: "))
if name == "alexandre" and age == 11:
    print("Twins")
else:
    print("Not twins")


# 4)დაწერე პროგრამა, რომელიც ამოწმებს რიცხვი არის თუ არა ის ერთდროულად 3-ისა და 5-ის ჯერადი.

number = int("Please enter a number: ")
if number % 3 == 0 and number % 5 == 0:
    print(True)
else:
    print(False)

# 5) დაწერე პროგრამა, რომელიც ამოწმებს პაროლის სიგრძეს.
# თუ პაროლი 8 სიმბოლოზე ნაკლებია → „სუსტი პაროლი“,
# წინააღმდეგ შემთხვევაში → „კარგი პაროლი“.
password = int(input("Please enter your password: "))
for i in password:
    if i > 8:
        print("strong")
    else:
        print("weak")