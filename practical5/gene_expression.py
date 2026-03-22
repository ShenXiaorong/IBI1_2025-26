genes={'TP53': 12.4, 'EGFR': 15.1, 'BRCA1': 8.2, 'PTEN': 5.3, 'ESR1': 10.7}
print('Genes:', genes)
genes['MYC']=11.6
import matplotlib.pyplot as plt
import numpy as np
labels = list(genes.keys())
values = list(genes.values())
ind = np.arange(len(labels))
plt.bar(ind, values)
plt.xticks(ind, labels)
plt.ylabel('Expression Level')
plt.title('Gene Expression Levels')
plt.xticks(ind, ('TP53', 'EGFR', 'BRCA1', 'PTEN', 'ESR1', 'MYC'))
plt.yticks(np.arange(0, 16, 2))
plt.show()
gene_of_interest='EGFR' # CHANGE THIS VALUE TO TEST DIFFERENT GENES
if gene_of_interest in genes:
    print(f"Expression level of {gene_of_interest}: {genes[gene_of_interest]}")
else:
    print("Gene not found")
average = sum(genes.values()) / len(genes)
print('Average expression level:', average)

