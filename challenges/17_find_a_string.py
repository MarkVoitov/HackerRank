def count_substring(string, sub_string):
    index = 0
    count = 0
    while index != -1:
        if sub_string in string:
            count += 1
        index = string.find(sub_string)
        string = string[index+1:]
        if index == -1:
            break
    return count

  
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
