import codecs

def correct_character(x):
    if not(x.isalpha() or x.isdigit()):
        return False
    return True

def wordLength(line):
    result = ''
    i = 0
    if not correct_character(line[0]):
        while not correct_character(line[i]):
            result += line[i]
            i += 1

    count = 0
    for x in line[i:]:
        if not correct_character(x):
            if count !=0:
                result += '(' + str(count) + ')'
            result += x
            count = 0
        else:
            result += x
            count += 1
    if count > 0:
        result += '(' + str(count) + ')'
    return result

if __name__ == '__main__':
    input = codecs.open('input.txt', encoding='utf-8')
    output = open("output.txt", 'w')
    line = input.read()
    line = wordLength(line)
    output.write(line)

    input.close()
    output.close()
