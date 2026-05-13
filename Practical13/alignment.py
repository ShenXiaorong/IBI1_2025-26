seq1	=	'MTGVFDRRVPSIRSGDFQAPFQTSAAMHHPSQESPTLPESSATDSDYYSPTGGAPHGYCSPTSASYGKALNPYQYQYHGVNGSAGSYPAKAYADYSYASSYHQYGGAYNRVPSATNQPEKEVTEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYTSAASSINSHLPPPGSLQHPLALASGTLY'	
seq2	=	"MTGVFDRRVPSIRSGDFQAPFPTSAAMHHPSQESPTLPESSATDSDYYSPAGAAPHGYCSPTSASYGKALNPYQYQYHGVNGSAAGYPAKAYADYGYASPYHQYGGAYNRVPSATSQPEKEVAEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYPSAASSINSHLPPPGSLQHPLALASGTLY"	
seq3    =   'HRWVQMVFNIARSTAMAIMHYFWDNWADQAWAAPIFEFCCAPSQEPHDEQHYEMYCITIKDNGRPCTKRYDETFYHMGKGEVYACTQSYKNCCHKAHAGLRCHVFFQTPEQILQIRSSFRNCLILRPVKYWRFCSMHFHCDHKQCWATAKKEDSNVCAAFACYEVGNALHSRRGMDWYYVNQHQAPVGWTDYMSAPTTRNRQQDSEAWSRPKLQQSCLKPPANHVEDDFIERPEWWTPIIFPPYLKYGYHQPYIQYEFMMAYIRCNVCFPCELPPDIFRPELIRVSGEV'
edit_distance	=	0		
#set	initial	distance	as	zero	
for	i	in	range(len(seq1)):	#compare	each	amino	acid	
  if	seq1[i]!=seq2[i]:				
    edit_distance	+=	1	#add	a	score	1	if	amino	acids	are	different		
identical_percentage    =	(1-(edit_distance/len(seq1)))*100	#calculate	the	percentage	of	identical	residues
print	("alignment score for human and mouse sequences: {}".format(edit_distance))
print	("Identical percentage for human and mouse sequences: {:.2f}%".format(identical_percentage))

edit_distance	=	0		
#set	initial	distance	as	zero	
for	i	in	range(len(seq1)):	#compare	each	amino	acid	
  if	seq1[i]!=seq3[i]:				
    edit_distance	+=	1	#add	a	score	1	if	amino	acids	are	different		
identical_percentage    =	(1-(edit_distance/len(seq1)))*100	#calculate	the	percentage	of	identical	residues
print	("alignment score for human and random sequences: {}".format(edit_distance))    
print	("Identical percentage for human and random sequences: {:.2f}%".format(identical_percentage))

edit_distance	=	0		
#set	initial	distance	as	zero	
for	i	in	range(len(seq1)):	#compare	each	amino	acid	
  if	seq2[i]!=seq3[i]:				
    edit_distance	+=	1	#add	a	score	1	if	amino	acids	are	different		
identical_percentage    =	(1-(edit_distance/len(seq2)))*100	#calculate	the	percentage	of	identical	residues
print	("alignment score for mouse and random sequences: {}".format(edit_distance))
print	("Identical percentage for mouse and random sequences: {:.2f}%".format(identical_percentage))

