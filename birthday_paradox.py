import random
import collections
import matplotlib.pyplot as my_plot

"""
    Simulate the birthday problem.
    https://en.wikipedia.org/wiki/Birthday_problem
"""


def generate_birthdays(number_people):
    """
        Returns a list of birthday dates in 'daymonth' format.
    """
    birthday_list = []
    for i in range(number_people):
        day = str(random.randint(1,31))
        month = str(random.randint(1,12))
        birthday_list.append(day + month)
    return birthday_list

def frequency(birthday_list):
    """
        Counts the number of people who share a birthday.
    """
    counter = collections.Counter(birthday_list)
    for value in counter.values():
        if value > 1:
            return 1
    return 0

def probability(records, number_people):
    """
        Makes the probability that at least two people share a birthday.
    """
    freq = 0
    for i in range(records):
        birthdays = generate_birthdays(number_people)
        freq += frequency(birthdays)
    return freq * 100 / records

if __name__ == "__main__":
    x_axis = []
    y_axis = []
    print('Calculating Probabilities...')
    for number_people in range(2, 60):
        print(f' * Group [{number_people}]')
        x_axis.append(number_people)
        y_axis.append(probability(10000, number_people))
    print('Plotting Graph...')
    my_plot.plot(x_axis, y_axis) 
    my_plot.xlabel('Number of People') 
    my_plot.ylabel('Probability of Pair') 
    my_plot.title('Birthday Problem') 
    my_plot.show()
    print('End')

