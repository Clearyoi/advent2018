class Parser(object):

    def __init__(self, nodes):
        self.nodes = nodes
        self.left = min(self.nodes, key=lambda x: x[0])[0]
        self.right = max(self.nodes, key=lambda x: x[0])[0]
        self.top = min(self.nodes, key=lambda x: x[1])[1]
        self.bottom = max(self.nodes, key=lambda x: x[1])[1]
        self.plain = []

    def build_plain(self):
        self.plain = [(x, y) for x in range(self.left, self.right + 1) for y in range(self.top, self.bottom + 1) if self.near_all_nodes(x, y)]

    def near_all_nodes(self, x, y):
        total_distance = sum(self.get_distance_between_points(node, x, y) for node in self.nodes)
        return total_distance < 10000

    def get_distance_between_points(self, node, x, y):
        return abs(node[0]-x) + abs(node[1] - y)

    def perform_work(self):
        self.build_plain()
        print len(self.plain)


nodes = set([(tuple(map(int, (x.split(', '))))) for x in open("input.txt").read().strip().split('\n')])
parser = Parser(nodes)
parser.perform_work()
