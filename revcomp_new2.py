def reverse_complement(seq, material='DNA'):
    """Compute reverse complement of the input sequence."""
    seq_1 = seq.upper()
    seq_2 = seq_1[::-1]
    seq_3 = seq_2.replace('A', 't')
    seq_4 = seq_3.replace('C', 'g')
    seq_5 = seq_4.replace('T', 'a')
    seq_6 = seq_5.replace('G', 'c')
    seq_7 = seq_6.upper()
    return seq_7
