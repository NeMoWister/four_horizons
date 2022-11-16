a = open('in.txt', 'r', encoding="utf8")
b = open('out.txt', 'w')
c = 0
for line in a:
    line = line.strip()
    if line == '':
        b.write(line + "\n")
    elif 32 <= ord(line[len(line) - 2]) <= 122:
        b.write(line + "\n")
    elif line[-1:] == "'" and not (line[len(line) - 2]) in {'!', '?', '.'}:
        print(line[len(line) - 2])
        b.write(line[:-1] + ".'\n")
        c += 1
    else:
        b.write(line + "\n")
a.close()
b.close()
print(c)