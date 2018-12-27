import sys

work_day_len = 240 # 4 hours
tq = 120 # 2 hours, time quantum, amount of time to work before priority is reduced

class model:
    def __init__(self):
        self.proj_lst = []      # list of projects, i.e., the main work queue
        self.day_sched = []     # list of day_tasks, to be printed when displaying the day's schedule
        self.cur_pri = 1        # currently the highest priority

    def add_proj(self, proj):
        self.proj_lst.append(proj)
        self.update_sched()

    # method to update date, called when model changes
    def update_sched(self):

        self.day_sched = []

        day_sched_time = 0
        i = 0

        # look in proj_lst for project that has pri that equals cur_pri
        # i.e, while the total day_sched time is less than work_day_len
        while day_sched_time < work_day_len:
            
            # determine amount of time
            work_time = tq  #placeholder for more logic

            # create day_task for that project and add it to the day_sched, allocate at most tq time
            if (self.proj_lst[i].pri <= self.cur_pri):
                self.day_sched.append(day_task(self.proj_lst[i].id, work_time, self.proj_lst[i].pri))
                day_sched_time += work_time
            
            i += 1

            # if the end of the list is reached, then...
            if (i == len(self.proj_lst)):
                self.cur_pri += 1
                i = 0

    # method to display current date, does not make any changes
    def display_day_sched(self):
        for each in self.day_sched:
            print(each)


# class to display task for day schedule
class day_task:
    def __init__(self, id, time, pri):
        self.id = id
        self.time = time
        self.pri = pri
        
    def __str__(self):
        return "Work on project " + self.id + " for " + str(self.time) + " minutes, it's at priority " + str(self.pri)
        
class project:
    def __init__(self, id):       # should also accept time to finish
        self.id = id
        self.pri = 1
        self.tq = tq

    def do_work(self, time):
        self.tq -= time
        if (self.tq == 0):
            self.tq = tq
            self.pri += 1


def main():
    
    m = model()

    count = int(input("How many projects?:\n"))
    
    for i in range(count):
        proj_name = input("Name of project " + str(i+1) + "?\n")
        m.add_proj(project(proj_name))

    # display current day's plan
    m.display_day_sched()

    # accept input for progress


if __name__ == "__main__":
    main()