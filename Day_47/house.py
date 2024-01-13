from csv import reader

# Open and read the dataset
opened_file_char = open("Characters.csv", encoding="utf-8-sig")
read_file_char = reader(opened_file_char)
hp_characters = list(read_file_char)

# Initialize an empty dictionary that will hold a frequency table
houses = {}

# Create a frequency table
for character in hp_characters[1:]: # Note that we should not include the header in the looping; therefore, we start from index 1
    house = character[4]
    if house in houses:
        houses[house] += 1
    elif house == "":
        continue
    else:
        houses[house] = 1

print(houses)
{'Gryffindor': 31, 'Slytherin'
