## List
# # You can create a simple collection of ordered items using a Python list. e.g.
# # fruits = ["Cherry", "Apple", "Pear"]

indian_states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar",
    "Chhattisgarh", "Goa", "Gujarat", "Haryana",
    "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala",
    "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
    "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
    "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
]

indian_states[1] ="West"
indian_states.append("Noida")
indian_states.extend(["Noida","kushinager"])
print(indian_states)
print(indian_states[10])
print(indian_states[-2])