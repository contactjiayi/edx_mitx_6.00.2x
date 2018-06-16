def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for
        the largest value in L then for the second largest, and so on to
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does
                not yield a set of multipliers such that the equation sums to 's'
    """
    remaining = s
    multipliers = []
    for integer in L:
        max_multiplier = remaining // integer
        multipliers.append(max_multiplier)
        remaining -= max_multiplier * integer
    return sum(multipliers) if remaining == 0 else 'no solution'
