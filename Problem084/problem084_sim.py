# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 84

# Find the minimal path sum from the top left to the bottom right by moving left, right, up, and down in matrix.txt


# This is a simulation of monopoly
from random import randint, choice
from math import ceil
import csv

board = ['GO','A1','CC1','A2','T1','R1','B1','CH1','B2','B3','JAIL','C1','U1','C2','C3','R2','D1','CC2','D2','D3','FP','E1','CH2','E2','E3','R3','F1','F2','U2','F3','G2J','G1','G2','CC3','G3','R4','CH3','H1','T2','H2']
chance = ['GO', 'JAIL','C1','E3','H2','R1','NEXT_R','NEXT_R','NEXT_U','BACK_3','','','','','','']
comm_chest = ['GO','JAIL','','','','','','','','','','','','','','']

def monopoly_sim(dx, rounds):
    counts = [[0]*len(board)]*len(board)
    
    pos = 0
    doubles = 0
    for _ in range(rounds):
        d1,d2 = randint(1,dx), randint(1,dx)
        new_pos = (pos + d1 + d2) % len(board)
        new_space = board[new_pos]

        if d1 == d2:
            doubles += 1
            if doubles == 3:
                new_pos = 10
                doubles = 0
            new_space = board[new_pos]
        if new_space in {'CH1','CH2','CH3'}:
            card = choice(chance)
            if card in board:
                new_pos = board.index(card)
            elif card == 'NEXT_R':
                new_pos = (round(10 * ceil((new_pos-5)/10)) + 5) % len(board)
            elif card == 'NEXT_U':
                new_pos = 28 if 13 <= new_pos <= 28 else 12
            elif card == 'BACK_3':
                new_pos = (new_pos-3) % len(board)
            new_space = board[new_pos]
        if new_space in {'CC1','CC2','CC3'}:
            card = choice(comm_chest)
            if card in board:
                new_pos = board.index(card)
            new_space = board[new_pos]
        if new_space == 'G2J':
            new_pos = 10
            new_space = board[new_pos]

        counts[pos][new_pos] += 1/rounds*100
        pos = new_pos

    with open("Problem084/output.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(counts)
    most_common = {str(i).rjust(2,'0'): round(sum(row[i] for row in counts)/len(board),5) for i in range(len(counts))}
    print(most_common)
    modal_string = ''.join(sorted(most_common, key=most_common.get)[::-1])
    return modal_string[:6]

print(monopoly_sim(4,1000000))