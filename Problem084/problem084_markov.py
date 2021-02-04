# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 84

# Find the minimal path sum from the top left to the bottom right by moving left, right, up, and down in matrix.txt


# This generates a markov chain for a monopoly board. This does not take into account probability of where one starts their turn.

import csv
from math import ceil

board = ['GO','A1','CC1','A2','T1','R1','B1','CH1','B2','B3','JAIL','C1','U1','C2','C3','R2','D1','CC2','D2','D3','FP','E1','CH2','E2','E3','R3','F1','F2','U2','F3','G2J','G1','G2','CC3','G3','R4','CH3','H1','T2','H2']
chance = {'GO', 'JAIL','C1','E3','H2','R1','NEXT_R','NEXT_R','NEXT_U','BACK_3'}

def monopoly_odds(dx):
    single_odd = 1/dx**2
    card_odd = single_odd * 1/16

    odds = []
    for pos in range(len(board)):
        if pos == 'G2J':
            continue
        odds.append([0]*len(board))
        for d1 in range(1,dx+1):
            for d2 in range(1,dx+1):
                new_pos = (pos + d1 + d2) % len(board)
                new_space = board[new_pos]
                if new_space not in {'CC1','CC2','CC3','CH1','CH2','CH3','G2J'} and d1 != d2:
                    odds[pos][new_pos] += single_odd
                elif new_space == 'G2J':
                    odds[pos][10] += single_odd
                elif d1 == d2:
                    odds[pos][new_pos] += single_odd - single_odd**3
                    odds[pos][10] += single_odd**3
                elif new_space in {'CC1','CC2','CC3'}:
                    odds[pos][new_pos] += card_odd * 14 #Fourteen cards will leave you in place
                    odds[pos][0] += card_odd
                    odds[pos][10] += card_odd
                elif new_space in {'CH1','CH2','CH3'}:
                    next_rail = (round(10 * ceil((new_pos-5)/10)) + 5) % len(board)
                    next_util = 28 if 13 <= new_pos <= 28 else 12
                    back_3 = (pos-3) % len(board)
                    if board[back_3] == 'G2J':
                        back_3 = 10

                    odds[pos][new_pos] += card_odd * 6 #Six cards will leave you in place
                    odds[pos][0] += card_odd
                    odds[pos][5] += card_odd
                    odds[pos][10] += card_odd
                    odds[pos][11] += card_odd
                    odds[pos][24] += card_odd
                    odds[pos][39] += card_odd
                    odds[pos][next_rail] += card_odd * 2 #Two cards take you to next rail
                    odds[pos][next_util] += card_odd
                    odds[pos][back_3] += card_odd

    for row in range(len(odds)):
        for col in range(len(odds)):
            odds[row][col] = round(odds[row][col],5)


    with open("Problem084/output.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(odds)
    most_common = {str(i).rjust(2,'0'): round(sum(row[i] for row in odds)/len(board),5) for i in range(len(odds))}
    print(most_common)
    modal_string = ''.join(sorted(most_common, key=most_common.get)[::-1])
    return modal_string[:6]

print(monopoly_odds(6))
