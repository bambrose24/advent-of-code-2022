
from collections import defaultdict
filesystem = {'/': {}}
dir_sizes = defaultdict(int)
total_file_sizes = 0
with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    curr_dir_stack = []
    curr_dir = {}
    filesystem['/'] = curr_dir
    for line in lines[1:]:
      if line[0] == '$':
        # command happened
        # if line[2:4] == 'ls':
          # do nothing, might need to track that ls is printing tho
        if line[2:4] == 'cd':
          _,_,where = line.split(' ')
          if where == '..':
            curr_dir_stack.pop()
            curr_dir = filesystem['/']
            for directory in curr_dir_stack:
              curr_dir = curr_dir[directory]
          else:
            curr_dir_stack.append(where)
            curr_dir = curr_dir[where]
      elif line[:3] == 'dir':
        # another dir exists
        _,d = line.split(' ')
        curr_dir[d] = {}
      else:
        num,filename = line.split(' ')
        num = int(num)
        curr_dir[filename] = num
        total_file_sizes += num
        curr_dir_stack_cloned = [x for x in curr_dir_stack]
        while len(curr_dir_stack_cloned) > 0:
          dir_sizes[','.join(curr_dir_stack_cloned)] += num
          curr_dir_stack_cloned.pop()  

total = 0
for k,v in dir_sizes.items():
  if (v <= 100000):
    total += v


total_avail_space = 70000000
space_needed_to_run = 30000000
free_space = total_avail_space - total_file_sizes
min_deletion_needed = space_needed_to_run - free_space

dir_sizes = list(sorted(dir_sizes.items(), key=lambda x: x[1]))
for k,v in dir_sizes:
  if v >= min_deletion_needed:
    print('answer:', v)
    break
        
        
