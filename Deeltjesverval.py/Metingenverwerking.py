import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df_X_orientatie = pd.DataFrame(
    [
        [0, "weinig"],
        [2.5, "weinig"],
        [5, "veel"],
        [7.5, "weinig"],
        [10, "redelijk"],
        [12.5, "redelijk"],
        [15, "weinig"],
        [17.5, "weinig"],
        [20, "weinig"],
        [22.5, "weinig"],
        [25, "weinig"],
        [27.5, "redelijk"],
        [29.5, "vrij weinig"],
    ],
    columns=["afstand (cm)", "relatief activiviteit"],
)
# print(df_X_orientatie)

MAXVERSTAPPEN = []
loca = []
N = []

for O in np.arange(2.5, 8, 0.5):
    dfO = pd.read_csv(f"metingen_pet/spectrum_{O}.csv")
    a = dfO["counts_ch_B"]
    N.append(len(np.sqrt(a)))
    top_4_idx = np.argsort(a)[-4:]
    MAXVERSTAPPEN.append(np.mean([a[i] for i in top_4_idx]))
    loca.append(O)


for P in np.arange(8, 15.5, 0.5):
    dfP = pd.read_csv(f"metingen_pet/spectrum_{P}.csv")
    a = dfP["counts_ch_B"]
    N.append(len(np.sqrt(a)))
    top_4_idx = np.argsort(a)[-4:]
    MAXVERSTAPPEN.append(np.mean([a[i] for i in top_4_idx]))
    loca.append(P)


for Q in np.arange(25, 29.5, 0.5):
    dfQ = pd.read_csv(f"metingen_pet/spectrum_{Q}.csv")
    a = dfQ["counts_ch_B"]
    N.append(len(np.sqrt(a)))
    top_4_idx = np.argsort(a)[-4:]
    MAXVERSTAPPEN.append(np.mean([a[i] for i in top_4_idx]))
    loca.append(Q)

df = pd.DataFrame(MAXVERSTAPPEN, loca)
print(df)
# plt.errorbar(loca, MAXVERSTAPPEN, xerr=2.75, yerr=None)
# plt.show()

MAXVERSTAPPENR = []
locaR = []
NR = []
for R in range(0, 12):
    dfR = pd.read_csv(f"metingen_pet_30/spectrum_30.{R}.csv")
    a = dfR["counts_ch_B"]
    NR.append(len(np.sqrt(a)))
    top_4_idx = np.argsort(a)[-4:]
    MAXVERSTAPPENR.append(np.mean([a[i] for i in top_4_idx]))
    locaR.append(R)
dfR = pd.DataFrame(MAXVERSTAPPENR, locaR)
print(dfR)
# plt.errorbar(locaR, MAXVERSTAPPENR, xerr=2.75, yerr=None)
# plt.show()

MAXVERSTAPPENS = []
locaS = []
NS = []
for S in range(0, 23):
    dfS = pd.read_csv(f"metingen_pet_50/spectrum_50.{S}.csv")
    a = dfS["counts_ch_B"]
    NS.append(len(np.sqrt(a)))
    top_4_idx = np.argsort(a)[-4:]
    MAXVERSTAPPENS.append(np.mean([a[i] for i in top_4_idx]))
    locaS.append(S)
dfS = pd.DataFrame(MAXVERSTAPPENS, locaS)
print(dfS)
# plt.errorbar(locaS, MAXVERSTAPPENS, xerr=2.75, yerr=None)
# plt.show()

MAXVERSTAPPENT = []
locaT = []
NT = []
for T in np.arange(0, 21.25, 1.25):
    dfT = pd.read_csv(f"metingen_pet_vert/spectrum_ver_{T}.csv")
    a = dfT["counts_ch_B"]
    top_4_idx = np.argsort(a)[-4:]
    MAXVERSTAPPENT.append(np.mean([a[i] for i in top_4_idx]))
    locaT.append(T)
dfT = pd.DataFrame(MAXVERSTAPPENT, locaT)
print(dfT)
plt.errorbar(locaT, MAXVERSTAPPENT, xerr=np.sqrt(2.25), yerr=None)
plt.show()
