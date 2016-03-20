__author__ = 'eric'

def reverse(st):
    '''
    :param st: string to reverse
    :return: Reversed string
    '''

    pass
    # handle base case first:
    #  the "simplest" value of st whose
    #  answer we can return immediately

    # if not simplest, solve part of the
    #  problem, then combine it with a
    #  recursive call for "simpler" st

def gcd(m,n):
    '''
    :param m: integer >= 0
    :param n: integer >= 0
    :return: greatest common divisor of m and n
    '''
    # check if base case applies: n == 0
    # otherwise reduce using identity given in
    # handout

    pass

def bsearch(lookfor,left,right,lst):
    '''
    :param lookfor: value in list lst to search for
    :param left: leftmost index within lst for search
    :param right: rightmost index within lst for search
    :param lst: list to search, assumed in ascending order
    :return: index i with lst[i]==lookfor if found, -1 if not
    '''
    if left > right:
        return -1
    # else mid=(left+right)//2 and continue as in handout...

def main():

    s2rev = input("Enter a string to reverse: ")

    print ("The string '%s' reversed is: '%s'." % (s2rev,reverse(s2rev)))

main()
