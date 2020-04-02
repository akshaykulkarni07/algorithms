# Given an array of jobs where every job has a deadline and 
# associated profit if the job is finished before the deadline. 
# It is also given that every job takes single unit of time, so 
# the minimum possible deadline for any job is 1. How to maximize 
# total profit if only one job can be scheduled at a time.

class Job(object):
    def __init__(self, name, deadline, profit):
        self.name = name
        self.deadline = deadline
        self.profit = profit

def job_sequencing(job_list):
    # sort the jobs according to profit
    for i in range(len(job_list)):
        for j in range(len(job_list) - i - 1):
            if job_list[j].profit < job_list[j + 1].profit:
                job_list[j + 1], job_list[j] = job_list[j], job_list[j + 1]

    job_seq = ['-1'] * len(job_list)
    time_slots = [False] * len(job_list)
    for i in range(len(job_list)):
        for j in range(min(len(job_list), job_list[i].deadline) - 1, -1, -1):
            if time_slots[j] == False:
                time_slots[j] = True
                job_seq[j] = job_list[i].name
                break
    return job_seq

if __name__ == '__main__':
    job_list = [Job('a', 2, 100), Job('b', 1, 19), Job('c', 2, 27), Job('d', 1, 25), Job('e', 3, 15)]
    job_seq = job_sequencing(job_list)
    for job in job_seq:
        if job != '-1':
            print(job)