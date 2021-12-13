import pandas as pd
import math
import statistics
import matplotlib.pyplot as plt
import numpy as np
from lmfit import models

constants = {"labda": 632.8 * 10 ** -9}


def interferentieafstand(gl, hkn):
    teller = gl
    noemer = 1.33 * 2 * (np.sin(hkn))
    return teller / noemer


def afstand(hoek, afstand):
    """Berekend de positie in een buis met water.
    Args:
        hoek (float): De hoek gemeten in lucht.
        afstand (float): De afstand tot het midden van de buis in lucht.

    Returns:
        float: De positie ten opzichte van het midden van de buis
    """
    hoekinwater = np.sin(hoek) / 1.33
    plek = 1.5 - afstand
    T = plek * np.tan(hoek)
    N = np.tan(hoekinwater)
    return (T / N) + 1.5


def hoek(d, r):
    """Berekend de hoek van de LDA opstelling met een lege buis.

    args:
    d (int): The distance between the crossingpoint and the measuring point of r.
    r (int): The distance between the laser bursts at a distance d from the crossingpoint of the laser."""
    tant = r / (2 * d)
    t = math.atan(tant)
    return t


def lengte(waarde, q):
    """Maakt een lijst met dezelfde x waarde voor het aantal y waarden.

    args:
    waarde (float): De waarden voor die in de lijst moet komen.
    q (int): De lengte van de y-waarden.
    """
    lijst = []
    for i in range(0, q):
        lijst.append(waarde)
    return lijst


# metingen dag 1

# berekening van de hoek zonder waterbuis:
afstand_d_1 = [70, 190]
afstand_r_1 = [19, 51]
lensafstand_1 = 125
hoeken_1 = []
for idx, q in enumerate(afstand_d_1):
    hoeken_1.append(hoek(q, afstand_r_1[idx]))
hoek_1 = statistics.mean(hoeken_1)

d_1 = interferentieafstand(constants["labda"], hoek_1)
sigma_noemer = 2 * np.sqrt(2000 * np.log(2))

# ruwe metingen: _=-, __=+

df_00_1 = pd.DataFrame(
    [
        [15301, 1153],
        [15453, 1240],
        [15425, 1172],
    ],
    columns=["frequentie", "fwhm"],
)
df_00_1["positie"] = afstand(hoek_1, 0)
df_00_1["snelheid"] = d_1 * df_00_1["frequentie"]
df_00_1["sigma_freq"] = df_00_1["fwhm"] / sigma_noemer
df_00_1["sigma"] = d_1 * df_00_1["sigma_freq"]
mean_00_1 = statistics.mean(df_00_1["snelheid"])
std_00_1 = statistics.stdev(df_00_1["snelheid"]) / np.sqrt(len(df_00_1["snelheid"]))
sig_00_1 = statistics.mean(df_00_1["sigma"])
# print(df_00_1)

df_25_1 = pd.DataFrame(
    [
        [15072, 1544],
        [15036, 1658],
        [15080, 1451],
    ],
    columns=["frequentie", "fwhm"],
)
df_25_1["positie"] = afstand(hoek_1, 2.5)
df_25_1["snelheid"] = d_1 * df_25_1["frequentie"]
df_25_1["sigma_freq"] = df_25_1["fwhm"] / sigma_noemer
df_25_1["sigma"] = d_1 * df_25_1["sigma_freq"]
mean_25_1 = statistics.mean(df_25_1["snelheid"])
std_25_1 = statistics.stdev(df_25_1["snelheid"]) / np.sqrt(len(df_25_1["snelheid"]))
sig_25_1 = statistics.mean(df_25_1["sigma"])
# print(df_25_1)

df_50_1 = pd.DataFrame(
    [
        [13511, 2149],
        [13805, 1966],
        [13484, 2168],
        [13524, 2497],
        [13632, 2475],
    ],
    columns=["frequentie", "fwhm"],
)
df_50_1["positie"] = afstand(hoek_1, -5)
df_50_1["snelheid"] = d_1 * df_50_1["frequentie"]
df_50_1["sigma_freq"] = df_50_1["fwhm"] / sigma_noemer
df_50_1["sigma"] = d_1 * df_50_1["sigma_freq"]
mean_50_1 = statistics.mean(df_50_1["snelheid"])
std_50_1 = statistics.stdev(df_50_1["snelheid"]) / np.sqrt(len(df_50_1["snelheid"]))
sig_50_1 = statistics.mean(df_50_1["sigma"])
# print(df_50_1)

df__25_1 = pd.DataFrame(
    [
        [14845, 1520],
        [14995, 1890],
        [14868, 1607],
    ],
    columns=["frequentie", "fwhm"],
)
df__25_1["positie"] = afstand(hoek_1, 2.5)
df__25_1["snelheid"] = d_1 * df__25_1["frequentie"]
df__25_1["sigma_freq"] = df__25_1["fwhm"] / sigma_noemer
df__25_1["sigma"] = d_1 * df__25_1["sigma_freq"]
mean__25_1 = statistics.mean(df__25_1["snelheid"])
std__25_1 = statistics.stdev(df__25_1["snelheid"]) / np.sqrt(len(df__25_1["snelheid"]))
sig__25_1 = statistics.mean(df_25_1["sigma"])
# print(df__25_1)


# metingen dag 2

# berekening van de hoek zonder waterbuis:
afstand_d_2 = [78, 198]
afstand_r_2 = [11.5, 28]
lensafstand_2 = 133
hoeken_2 = []
for idx, q in enumerate(afstand_d_2):
    hoeken_2.append(hoek(q, afstand_r_2[idx]))
hoek_2 = statistics.mean(hoeken_2)

d_2 = interferentieafstand(constants["labda"], hoek_2)

# print(d_2)

df_00_2 = pd.DataFrame(
    [
        [7567, 804],
        [7634, 874],
    ],
    columns=["frequentie", "fwhm"],
)
df_00_2["positie"] = afstand(hoek_2, 0)
df_00_2["snelheid"] = d_2 * df_00_2["frequentie"]
df_00_2["sigma_freq"] = df_00_2["fwhm"] / sigma_noemer
df_00_2["sigma"] = d_1 * df_00_2["sigma_freq"]
mean_00_2 = statistics.mean(df_00_2["snelheid"])
std_00_2 = statistics.stdev(df_00_2["snelheid"]) / np.sqrt(len(df_00_2["snelheid"]))
sig_00_2 = statistics.mean(df_00_2["sigma"])
# print(df_00_2)

df__50_2 = pd.DataFrame(
    [
        [3305, 962],
        [3406, 1035],
        [3318, 890],
        [3266, 745],
        [3322, 746],
        [3297, 815],
    ],
    columns=["frequentie", "fwhm"],
)
df__50_2["positie"] = afstand(hoek_2, 5)
df__50_2["snelheid"] = d_2 * df__50_2["frequentie"]
df__50_2["sigma_freq"] = df__50_2["fwhm"] / sigma_noemer
df__50_2["sigma"] = d_1 * df__50_2["sigma_freq"]
mean__50_2 = statistics.mean(df__50_2["snelheid"])
std__50_2 = statistics.stdev(df__50_2["snelheid"]) / np.sqrt(len(df__50_2["snelheid"]))
sig__50_2 = statistics.mean(df__50_2["sigma"])
# print(df__50_2)

df__60_2 = pd.DataFrame(
    [
        [2609, 757],
        [2276, 840],
        [2365, 839],
        [2338, 836],
        [2283, 895],
    ],
    columns=["frequentie", "fwhm"],
)
df__60_2["positie"] = afstand(hoek_2, 6)
df__60_2["snelheid"] = d_2 * df__60_2["frequentie"]
df__60_2["sigma_freq"] = df__60_2["fwhm"] / sigma_noemer
df__60_2["sigma"] = d_1 * df__60_2["sigma_freq"]
mean__60_2 = statistics.mean(df__60_2["snelheid"])
std__60_2 = statistics.stdev(df__60_2["snelheid"]) / np.sqrt(len(df__60_2["snelheid"]))
sig__60_2 = statistics.mean(df__60_2["sigma"])
# print(df__60_2)

df__25_2_1 = pd.DataFrame(
    [
        [3268, 971],
        [3267, 974],
        [3293, 917],
    ],
    columns=["frequentie", "fwhm"],
)
df__25_2_1["positie"] = afstand(hoek_2, 2.5)
df__25_2_1["snelheid"] = d_2 * df__25_2_1["frequentie"]
df__25_2_1["sigma_freq"] = df__25_2_1["fwhm"] / sigma_noemer
df__25_2_1["sigma"] = d_1 * df__25_2_1["sigma_freq"]
mean__25_2_1 = statistics.mean(df__25_2_1["snelheid"])
std__25_2_1 = statistics.stdev(df__25_2_1["snelheid"]) / np.sqrt(
    len(df__25_2_1["snelheid"])
)
sig__25_2_1 = statistics.mean(df__25_2_1["sigma"])
# print(df__25_2_1)

df__25_2_2 = pd.DataFrame(
    [
        [6913, 1815],
        [6745, 1750],
        [6816, 1677],
    ],
    columns=["frequentie", "fwhm"],
)
df__25_2_2["positie"] = afstand(hoek_2, 2.5)
df__25_2_2["snelheid"] = d_2 * df__25_2_2["frequentie"]
df__25_2_2["sigma_freq"] = df__25_2_2["fwhm"] / sigma_noemer
df__25_2_2["sigma"] = d_1 * df__25_2_2["sigma_freq"]
mean__25_2_2 = statistics.mean(df__25_2_2["snelheid"])
std__25_2_2 = statistics.stdev(df__25_2_2["snelheid"]) / np.sqrt(
    len(df__25_2_2["snelheid"])
)
sig__25_2_2 = statistics.mean(df__25_2_2["sigma"])
# print(df__25_2_2)

df_25_2 = pd.DataFrame(
    [
        [7890, 658],
        [7779, 820],
        [7754, 743],
    ],
    columns=["frequentie", "fwhm"],
)
df_25_2["positie"] = afstand(hoek_2, -2.5)
df_25_2["snelheid"] = d_2 * df_25_2["frequentie"]
df_25_2["sigma_freq"] = df_25_2["fwhm"] / sigma_noemer
df_25_2["sigma"] = d_1 * df_25_2["sigma_freq"]
mean_25_2 = statistics.mean(df_00_2["snelheid"])
std_25_2 = statistics.stdev(df_00_2["snelheid"]) / np.sqrt(len(df_00_2["snelheid"]))
sig_25_2 = statistics.mean(df_25_2["sigma"])
# print(df_25_2)

df_50_2 = pd.DataFrame(
    [
        [7632, 932],
        [7489, 1219],
        [7629, 843],
    ],
    columns=["frequentie", "fwhm"],
)
df_50_2["positie"] = afstand(hoek_2, -5)
df_50_2["snelheid"] = d_2 * df_50_2["frequentie"]
df_50_2["sigma_freq"] = df_50_2["fwhm"] / sigma_noemer
df_50_2["sigma"] = d_1 * df_50_2["sigma_freq"]
mean_50_2 = statistics.mean(df_50_2["snelheid"])
std_50_2 = statistics.stdev(df_50_2["snelheid"]) / np.sqrt(len(df_50_2["snelheid"]))
sig_50_2 = statistics.mean(df_50_2["sigma"])
# print(df_50_2)

mean_00 = (mean_00_1 + mean_00_2) / 2
mean__25 = (mean__25_1 + mean__25_2_2) / 2
mean_25 = (mean_25_1 + mean_25_2) / 2
mean_50 = (mean_50_1 + mean_50_2) / 2

err_00 = np.sqrt(std_00_1 ** 2 + sig_00_1 ** 2 + std_00_2 ** 2 + sig_00_2 ** 2)
err__25 = np.sqrt(std__25_1 ** 2 + sig__25_1 ** 2 + std__25_2_2 ** 2 + sig__25_2_2 ** 2)
err_25 = np.sqrt(std_25_1 ** 2 + sig_25_1 ** 2 + std_25_2 ** 2 + sig_25_2 ** 2)
err_50 = np.sqrt(std_50_1 ** 2 + sig_50_1 ** 2 + std_50_2 ** 2 + sig_50_2 ** 2)
err__50 = np.sqrt((std__50_2) ** 2 + (sig__50_2) ** 2)
err__60 = np.sqrt((std__60_2) ** 2 + (sig__60_2) ** 2)
# err = [std_50_1, std_25_1, std_00_1, std__25_1, std__50_2, std__60_2]
# print(err)

# # verwerking:
figure, axes = plt.subplots(1, 2, figsize=(20, 6))
df_00_1.plot.scatter("positie", "snelheid", yerr="sigma", c="navy", ax=axes[0])
df_25_1.plot.scatter("positie", "snelheid", yerr="sigma", c="navy", ax=axes[0])
df_50_1.plot.scatter("positie", "snelheid", yerr="sigma", c="navy", ax=axes[0])
df__25_1.plot.scatter("positie", "snelheid", yerr="sigma", c="navy", ax=axes[0])
df_00_2.plot.scatter("positie", "snelheid", yerr="sigma", c="deepskyblue", ax=axes[0])
df_50_2.plot.scatter("positie", "snelheid", yerr="sigma", c="deepskyblue", ax=axes[0])
df_25_2.plot.scatter("positie", "snelheid", yerr="sigma", c="deepskyblue", ax=axes[0])
df__60_2.plot.scatter("positie", "snelheid", yerr="sigma", c="deepskyblue", ax=axes[0])
df__50_2.plot.scatter("positie", "snelheid", yerr="sigma", c="deepskyblue", ax=axes[0])
df__25_2_1.plot.scatter("positie", "snelheid", yerr="sigma", c="r", ax=axes[0])
df__25_2_2.plot.scatter(
    "positie",
    "snelheid",
    yerr="sigma",
    c="deepskyblue",
    ax=axes[0],
    title=("(x-v) diagram, met alle losse metingen."),
)
axes[0].set_xlabel("positie (mm)")
axes[0].set_ylabel("snelheid (m/s)")


# plt.subplot(1, 3, 2)
# plt.errorbar(0, mean_00_1, yerr=err_00_1, fmt="o", c="navy")
# plt.errorbar(-2.5, mean_25_1, yerr=err_25_1, fmt="o", c="navy")
# plt.errorbar(-5.0, mean_50_1, yerr=err_50_1, fmt="o", c="navy")
# plt.errorbar(2.5, mean__25_1, yerr=err__25_1, fmt="o", c="navy")
# plt.errorbar(0, mean_00_2, yerr=err_00_2, fmt="o", c="deepskyblue")
# plt.errorbar(-5.0, mean_50_2, yerr=err_50_2, fmt="o", c="deepskyblue")
# plt.errorbar(-2.5, mean_25_2, yerr=err_25_2, fmt="o", c="deepskyblue")
# plt.errorbar(6.0, mean__60_2, yerr=err__60_2, fmt="o", c="deepskyblue")
# plt.errorbar(5.0, mean__50_2, yerr=err__50_2, fmt="o", c="deepskyblue")
# plt.errorbar(2.5, mean__25_2_1, yerr=err__25_2_1, fmt="o", c="r")
# plt.errorbar(2.5, mean__25_2_2, yerr=err__25_2_2, fmt="o", c="deepskyblue")
# plt.xlabel("positie (mm)")
# plt.ylabel("snelheid (m/s)")
# plt.title("(x-v) diagram, met gecombineerde datasets.")

plt.subplot(2, 1, 2)
plt.errorbar(0, mean_00, yerr=sig_00_2, fmt="o", c="magenta")
plt.errorbar(2.5, mean__25, yerr=sig__25_2_2, fmt="o", c="magenta")
plt.errorbar(-2.5, mean_25, yerr=sig_25_2, fmt="o", c="magenta")
plt.errorbar(-5.0, mean_50, yerr=sig_50_2, fmt="o", c="magenta")
plt.errorbar(6.0, mean__60_2, yerr=sig__60_2, fmt="o", c="magenta")
plt.errorbar(5.0, mean__50_2, yerr=sig__50_2, fmt="o", c="magenta")
plt.xlabel("positie (mm)")
plt.ylabel("snelheid (m/s)")
plt.title("(x-v) diagram, met gecombineerde metingen.")
plt.savefig("nsp2_metingen.png")


yen = [mean_50, mean_25, mean_00, mean__25, mean__50_2, mean__60_2]
xen = [-5.0, -2.5, 0, 2.5, 5.0, 6.0]

f = lambda x, a, b, x0: a + b * (x - x0) ** 2
mod_snelheid = models.Model(f, name="snelheidsprofiel")
fit = mod_snelheid.fit(yen, x=xen, a=1, b=1, x0=1)
fit.plot(numpoints=50, xlabel="positie (mm)", ylabel="snelheid (m / s)")
plt.show("nsp2_fit.png")
print(fit.fit_report())
