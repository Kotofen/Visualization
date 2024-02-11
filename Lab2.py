import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from  ChernoffFace import *


dfp = pd.read_csv("Puromycin.csv")

dfp2 = dfp
dfp2["state"] = dfp2["state"].replace("treated", 1)
dfp2["state"] = dfp2["state"].replace("untreated", 0)
dfp2 = variables_rescale(dfp)
fig = chernoff_face(data=dfp2, n_columns=6,
                    titles=[str(x) for x in list(range(len(dfp)))],
                    color_mapper=matplotlib.cm.Pastel1)
fig.tight_layout()
plt.show()

pd.plotting.andrews_curves(dfp, 'state', colormap=matplotlib.cm.Dark2)
plt.show()