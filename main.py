def main():
  book_path = './books/frankenstein.txt'
  book_text = get_book_text(book_path)
  text_num_words = get_text_words_len(book_text)
  text_chars_count = get_text_chars_count(book_text)

  print(f"total of words: {text_num_words}, letters dict: {text_chars_count}")
    
def get_book_text(path):
  with open(path) as f:
    return f.read()

# Add a new function to your script that takes the text from the book as a string, and returns the number of words in the string.
def get_text_words_len(text):
  words_array = text.split()
  return len(words_array)

# Add a new function to your script that takes the text from the book as a string, 
# and returns the number of times each character appears in the string. 
# Convert any uppercase letters to lowercase letters, we don't want duplicates.
def get_text_chars_count(text):
  letters_dict = {}

  for letter in text:
    letter = letter.lower()

    if letter in letters_dict:
      letters_dict[letter] += 1
    else:
      letters_dict[letter] = 1
  
  return letters_dict

main()