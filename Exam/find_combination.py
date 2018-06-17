import numpy as np
from itertools import chain, combinations


def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """
    powerset = chain.from_iterable(
        combinations(choices, r) for r in range(len(choices) + 1)
    )

    def find_result(subset):
        result = [0] * len(choices)
        used_indices = []
        for el in subset:
            indices = [i for i, val in enumerate(choices) if val == el]
            for idx in indices:
                if idx not in used_indices:
                    result[idx] = 1
                    used_indices.append(idx)
                    break
        return result

    best_match = (None, None)
    for subset in powerset:
        # found an exact match
        if sum(subset) == total:
            best_match = (find_result(subset), 0)
            break
        # no exact match, find the closest match
        else:
            match = find_result(subset)
            diff = total - sum(subset)
            if diff < 0:
                continue
            if not best_match[1] or diff < best_match[1]:
                best_match = (match, diff)
    return np.array(best_match[0])
