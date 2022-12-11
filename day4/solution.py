def main():
    with open("input.txt") as f:
        lines = [x.strip() for x in f.readlines()]
        total = 0
        for line in lines:
            a_range,b_range = line.split(',')
            a1,a2 = [int(x) for x in a_range.split('-')]
            b1,b2 = [int(x) for x in b_range.split('-')]
            if a1 <= b1 and a2 >= b2:
                total += 1
            elif b1 <= a1 and b2 >= a2:
                total += 1
        print(f'answer: {total}')

def two():
    with open("input.txt") as f:
        lines = [x.strip() for x in f.readlines()]
        total = 0
        for line in lines:
            a_range,b_range = line.split(',')
            a1,a2 = [int(x) for x in a_range.split('-')]
            b1,b2 = [int(x) for x in b_range.split('-')]
            if (a1 <= b2 and a1 >= b1) or (b1 <= a2 and b1 >= a1) or (b2 >= a1 and b2 <= a2) or (a2 <= b2 and a2 >= b1):
                total += 1
        print(f'answer: {total}')


if __name__ == "__main__":
    two()
