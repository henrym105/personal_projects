import random

def random_word():
    words = ['apple', 'banana', 'orange', 'pear', 'grape', 'water', 'coffee', 'bread', 'cheese', 'milk', 
         'eggs', 'chicken', 'beef', 'pork', 'fish', 'potato', 'carrot', 'onion', 'tomato', 'pepper', 
         'lettuce', 'spinach', 'broccoli', 'cabbage', 'pasta', 'rice', 'beans', 'sugar', 'salt', 'peanut', 
         'almond', 'cashew', 'walnut', 'honey', 'butter', 'oil', 'vinegar', 'mayo', 'ketchup', 'mustard', 
         'jam', 'jelly', 'syrup', 'cereal', 'yogurt', 'cookie', 'cake', 'pie', 'candy', 'chips']
    return words[random.randint(0, len(words))]
    # return "beef"

# print(random_word())

