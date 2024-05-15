import re

def get_destination(input: int, 
                    src_start: list[int], 
                    dst_start: list[int], 
                    range_len: list[int],
                    ) -> int:
    """Given an input and source and destination ranges, returns the
    corresponding destination value. If input is not in any of the
    ranges, returns the input"""
    for i in range(len(src_start)):
        if input in range(int(src_start[i]), int(src_start[i]) + int(range_len[i])):
            return input - src_start[i] + dst_start[i]
    return input

with open('test.txt', 'r') as file:

    seeds = re.findall(r'\d+', next(file))
    src_start = []
    dst_start = []
    range_len = []

    for line in file:
        same_map = True


        if re.search(r':', line): 
            # print(dst_start)
            for i, seed in enumerate(seeds):
                seeds[i] = get_destination(seed, src_start, dst_start, range_len)
            # run get_destination with the seeds and update seeds
            # reset src_start, dst_start and range_len
            src_start = []
            dst_start = []
            range_len = []
        else:
            m = re.findall(r'\d+', line)
            if len(m) == 3:
                dst_start.append(m[0])
                src_start.append(m[1])
                range_len.append(m[2])
    for i, seed in enumerate(seeds):
        seeds[i] = get_destination(seed, src_start, dst_start, range_len)

    print(seeds) # It does not work yet. I'm not sure what is wrong, but would start by looking at get_destination next


