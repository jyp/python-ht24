


class Tracker:
    def __init__(self,now):
        # instance attributes:
        # "now" remembers the current time
        self.now = now
        # remember which activities are started, and when
        self.start_time = dict()
        # remember which activities are done (and their timespan)
        # each entry is a tuple (see Q2)
        self.completed = []
    def tick(self,n):
        # advance the time by n units of time.
        self.now = self.now + n
    def start(self,task):
        # records that task is starting. A warning message is printed if the task is already started.
        if task in self.start_time:
            print("Task already started")
        else:
            self.start_time[task] = self.now
    def stop(self,task):
        # records that task stops. A warning message is printed if the task is not started.
        if self.start_time.get(task) == None:
            print("Task not started")
        else:
            self.completed.append((self.start_time[task],self.now,task))
            self.start_time[task] = None # homework: change this to use pop.
    def stop_all(self):
        # records that all ongoing tasks stop.
        for task in self.start_time:
            self.stop(task)
    def print_agenda(self):
        # prints the agenda for the day in the format of agenda.txt (see Question 2).
        if len(self.start_time) > 0:
            print("there are tasks which are not stopped")
        for (start,stop,task) in self.completed:
            print(start,stop,task)

a = Tracker(9)
a.start("exam")
a.tick(3)
a.start("lunch")
a.tick(1)
a.stop("exam")
a.tick(1)
a.stop("lunch")
a.tick(1)
a.start("dance-class")
a.tick(1)
a.tick(1)
a.stop("dance-class")
a.tick(1)
a.start("meet-friends")
a.tick(4)
a.stop_all()
a.print_agenda()
            
