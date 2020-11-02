

# Question 1
# menu = {'lagman': 120, 'plov': 120, 'borsh': 100}
# menu["Besh barmak"] = 130
# menu['lagman'] = 135
# del menu["borsh"]
# print(menu)

# Question 2 

# slovar = {'hello': 'hi', "good": "nice", 'price': 'cost'}
# print(slovar["price"])

#Question 3
# 1-way

# country = ['Russia', 'USA', 'German']
# cities = ['Moscow', 'New York', 'Berlin']
# dictionary = {country:cities for country, value in zip(country, cities)}
# dictionary2 = dict(zip(country, cities))

# print(dictionary2)


# 2 way

# country = ['Russia', 'USA', 'German'],['New York', 'Berlin', 'Moscow']
# for country in range(3):
#     new_country = {"Russia": "Moscow", "USA": "New York", "German": "Berlin"}
# print(new_country)




# Question 4
# dog = {'name':'Bobik', 'color': 'black', 'age': '5'}
# cat = {'name': 'Barsik', 'color': 'white', 'age': '3'}
# print("This is a dog. His name is " + dog["name"] + "." + " He is " + dog["color"] + 
#     " and he is already " + dog['age'] + " years old.")
# print("\t This is a dog. His name is " + dog["name"] + "." + " He is " + dog["color"] + 
#     " and he is already " + dog['age'] + " years old.")


# Question 5
# students = {
#     '1a': ['John', 'Jessica', 'Tom'], 
#     '2a': ['Ben', 'Adam', 'Elena'],
#     }
# print("This is " + students["1a"][2] + ". " + "He is in grade " + "1a" + ".")