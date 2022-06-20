n = int(input().split()[0])
m = 3*n

# top part
for i in range(n//2):
    print('.'.rjust(m//2 - i*3, '-') + '|..'*i + '|'+ '..|'*i +'.'.ljust(m//2 - i*3, '-'))
    
# middle part - welcome
print('WELCOME'.center(m, '-'))

# bottom part
for i in reversed(range(n//2)):
    print('.'.rjust(m//2 - i*3, '-') + '|..'*i + '|'+ '..|'*i +'.'.ljust(m//2 - i*3, '-'))
