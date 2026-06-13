from Bio.Seq import Seq
dna= Seq("ATGCGT")
print(dna)
#print(dna.complement()
rna=dna.transcribe()
print(rna)
print(rna.translate())
protein=rna.translate()
print(protein)