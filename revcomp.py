def reverse_complement(seq, material='DNA'):
    """Compute reverse complement of the input sequence."""
#Initialize the reverse complement
    rev_seq = ''

    for base in reversed(seq):
        rev_seq += complement_base(base, material=material)

    return rev_seq

def complement_base(base, material='DNA'):
    """Returns the Watson-Crick complement of a base."""
    base = base.lower()
    if base in 'a':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
    elif base in 'tu':
        return 'A';
    elif base in 'g':
        return 'C'
    else:
        return 'G'
