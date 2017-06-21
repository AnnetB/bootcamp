def longest_common_sub(seq_1, seq_2):
    """Find longest common substring of seq_1 and seq_2"""

    #loop through the sequence and compare to second sequence
    for i in seq_1:
        if i in seq_2 == i in seq_1:
            for i+1 in seq_1:
                if i in seq_2 == i in seq_1:
    else:
            print ('No common substring found.')
    return
    # Show the result
    if i == len(seq):
        print('No common substring found.')
    else:
        print('The longest common substring is', i)
