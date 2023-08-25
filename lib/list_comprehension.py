#!/usr/bin/env python3

def return_evens(num_list):
    # Use a list comprehension to filter even elements
    even_elements = [x for x in num_list if x % 2 == 0]
    return even_elements
return_evens([0, 1, 3, 5, 7, 8, 9])

def make_exclamation(sentence_list):
    # Use a list comprehension to add exclamation marks
    exclaimed_sentences = [sentence + "!" for sentence in sentence_list]
    return exclaimed_sentences
make_exclamation(["Hello", "I'm doing great", "Python is fun"])
