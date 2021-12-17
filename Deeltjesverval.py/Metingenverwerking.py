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

# horizontaal
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
plt.plot(loca, MAXVERSTAPPEN, "r.")
plt.errorbar(loca, MAXVERSTAPPEN, fmt="r--", xerr=(0.3), yerr=1.25, ecolor="k")
plt.show()

# 30 graden
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
plt.plot(locaR, MAXVERSTAPPENR, "r.")
plt.errorbar(locaR, MAXVERSTAPPENR, fmt="r--", xerr=0.5, yerr=1.25, ecolor="k")
plt.show()

# 50 graden!
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
plt.plot(locaS, MAXVERSTAPPENS, "r.")
plt.errorbar(locaS, MAXVERSTAPPENS, fmt="r--", xerr=0.5, yerr=1.25, ecolor="k")
plt.show()

# verticaal
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
plt.plot(locaT, MAXVERSTAPPENT, "r.")
plt.errorbar(locaT, MAXVERSTAPPENT, fmt="r--", xerr=0.75, yerr=1.25, ecolor="k")
plt.show()

xht_1 = []
xht_2 = []
xht_3 = []
xht_4 = []
yht = []
xhterr = []
yhterr = []
for waarde in np.arange(0, 19.5, 0.5):
    xht_1.append(28 - 5.5)
    xht_2.append(28 - 11.0)
    xht_3.append(28 - 12.0)
    xht_4.append(28 - 27.0)
    yht.append(waarde)
    xhterr.append(0.3)
    yhterr.append(1.25)

x30 = []
x30err = []
y30 = []
y30err = []
for waarde in np.arange(23, 29.5, 0.5):
    x30.append(28 - waarde)
    x30err.append(0.5)
    y30.append(np.tan(0.6) * (waarde - 23))
    y30err.append(1.25)

x50_1 = []
x50_1err = []
y50_1 = []
y50_1err = []
for waarde in np.arange(0, 15.5, 0.5):
    x50_1.append(28 - waarde)
    x50_1err.append(0.5)
    y50_1.append(np.tan(0.82) * (15 - waarde))
    y50_1err.append(1.25)

x50_2 = []
x50_2err = []
y50_2 = []
y50_2err = []
for waarde in np.arange(0, 27.5, 0.5):
    x50_2.append(28 - waarde)
    x50_2err.append(0.5)
    y50_2.append(np.tan(0.82) * (27 - waarde))
    y50_2err.append(1.25)

yvc_1 = []
yvc_2 = []
yvc_3 = []
yvc_4 = []
xvc = []
yvcerr = []
xvcerr = []
for waarde in np.arange(0, 29.5, 0.5):
    yvc_1.append(3.75)
    yvc_2.append(10.0)
    yvc_3.append(12.50)
    yvc_4.append(18.75)
    yvcerr.append(0.75)
    xvc.append(waarde)
    xvcerr.append(1.25)


plt.plot(
    xht_1,
    yht,
    "k",
    xht_2,
    yht,
    "k",
    xht_4,
    yht,
    "k",
    x30,
    y30,
    "k",
    x50_1,
    y50_1,
    "k",
    x50_2,
    y50_2,
    "k",
    xvc,
    yvc_1,
    "k",
    xvc,
    yvc_4,
    "k",
    xvc,
    yvc_3,
    "k",
)
plt.xlim(0, 29)
plt.xlabel("X, (cm)")
plt.ylim(0, 19)
plt.ylabel("Y, (cm)")
plt.savefig("patient_1.png")

plt.plot(
    xht_1,
    yht,
    "k",
    xht_2,
    yht,
    "k",
    xht_3,
    yht,
    "k",
    xht_4,
    yht,
    "k",
    x30,
    y30,
    "k",
    x50_1,
    y50_1,
    "k",
    x50_2,
    y50_2,
    "k",
    xvc,
    yvc_1,
    "k",
    xvc,
    yvc_2,
    "k",
    xvc,
    yvc_3,
    "k",
    xvc,
    yvc_4,
    "k",
)
plt.xlim(0, 29)
plt.xlabel("X, (cm)")
plt.ylim(0, 19)
plt.ylabel("Y, (cm)")
plt.savefig("patient_2.png")
