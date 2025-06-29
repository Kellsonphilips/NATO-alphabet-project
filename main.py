import pandas


# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:

word_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(words)

# converting the data in word_data to a DataFrame which is a tabular format
list_word = pandas.DataFrame(word_data)
# print(list_word)

# we need to iterate through the rows of our dataframe
# when iterating though each and every row with the row indexes
# from the row we pick the row.letter as the dictionary key and row.code as the key value
# compiling all the keys and values from all iteration, and we have our dictionary words_dict
words_dict = {row.letter: row.code for (index, row) in list_word.iterrows()}
# print(words_dict)


def word_search():
    user_guess = input("Enter any word: ").upper()
    try:
        matched_words = [words_dict[letter] for letter in user_guess]

    # In our dictionary words_dict we convert user imputed word to word list
    # the list of words are matched to a key in words_dict dictionary
    # So we can print the key value as a list of words in a split format
    except KeyError:
        print("Sorry, only letter in your input please.")
        word_search()
    else:
        print(matched_words)


word_search()
