
def load_agenda(file_name):
    # reads the agenda and returns a list of tuples with Start, Stop and Task, using appropriate data types.
    result = []
    with open(file_name) as f:
        for line in f:
            [start, stop,task] = line.split()
            result.append((int(start),int(stop),task))
    return result

print(load_agenda("agenda.txt"))

def tabulate_agenda(agenda):
    # takes the result of the previous function
    # returns a list of lists results, such that result[t] is the list of tasks happening at time t.
    # assumption: there are maximum 24 hours in an agenda.
    result = []
    for _ in range(0,24):
        result.append([])
    for item in agenda:
        (start,stop,task) = item
        for t in range(start,stop+1):
            result[t].append(task)
    return result

    # Note that tasks can overlap. For instance, assuming the above agenda, result[13] = ['exam','lunch'].
    
print(tabulate_agenda(load_agenda("agenda.txt"))[13])
