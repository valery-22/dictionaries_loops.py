myDictionary = {
    "name" : "Ian", "health": 219, "Strength": 199, "equipped": "Axe"
}

for name, value in myDictionary.items():
    print(f"{name}:{value}")

    if (name == "Strength"):
        print("Whoa, So strong!")