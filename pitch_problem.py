import time
import threading
from number import Number

pitches = []

def checkNum( num ):
    """Check if given <num.value> satisfies following requirements:
        1. sum(num.divisors) > num.value
        2. No subset from powerset of <num.divisors> adds up to exactly <num.value>
    """
    global pitches

    num = Number( num )

    isOfInterest = True

    if sum( num.divisors ) > num.value:
        subsets = num.powerset()
        for subset in subsets:
            if sum( subset ) == num.value:
                isOfInterest = False
                break
    else:
        isOfInterest = False

    if isOfInterest:
        pitches.append( num.value )

def pitchup():
    """ """
    for num in range( 1, 553 ):
        thread = threading.Thread( target = checkNum, name = "checkNum_%i" % num, args = ( num, ) )
        thread.start()

    while threading.activeCount() > 1:
        time.sleep( 1 )

    return

if __name__ == '__main__':
    pitchup()
    if pitches != []:
        for pitch in pitches:
            print "Selected pitch: %i" % pitch
    else:
        print "No pitch selected"