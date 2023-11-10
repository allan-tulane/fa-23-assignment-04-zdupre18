import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions, and substitutions
    if not S:
        return len(T)
    elif not T:
        return len(S)
    else:
        if S[0] == T[0]:
            return MED(S[1:], T[1:])
        else:
            insert_cost = 1 + MED(S, T[1:])
            delete_cost = 1 + MED(S[1:], T)
            substitute_cost = 1 + MED(S[1:], T[1:])
            return min(insert_cost, delete_cost, substitute_cost)


def fast_MED(S, T, MED={}):
    # TODO -  implement top-down memoization
    if (S, T) in MED:
        return MED[(S, T)]

    # Base cases
    if not S:
        result = len(T)
    elif not T:
        result = len(S)
    elif S[0] == T[0]:
        result = fast_MED(S[1:], T[1:], MED)
    else:
        insert_cost = 1 + fast_MED(S, T[1:], MED)
        delete_cost = 1 + fast_MED(S[1:], T, MED)
        substitute_cost = 1 + fast_MED(S[1:], T[1:], MED)
        result = min(insert_cost, delete_cost, substitute_cost)

    MED[(S, T)] = result
    return result


def fast_align_MED(S, T, MED={}):
    # TODO - keep track of alignment
      if (S, T) in MED:
        return MED[(S, T)], alignment + MED[(S, T)][1]

    # Base cases
    if not S:
        result = len(T), [('I', t) for t in T]  # Insertion
    elif not T:
        result = len(S), [('D', s) for s in S]  # Deletion
    elif S[0] == T[0]:
        sub_result, sub_alignment = fast_align_MED(S[1:], T[1:], MED, alignment)
        result = sub_result, [('M', S[0])] + sub_alignment  # Match
    else:
        # Consider three possible operations: insertion, deletion, substitution
        insert_cost, insert_alignment = fast_align_MED(S, T[1:], MED, alignment)
        delete_cost, delete_alignment = fast_align_MED(S[1:], T, MED, alignment)
        substitute_cost, substitute_alignment = fast_align_MED(S[1:], T[1:], MED, alignment)

        # Find the operation with the minimum cost
        if insert_cost <= delete_cost and insert_cost <= substitute_cost:
            result = insert_cost, [('I', T[0])] + insert_alignment  # Insertion
        elif delete_cost <= insert_cost and delete_cost <= substitute_cost:
            result = delete_cost, [('D', S[0])] + delete_alignment  # Deletion
        else:
            result = substitute_cost, [('S', S[0], T[0])] + substitute_alignment  # Substitution

    MED[(S, T)] = result
    return result

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
