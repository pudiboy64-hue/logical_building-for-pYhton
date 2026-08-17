import random
import string

all_pool= string.ascii_letters+string.digits+string.punctuation
character=random.choice(all_pool)
print(character)
if character in string.digits :
    print(f"the {character} character is string.digits ")
elif character in string.ascii_letters:
    print(f" the {character} character is ascii_letter")   
elif character in string.punctuation:
    print(f"the {character} character is punctuation")    