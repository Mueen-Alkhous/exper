"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

# helper function
def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

# main code
def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    score_boxs = dict()
    for idx in hand:
        score_boxs[idx] = hand.count(idx) * idx
    return max(score_boxs.values())
    

def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    sum_of_scores = 0.0
    for tup in gen_all_sequences([idx+1 for idx in range(num_die_sides)], num_free_dice):
        sum_of_scores += score(held_dice + tup)
    return sum_of_scores / (num_die_sides**num_free_dice)


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    
    all_holds = set([()])
    for die in hand:
        for partial_sequence in set(all_holds):
            new_hold = list(partial_sequence)    
            new_hold.append(die)
            all_holds.add(tuple(new_hold))
    return all_holds




def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    all_holds = list(gen_all_holds(hand))
    expected_values = []
    for tup in all_holds:
        expected = expected_value(tup, num_die_sides, (len(hand) - len(tup)))
        expected_values.append(expected)
    combine_holds_values = zip(expected_values, all_holds)
    idx_of_max = expected_values.index(max(expected_values))
    return combine_holds_values[idx_of_max]


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
#run_example()


#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
    
    
    
print expected_value((0,), 6, 1)


