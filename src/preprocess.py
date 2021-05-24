from utils import *
import re

def generates_normalized_column(df, column_to_normalize, column_normalized):
    df[column_to_normalize] = df[column_to_normalize].astype(str)
    df[column_normalized] = df[column_to_normalize].apply(replace_accents)
    df[column_normalized] = df[column_normalized].apply(lambda x: re.sub(r"[^a-zA-Z\d\_]+", " ", x))
    df[column_normalized] = df[column_normalized].str.upper()
    return df


def keep_last_date(df, column_dates):
    return df[df[column_dates] == df[column_dates].max()]


def plot_grouped_df(df_grouped, xlabel, ylabel, figsize=(8,5), rot=0):
    ax = (df_grouped
      .count()
      .plot(kind='bar',
            figsize=figsize,
            rot=rot, 
            grid=True))

    ax.set_ylabel(xlabel);
    ax.set_xlabel(ylabel);

    for p in ax.patches:
        ax.annotate(p.get_height(), (p.get_x(), p.get_height() + 200))
