import re

def _get_destination(input: int,
                    src_start: list[int], 
                    dst_start: list[int], 
                    range_len: list[int],
                    ) -> list[int]:
    """Given an input and source and destination ranges, returns the
    corresponding destination value. If input is not in any of the
    ranges, returns the input"""
    for i in range(len(src_start)):
        if input in range(int(src_start[i]), int(src_start[i]) + int(range_len[i])):
            return int(input) - int(src_start[i]) + int(dst_start[i])
    return int(input)

def get_destinations(input: list[int] | int, 
                    src_start: list[int], 
                    dst_start: list[int], 
                    range_len: list[int],
                    ) -> list[int]:
    if type(input) is int:
        input = [input]
    for i, seed in enumerate(input):
        input[i] = _get_destination(seed, src_start, dst_start, range_len)
    return input

with open('input5.txt', 'r') as file:

    seeds = re.findall(r'\d+', next(file))

    seeds2 = []
    for i, seed in enumerate(seeds):
        if i % 2 == 0: # is start value
            start_value = seed
        else:
            for v in range(int(start_value), int(seed) + int(start_value)):
                seeds2.append(v)

    print(f'input seeds: {seeds}')
    print(f'input seeds2: {seeds2}')
    src_start = []
    dst_start = []
    range_len = []

    for k, line in enumerate(file):
        if len(line) == 1 or re.search(r':', line):
            seeds = get_destinations(seeds, src_start, dst_start, range_len)
            seeds2 = get_destinations(seeds2, src_start, dst_start, range_len)

            dst_start = []
            src_start = []
            range_len = []
        else:
            m = re.findall(r'\d+', line)
            dst_start.append(m[0])
            src_start.append(m[1])
            range_len.append(m[2])
    seeds = get_destinations(seeds, src_start, dst_start, range_len)
    seeds2 = get_destinations(seeds2, src_start, dst_start, range_len)
    print(f'minimum seed task 1: {min(seeds)}') 
    print(f'minimum seed task 2: {min(seeds2)}') # Task 2 is way to slow. I'll have to handle ranges instead of individual values


