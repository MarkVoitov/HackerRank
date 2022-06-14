if __name__ == '__main__':
    n = int(input())
    n_string = []
    for i in range(n):
        n_string.append(str(i+1))
    print(''.join(n_string))
