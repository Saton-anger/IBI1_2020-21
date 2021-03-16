import matplotlib.pyplot as plt
import numpy as np
gene_lengths = [9410, 394141, 4442, 105338, 19149, 76779, 126550, 36296, 842, 15981]
exon_counts = [51, 1142, 42, 216, 25, 650, 32533, 57, 1, 523]
exon_counts.sort()
eal = np.array(exon_counts) * 3  # eal means exon average length
print(eal)
plt.boxplot(eal,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=type,
            notch=False
            )
plt.show()