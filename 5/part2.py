import string


class Parser(object):

    def check_for_collision(self, word, letter):
        end_of_word = word[-1:]
        return end_of_word != letter and end_of_word.lower() == letter.lower()

    def shorten_string(self, input):
        output = ''
        for char in input:
            if self.check_for_collision(output, char):
                output = output[:-1]
            else:
                output += char
        return output

    def perform_work(self, input):
        min_length = len(input)
        for letter in string.ascii_lowercase:
            min_length = min(min_length, len(self.shorten_string(input.replace(letter, "").replace(letter.upper(), ""))))
        print min_length

input = open("input.txt").read().strip()
parser = Parser()
parser.perform_work(input)
