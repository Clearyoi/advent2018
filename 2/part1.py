class DuplicatesCounter(object):

    def __init__(self):
        self.doubles = 0
        self.triples = 0

    def count_letters(self, word):
        letter_counts = {}
        for letter in word:
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
        return letter_counts

    def count_duplicates(self, word):
        letter_counts = self.count_letters(word)
        if 2 in letter_counts.values():
            self.doubles += 1
        if 3 in letter_counts.values():
            self.triples += 1

    def perform_work(self, words):
        for word in words:
            self.count_duplicates(word)
        print self.doubles
        print self.triples
        return self.doubles * self.triples

words = open("input.txt").read().strip().split('\n')
counter = DuplicatesCounter()
print counter.perform_work(words)
