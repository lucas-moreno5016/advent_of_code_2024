import numpy as np

def safety_check(reports):
    n = len(reports)

    # initialize list of safe and unsafe reports (1 is safe, 0 is unsafe)
    safety_list = np.ones(n, dtype = np.int8)

    for report_index in range(n):
        report = reports[report_index]
        diff = report[1:] - report[:-1]

        # Condition 1: check for constance increase or decrease        
        if not (np.all(diff>0) or np.all(diff<0)):
            # if safety condition 1 is not met, mark as unsafe
            safety_list[report_index] = 0

        # Condition 2: check for successive decreases below 4
        if not np.all(abs(diff)<4):
            # if safety condition 2 is not met, mark as unsafe
            safety_list[report_index] = 0
    
    safe_nb = np.sum(safety_list)

    return(safe_nb)


# Solve with real inputs
reports = []
with open('input_02.txt', 'r') as file:
    for line in file:
        values = [int(v) for v in line.strip().split()]
        reports.append(np.array(values, dtype=np.int8))


print(safety_check(reports))