from Bio import SeqIO

source = 'fasta_file_name.fa'
outfile = 'filtered.fa'
sub1 ='GTACAGTAGG'
sub2 = 'CAACGGTTTTGCC'

def seq_check(seq, sub1, sub2):
    # basically a function to check whether seq starts or ends with sub1 or sub2
    return seq.startswith(sub1) or seq.startswith(sub2) or \
        seq.endswith(sub1) or seq.endswith(sub2)

seqs = SeqIO.parse(source, 'fasta')
filtered = (seq for seq in seqs if seq_check(seq.seq, sub1, sub2))
SeqIO.write(filtered, outfile, 'fasta')