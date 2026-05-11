input_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')

stop_codon = input('Please input a stop codon (TAA/TAG/TGA): ')
while stop_codon not in ['TAA', 'TAG', 'TGA']:
    print('Invalid input. Please enter a valid stop codon (TAA/TAG/TGA).')
    stop_codon = input('Please input a stop codon (TAA/TAG/TGA): ')

header = ''
seq_lines = []
count = {}

all_stops = ['TAA', 'TAG', 'TGA']

def longest_orf_for_stop(seq, target_stop):
    best_orf = ''

    # try every possible ATG
    for start in range(len(seq) - 2):
        if seq[start:start+3] == 'ATG':
            # scan forward in the same frame
            for i in range(start + 3, len(seq) - 2, 3):
                codon = seq[i:i+3]

                # ORF ends at the first in-frame stop codon
                if codon in all_stops:
                    if codon == target_stop:
                        orf = seq[start:i+3]
                        if len(orf) > len(best_orf):
                            best_orf = orf
                    break

    return best_orf


for line in input_file:
    line = line.strip()

    if line.startswith('>'):
        if header:
            seq = ''.join(seq_lines)
            best_orf = longest_orf_for_stop(seq, stop_codon)

            if best_orf:
                coding_part = best_orf[:-3]   # remove stop codon
                for i in range(0, len(coding_part), 3):
                    codon = coding_part[i:i+3]
                    if codon in count:
                        count[codon] += 1
                    else:
                        count[codon] = 1

        header = line
        seq_lines = []

    else:
        seq_lines.append(line)

# process last gene
if header:
    seq = ''.join(seq_lines)
    best_orf = longest_orf_for_stop(seq, stop_codon)

    if best_orf:
        coding_part = best_orf[:-3]
        for i in range(0, len(coding_part), 3):
            codon = coding_part[i:i+3]
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

