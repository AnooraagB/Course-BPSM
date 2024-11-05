!#user/bin/python3

#import modules
import subprocess, shutil

plain_genomic_seq = open("plain_genomic_seq.txt").read()
print("Plain genomic sequence :\n" + plain_genomic_seq)
plain_genomic_seq_stripped = plain_genomic_seq.rstrip("\n")
plain_genomic_seq_stripped_upper = plain_genomic_seq_stripped.upper()
localseqoneline
localseq = plain_genomic_seq_stripped_upper.replace("G","").replace("A","").replace("T","").replace("C","")
localseq
myseq = plain_genomic_seq_stripped.replace("X","")
myseq = myseq.replace("t","")
myseq = myseq.replace("G","")
myseq = myseq.replace("S","")
myseq = myseq.replace("K","")
localseq = myseq.replace("L","")
print("Local sequence :\n" + localseq)
len(localseq)
exon1 = localseq[:63]
print("Exon 1 :\n" + exon1)
exon2 = localseq[90:]
print("Exon 2 :\n" + exon2)
intron = localseq[63:90]
print("Intron :\n" + intron)
len(exon1) + len(exon2) + len(intron)

##remote file

subprocess.call("esearch -db nucleotide -query \ "AJ223353[accession]\" | efecth -format fasta | grep -v \ "> \" > AJ223353_noheader.fasta3", shell=True)
remotefile = open("AJ223353_noheader.fast3").read().upper()
print("The remote file is :\n" + remotefile)

remotefileoneline = remotefile.replace("\n","")
print("The remote file in a single line is :\n" + remotefileoneline)

remoteseq = remotefileoneline
print("Length of the remote file is :\n" + len(remoteseq))


remotefileonelineanythingleft = remotefileoneline.replace("G","").replace("A","").replace("T","").replace("C","")
