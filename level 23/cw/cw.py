# 1) ახსენით როგორ მუშაობს .upper(), .lower(), .capitalize()
#.upper - ყველა პატარა ასოს დიდს ხდის
#.lower - ყველა დიდ ასოს პატარას ხდის
#.capitalize - ყველაზე პირველ ასოს დიდს ხდის
# 2) მომხმარებელს შემოატანინეთ მისი სახელი და დაპრინტეთ ის დიდი ასოებით
name = input("Please enter your name: ")
print(name.upper())
# 3)შექმენით სტრინგების სია და შეინახეთ 5 სტრინგი, დაპრინტეთ ამ სიაში არსებული ყველა სტრინგი ისე რომ პირველი ასო იყოს დიდი, დანარჩენი კი პატარები
list_ofnames = ["hi","hello","bye","goodbye","how are you"]
print(list_ofnames.capitalize())
# 4)მომხმარებელს შემოატანინე თავისი გვარი და გაარკვიე არის თუ არა ამ გვარში ასო ტ, თუ არის დაპრინტე True, სხვა შემთხვევაში False
surname = input("Please enter your surname: ")
if surname.find("T") == True:
    print(True)
else:
    print(False)
# 5)მომხმარებელს შემოატანინე მისი გვარი, შემდეგ შეეიკითხე რომელ case-ში უნდა რომ მისი გვარი დაიწეროს (თუ შემოიტანა upper, დაუბეჭდეთ მისი გვარი გადიდებულად / თუ შემოიტანა lower, დაუბეჭდეთ მისი გვარი დაპატარავებული ასოებით / თუ შემოიტანა capitalize, პირველი ასო გაადიდეთ დანარჩენი დააპატარავეთ, თუ შემოიტანა none მაშინ არ შეცვალოთ და სხვა შემთხვევაში დაუბეჭდეთ incorrect input
surname2 = input("Please enter your name: ")
type = input("Please enter your type of surname: ")
if type == "Upper":
    print(surname2.upper())
elif type == "Lower":
    print(surname2.lower())
elif type == "Capitalize":
    print(surname2.capitalize())
elif type == "None":
    print(surname2)

# 6)მომხმარებელს შემოტანინეთ წინადადება და სიმბოლო, საბოლოოდ დაუპრინტეთ რომელ ინდექსზე დგას პირველივე შემხვედრი შემოტანილი სიმბოლო

# 7)მომხმარებელს შემოტანანინე წინადადება და სიმბოლო, საბოლოოდ იპოვე ამ წინადადებაში რომელ ინდექსებზე დგას ყველა ეს სიმბოლო (როგორც ჩვენ გავაკეთეთ)
sentence = input("Please enter a sencentce: ")
pickle = ""

for i in range(len(sentence)):
    if(sentence[i] == "?"):
        pickle += str(i) + " "
print(pickle)