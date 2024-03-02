#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=""):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value  
        else:
            print("The value must be a string.")  

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        sentences = [sentence.strip() for sentence in re.split(r'[.!?]', self._value) if sentence.strip()]
        return len(sentences)
