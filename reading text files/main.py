# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
from string import punctuation

def read_file_content(filename):
    # [assignment] Add your code here 
    
    file_content = None

    try:
        with open(filename, "r") as file:
            file_content = file.read()      
    except FileNotFoundError as err:
        print(f"File not found: {err}")

    return file_content


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    # remove punctuations and new line characters
    # changed character to lower because python dictionary keys are case sensitive i.e Students != students 
    text = "".join([char.lower() for char in text if char not in punctuation and char != "\n"]) # list comprehension

    # remove extra spaces
    text = [word for word in text.split(" ") if word != ""]

    text_histogram = {}

    for word in text:
        text_histogram[word] = text_histogram.get(word, 0) + 1

    return text_histogram

print(count_words())