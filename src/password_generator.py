from abc import ABC, abstractmethod
import random
import string

import nltk
from nltk.corpus import words


nltk.download('words')

class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class PinCode(PasswordGenerator):
    def __init__(self, length):
        self.type_password = "PinCode"
        self.length = length

    def generate(self):
        self.password = ""
        for _ in range(self.length):
            self.password += random.choice('0123456789')

        return f"{self.type_password}: {self.password}"


class RandomPassword(PasswordGenerator):
    def __init__(self, length, numbers, punctuation):
        self.type_password = "RandomPassword"
        self.length = length
        self.numbers = numbers
        self.punctuation = punctuation
    
    words = string.ascii_letters
    password = ""
    def generate(self):
        if self.numbers :
            self.words += string.digits
        if self.punctuation :
            self.words += string.punctuation
        
        for _ in range(self.length):
            self.password += random.choice(self.words)
        return(self.password)


class MemorablePassword(PasswordGenerator):
    def __init__(self, length, separator, capitalize):
        self.type_password = "MemorablePassword"
        self.length = length
        self.separator = separator
        self.capitalize = capitalize
        all_words = words.words()
        self.words = [word.lower() for word in all_words if word.isalpha() and 3 <= len(word) <= 8]
        self.password = []

    def generate(self):
        self.password = [random.choice(self.words) for _ in range(self.length)]
        if self.capitalize:
            self.password = [word.upper() for word in self.password]
        return self.separator.join(self.password)
    

if __name__ == "__main__":
    #Pincode
    my_pin = PinCode()
    print(my_pin.generate())

    #Randompassword
    my_randompass = RandomPassword(16, True, True, True)
    my_randompass.generate()

    #Memorablepassword
    my_memorable = MemorablePassword(5,'-',False)
    print(my_memorable.generate())