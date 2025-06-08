import numpy as np

#  FIRST HALF OF THE PUZZLE

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

print('Answer to the first half of the puzzle:')
print(safety_check(reports))
print('  ')

# SECOND HALF OF THE PUZZLE

def safety_check_dampened(reports):
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

        if safety_list[report_index] == 0:
            # if the report itself is not safe, investigate subreports obtained by removing a single level
            subreport_safety_list = np.ones(len(report), dtype = np.int8)
            for level_index in range(len(report)):
                # exclude level corresponding to index_level
                subreport = np.concatenate((report[:level_index],report[level_index+1:])) 

                diff = subreport[1:] - subreport[:-1]
                
                # Condition 1: check for constance increase or decrease        
                if not (np.all(diff>0) or np.all(diff<0)):
                    # if safety condition 1 is not met, mark as unsafe
                    subreport_safety_list[level_index] = 0

                # Condition 2: check for successive decreases below 4
                if not np.all(abs(diff)<4):
                    # if safety condition 2 is not met, mark as unsafe
                    subreport_safety_list[level_index] = 0

            if (subreport_safety_list == 1).sum() >= 1:
                # if a subreport is safe, mark the report as safe
                safety_list[report_index] = 1
    
    safe_nb = np.sum(safety_list)

    return(safe_nb)

print('Answer to the second half of the puzzle:')
print(safety_check_dampened(reports))
print('  ')