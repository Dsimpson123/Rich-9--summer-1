favSnacks = ["Munchies flamin hot", "Skittles", "Twix", "Sour cream and onion lays", "Starburst"]

favSnacks.append("Sour Patch kids")
favSnacks.insert(4, "Gummies")
favSnacks.sort()
for snack in favSnacks:
    print(snack)

myColleges = ("Howard", "Michigan University", "USC", "Syrcause", "NYU")
print(myColleges)
for college in myColleges:
    print(college)

myData = {33, 85, 46, 77, 66}
for grade in myData:
    print(grade)
    


carAttribute = {"Brand": "Chervolet",
                "Model": "Camero", 
                "Year": 2016,
                "Engine": "V6",
                 "wheelSize": "20in"}
carAttribute["color"] = "Navy Blue"
for Attribute in carAttribute:
    print(carAttribute.get(Attribute))


                    

 
