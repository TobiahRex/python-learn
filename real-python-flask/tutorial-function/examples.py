from decorators import *

@timer
def waste_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

for _ in rang