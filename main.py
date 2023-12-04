file = "books/frankenstein.txt"
with open(file) as f:
    file_contents = f.read()

words = file_contents.split()
character_counts = {}
for character in file_contents.lower():
    if character in character_counts:
        character_counts[character] += 1
    else:
        character_counts[character] = 1

list_of_alpha = [(character, count) for character, count in character_counts.items() if character.isalpha()]
list_of_alpha.sort(key=lambda x: x[1], reverse=True)
print(f"--- Begin report of {file} ---")
print(f"{len(words)} words found in the document")
for character, count in list_of_alpha:
    print(f"The {character} character was found {count} times")
print(f"--- End report ---")