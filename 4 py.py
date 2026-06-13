from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
dna = Seq ("ATGCGT")
record = SeqRecord(
    dna,
    id="Gene1",
    name= "Eample Gene",
    description = " Sample DNA seq for practice"
)

print(record.id)
print(record.name)
print(record.description)
#print(record.seq)
protein_seq = Seq("MKTLLV")
protein_record= SeqRecord(
    protein_seq,                 
    "test protein", #id
    "prot01",            #name
    "sample protein seq example"#description
)
print(protein_record.description)