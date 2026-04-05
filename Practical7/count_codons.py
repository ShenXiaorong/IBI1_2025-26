input_file=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
stop_codon = input('Please input a stop codon (TAA/TAG/TGA): ')
while stop_codon not in ['TAA', 'TAG', 'TGA']:
    print('Invalid input. Please enter a valid stop codon (TAA/TAG/TGA).')
    stop_codon = input('Please input a stop codon (TAA/TAG/TGA): ')
header=''
seq_lines=[]
count={}
import re
for line in input_file:
    line=line.strip()
    if line.startswith('>'):
        if header:
           seq=''.join(seq_lines)
           matches = re.findall(rf'(?=(ATG(?:...)*?{stop_codon}))', seq)
           if matches:
              largest_match=max(matches, key=len)
              coding_part=largest_match[:-3]
              for i in range(0, len(coding_part), 3):
                    codon=coding_part[i:i+3]
                    if codon in count:
                        count[codon] += 1
                    else:
                        count[codon] = 1
        header=line
        seq_lines=[]
        
    else:
        seq_lines.append(line)
if header:
           seq=''.join(seq_lines)
           matches = re.findall(rf'(?=(ATG(?:...)*?{stop_codon}))', seq)
           if matches:
              largest_match=max(matches, key=len)
              coding_part=largest_match[:-3]
              for i in range(0, len(coding_part), 3):
                    codon=coding_part[i:i+3]
                    if codon in count:
                        count[codon] += 1
                    else:
                        count[codon] = 1
input_file.close()

import matplotlib.pyplot as plt
labels = list(count.keys())
sizes = list(count.values())
plt.figure(figsize=(10, 10))
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title(f'Codon frequency upstream of {stop_codon}')
plt.savefig(f'codon_frequency_{stop_codon}.png')
plt.close()

