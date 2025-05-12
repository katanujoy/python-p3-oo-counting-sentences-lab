import re

class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value  # Use setter for type check & print message

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
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        # Split based on ., ! or ? followed by optional whitespace
        parts = re.split(r'[.!?]+(?:\s|$)', self._value)
        # Filter out any empty or whitespace-only strings
        sentences = [s for s in parts if s.strip()]
        return len(sentences)