
1. #A restaurant menu with prices for each item
2. #High scores to an arcade game
3. #All of the months of the year
4. #All the items in your backpack
5. #Look up Student emails by their names
6. #A shopping cart of groceries 
print("Scenrio #1:A restaurant menu with prices for each item")
print("Best Structure: best to pair food with price in key/value")
menu ={
    "French Toast": 12,
    "Grand Slam": 12,
    "T-Bone Steak": 18,
    "Avocado Toast": 15,


}
for key, item in menu.item():
    print(Key, ": ", item)


print("Scenario #2: High scores to an arcade game")
print("Best Structure list: Need a mutable structure to update real time")
highScores = [
    100,
    105,
    110,
    99

]
for score in highScores:
    print(score)

print(" Scenario #3 #All of the months of the year")
print("Best structure list: Tuple: We need a collection that does not change ")
monthsInYear = {

    "January",
    "Febuary",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "Setember",
    "October",
    "Novemeber",
    "December",
}
for month in monthsInYear:
    print(month)


print("Scenerio #4  #All the items in your backpack ")
print("Best structure: List: We need items that you can change and switch up")
items ={
    "Books"
    "Pencils"
    "Folders"
    "Notebooks"
    "Pens"



}
for item in backpack:
    print(item)

#5. Look up Student emails by their names
print("\nScenario #5: Look up student emails by their names.")
print("Best Structure: Dictionary; allows fast lookups by name.")
student_emails = {
    "Jason": "Jason@example.com",
    "John": "John@example.com",
    "Jamal": "Jamal@example.com"
}
for name, email in student_emails.items():
    print(name, "->", email)

#6. A shopping cart of groceries
print("\nScenario #6: A shopping cart of groceries.")
print("Best Structure: List; ordered, can contain duplicates (e.g., 2 apples).")
shopping_cart = ["Apple", "Banana", "Milk", "Apple", "Bread"]
for item in shopping_cart:
    print(item)

    
#7. Scenario: List of favorite programming languages
print("\nScenario #7: List of favorite programming languages.")
print("Best Structure: Set; only unique languages, no duplicates.")
favorite_languages = {"Python", "JavaScript", "C++", "Python", "Get.do"}
for lang in favorite_languages:
    print(lang)

