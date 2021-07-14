import os
import sys


if __name__ == "__main__":
    fd = open('dictString.txt')
    sys.stdin = fd

    lines = []
    while True:
        try:
            line = input()
            if line:
                lines.append(line)
            else:
                break
        except EOFError:
            fd.close()
            break

    print(lines)
    for line in lines:
        values = line.split(": ")
        # Extract Variable Names
        var = values[0]
        # Join the rest of the expression back
        exp = ": ".join(values[1:])
        exec(var + " = " + exp)

    print(f'l is {l}')
    print(type(l))
    print(f'r is {r}')
    print(type(r))
    print(f'p is {p}')
    print(type(p))
    print(f's is {s}')
    print(type(s))

    print(f'd is {d}')
    print(type(d))
    print(f'a is {a}')
    print(type(a))
    
    
