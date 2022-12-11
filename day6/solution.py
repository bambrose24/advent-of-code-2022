def main():
  num = 14
  with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    data = lines[0]
    for i in range(len(data)-num):
      vals = data[i:i+num]
      if len(set(vals)) == num:
        print(f'answer: {i+num}')
        break
  
if __name__ == '__main__':
  main()