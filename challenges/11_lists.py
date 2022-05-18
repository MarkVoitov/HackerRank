if __name__ == '__main__':
    N = int(input())
    my_list = []
    for _ in range(N):
        i = input().split(' ')
        if i[0] == 'insert':
            my_list.insert(int(i[1]), int(i[2]))
        if i[0] == 'print':
            print(my_list)
        if i[0] == 'remove':
            my_list.remove(int(i[1]))
        if i[0] == 'append':
            my_list.append(int(i[1]))
        if i[0] == 'sort':
            my_list.sort()
        if i[0] == 'pop':
            my_list.pop()
        if i[0] == 'reverse':
            my_list.reverse()
 
