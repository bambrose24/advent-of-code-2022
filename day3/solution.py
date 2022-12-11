def main():
    with open('input.txt') as f:
        lines = [x.strip() for x in f.readlines()]

        total = 0
        for l in lines:
            a, b = l[:len(l)//2], l[len(l)//2:]
            a_set, b_set = set(a), set(b)
            # print(a_set, b_set)
            char = [x for x in a_set.intersection(b_set)][0]
            print(f'char {char}')
            total += val(char)
        print(f'answer: {total}')


def two():
    with open('input.txt') as f:
        lines = [x.strip() for x in f.readlines()]
        total = 0
        idx = 0
        while idx < len(lines):
            triplets = []
            for i in range(3):
                triplets.append(lines[idx])
                idx += 1
            a, b, c = triplets
            s1 = set(a).intersection(set(b))
            char = [x for x in s1.intersection(set(c))][0]
            total += val(char)
        print(f'answer: {total}')


def val(c: str):
    if c.lower() == c:
        return ord(c) - 96
    return ord(c) - 64 + 26


if __name__ == '__main__':
    two()
