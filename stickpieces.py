import random

PIECES = 4
SAMPLES = 1000
count = 0

def cut_pieces(PIECES):
    pieces = []
    for i in range(PIECES):
        pieces.append(random.random())
    pieces.sort()
    return pieces

def is_possible():
    pieces = cut_pieces(PIECES)
    if pieces[3] >= pieces[2] + pieces[1] and pieces[2] >= pieces[1] + pieces[0]:
        return False
    else:
        return True
    
for i in range(SAMPLES):
    if is_possible():
        count += 1

print(f"Probability to arrange 3 of the 4 pieces in a triangle is {count/SAMPLES}")