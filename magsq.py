#!/usr/bin/env python

# The candidate magic square is represented as a list
# of integers - the challenge says to assume that numbers
# in the list are unique so we don't have to check.
# Each position in the list represents a position in the 
# square as so: [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] 
# would represent the following candidate square:
#   1   2   3
#   4   5   6
#   7   8   9
# Which is of course not a magic square but, I'll refer
# to the *positions* of the square as they are numbered
# above. However, since list / array indexing starts at 0
# the indexes will be one less.

def t7of9(S):
    # This test checks if 7 or 9 is in any corner or the
    # center position (1, 3, 5, 7, or 9). Any candidate
    # that has this condition is automatically rejected.
    # This is because for each of these numbers there are
    # only 2 pairs of integers in the remaining digits
    # that will add up with the first digit (7 or 9) to
    # make 15. The corners require 3 pairs and the center
    # requires 4 pairs.
    # True means the candidate square passed the test and
    # should be tested further.
    for i in range(0,9,2):
        if S[i] in [ 7, 9 ]:
            return False

    return True

def tcol(S, c):
    # Tests column 'c' in the candidate square 'S' by
    # summing the values in the column. Return value of
    # True means that the candidate square passed and should
    # be tested further. (Column # must be 1, 2 or 3)
    c -= 1
    return ((S[0+c]+S[3+c]+S[6+c]) == 15)

def trow(S, r):
    # Tests row 'r' in the candidate square 'S' by
    # summing the values of the row.
    i = 3*r - 3
    return ((S[i]+S[i+1]+S[i+2]) == 15)

def tdiag(S):
    # Tests diagonals by summing
    return ((S[0]+S[4]+S[8]) == 15) and ((S[2]+S[4]+S[6]) == 15)

import itertools
sqr = [1, 2, 3, 4, 5, 6, 7, 8 ,9]
#sqr = [8, 1, 6, 3, 5, 7, 4, 9, 2] ## known good
#sqr = [8, 1, 6, 3, 5, 7, 2, 9, 4] ## known bad

# 362880 permutations
for S in itertools.permutations(sqr):
    if all([t7of9(S),  tcol(S,1), tcol(S,2), tcol(S,3),
            trow(S,1), trow(S,2), trow(S,3), tdiag(S)]):
        print(S)
