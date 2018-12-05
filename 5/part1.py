from datetime import datetime
from collections import defaultdict


class Parser(object):

    def __init__(self):
        self.guards = defaultdict(dict)

    def check_for_collision(self, word, letter):
        end_of_word = word[-1:]
        return end_of_word != letter and end_of_word.lower() == letter.lower()

    def perform_work(self, input):
        output = ''
        for char in input:
            if self.check_for_collision(output, char):
                output = output[:-1]
            else:
                output += char
        print len(output)

input = [x for x in open("input.txt").read().strip()]
parser = Parser()
parser.perform_work(input)
