from pyeasyga import pyeasyga
from collections import namedtuple

# setup the data
investments = [30,74,7,10,15,18,48,24,24,78,50,63,25,37,37,6,1,34,16,56,32,47,75,28,22,60,76,37,51,8,74,4,49,37,16,50,29,63,53,43,21,73,47,8,41,39,58,20,55,46,31,52,76,32,24,47,17,9,43,70,2,52,52,59,26,1,0,29,12,44,72,51,2,7,65,17,50,78,79,68,66,31,24,65,33,36,73,57,70,6,16,2,18,35,9,20,51,56,66,35]
values = [13,41,95,1,3,48,53,24,5,15,9,61,23,1,98,55,59,96,57,67,78,97,21,90,57,23,73,96,4,8,12,45,62,61,89,10,4,18,13,79,97,6,39,47,7,86,85,16,46,70,48,43,96,4,98,32,63,78,86,40,42,1,97,49,3,42,17,28,11,45,5,81,59,50,1,65,75,88,87,0,22,30,0,39,1,8,56,46,45,35,34,4,43,97,43,57,38,94,40,55]
available_funds = 2000
linked_groups = [[0,1,2,3], [23,24,25,26,27,28], [79,80,81,82]]
group_bonuses = [80, 100, 200]

company = namedtuple('company', 'company_no, value, investment')
data = [company(company_no, value, investment) for (company_no, (value, investment)) in enumerate(zip (values, investments), 1)]

# initialise the GA with the data
ga = pyeasyga.GeneticAlgorithm(data)

# set values for population and generation size if not satisfied with the defaults
ga.population_size = 100     # default is 50
ga.generations = 500         # default is 100

# define the fitness function
def fitness(individual, data):
    fitness_val = 0.0
    value, investment = 0, 0

    for selected, company in zip(individual, data):
        if selected:
            value += company.value
            investment += company.investment

    # if no company was selected return
    if value, investment == 0, 0:
        return 0.0

    # penalise investments that go over available funds
    if investment > available_funds:
        fitness_val = 0.0
    else:
        # apply the appropriate group bonues
        for group, bonus in zip(linked_groups, group_bonuses):
            if all([individual[member] for member in group]):
                value += bonus

        # Lower investments for the same value have a higher fitness
        fitness_val = value + (1.0 / investment)

    return fitness_val

def main():
    ga.fitness_function = fitness               # set the GA's fitness function
    ga.run()                                    # run the GA
    best_solution = ga.best_individual()        # get the GA's best solution
    selected_individuals = best_solution[1]     # the binary list of selected companies

    # get the total value and investment for the selected companies
    total_value, total_investment = 0, 0
    selected_companies = []
    for selected, company in zip(selected_individuals, data):
        if selected:
            total_value += company.value
            total_investment += company.investment
            selected_companies.append(company.company_no)

    # apply the appropriate group bonues
    for group, bonus in zip(linked_groups, group_bonuses):
        if all([selected_individuals[member] for member in group]):
            total_value += bonus

    print ("%d Selected Companies: %s" % (len(selected_companies), selected_companies))
    print ("Total Investment: %d" % total_investment)
    print ("Total Value: %d" % total_value)

if __name__ == "__main__":
    main()
