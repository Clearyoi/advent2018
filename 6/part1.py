class Parser(object):

    def __init__(self, nodes):
        self.nodes = nodes
        self.left = min(self.nodes, key=lambda x: x[0])[0]
        self.right = max(self.nodes, key=lambda x: x[0])[0]
        self.top = min(self.nodes, key=lambda x: x[1])[1]
        self.bottom = max(self.nodes, key=lambda x: x[1])[1]
        self.plain = []
        self.infinite_nodes = set()
        self.valid_nodes = set()

    def build_plain(self):
        self.plain = [((x, y), self.find_nearest_node(x, y)) for x in range(self.left, self.right + 1) for y in range(self.top, self.bottom + 1)]
        self.infinite_nodes = set([x[1] for x in self.plain if self.is_edge(x[0])])
        self.valid_nodes = self.nodes - self.infinite_nodes

    def is_edge(self, point):
        if point[0] == self.left or point[0] == self.right or point[1] == self.top or point[1] == self.bottom:
            return True
        return False

    def find_nearest_node(self, x, y):
        closest_node = None
        distance = None
        for node in self.nodes:
            new_distance = self.get_distance_between_points(node, x, y)
            if distance is None or new_distance < distance:
                closest_node = node
                distance = new_distance
            elif new_distance == distance:
                closest_node = None
        return closest_node

    def get_distance_between_points(self, node, x, y):
        return abs(node[0]-x) + abs(node[1] - y)

    def perform_work(self):
        self.build_plain()
        most_common_node = max([(node, len([x for x in self.plain if x[1] == node])) for node in self.valid_nodes], key=lambda x: x[1])
        print most_common_node


nodes = set([(tuple(map(int, (x.split(', '))))) for x in open("input.txt").read().strip().split('\n')])
parser = Parser(nodes)
parser.perform_work()
