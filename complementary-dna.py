def DNA_strand(dna):

    di = {
        'A':'T',
        'G':'C',
        'T':'A',
        'C':'G'
    }
    dna_strand = ''
    for i in dna:
        dna_strand+=di[i]

    return dna_strand



print(DNA_strand("GTAT"))