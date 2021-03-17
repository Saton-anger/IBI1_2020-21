import matplotlib.pyplot as plt
import numpy as np
glen = [9410, 394141, 4442, 105338, 19149, 76779, 126550, 36296, 842, 15981]  # glen means gene length
ec = [51, 1142, 42, 216, 25, 650, 32533, 57, 1, 523]  # ec means exon counts
aver = []
for i in range(len(glen)):
    aver.append(glen[i]/ec[i])
aver = sorted(aver)
print('sorted values:', aver)
