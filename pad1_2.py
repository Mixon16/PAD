class Worker():
    def __init__(self, number, name, age, salary):
        self.number = number
        self.age = datetime.now().year - age
        self.salary = salary
        self.name = name
    
w1 = Worker(1, 'Adam', 1983, 1500)
w2 = Worker(2, 'Anna', 1981, 1700)
w3 = Worker(3, 'Błazej', 1990, 1800)
w4 = Worker(4, 'Beata', 1992, 1600)
w5 = Worker(5, 'Czesław', 1980, 2000)
w6 = Worker(6, 'Cecylia', 1983, 2100)
w7 = Worker(7, 'Daniel', 1976, 1900)

workers = [w1,w2,w3,w4,w5,w6,w7]

def meanSalary(workers):
    sum = 0
    for  w in workers:
        sum += w.salary
    return sum/len(workers)

meanSalary(workers)
def compareOldSalariesAndYoung(workers):
    sum_old = 0
    sum_young = 0
    count_young = 0
    count_old = 0
    for w in workers:
        if w.age < 31:
            sum_young += w.salary
            count_young += 1
        else:
            sum_old += w.salary
            count_old += 1
    mean_young = sum_young/count_young
    mean_old = sum_old/count_old
    difference = mean_young/mean_old
    print('Średnia pensja młodszych niz 30 lat to: {:.3f}'.format(mean_young) + '\nŚrednia pensja starszych to: {:.3f}'.format(mean_old))
    print('Średnia pensja młodyszych to {:1.3f}'.format(difference) + ' pensji starszych')

compareOldSalariesAndYoung(workers)