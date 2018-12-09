class Parser(object):

    def build_tree(self, input, index):
        if index > len(input):
            return
        num_children = int(input[index])
        index += 1
        num_meta = int(input[index])
        index += 1
        children = []
        for i in range(num_children):
            new_child = self.build_tree(input, index)
            if new_child is not None:
                children.append(new_child)
                index = new_child.endIndex
        end_index = index + num_meta
        meta_data = map(int, input[index: end_index])
        return Node(children, meta_data, end_index)

    def perform_work(self, input):
        return self.build_tree(input, 0)


class Node(object):

    def __init__(self, children, data, end_index):
        self.children = children
        self.data = data
        self.endIndex = end_index

    def sum_up(self):
        return sum(self.data) + sum([child.sum_up() for child in self.children])

input = open("input.txt").read().strip().split(' ')
parser = Parser()
print parser.perform_work(input).sum_up()
