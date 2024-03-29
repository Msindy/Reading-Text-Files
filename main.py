# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


from collections import defaultdict
import re


def read_file_content(filename): 
    # [assignment] Add your code here 
    with open(filename) as file_handler:
        lines = file_handler.readlines()
        content = "".join(lines)
    return content

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    word_count = defaultdict(int)
    words = re.split('\W+', text.lower())
    for word in words:
        word_count[word]+= 1
    return dict(word_count)
print(count_words())

  