import json
import csv
from mpl_toolkits.mplot3d import Axes3D
import argparse
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sys import argv
import argparse

parser = argparse.ArgumentParser(description='JSON to CSV')
parser.add_argument('--json_path',  default=None)
args = parser.parse_args()

if not args.json_path:
    raise ValueError("No json_path provided")

with open(args.json_path, 'r') as f:
    j = json.load(f)
    sorted_j = sorted(j, key = lambda res: res[5])

    with open(args.json_path.replace('.json', '.csv'), 'w') as f2:
        c = csv.writer(f2)
        c.writerow(["index", "mesh_x","mesh_y","lm_alpha", "lm_beta", "wer", "cer"])

        for res in sorted_j:
            c.writerow([res[0], res[1], res[2], res[3], res[4], res[5], res[6]])

    print("Best params: {}".format(sorted_j[0]))

df = pd.read_csv(args.json_path.replace('.json', '.csv'), engine="python")
fig = plt.figure()
ax = Axes3D(fig)
surf = ax.plot_trisurf(df.lm_alpha.values, df.lm_beta.values, df.wer.values, cmap=matplotlib.cm.jet, linewidth=0.1)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.savefig(args.json_path.replace('.json','.png'))

