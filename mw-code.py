shop = {'hat':10, 'dog': 50, 'purse': 200, 'candy': 1, 'ring': 10000}

most_expensive = 0
item = ""

for obj, price in shop.items():
    if price > most_expensive:
        most_expensive = price
        item = obj

print item, most_expensive


def count_letters_in_name():
    name = raw_input("Please type your full name: ").lower()
    dict = {}

    for letter in name:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1

    return dict

print count_letters_in_name()
