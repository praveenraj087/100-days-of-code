import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

inp = input("Enter a word: ").upper()
nato = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
final_list = [nato_dict[word] for word in inp]
print(final_list)
