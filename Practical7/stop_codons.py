input=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
output=open('stop_genes.fa', 'w')
header=''
seq_lines=[]
import re
for line in input:
    line=line.strip()
    if line.startswith('>'):
        if header:
           seq=''.join(seq_lines)
           gene_name = header.split()[0][1:]
           matches = re.findall(r'(?=(ATG(?:...)*?(TAA|TAG|TGA)))', seq)
           found_stops = set()
           for match in matches:
               stop = match[1]
               found_stops.add(stop)
           if found_stops:
                stop_list = ','.join(sorted(found_stops))
                output.write(f'>{gene_name};{stop_list}\n')
                for i in range(0, len(seq), 80):
                      output.write(seq[i:i+80] + '\n')
        header=line
        seq_lines=[]
        
    else:
        seq_lines.append(line)

if header:
    seq = ''.join(seq_lines)
    gene_name = header.split()[0][1:]
    matches = re.findall(r'(?=(ATG(?:...)*?(TAA|TAG|TGA)))', seq)
    found_stops = set()
    for match in matches:
        stop = match[1]
        found_stops.add(stop)
    if found_stops:
        stop_list = ','.join(sorted(found_stops))
        output.write(f'>{gene_name};{stop_list}\n')
        for i in range(0, len(seq), 80):
            output.write(seq[i:i+80] + '\n')
input.close()
output.close()
