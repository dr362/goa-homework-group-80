# 0) კომენტარის სახით ახსენი რა განსხვავებაა tuple-სა და list შორის
#tuple არის უცვლელი ხოლო list ცვალებადი(არვიცი სიტყვა სწორად დავწერე თუ არა) არის
# 1)შექმენი sports tuple რომელშიც შეინახავ 5 ელემენტს
sports = ("football","basketball","tennis","swimming","dancing")
# 2)გვაქვს tuple-ში შემდეგი ელემენტები banana,cucumber,tomato,apple და სამი ცვლადი green red და yellow
# დაალეგე ეს ელემენტები tuple ში ისე რომ unpacking-ის შემდეგ ყველა ცვლადში შესაბამისი ფერის მქონე იყოს
# (ცვლადების მიმდევრობა არ უნდა შეცვალო, უნდა იყოს green, red და yellow)
fruits = ("apple","cucumber","tomato","banana")
(*green, red, yellow) = fruits

# 3) N1 დავალებაში შექმნილ tuple-ში შეანაცვლე რომელიმე ელემენტი
sports = list(sports)
sports[1] = "running"
# 4)შექმენი tuple და გაამრავლე ის მომხმარებლის მიერ შემოტანილ რიცხვზე
num = int(input("Please enter the number you want to multiply a tuple with: "))
tup = ("a","b","c","d","e","f","g")
print(tup * num)
print(sports)
print(fruits)





# 0) კომენტარის სახით ახსენი set-ის თავისებურებებi
#set - ყველაფერს დაულაგებლად ალაგებს და სულ ურევს ელემენტებს(შანსი არის რომ დალაგებულიც იყოს), დუპლიკატებს შლის, 0 = false
# 1)შექმენი დუპლიკატებიანი სეტი და დაპრინტე რათა ნახო შედეგი
s = {"alex","deme","gabriel","gabriel","daniel"}
print(s)