import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
import seaborn.objects as so

df = pd.read_csv('coords.csv')
df.columns = df.columns.str.strip()
df['time'] = pd.to_datetime(df['time'], errors='coerce')
df['time'] = df['time'].dt.hour

def individual_plot():
    g = sns.FacetGrid(df, col="user", col_wrap=4, height=3)
    g.map(sns.histplot, "time", bins=24, kde=True)
    plt.show()

def combined_plot():
    sns.histplot(data=df, x="time",hue="user", bins=24, kde=True, )
    plt.show()

def average_plot():
    sns.histplot(data=df, x="time", bins=24, kde=True)
    plt.show()

