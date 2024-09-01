

class RevertString:

    string = ""

    def __init__(self, string_input):
        self.string = string_input

    def reverseString(self):
        new_string = ""

        for char in self.string:
            new_string = char + new_string

        return new_string


print(RevertString("Pedro").reverseString())