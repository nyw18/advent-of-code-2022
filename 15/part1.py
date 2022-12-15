import re

f = open("input.txt", "r")
input_re = re.compile("Sensor at x=(-?\\d+), y=(-?\\d+): closest beacon is at x=(-?\\d+), y=(-?\\d+)")
dists = []
beacons = []


def calc_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


for line in f:
    input_line = line.strip()
    input_match = input_re.match(input_line)
    sensor_x = int(input_match.group(1))
    sensor_y = int(input_match.group(2))
    sensor = [sensor_x, sensor_y]
    beacon_x = int(input_match.group(3))
    beacon_y = int(input_match.group(4))
    beacon = [beacon_x, beacon_y]
    dist = calc_dist(sensor, beacon)
    dists.append([sensor, dist])
    beacons.append(beacon)

y = 2000000
in_range = set()

for data in dists:
    pos_x = data[0][0]
    pos_y = data[0][1]
    dist = data[1]
    start_x = pos_x - dist - 1
    end_x = pos_x + dist + 1
    start_y = pos_y - dist - 1
    end_y = pos_y + dist + 1
    if start_y <= y <= end_y:
        for x in range(start_x, end_x):
            if calc_dist([x, y], data[0]) <= data[1]:
                in_range.add(x)
                continue

for beacon in beacons:
    if beacon[1] == y and beacon[0] in in_range:
        in_range.remove(beacon[0])
print(len(in_range))
