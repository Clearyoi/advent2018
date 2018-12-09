class NearDuplicateFinder(object):

    def __init__(self):
        self.match = ""

    def check_for_duplicates(self, short_words):
        list_of_words = set()
        for word in short_words:
            if word in list_of_words:
                self.match = word
                break
            else:
                list_of_words.add(word)

    def perform_work(self, words):
        for i in range(len(words[0])):
            short_words = [(x[:i]+x[i+1:]) for x in words]
            self.check_for_duplicates(short_words)
            if self.match != "":
                break
        return self.match

words = open("input.txt").read().strip().split('\n')
finder = NearDuplicateFinder()
print finder.perform_work(words)
