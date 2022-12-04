import re


def get_range(range):
    return [int(range[0]), int(range[2])]


f = open("input.txt", "r")
overlaps = 0

for line in f:
    ranges = line.strip()
    range_re = re.compile('(\d+)-(\d+),(\d+)-(\d+)')

    ranges_match = range_re.match(ranges)
    a_lb, a_ub = int(ranges_match.group(1)), int(ranges_match.group(2))
    b_lb, b_ub = int(ranges_match.group(3)), int(ranges_match.group(4))
    # b_lb, b_ub = get_range(ranges[4:8])

    if (a_lb >= b_lb and a_ub <= b_ub) or (a_lb <= b_lb and a_ub >= b_ub):
        overlaps += 1

print(overlaps)