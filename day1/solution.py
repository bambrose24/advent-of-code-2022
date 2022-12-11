from collections import defaultdict
def main():
  with open('input.txt') as f:
    print('hi')
    lines = [x.strip() for x in f.readlines()]
    all = defaultdict(int)
    curr_elf = 0
    for i in range(len(lines)):
      l = lines[i]
      if l == '':
        curr_elf += 1
      else:
        all[curr_elf] += int(l)
    best = [x for x in all.values()]
    best.sort()
    print(f'solution: {sum(best[-3:])}')

if __name__ == '__main__':
  main()