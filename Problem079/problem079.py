# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 79

# Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.


import os

with open('Problem079/keylog.txt','r') as keys:
    lines = [line.rstrip() for line in keys]

with open('Problem079/graph.dot','w',newline='') as dotfile:
    dotfile.write('digraph {\n')
    dotfile.write('\tnewrank="true";\n')
    for line in lines:
        for char in line:
            dotfile.write('\t' + char + ';\n')
    dotfile.write('\n')
    for line in lines:
        dotfile.write('\t' + line[0] + ' -> ' + line[1] + ';\n')
        dotfile.write('\t' + line[1] + ' -> ' + line[2] + ';\n')
    dotfile.write('}')

os.system('dot -Tpng Problem079/graph.dot -o Problem079/graph.png')