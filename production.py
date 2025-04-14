'''
A file for the production code
'''
import sys

def reverse_word(word):
 if word == "":
     return ""
 elif len(word) == 1:
    return word
 else: 
    return word[::-1]
 
def reverse_all_words(sentence):
    words = sentence.split()
    output = []
    for word in words:
       current = reverse_word(word)
       output.append(current)
    return " ".join(output)

def main():
    if len(sys.argv) < 2:
        print("Provide a phrase.")
        return
    phrase = " ".join(sys.argv[1:])
    print(reverse_all_words(phrase))