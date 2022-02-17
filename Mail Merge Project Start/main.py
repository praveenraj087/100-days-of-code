
# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# with open("G:/100DaysofCode/Day 24 - File System/Mail Merge Project Start/Input/Letters/starting_letter.txt") as start_letter:
#     contents = start_letter.readlines(1)
#     print(contents)


letter = open(
    "G:/100DaysofCode/Day 24 - File System/Mail Merge Project Start/Input/Letters/starting_letter.txt")
contents = letter.read()
print(contents)

inv_names = open(
    "G:/100DaysofCode/Day 24 - File System/Mail Merge Project Start/Input/Names/invited_names.txt")
names = inv_names.readlines()

for name in names:
    new_name = name.strip()
    new_letter = contents.replace("[name]", new_name)
    letter_name = open(
        f"G:/100DaysofCode/Day 24 - File System/Mail Merge Project Start/Output/ReadyToSend/letter_for_{new_name}.txt", "w")
    letter_name.write(new_letter)
    letter_name.close()

inv_names.close()
letter.close()
