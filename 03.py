import numpy as np

#  FIRST HALF OF THE PUZZLE

def uncorrupt(data):
    # initialize list of indexes at which the subsequence 'mul(' is found.
    indexes = []

    # initialize lists of numbers to multiply in valid subsequencies
    a = []
    b = []
    

    # get indexes at which the subsequence 'mul(' is found. No overlaps possible.
    for sweep_index in range(len(data)):
        index = data[sweep_index:].find('mul(')
        if index !=-1 and not(sweep_index + index in indexes):
            indexes.append(sweep_index + index)


    # loop through instances of 'mul('
    for index in indexes:
        # look for ',' in next caracters
        comma_index = data[index + len('mul(') : index + len('mul(aaa,') + 1 ].find(',')
        
        if comma_index != -1:  
            # if ',' is found, look for  ')' in next caracters
            par_index = data[index + len('mul(') + comma_index + 1 : index + len('mul(') + comma_index + len('bbb)') + 1 ].find(')')
            
            if par_index !=-1:
                # if ')' is found, get strings corresponding to both numbers
                a_nb = data[index + len('mul(') : index + len('mul(') + comma_index]
                b_nb = data[index + len('mul(') + comma_index +1 : index + len('mul(') + comma_index + 1 + par_index]
                
                if a_nb.isdigit() and b_nb.isdigit():
                    # if both strings correspond to integers without undesired caracters, the sequence is declared valid and the numbers are appended to the lists of numbers to multiply
                    a.append(int(a_nb))
                    b.append(int(b_nb))
        
    # return the sum of element-wise multiplication of a and b ie. scalar product of a and b
    return(np.dot(a,b))

# Solve with real input
data = open('input_03.txt', 'r').read()


print('Answer to the first half of the puzzle:')
print(uncorrupt(data))
print('  ')

# SECOND HALF OF THE PUZZLE

def uncorrupt2(data):
    # initialize list of indexes at which the subsequence 'mul(' is found.
    indexes = []

    # initialize lists of numbers to multiply in valid subsequencies
    a = []
    b = []
    
    # get indexes at which the subsequence 'mul(' is found, only when the mul sequences is enabled. No overlaps possible.
    for sweep_index in range(len(data)):
        index = data[sweep_index:].find('mul(')
        if index !=-1 and not(sweep_index + index in indexes):

            # get last occurences of of the "do()" and "don't()" sequencies before the index at which 'mul(' is found
            do_index = data[:sweep_index + index].rfind("do()")
            dont_index = data[:sweep_index + index].rfind("don't()")

            # compare which command is given last. If not found, the index is -1 and the coparison is valid
            if dont_index <= do_index:
                # if the do command is ulterior or neither do or dont have already appeared, the command is valid
                indexes.append(sweep_index + index)
    

    # loop through the selected instances of 'mul(', only in do mode 
    for index in indexes:
        # look for ',' in next caracters
        comma_index = data[index + len('mul(') : index + len('mul(aaa,') + 1 ].find(',')
        
        if comma_index != -1:  
            # if ',' is found, look for  ')' in next caracters
            par_index = data[index + len('mul(') + comma_index + 1 : index + len('mul(') + comma_index + len('bbb)') + 1 ].find(')')
            
            if par_index !=-1:
                # if ')' is found, get strings corresponding to both numbers
                a_nb = data[index + len('mul(') : index + len('mul(') + comma_index]
                b_nb = data[index + len('mul(') + comma_index +1 : index + len('mul(') + comma_index + 1 + par_index]
                
                if a_nb.isdigit() and b_nb.isdigit():
                    # if both strings correspond to integers without undesired caracters, the sequence is declared valid and the numbers are appended to the lists of numbers to multiply
                    a.append(int(a_nb))
                    b.append(int(b_nb))
        
    # return the sum of element-wise multiplication of a and b ie. scalar product of a and b
    return(np.dot(a,b))


print('Answer to the second half of the puzzle:')
print(uncorrupt2(data))
print('  ')