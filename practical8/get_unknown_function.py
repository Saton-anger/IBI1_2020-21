import os
import re
os.chdir('/Users/apple/Documents/Practical8')
original = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
uf = open('unknown_function.fa', 'w')
line = next(original, '-1')
while True:
    if line.startswith('>'):
        if re.search(r'unknown function', line):
            m = re.findall('gene:(\S+)', line)
            s = ''
            while True:
                line = next(original, '-1')
                if line.startswith('>') or (line == '-1'):
                    break
                line1 = line.replace('\n', '')
                s = s + line1
            f = '>>' + m[0]
            uf.write(f'{f:14}')
            uf.write(str(int(len(s))))
            uf.write('\n')
            uf.write(s)
            uf.write('\n')
        else:
            line = next(original, '-1')
    else:
        line = next(original, '-1')
    if line == '-1':
        break
print('unknown_function.fa')
original.close()
uf.close()



