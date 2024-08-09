from typing import Dict, Optional

print("Website Rating")
print()

website: Dict[str, Optional[str]] = {"name": None, "url": None,"description": None,"rating": None}

# Get input from user in one line and split the input
input_data = input("Input the website name, URL, description, and a star rating ")

input_values = input_data.split(", ")
keys = list(website.keys())

for i in range(len(keys)):
    website[keys[i]] = input_values[i]
    
print()

# Output the dictionary content
for name, value in website.items():
    print(f"{name}:  {value}")
    