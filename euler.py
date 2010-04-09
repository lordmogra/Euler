#!/usr/bin/python

#Imports
import time
from optparse import OptionParser

#Parser
parser = OptionParser()

parser.add_option("-d", "--debug", action="store_true", dest="debug", default=False)

#Variables
(opts, args) = parser.parse_args()

#Global Functions
def print_timing(func):
    def wrapper(*arg):
        t1 = time.time()
        res = func(*arg)
        t2 = time.time()
        if (opts.debug):
            print '%s took %0.3f ms' % (func.func_name, (t2-t1)*1000)
        return res
    return wrapper

#Classes
class ProblemBase:
    def execute(self):
        raise NotImplementedError

class Problem1(ProblemBase):
    @print_timing
    def sum_values_divisible_by_three_or_five(self, max):
        total = 0

        i = 3
        while (i < max):
            total = total + i
            i = i + 3

        i = 5
        while (i < max):
            if ( i % 3 != 0):
                total = total + i
            i = i + 5

        return total

    @print_timing
    def their_way(self, max):
        total = 0

        for i in range(0,max):
            if (i%3 == 0) or (i%5 == 0):
                total = total + i

        return total

    def execute(self, max=1000):
        print "Problem 1:"

        print "\nFind the sum of all the multiples of 3 or 5 below 1000."

        print "\nThe Answer is:",
        print self.sum_values_divisible_by_three_or_five(max)


class Problem2(ProblemBase):
    @print_timing
    def fibbonacci(self, max):
        a,b = 0,1
        values = []

        while (a < max):
            values.append(a)
            a,b = b, a+b

        return values

    def execute(self, max=4000000):
        print "Problem 2:"

        print "\nFind the sum of all the even-valued terms in the sequence which do not exceed four million."

        print "\nThe Answer is :",
        print sum(i for i in self.fibbonacci(max) if (i%2 == 0))

class Problem3(ProblemBase):
    @print_timing
    def get_largest_prime_factor(self, num):
        pass

    def execute(self, num=600851475143):
        print "Problem 3:"

        print "\nWhat is the largest prime factor of the number 600851475143?"

        print "\nThe Answer is :",
        print self.get_largest_prime_factor(num)

def main():
    #Problem1().execute()
    #Problem2().execute()
    #Problem3().execute()

if __name__ == '__main__': main()
