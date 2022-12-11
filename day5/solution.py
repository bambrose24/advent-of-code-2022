import re

def main():
    with open("input.txt") as f:
        nums_starts_with = ' 1   2'
        lines = [re.sub('\n', '', x )for x in f.readlines()]
        with_nums = [l for l in lines if l.startswith(nums_starts_with)]
        print('with nums?', with_nums)
        num_stacks = max([int(x) for x in with_nums[0].split(' ') if x != ''])
        print('num stacks?', num_stacks)
        stacks = [[] for _ in range(num_stacks)]
        for l in lines:
          print(l)
          if l.startswith(nums_starts_with):
            break
          for i in range(len(l)):
            if (i-1) % 4 == 0 and l[i] != ' ':
              stack = (i-1) // 4
              stacks[stack].append(l[i])
        stacks = [list(reversed(s)) for s in stacks]

        dirs = [l.strip() for l in lines if l.startswith('move')]
        print('starting stacks', stacks)
        for d in dirs:
          _,num_to_move,_,frm,_,to = d.split(' ')
          # for i in range(int(num_to_move)):
          #   stacks[int(to)-1].append(stacks[int(frm)-1].pop())
          from_stack = stacks[int(frm)-1]
          to_stack = stacks[int(to)-1]
          tmp = list(reversed([from_stack.pop() for _ in range(int(num_to_move))]))
          print('stacks', stacks)
          print('tmp', tmp)
          stacks[int(to)-1] =  to_stack + tmp

        print(stacks)
        print('answer:', ''.join([s[-1] for s in stacks]))



if __name__ == '__main__':
  main()