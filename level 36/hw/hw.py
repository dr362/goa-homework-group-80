# 0) შექმენი ხილების სეტი და ჩაამატე ყურძენი
fruits = {"apple","orange","pear"}
add = fruits.add("grape")
print(fruits)
# 1)შექმენი ფერების სეტი და მოაშორე ფერი რომელიც ყველაზე მეტად არ მოგწონს
colors = {"black","white","red","blue","pink"}
remove = colors.discard("pink")
print(colors)
# 2)მომხმარებელს შემოატანინე რაიმე ცხოველები და ჩასვი ისინი სეტში, შემდეგ მთლიანად გაასუფთავე ეს სეტი
animal = input("Please enter an animal: ")
ste = {"dog","cat","parrot"}
add2 = ste.add(animal)
print(ste)

# 3)group1 = {"Ana", "Gio", "Nika"} group2 = {"Nika", "Luka", "Saba"} ამ ორი სეტიდან დაპრინტე ის მოსწავლეები რომლებიც ორივე ჯგუფში არიან
group1 = {"Ana", "Gio", "Nika"}
group2 = {"Nika", "Luka", "Saba"}
inter = group1.intersection(group2)
print(inter)
# 4)პითონის გაშვების გარეშე კომენტარის სახით დაწერე რას გამოიტანს თითოეული პრინტი

# A = {1, 2, 3, 4} B = {3, 4, 5, 6}

# print(A.intersection(B)) - ამ ორი სეტიდან დუპლიკატებს ამოიღებს და დააბრუნებს მათ
# print(A.union(B)) - შეართებს სეტებს განახლების გარეშე
# print(A.difference(B)) - ამოიღებს განსხვავებულ ელემენტებს ამ ორი სეტიდან და დააბრუნებს მათ
# print(A.symmetric_difference(B)) - შეართებს ამ ორ სეტს დუპლიკატების გარეშე