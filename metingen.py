import math
import statistics


def hoek(d, r):
    """berekend de hoek van de LDA opstelling met een lege buis.

    args:
    d (int): The distance between the crossingpoint and the measuring point of r.
    r (int): The distance between the laser bursts at a distance d from the crossingpoint of the laser."""
    tant = r / (2 * d)
    t = math.degrees(math.atan(tant))
    return t


# metingen dag 1

afstand_d_1 = [70, 190]
afstand_r_1 = [19, 51]
hoeken_1 = []
for idx, q in enumerate(afstand_d_1):
    hoeken_1.append(hoek(q, afstand_r_1[idx]))
hoek_1 = statistics.mean(hoeken_1)
print(hoek_1)


df_00 = [15301, 15453, 15425]
fwhm_00 = [1153, 1240, 1172]
df_25 = [15072, 15036, 15080]
fwhm_25 = [1544, 1658, 1451]
df_50 = [13511, 13805, 13484, 13524, 13632]
fwhm_50 = [2149, 1966, 2168, 2497, 2475]
df__25 = [14845, 14995, 14868]
fwhm__25 = [1520, 1890, 1607]

# metingen dag 2
