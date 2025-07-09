Bedroom =["Underwear", "Shoes", "Shirts", "Shorts", "Pajamas", "Pants"]

travelBag = []
print("Pack your bags")
print("Enter the index of an item you'd like to move from your room to your bag")
print("Type 'done' when are done packing")
for item in Bedroom:
    print(item)

item = int(input("Item index"))

while item != 100:
 travelBag.append(Bedroom(item))
item = input("Remove item from Bedroom:")
Bedroom.remove(Bedroom[item])
print(Bedroom)
print("/nYour Travel Bag")
print(travelBag)
item = int(input("Item index: "))

print("\nYou travel bag:")
for item in travelBag:
   print(item)
