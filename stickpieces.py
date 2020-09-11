import random

PIECES = 4
SAMPLES = 100000
count = 0
count2 = 0

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

def all_are_possible():
    pieces = cut_pieces(PIECES)
    if pieces[3] >= pieces[1] + pieces[0]:
        return False
    else:
        return True
   
for i in range(SAMPLES):
    if is_possible():
        count += 1
    if all_are_possible():
        count2 += 1

print(f"Probability to arrange 3 of the 4 pieces in a triangle is {count/SAMPLES}")
print(f"Probability to be able to arrange any 3 of the 4 pieces into a triangle is {count2/SAMPLES}")