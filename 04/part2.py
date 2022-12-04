import re

f = open("input.txt", "r")
overlaps = 0

for line in f:
    ranges = line.strip()
    range_re = re.compile('(\d+)-(\d+),(\d+)-(\d+)')

    ranges_match = range_re.match(ranges)
    a_lb, a_ub = int(ranges_match.group(1)), int(ranges_match.group(2))
    b_lb, b_ub = int(ranges_match.group(3)), int(ranges_match.group(4))
    overlap = set(range(a_lb, a_ub + 1)) & set(range(b_lb, b_ub + 1))

    if len(overlap):
        overlaps += 1

print(overlaps)