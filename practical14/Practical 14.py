import matplotlib.pyplot as plt
import numpy as np
import re
from xml.dom.minidom import parse
import xml.dom.minidom
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")
#print(defstrs)

def childNodes_counter(c):
    a = 0
    b = ''
    for term in terms:
        defstr_context = term.getElementsByTagName('defstr')[0]
        b = defstr_context.childNodes[0].data
        if re.search(f'{c}', b):
            a = a + 1
    return a
DNA_childnodes = 0
RNA_childnodes = 0
protein_childnodes = 0
enzyme_childnodes = 0
DNA_childnodes = childNodes_counter("DNA")
RNA_childnodes = childNodes_counter("RNA")
protein_childnodes = childNodes_counter("protein")
enzyme_childnodes = childNodes_counter("enzyme")

print(DNA_childnodes)
print(RNA_childnodes)
print(protein_childnodes)
print(enzyme_childnodes)

labels = 'DNA', 'RNA', 'protein', 'enzyme'
sizes = [DNA_childnodes, RNA_childnodes, protein_childnodes, enzyme_childnodes]
explode = (0,0,0.1,0)
plt.pie(sizes, explode = explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')
plt.title('childNodes for different macromolecules')
plt.show()

