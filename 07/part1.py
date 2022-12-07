import re


def get_location():
    ptr = dir_tree
    for dir in cur_path:
        ptr = ptr[dir]
    return ptr


def set_location(data):
    ptr = dir_tree
    for dir in cur_path[:-1]:
        ptr = ptr[dir]
    ptr[cur_path[-1]] = data


def get_dir_size(dir):
    size = 0
    for subdir in dir.values():
        if isinstance(subdir, int):
            size += subdir
        else:
            size += get_dir_size(subdir)
    return size


def count_folders(dir):
    count = 0
    to_check = [dir]
    if len(to_check) == 0:
        return 0
    while cur_dir := to_check.pop():
        for subdir in cur_dir.values():
            if isinstance(subdir, int):
                continue
            if get_dir_size(subdir) <= 100000:
                count += get_dir_size(subdir)
            to_check.append(subdir)
        if len(to_check) == 0:
            break
    return count


f = open("input.txt", "r")
dir_tree = {}
cur_path = []
output = 0

for line in f:
    input_row = line.strip()
    cd_re = re.compile("\$ cd (.+)")
    ls_re = re.compile("\$ ls")
    folder_re = re.compile("dir (.+)")
    file_re = re.compile("([0-9]+) (.+)")
    cd_re_match = cd_re.match(input_row)
    ls_re_match = ls_re.match(input_row)
    folder_re_match = folder_re.match(input_row)
    file_re_match = file_re.match(input_row)
    if cd_re_match:
        path = cd_re_match.group(1)
        if (path == "/"):
            continue
        elif path == "..":
            cur_path.pop()
        else:
            cur_path.append(path)
    elif ls_re_match:
        continue
    elif folder_re_match:
        folder_data = get_location()
        folder_data[folder_re_match.group(1)] = {}
    elif file_re_match:
        folder_data = get_location()
        folder_data[file_re_match.group(2)] = int(file_re_match.group(1))
    else:
        raise RuntimeError("unexpected input " + input_row)

output = count_folders(dir_tree)
print(output)
