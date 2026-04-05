seq='AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
import re
ORF=re.findall(r'(?=(AUG(?:...)*?(?:UAA|UAG|UGA)))', seq)
largest_ORF=max(ORF, key=len)
print('All ORFs:', ORF)
print('Largest ORF:', largest_ORF)
print("Length:", len(largest_ORF))