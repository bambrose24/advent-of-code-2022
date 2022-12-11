def main():
  with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]
    score = 0
    for line in lines:
      one,two = line.split(' ')
      if one != '' and two != '':
        round_score =  get_score2(one, two)
        print(f'{line} {round_score}')
        score += round_score
    print(f'answer: {score}')

one_options = ['A', 'B', 'C']
two_options = ['X', 'Y', 'Z']

def get_score(one: str, two: str):
  one_idx, two_idx = one_options.index(one), two_options.index(two)

  score = 0
  if one_idx == two_idx:
    score += 3
  elif one_idx == ((two_idx + 1) % 3):
    score += 0
  else:
    score += 6

  return score + (two_idx + 1)


def get_score2(one: str, two: str):
  one_idx = one_options.index(one)
  if two == 'X':
    two_idx = (one_idx - 1) % 3
  elif two == 'Y':
    two_idx = one_idx
  else:
    two_idx = (one_idx + 1) % 3
  two_choice = two_options[two_idx]
  return get_score(one, two_choice)

if __name__ == '__main__':
  main()