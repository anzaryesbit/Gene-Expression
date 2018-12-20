def aminoacid(a, b, c):
    dna_sequence = a + b + c
    print('DNA Sequence: ' + dna_sequence)

    #mRNA transcription
    if a == 'G':
        a1 = 'C'
    elif a == 'g':
        a1 = 'C'
    elif a == 'C':
        a1 = 'G'
    elif a == 'c':
        a1 = 'G'
    elif a == 'A':
        a1 = 'U'
    elif a == 'a':
        a1 = 'U'
    elif a == 'T':
        a1 = 'A'
    elif a == 't':
        a1 = 'A'
    else:
        print('that is not a nucleotide base')

    if b == 'G':
        b1 = 'C'
    elif b == 'g':
        b1 = 'C'
    elif b == 'C':
        b1 = 'G'
    elif b == 'c':
        b1 = 'G'
    elif b == 'A':
        b1 = 'U'
    elif b == 'a':
        b1 = 'U'
    elif b == 'T':
        b1 = 'A'
    elif b == 't':
        b1 = 'A'
    else:
        print('that is not a nucleotide base')

    if c == 'G':
        c1 = 'C'
    elif c == 'g':
        c1 = 'C'
    elif c == 'C':
        c1 = 'G'
    elif c == 'c':
        c1 = 'G'
    elif c == 'A':
        c1 = 'U'
    elif c == 'a':
        c1 = 'U'
    elif c == 'T':
        c1 = 'A'
    elif c == 't':
        c1 = 'A'
    else:
        print('that is not a nucleotide base')
    mrna_sequence = a1 + b1 + c1
    print('mRNA Sequence: ' + mrna_sequence)

    #tRNA translation
    if a1 == 'G':
        a2 = 'C'
    elif a1 == 'g':
        a2 = 'C'
    elif a1 == 'C':
        a2 = 'G'
    elif a1 == 'c':
        a2 = 'G'
    elif a1 == 'A':
        a2 = 'U'
    elif a1 == 'a':
        a2 = 'U'
    elif a1 == 'U':
        a2 = 'A'
    elif a1 == 'u':
        a2 = 'A'
    else:
        print('trna error: that is not a nucleotide base')

    if b1 == 'G':
        b2 = 'C'
    elif b1 == 'g':
        b2 = 'C'
    elif b1 == 'C':
        b2 = 'G'
    elif b1 == 'c':
        b2 = 'G'
    elif b1 == 'U':
        b2 = 'A'
    elif b1 == 'U':
        b2 = 'A'
    elif b1 == 'A':
        b2 = 'U'
    elif b1 == 'a':
        b2 = 'U'
    else:
        print('trna error: that is not a nucleotide base')

    if c1 == 'G':
        c2 = 'C'
    elif c1 == 'g':
        c2 = 'C'
    elif c1 == 'C':
        c2 = 'G'
    elif c1 == 'c':
        c2 = 'G'
    elif c1 == 'A':
        c2 = 'U'
    elif c1 == 'a':
        c2 = 'U'
    elif c1 == 'U':
        c2 = 'A'
    elif c1 == 'u':
        c2 = 'A'
    else:
        print('trna error: that is not a nucleotide base')

    trna_sequence = a2 + b2 + c2
    print('tRNA Sequence: ' + trna_sequence)

    #amino acid sequencing with codons
    #PHENYLALANINE
    if mrna_sequence == 'UUU':
        print('Amino Acid: Phenylalanine (Phe)')
    elif mrna_sequence == 'UUC':
        print('Amino Acid: Phenylalanine (Phe)')

    #LEUCINE
    elif mrna_sequence == 'UUA':
        print('Amino Acid: Leucine (Leu)')
    elif mrna_sequence == 'UUG':
        print('Amino Acid: Leucine (Leu)')
    elif mrna_sequence == 'CUU':
        print('Amino Acid: Leucine (Leu)')
    elif mrna_sequence == 'CUC':
        print('Amino Acid: Leucine (Leu)')
    elif mrna_sequence == 'CUA':
        print('Amino Acid: Leucine (Leu)')
    elif mrna_sequence == 'CUG':
        print('Amino Acid: Leucine (Leu)')

    #ISOLEUCINE
    elif mrna_sequence == 'AUU':
        print('Amino Acid: Isoleucine (Ile)')
    elif mrna_sequence == 'AUC':
        print('Amino Acid: Isoleucine (Ile)')
    elif mrna_sequence == 'AUA':
        print('Amino Acid: Isoleucine (Ile)')

    #START CODON
    elif mrna_sequence == 'AUG':
        print('Amino Acid: Start codon; Methionine (Met)')

    #VALINE
    elif mrna_sequence == 'GUU':
        print('Amino Acid: Valine (Val)')
    elif mrna_sequence == 'GUC':
        print('Amino Acid: Valine (Val)')
    elif mrna_sequence == 'GUA':
        print('Amino Acid: Valine (Val)')
    elif mrna_sequence == 'GUG':
        print('Amino Acid: Valine (Val)')

    #SERINE
    elif mrna_sequence == 'UCU':
        print('Amino Acid: Serine (Ser)')
    elif mrna_sequence == 'UCG':
        print('Amino Acid: Serine (Ser)')
    elif mrna_sequence == 'UCA':
        print('Amino Acid: Serine (Ser)')
    elif mrna_sequence == 'UCG':
        print('Amino Acid: Serine (Ser)')
    elif mrna_sequence == 'AGU':
        print('Amino Acid: Serine (Ser)')
    elif mrna_sequence == 'AGC':
        print('Amino Acid: Serine (Ser)')

    #PROLINE
    elif mrna_sequence == 'CCU':
        print('Amino Acid: Proline (Pro)')
    elif mrna_sequence == 'CCC':
        print('Amino Acid: Proline (Pro)')
    elif mrna_sequence == 'CCA':
        print('Amino Acid: Proline (Pro)')
    elif mrna_sequence == 'CCG':
        print('Amino Acid: Proline (Pro)')

    #THREONINE
    elif mrna_sequence == 'ACU':
        print('Amino Acid: Threonine (Thr)')
    elif mrna_sequence == 'ACC':
        print('Amino Acid: Threonine (Thr)')
    elif mrna_sequence == 'ACA':
        print('Amino Acid: Threonine (Thr)')
    elif mrna_sequence == 'ACG':
        print('Amino Acid: Threonine (Thr)')

    #ALANINE
    elif mrna_sequence == 'GCU':
        print('Amino Acid: Alanine (Ala)')
    elif mrna_sequence == 'GCC':
        print('Amino Acid: Alanine (Ala)')
    elif mrna_sequence == 'GCA':
        print('Amino Acid: Alanine (Ala)')
    elif mrna_sequence == 'GCG':
        print('Amino Acid: Alanine (Ala)')

    #TYROSINE
    elif mrna_sequence == 'UAU':
        print('Amino Acid: Tyrosine (Tyr)')
    elif mrna_sequence == 'UAC':
        print('Amino Acid: Tyrosine (Tyr)')

    #HISTIDINE
    elif mrna_sequence == 'CAU':
        print('Amino Acid: Histidine (His)')
    elif mrna_sequence == 'CAC':
        print('Amino Acid: Histidine (His)')

    #GLUTAMINE
    elif mrna_sequence == 'CAA':
        print('Amino Acid: Glutamine (Gln)')
    elif mrna_sequence == 'CAG':
        print('Amino Acid: Glutamine (Gln)')

    #ASPARAGINE
    elif mrna_sequence == 'AAU':
        print('Amino Acid: Asparagine (Asn)')
    elif mrna_sequence == 'AAC':
        print('Amino Acid: Asparagine (Asn)')

    #LYSINE
    elif mrna_sequence == 'AAA':
        print('Amino Acid: Lysine (Lys)')
    elif mrna_sequence == 'AAG':
        print('Amino Acid: Lysine (Lys)')

    #ASPARTIC ACID
    elif mrna_sequence == 'GAU':
        print('Amino Acid: Aspartic Acid (Asp)')
    elif mrna_sequence == 'GAC':
        print('Amino Acid: Aspartic Acid (Asp)')

    #GLUTAMIC ACID
    elif mrna_sequence == 'GAA':
        print('Amino Acid: Glutamic Acid (Glu)')
    elif mrna_sequence == 'GAG':
        print('Amino Acid: Glutamic Acid (GlU)')

    #CYSTENINE
    elif mrna_sequence == 'UGU':
        print('Amino Acid: Cystenine (Cys)')
    elif mrna_sequence == 'UGC':
        print('Amino Acid: Cystenine (Cys)')

    #TYRPTOPHAN
    elif mrna_sequence == 'UGG':
        print('Amino Acid: Tryptophan (Trp)')

    #ARGININE
    elif mrna_sequence == 'CGU':
        print('Amino Acid: Arginine (Arg)')
    elif mrna_sequence == 'CGC':
        print('Amino Acid: Arginine (Arg)')
    elif mrna_sequence == 'CGA':
        print('Amino Acid: Arginine (Arg)')
    elif mrna_sequence == 'CGG':
        print('Amino Acid: Arginine (Arg)')
    elif mrna_sequence == 'AGA':
        print('Amino Acid: Arginine (Arg)')
    elif mrna_sequence == 'AGG':
        print('Amino Acid: Arginine (Arg)')

    #GLYCINE
    elif mrna_sequence == 'GGU':
        print('Amino Acid: Glycine (Gly)')
    elif mrna_sequence == 'GGC':
        print('Amino Acid: Glycine (Gly)')
    elif mrna_sequence == 'GGA':
        print('Amino Acid: Glycine (Gly)')
    elif mrna_sequence == 'GGG':
        print('Amino Acid: Glycine (Gly)')

    #END CODONS
    elif mrna_sequence == 'UAA':
        print('End Codon')
    elif mrna_sequence == 'UAG':
        print('End Codon')
    elif mrna_sequence == 'UGA':
        print('End Codon')

    else:
        print('There is no amino acid!')

input1 = input("first dna nucleotide base ")
input2 = input("second dna nucleotide base ")
input3 = input("third dna nucleotide base ")

aminoacid(input1, input2, input3)

repeat = input("do you want to put in another nucleotide base? [y/n] ")
while repeat == 'y':
    input1 = input("first dna nucleotide base: ")
    input2 = input("second dna nucleotide base: ")
    input3 = input("third dna nucleotide base: ")
    aminoacid(input1, input2, input3)
    repeat = input("do you want to put in another nucleotide base? [y/n] ")
