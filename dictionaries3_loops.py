myDictionary = {
    "name" : "David the Mildy Terrifying", 
    "health": 186, "Strength": 4,
    "equipped":"l33t haxx0r p0werz"}
for name,value in myDictionary.items():
    print(f"{name}:{value}")
if (name == "Strength"):
    if value > 1000:
        print("Whoa, SO STRONG")
    else:
        print("Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!")