# Madlibs is a word game where one player prompts another player for a list of words to substitute for blanks in a story.

# This can be done using string concatenation i.e. how to put strings together

# Source Code
print('Welcome to Madlibs World')
adjective_1 = input("Adjective: ")
adjective_2 = input("Adjective: ")
bird = input("Type of bird: ")
room = input("Room in a house: ")
verb_1 = input("Verb(past tense): ")
verb_2 = input("Verb : ")
name = input("Relative's name: ")
noun_1 = input("Noun: ")
liquid = input("A liquid: ")
verb_3 = input("Verb ending in -ing: ")
part = input("Part of the body (plural): ")
noun_2 = input("Plural Noun: ")
verb_4 = input("Verb ending in -ing: ")
noun_3 = input("Noun: ")



madlibs = f"It was a {adjective_1}, cold November day. I woke up to the {adjective_2} smell of {bird} roasting in the {room} downstairs. I {verb_1} down the stairs to see if I could help {verb_2} the dinner. My mom said, 'See if {name} needs a fresh {noun_1}.' So I carried a tray of glasses full of {liquid} into the {verb_3} room. When I got there, I couldn't believe my {part}! There were {noun_2} {verb_4} on the {noun_3}! "

print(madlibs)