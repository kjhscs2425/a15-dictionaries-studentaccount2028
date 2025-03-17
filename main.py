text = """
Everyone counts.
Everyone has access to great learning.
Every person's unique talents are valued equally.
Everyone takes responsibility for themselves and their community."""

# Make a dictionary where the keys are characters and the values are the number of times that character appears in the `text` print the dicitonary
character_count = {}
for character in text:
    if character in character_count:
        character_count[character] += 1
    else:
        character_count[character] = 1
print(character_count)