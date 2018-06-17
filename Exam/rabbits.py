import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30


def rabbitGrowth():
    """
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up,
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    if CURRENTRABBITPOP == MAXRABBITPOP:
        return
    for n in range(CURRENTRABBITPOP):
        reproduction_prob = 1 - (CURRENTRABBITPOP / MAXRABBITPOP)
        if random.random() <= reproduction_prob:
            CURRENTRABBITPOP += 1


def foxGrowth():
    """
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    MIN_POP = 10

    for n in range(CURRENTFOXPOP):
        hunt_success_prob = CURRENTRABBITPOP / MAXRABBITPOP
        if random.random() <= hunt_success_prob:
            if CURRENTRABBITPOP > MIN_POP:
                CURRENTRABBITPOP -= 1
            reproduction_prob = 1 / 3
            if random.random() <= reproduction_prob:
                CURRENTFOXPOP += 1
        else:
            dying_prob = 1 / 10
            if random.random() <= dying_prob and CURRENTFOXPOP > MIN_POP:
                CURRENTFOXPOP -= 1


def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the
      END of each time step, and fox_populations is a record of the fox
      population at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbits = []
    foxes = []
    for s in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbits.append(CURRENTRABBITPOP)
        foxes.append(CURRENTFOXPOP)
    return rabbits, foxes


def plotSimulation(numSteps):
    rabbits, foxes = runSimulation(numSteps)

    pylab.plot(range(numSteps), rabbits, label='Rabbits')
    rabbit_coefficients = pylab.polyfix(range(len(rabbits)), rabbits, 2)
    pylab.plot(
        pylab.polyval(rabbit_coefficients, range(numSteps))
    )
    pylab.plot(range(numSteps), foxes, label='Foxes')
    fox_coefficients = pylab.polyfix(range(len(foxes)), foxes, 2)
    pylab.plot(
        pylab.polyval(fox_coefficients, range(numSteps))
    )
    pylab.show()
