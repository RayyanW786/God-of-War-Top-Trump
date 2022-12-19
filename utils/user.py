from .db import DBUtils
from typing import Union
from fuzzywuzzy import fuzz
from dataclasses import dataclass


class UserUtils(object):
    def __init__(self):
        self.db: DBUtils = DBUtils()

    def encrypt(self, words: str) -> str:  # would not recommend using this, please use hashes instead!
        seqeven = [words[x] for x in range(len(words)) if x % 2 == 0]
        seqodd = [words[x] for x in range(len(words)) if x % 2 != 0]
        return f"{''.join(seqodd)}{''.join(seqeven)}"  # encyptes the password (very basic)

    def decrypt(self, words: str) -> str:  # decyptes the encypted password
        midpoint = int(len(words) / 2)
        even = True if len(words) % 2 == 0 else False
        first_half, second_half = words[midpoint:], words[:midpoint]
        res = ""
        for x in range(midpoint):
            res += first_half[x]
            res += second_half[x]
        if even == False:
            res += first_half[midpoint:]
        return res

    def lookup(self, username: str) -> bool:  # checks if username already exists in db (False = Not Found)
        res = self.db.get_user(username)
        if res is not False:
            return True
        else:
            return False

    def register_checks(self, username: str, password: str) -> Union[bool, list]:
        flags = [False, False, False, False,
                 False]  # should be True True True True True, order being digit check, uppercase check, lowercase check ratio check, length check
        feedback = []
        if len(password) >= 8:
            flags[4] = True
        if fuzz.ratio(username, password) < 70:
            flags[3] = True
        for chr in password:
            if all(flags):  # if all of the flags are True it breaks out of the loop
                break
            if chr.isdigit() == True:  # checks for digits
                flags[0] = True
            if chr.isupper():  # checks for uppercase letter
                flags[1] = True
            if chr.islower():  # checks for lowercase letter
                flags[2] = True
        if not all(flags):  # means they are missing something in their password
            feedback.append("Your password is missing the following criteria:")
            for index, val in enumerate(flags):  # we want the index and so we use enumerate
                if val == False:
                    if index == 0:
                        feedback.append("- password must have at least one digit!")
                    elif index == 1:
                        feedback.append("- password must have at least one uppercase!")
                    elif index == 2:
                        feedback.append("- password must have at least one lowercase!")
                    elif index == 3:
                        feedback.append("- Your username cannot be in your password!")
                    elif index == 4:
                        feedback.append("- Your password must be a length of 8 characters or more!")
            return feedback
        else:
            return True

    def login(self, username: str, password: str) -> bool:  # True = correct pwd
        pwd = self.db.get_user(username)
        if pwd == False:
            return False
        if self.decrypt(pwd) == password:
            return True
        else:
            return False

    def register(self, username: str, password: str) -> bool:  # True = account created
        return self.db.add_user(username, self.encrypt(password))


@dataclass
class userdata:
    username: str
    password: str