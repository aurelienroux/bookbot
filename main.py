def main():
  book_path = './books/frankenstein.txt'
  book_text = get_book_text(book_path)
  text_num_words = get_text_words_len(book_text)
  print(text_num_words)
    
def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_text_words_len(text):
  words_array = text.split()
  return len(words_array)

main()