#!usr/bin/python3

##Q.1

print("\n\n####### QUESTION 1 #######\n\n")

seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
sequence_length = len(seq)
print("###Length of the sequence :\n" + str(sequence_length))
number_of_A = seq.count("A")
number_of_T = seq.count("T")
print("###Count the number of A nucleotides :\n" + str(number_of_A))
print("###Count the number of T nucelotides :\n" + str(number_of_T))
A_and_T_content = (number_of_A) + (number_of_T)/sequence_length
print("###Percentage of AT content in the sequence is :\n" + str(A_and_T_content) + "%")

##Q.2

print("\n\n####### QUESTION 2 #######\n\n")

print("###Original DNA sequence :\n" + seq)
complement_a_t = seq.replace("A", "t")
complement_t_a = complement_a_t.replace("T", "a")
complement_c_g = complement_t_a.replace("C", "g")
complement_g_c = complement_c_g.replace("G", "c")
complement_g_c
complement = complement_g_c.upper()
print("###Complement DNA sequence :\n" + complement)

##Q.3

print("\n\n####### QUESTION 3 #######\n\n")

seq_3 = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
motif = "GAATTC"
pos = seq_3.find(motif)
print("###Position of the motif in the sequence :\n" + str(pos))
fragment = seq_3[22:]
print("###Second fragment based on the cut position :\n" + fragment)
fragment_length = len(fragment)
print("###Length of the second fragment based on the cut position :\n" + str(fragment_length))

##Q.4

print("\n\n####### QUESTION 4 #######\n\n")

gendna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
gendna
exon1 = gendna[:63]
print("###First exon :\n" + exon1)
len(exon1)
exon2 = gendna[90:]
print("###Second exon :\n" + exon2)
codingseq = exon1+exon2
print("###Coding sequence :\n" + codingseq)
length_codingseq = len(codingseq)
print("###Length of the coding sequence :\n" + str(length_codingseq))
len(gendna)
perc_codingDNA = len(codingseq)/len(gendna) * 100
print("###Percentage of the coding DNA sequence :\n" + str(perc_codingDNA) + "%")
intron = gendna[63:90]
intron
len(exon1)
len(exon2)
len(intron)
len(exon1) + len(exon2) + len(intron)
print("###Exon intron (lowercase) exon\n" + exon1 + intron.lower() + exon2)
