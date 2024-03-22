def main():
  book_path = './books/frankenstein.txt'
  book_text = get_book_text(book_path)
  text_num_words = get_text_words_len(book_text)
  text_chars_count = get_text_chars_count(book_text)
  
  return print_report(book_path, text_num_words, text_chars_count)

def get_book_text(path):
  with open(path) as f:
    return f.read()

# Add a new function to your script that takes the text from the book as a string, and returns the number of words in the string.
def get_text_words_len(text):
  words_array = text.split()
  return len(words_array)

def sort_on(dict):
  return dict["num"]

# Add a new function to your script that takes the text from the book as a string, 
# and returns the number of times each character appears in the string. 
# Convert any uppercase letters to lowercase letters, we don't want duplicates.
def get_text_chars_count(text):
  letters_dict = {}
  letters_list = []

  for letter in text:
    letter = letter.lower()

    if letter in letters_dict:
      letters_dict[letter] += 1
    else:
      letters_dict[letter] = 1
  
  for key in letters_dict:
    letters_list.append({ "key": key, "num": letters_dict[key] })

  letters_list.sort(key=sort_on, reverse=True)

  return letters_list

def print_report(book_path, text_num_words, text_chars_count):
  print(f"--- Start report of {book_path} ---")
  print(f"Total of words: {text_num_words}")
  print("")
  for letter in text_chars_count:
    if letter["key"].isalpha():
      print(f"The {letter["key"]} character was found {letter["num"]} times")
  print('--- End report ---')

main()