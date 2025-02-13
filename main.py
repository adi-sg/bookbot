def main(path_to_books) :
  with open(path_to_books) as f:
    file_contents = f.read()

    word_count = count_words(file_contents)
    char_count = count_chars(file_contents)

    print(f"--- Begin report of {path_to_books} ---")
    print(f"{word_count} words found in the document\n")

    for char in char_count:
      if (char.isalpha()):
        print(f"The '{char}' character was found {char_count[char]} times")

    print("--- End report ---")

def count_words(book):
  word_list = book.split()
  return len(word_list)

def count_chars(book):
  char_dict = {}
  for char in book:
    char = char.lower()
    if (char not in char_dict):
      char_dict[char] = 1
    else:
      char_dict[char] += 1
  return char_dict



main("books/frankenstein.txt")