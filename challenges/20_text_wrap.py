import textwrap

def wrap(string, max_width):
    wrap_result = textwrap.fill(string, max_width)
    return wrap_result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
