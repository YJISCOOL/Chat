def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return (lines)

def convert(lines):
    new_lines = []
    person = None 
    for line in lines:
        if line == "Allen":
            person = "Allen"
            continue
        elif line == "Tom":
            person = "Tom"
            continue

        if person: #表示當person有值得時候才會做以下動作
            new_lines.append(person + ': ' + line)
        #若對話記錄第一行不是人名，而是對話，那程式會跑不出person，因此會當掉
    return (new_lines)

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('input.txt') #把‘input.txt'投幣丟進read_file()投幣孔
    lines = convert(lines) #再把lines丟到convert()投幣孔
    write_file('output.txt', lines)

main()

