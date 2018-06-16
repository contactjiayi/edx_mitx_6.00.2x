def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    max_sum = 0
    for start in range(0, len(L)):
        for end in range(1, len(L)):
            total = sum(L[start:end])
            if total > max_sum:
                max_sum = total
    return max_sum
