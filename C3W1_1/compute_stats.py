

def compute_stats(file):
    total = 0
    sum = 0
    average = 0
    with open(file, 'r') as f:
        first_line = int(f.readline())
        f.seek(0)
        min = first_line
        max = first_line
        for num in f:
            num = int(num)
            total += 1
            sum += num
            if min > num:
                min = num
            if max < num:
                max = num

        print(f'total = {total}')
        print(f'summation = {sum}')
        print(f'average = {round(sum / total)}')
        print(f'Minimum = {min}')
        print(f'Maximum = {max}')


if __name__ == '__main__':
    compute_stats('random_nums.txt')
