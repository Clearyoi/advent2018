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
        sleepiest_guard = max(self.guards.iteritems(), key=lambda x: sum(x[1].values()))
        sleepiest_time = max(sleepiest_guard[1], key=sleepiest_guard[1].get)
        print 'Guard id =', sleepiest_guard[0]
        print 'Time =', sleepiest_time
        print 'Answer =', int(sleepiest_guard[0]) * int(sleepiest_time)


lines = open("input.txt").read().strip().split('\n')
parser = Parser()
parser.perform_work(lines)
