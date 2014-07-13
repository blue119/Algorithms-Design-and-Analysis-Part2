from pprint import pprint
from time import time

# job compare
# compare by difference (weight - length).
# if two jobs have equal difference (weight - length),
# you should schedule the job with higher weight first.
#
# return
# 0 imply job1 is bigger
# 1 imply job2 is bigger
def job_cmp(job1, job2):
    #  print job1, job2
    w1, l1, d1 = job1
    w2, l2, d2 = job2

    if d1 == d2:
        if w1 > w2: return 0
        return 1

    if d1 > d2: return 0
    return 1

def find_insert_index(arr, job):
    for j in arr:
        if job_cmp(j, job):
            return arr.index(j)
    return len(arr) # append to tail

#  jobs_array = [weight, length, differnce, completion time]
whole_jobs = []
with open('jobs.txt', 'r') as f:
    number_of_jobs = int(f.readline())
    for line in f.readlines():
        weight = float(line.split()[0])
        length = float(line.split()[1])
        ct = 0
        #  whole_jobs.append([weight, length, weight - length, ]) # Question 1
        whole_jobs.append([weight, length, weight/length, ]) # Question 2
print "Totally Jobs: %d" % number_of_jobs

jobs_sorted = []
jobs_sorted.append(whole_jobs.pop())

print "jobs array sorting ... %f" % time()
for job in whole_jobs:
    idx = find_insert_index(jobs_sorted, job)
    jobs_sorted.insert(idx, job)

print "jobs array sorting ... Done %f" % time()
#  print job_cmp(whole_jobs[0], whole_jobs[1])

# 1. prioritize whole jobs
# 1.1 straightforward

# 1.2 HEAP Sort

# 2. find the comletion times and append to job array
print "compute completion time ... %f" % time()
completion_time = 0
for idx in xrange(len(jobs_sorted)):
    length = jobs_sorted[idx][1]
    completion_time += length
    jobs_sorted[idx].append(completion_time)

print "compute completion time ... Done %f" % time()
print "completion time: %d" % jobs_sorted[-1][-1]

# 3. find the sum of weighted completion times.
sum_of_wct = 0
for job in jobs_sorted:
    weight, ct = job[0], job[3]
    sum_of_wct += (weight * ct)

print "Sun of weighted completion times: %d" % sum_of_wct

