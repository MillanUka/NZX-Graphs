import matplotlib.pyplot as plt
import numpy as np


sx = markets[0]
dx = markets[1]
zx = markets[2]

sxCapitalisationSorted = sorted(sx, key=lambda x : x[6], reverse=True)

topTenSxCapitalisation = []
topTenSxCapitalisationCodes = []
for i in range(0, 10):
    topTenSxCapitalisation.append(sxCapitalisationSorted[i][6])
    topTenSxCapitalisationCodes.append(sxCapitalisationSorted[i][0])
    
x = np.arange(10)

plt.bar(x, topTenSxCapitalisation)
plt.xticks(x, topTenSxCapitalisationCodes)
plt.xlabel("Code")
plt.ylabel("Capitalisation")
plt.title("NZSX Top ten Instruments by Capitalisation")

plt.show()
dxOustandingSorted = sorted(dx, key=lambda x : x[6], reverse=True)

topTenDxOustanding = []
topTenDxOustandingCodes = []
for i in range(0, 10):
        topTenDxOustanding.append(dxOustandingSorted[i][6])
        topTenDxOustandingCodes.append(dxOustandingSorted[i][0])

plt.bar(x, topTenDxOustanding)
plt.xticks(x, topTenDxOustandingCodes)
plt.xlabel("Code")
plt.ylabel("Oustanding")
plt.title("NZSX Top ten Instruments by Debt")
plt.show()