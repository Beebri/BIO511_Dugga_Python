#part 2
import csv
import pandas as pd
import matplotlib.pyplot as plt
#2.1
df = pd.read_csv('CNV_log2_skin_melanoma.csv')

#2.2
import practice_dugga_func as pdf
chr_ordered = pdf.orderChromosomes()
print("chr_ordered made")
#2.3
import matplotlib.pyplot as plt
plt.scatter(df['chromosome'], df['cnv_log2'], xunits=chr_ordered)
plt.title('Chromosome vs CNV')
plt.xlabel('Chromosome')
plt.ylabel('CNV')
plt.savefig('chrom_cnv.png')
    

    
        


