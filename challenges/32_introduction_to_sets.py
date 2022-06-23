def average(array):
    avrg = sum(set(array))/len(set(array))
    return avrg

  
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
