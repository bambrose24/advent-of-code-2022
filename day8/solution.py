with open("input.txt") as f:
  lines = [x.strip() for x in f.readlines()]
  grid = [[int(x) for x in y.strip()] for y in lines]
  res = {}
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      should_print = r == 3 and c == 2
      if should_print:
        print('grid val', grid[r][c])
      if r == 0 or c == 0 or r+1 == len(grid) or c+1 == len(grid[0]):
        continue
      spot = (r,c)
      home = grid[r][c]
      res[spot] = 1
      for r_inc,c_inc in [(1,0), (0,1), (-1,0), (0,-1)]:
        r_curr, c_curr = r+r_inc,c+c_inc
        num = 1
        while r_curr < len(grid) and r_curr >= 0 and c_curr < len(grid[0]) and c_curr >= 0:
          if should_print:
            print((r_inc, c_inc), (r_curr, c_curr), grid[r_curr][c_curr])
          if grid[r_curr][c_curr] >= home:
            break
          r_curr += r_inc
          c_curr += c_inc
          if r_curr < len(grid) and r_curr >= 0 and c_curr < len(grid[0]) and c_curr >= 0:
            num += 1
        res[spot] *= num
  print(sorted(res.items(), key=lambda x: x[-1])[-1][-1])


  # part one below
  # visible = set()

  # for r in range(len(grid)):
  #   for c in range(len(grid[r])):
  #     if r == 0 or r+1 == len(grid) or c == 0 or c+1 == len(grid[r]):
  #       visible.add((r,c))

  # for r in range(len(grid)):
  #   highest_so_far = grid[r][0]
  #   for c in range(len(grid[r])):
  #     if r == 0 or r+1 == len(grid) or c == 0 or c+1 == len(grid[r]):
  #       continue
  #     val = grid[r][c]
  #     if val > highest_so_far:
  #       visible.add((r,c))
  #       highest_so_far= val

  #   highest_so_far = grid[r][-1]
  #   for c in sorted(range(len(grid[r])), key=lambda x: -x):
  #     if r == 0 or r+1 == len(grid) or c == 0 or c+1 == len(grid[r]):
  #       continue
  #     val = grid[r][c]
  #     if val > highest_so_far:
  #       visible.add((r,c))
  #       highest_so_far= val

  # for c in range(len(grid[0])):
  #   highest_so_far = grid[0][c]
  #   for r in range(len(grid)):
  #     if r == 0 or r+1 == len(grid) or c == 0 or c+1 == len(grid[r]):
  #       continue
  #     val = grid[r][c]
  #     if val > highest_so_far:
  #       visible.add((r,c))
  #       highest_so_far= val
    
  #   highest_so_far = grid[-1][c]
  #   for r in sorted(range(len(grid)), key=lambda x: -x):
  #     if r == 0 or r+1 == len(grid) or c == 0 or c+1 == len(grid[r]):
  #       continue
  #     val = grid[r][c]
  #     if val > highest_so_far:
  #       visible.add((r,c))
  #       highest_so_far= val
  

  # print([x for x in visible if x[0] == 1])
  # print('answer', len(visible))      
