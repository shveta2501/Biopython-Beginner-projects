from Bio.Seq import Seq
dna= Seq("ATGCGT")
print(dna)
#print(dna.complement()
rna=dna.transcribe()
print(rna)
print(rna.translate())
protein=dna.translate()
print(protein)