from Bio import SeqIO
record = SeqIO.read("cox1.fasta", "fasta")

print(record.id)
print(record.description)
print(len(record))