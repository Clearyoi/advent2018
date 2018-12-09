class DuplicateFinder(object):

    def __init__(self):
        self.duplicate_locations = set()
        self.locations = set()

    def create_list_of_cells(self, word):
        cells = set()
        word = word.split('@')[1].split(':')
        start_position = word[0].split(',')
        size = word[1].split('x')
        for i in range(int(size[0])):
            for j in range(int(size[1])):
                cells.add(str((int(start_position[0]) + i)) + ',' + str(int(start_position[1]) + j))
        return cells

    def check_for_duplicates(self, cells):
        for cell in cells:
            if cell in self.locations:
                self.duplicate_locations.add(cell)
            else:
                self.locations.add(cell)

    def check_if_unique_claim(self, cells):
        for cell in cells:
            if cell in self.duplicate_locations:
                return False
        return True

    def perform_work(self, words):
        for word in words:
            cells = self.create_list_of_cells(word)
            self.check_for_duplicates(cells)
        for word in words:
            cells = self.create_list_of_cells(word)
            if self.check_if_unique_claim(cells):
                return word

words = open("input.txt").read().strip().split('\n')
finder = DuplicateFinder()
print finder.perform_work(words)
