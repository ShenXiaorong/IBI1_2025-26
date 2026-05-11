input_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
output_file = open('stop_genes.fa', 'w')

header = ''
seq_lines = []

for line in input_file:
    line = line.strip()

    if line.startswith('>'):
        if header:
            seq = ''.join(seq_lines)
            gene_name = header.split()[0][1:]

            start_pos = seq.find('ATG')
            found_stops = set()

            if start_pos != -1:
                for i in range(start_pos + 3, len(seq) - 2, 3):
                    codon = seq[i:i+3]
                    if codon in ['TAA', 'TAG', 'TGA']:
                        found_stops.add(codon)

            if found_stops:
                stop_list = ','.join(sorted(found_stops))
                output_file.write(f'>{gene_name};{stop_list}\n')
                for i in range(0, len(seq), 80):
                    output_file.write(seq[i:i+80] + '\n')

        header = line
        seq_lines = []

    else:
        seq_lines.append(line)

# process the last gene
if header:
    seq = ''.join(seq_lines)
    gene_name = header.split()[0][1:]

    start_pos = seq.find('ATG')
    found_stops = set()

    if start_pos != -1:
        for i in range(start_pos + 3, len(seq) - 2, 3):
            codon = seq[i:i+3]
            if codon in ['TAA', 'TAG', 'TGA']:
                found_stops.add(codon)

    if found_stops:
        stop_list = ','.join(sorted(found_stops))
        output_file.write(f'>{gene_name};{stop_list}\n')
        for i in range(0, len(seq), 80):
            output_file.write(seq[i:i+80] + '\n')

input_file.close()
output_file.close()