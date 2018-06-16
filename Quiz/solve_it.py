def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True
        In case of ties, return any one of them.
    """
    best_solution = None
    for x in range(-1000, 1000):
        try:
            if test(x):
                if not best_solution or abs(x) <= abs(best_solution):
                    best_solution = x
        except IndexError:
            continue
    return best_solution


# This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15


print(solveit(f))


# This test case prints 0 ####
def f(x):
    return x == 0


print(solveit(f))


# This test case prints 100
def f(x):
    return x == 100


print(solveit(f))


# This test case prints 3
def f(x):
    return x**2 == 9


print(solveit(f))


# This test case prints -4
def f(x):
    return x == -4


print(solveit(f))


# This test case prints 0
def f(x):
    return x**2 + x + 0 == 0


print(solveit(f))


# This test case prints -80
def f(x):
    return x == -80


print(solveit(f))


# This test case prints 3
def f(x):
    return [1, 2, 3][-x] == 1 and x != 0


print(solveit(f))
