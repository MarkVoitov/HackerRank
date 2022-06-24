k = int(input())
my_list = list(map(int, input().split()))
my_set = set(my_list)
print(((sum(my_set)*k)-(sum(my_list)))//(k-1))
