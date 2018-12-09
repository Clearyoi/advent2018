from datetime import datetime
from collections import defaultdict


class Parser(object):

    def __init__(self):
        self.guards = defaultdict(dict)

    def count_guard_times(self, lines):
        for line in lines:
            if line.endswith('begins shift'):
                guard = line.split('#')[1].split(' ')[0]
            if line.endswith('falls asleep'):
                start_time = datetime.strptime(line.split(']')[0][1:], '%Y-%m-%d %H:%M').minute
            if line.endswith('wakes up'):
                for x in range(start_time, datetime.strptime(line.split(']')[0][1:], '%Y-%m-%d %H:%M').minute):
                    self.guards[guard][x] = (self.guards[guard].get(x, 0)) + 1

    def perform_work(self, lines):
        lines.sort(key=lambda x: datetime.strptime(x.split(']')[0][1:], '%Y-%m-%d %H:%M'), reverse=False)
        self.count_guard_times(lines)
        sleepiest_guard = max(map(lambda x: (x[0], max(x[1], key=x[1].get)), self.guards.iteritems()), key=lambda x: self.guards[x[0]][x[1]])
        print 'Guard id =', sleepiest_guard[0]
        print 'Time =', sleepiest_guard[1]
        print 'Answer =', int(sleepiest_guard[0]) * int(sleepiest_guard[1])


lines = open("input.txt").read().strip().split('\n')
parser = Parser()
parser.perform_work(lines)
