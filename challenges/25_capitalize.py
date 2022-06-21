def solve(s):
    capitalized_string = ' '.join(map(str.capitalize, s.split(' ')))
    return capitalized_string
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
