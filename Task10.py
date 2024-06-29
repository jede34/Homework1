#data = {'year': 2024,'lang': 'Python', 'version': 3.12}
#print(data)
cat = {"nick": "Simon","age": 7, "characteristics": "angry"}
info = {"status": "vaccinated", "breed": True}
age = cat.get("age")
cat.update(info)
print(cat)
