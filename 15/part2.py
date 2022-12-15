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

for i in range(0, 4000000):
    y = i
    bounds = []
    for data in dists:
        pos_x = data[0][0]
        pos_y = data[0][1]
        dy = abs(pos_y - y)
        dist = data[1]
        if dist < dy:
            continue
        start_x = max(pos_x - max(dist - dy, 0), 0)
        end_x = min(pos_x + max(dist - dy, 0), 4000000)
        start_y = max(pos_y - dist, 0)
        end_y = min(pos_y + dist, 4000000)
        bounds.append([start_x, end_x])

    bounds.sort(key=lambda x: x[0])
    current = 0
    for bound in bounds:
        if bound[0] <= current + 1 and current < bound[1]:
            current = bound[1]
    if min(current, 4000000) != 4000000:
        print("y=" + str(y))
        print("x=" + str(current + 1))
        print((current + 1) * 4000000 + y)
        exit(0)
    elif y % 100000 == 0:
        print("Not y=" + str(y))
