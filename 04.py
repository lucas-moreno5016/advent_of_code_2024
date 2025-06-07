import numpy as np

def count_XMAS(data):
    # reference sequence to compare to subsequencies in data
    ref_sequence = [np.str_('X'), np.str_('M'), np.str_('A'), np.str_('S'), ]

    count = 0
    [n,m] = [len(data), len(data[0])]

    # pad data with zeros
    data_padded = np.pad(data, pad_width=3, mode='constant', constant_values=0)
    
    for row in range(3,n+3):
        for col in range(3,m+3):

            # check if 'XMAS' is present by checking around the letter X in all directions
            # left to right
            sequence = [data_padded[row,col], data_padded[row,col+1], data_padded[row,col+2], data_padded[row,col+3]]
            if sequence == ref_sequence:
                count+=1

            # right to left
            sequence = [data_padded[row,col], data_padded[row,col-1], data_padded[row,col-2], data_padded[row,col-3]]
            if sequence == ref_sequence:
                count+=1
            
            # up to down
            sequence = [data_padded[row,col], data_padded[row+1,col], data_padded[row+2,col], data_padded[row+3,col]]
            if sequence == ref_sequence:
                count+=1

            # down to up
            sequence = [data_padded[row,col], data_padded[row-1,col], data_padded[row-2,col], data_padded[row-3,col]]
            if sequence == ref_sequence:
                count+=1

            # left down to right up
            sequence = [data_padded[row,col], data_padded[row-1,col+1], data_padded[row-2,col+2], data_padded[row-3,col+3]]
            if sequence == ref_sequence:
                count+=1

            # left up to right down
            sequence = [data_padded[row,col], data_padded[row+1,col+1], data_padded[row+2,col+2], data_padded[row+3,col+3]]
            if sequence == ref_sequence:
                count+=1
            
            # right up to left down
            sequence = [data_padded[row,col], data_padded[row+1,col-1], data_padded[row+2,col-2], data_padded[row+3,col-3]]
            if sequence == ref_sequence:
                count+=1

            # right down to left up
            sequence = [data_padded[row,col], data_padded[row-1,col-1], data_padded[row-2,col-2], data_padded[row-3,col-3]]
            if sequence == ref_sequence:
                count+=1

    return(count)


# Load text file line by line
with open('input_04.txt', 'r') as file:
    lines = [list(line.strip()) for line in file]
# Convert to NumPy array of strings
data = np.array(lines, dtype='<U1')


print(count_XMAS(data))