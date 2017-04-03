__author__ = 'plevytskyi'


class PrimeFinder(object):

    def __init__(self, algorithm):
        """
        Constructor, takes a callable object called algorithm.
        algorithm should take a limit argument and return an iterable of prime
        numbers below that limit.
        """
        self.algorithm = algorithm
        self.primes = []

    def calculate(self, limit):
        """ Will calculate all the primes below limit. """
        self.primes = self.algorithm(limit)

    def out(self):
        """ Prints the list of primes prefixed with which algorithm made it """
        print(self.algorithm.__name__)
        print(self.primes)


def hard_coded_algorithm(limit):
    """
    Has hardcoded values for all the primes under 50, returns a list of those
    which are less than the given limit.
    """
    hardcoded_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    primes = []
    for prime in hardcoded_primes:
        if prime < limit:
            primes.append(prime)
    return primes


def standard_algorithm(limit):
    """
    Not a great algorithm either, but it's the normal one to use.
    It puts 2 in a list, then for all the odd numbers less than the limit if
    none of the primes are a factor then add it to the list.
    """
    primes = [2]
    # check only odd numbers.
    for number in range(3, limit, 2):
        is_prime = True
        # divide it by all our known primes, could limit by sqrt(number)
        for prime in primes:
            if number % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    return primes

if __name__ == "__main__":
    hardcoded_primes = PrimeFinder(hard_coded_algorithm)
    hardcoded_primes.calculate(50)
    hardcoded_primes.out()

    standard_primes = PrimeFinder(standard_algorithm)
    standard_primes.calculate(50)
    standard_primes.out()