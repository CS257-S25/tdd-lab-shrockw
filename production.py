'''
A file for the production code
'''
import sys

def reverse_word(word):
    '''
    Function to reverse a word
    '''
    if word == "":
        return ""
    if len(word) == 1:
        return word
    else:
        return word[::-1]

def reverse_all_words(sentence):
    '''
    Function to reverse all words in a sentence
    '''
    words = sentence.split()
    output = []
    for word in words:
        current = reverse_word(word)
        output.append(current)
    return " ".join(output)

def main():
    '''
    Main function to run the script
    '''
    if len(sys.argv) < 2:
        print("Provide a phrase.")
        return
    phrase = " ".join(sys.argv[1:])
    print(reverse_all_words(phrase))
