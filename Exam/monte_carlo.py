import random


def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    '''
    success_count = 0
    for trial in range(numTrials):
        balls = ['r'] * 4 + ['g'] * 4
        draws = random.sample(balls, 3)
        if draws == ['r'] * 3 or draws == ['g'] * 3:
            success_count += 1
    return success_count / numTrials
