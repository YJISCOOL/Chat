#計算兩個人講的字數
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return (lines)


def convert(lines): #改編chat1.py的語法
    name = None
    allen_word_count = 0
    allen_sticker_count = 0
    allen_photo_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_photo_count = 0
    for line in lines:
        l =  line.split(' ')
        time = l[0]
        name = l[1]
        if name == 'Allen':
            if l[2] == '貼圖':
                allen_sticker_count += 1
            elif l[2] == '圖片':
                allen_photo_count += 1
            else:
                for x in l[2:]:
                    allen_word_count += len(x)
        elif name == 'Viki':
            if l[2] == '貼圖':
                viki_sticker_count += 1
            elif l[2] == '圖片':
                viki_photo_count += 1
            else:
                for x in l[2:]:
                    viki_word_count += len(x)
    print ('Allen說了', allen_word_count, '個字', '\n',
        '傳了', allen_photo_count, '張照片', '\n',
        '以及', allen_sticker_count, '個貼圖')
    print ('Viki說了', viki_word_count, '個字', '\n',
        '傳了', viki_photo_count, '張照片', '\n',
        '以及', viki_sticker_count, '個貼圖')


def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('LINE-Viki.txt') #把‘input.txt'投幣丟進read_file()投幣孔
    lines = convert(lines) #再把lines丟到convert()投幣孔
    #write_file('output.txt', lines)
main()