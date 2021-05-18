import os
import re

os.chdir("/Users/apple/Documents/Practical8")
code = {
    "TTT":'F',"TTC":'F',"TTA":'L',"TTG":'L',
    "TCT":'S',"TCC":'S',"TCA":'S',"TCG":'S',
    "TAT":'Y',"TAC":'Y',"TAA":'O',"TAG":'U',
    "TGT":'C',"TGC":'C',"TGA":'X',"TGG":'W',
    "CTT":'L',"CTC":'L',"CTA":'L',"CTG":'L',
    "CCT":'P',"CCC":'P',"CCA":'P',"CCG":'P',
    "CAT":'H',"CAC":'H',"CAA":'Q',"CAG":'Z',
    "CGT":'R',"CGC":'R',"CGA":'R',"CGG":'R',
    "ATT":'I',"ATC":'I',"ATA":'J',"ATG":'M',
    "ACT":'T',"ACC":'T',"ACA":'T',"ACG":'T',
    "AAT":'N',"AAC":'B',"AAA":'K',"AAG":'K',
    "AGT":'S',"AGC":'S',"AGA":'R',"AGG":'R',
    "GTT":'V',"GTC":'V',"GTA":'V',"GTG":'V',
    "GCT":'A',"GCC":'A',"GCA":'A',"GCG":'A',
    "GAT":'D',"GAC":'D',"GAA":'E',"GAG":'E',
    "GGT":'G',"GGC":'G',"GGA":'G',"GGG":'G',
     }
# turn DNA to amino
def decode(seq):
    a1 = re.findall(r'...', seq)
    amino = ''
    for i in range(len(a1)):
        a2 = code[a1[i]]
        amino = amino + a2
    return amino


file_name = input('Please write the file name there: ')
file_origin = open('unknown_function.fa', 'r')
file_result = open(file_name, 'w')

line = next(file_origin, '-1') # skip the empty line
while True:
    if line.startswith('>>'):
        m = line
        line = next(file_origin, '-1')
        s = line.replace('\n', '') # the DNA sequence has been turned into one line
        context = m[0:14] + str(int(len(s)/3))
        file_result.write(context)
        file_result.write('\n')
        file_result.write(decode(s))
        file_result.write('\n')
    if line == '-1':
        break
    line = next(file_origin, '-1')
file_origin.close()
file_result.close()






