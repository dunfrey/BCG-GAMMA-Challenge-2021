from collections import Counter

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


def inspect(df):
    print('shape:', df.shape)
    print('columns:', df.columns.tolist())
    display(df.head())

    return df


def replace_accents(word):
    repl = {
        'à': 'a', 'á': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a', 'å': 'a', 'ã': 'a',
        'è': 'e', 'é': 'e', 'ê': 'e', 'ë': 'e',
        'ì': 'i', 'í': 'i', 'î': 'i', 'ï': 'i',
        'ò': 'o', 'ó': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o',
        'ù': 'u', 'ú': 'u', 'ü': 'u', 'û': 'u',
        'ý': 'y', 'ÿ': 'y',
        'ç': 'c'        
    }

    new_word = ''.join([repl[c] if c in repl else c for c in word])
    return new_word


def rank(df, feature_col, n=None, ascending=False):

    return df.sort_values(feature_col, ascending=ascending).head(n)


def plot_bar(df, x, y, rotation=90, palette="Blues_d"):
    sns.barplot(x=x, y=y, data=df, palette=palette)

    plt.xticks(rotation=rotation)
    plt.tight_layout()


def underscore_to_camelcase(word):
    '''
    https://stackoverflow.com/questions/40454141/capitalize-first-letter-only-of-a-string-in-python
    '''
    if '_' in word:
        word = ''.join(x.capitalize() or '_' for x in word.split('_'))
        return word[0].lower() + word[1:]

    return word


def strat_sample_from_base_dist(df, base_df, target_col):
    '''
    Generate stratified sample from a dataframe based on the distribuition of `base_df[target_col]`
    '''
    target_col_dist = Counter(base_df[target_col])

    partial_sample_dfs = []

    # pra cada faixaPopulacaoEstimada de municipios mais violentos, gerar mesmo numero de sample...
    for label, label_size in target_col_dist.items():
        _sample_df = df[(df[target_col] == label)]

        if len(_sample_df) > label_size:
            _sample_df = _sample_df.iloc[0:label_size]

        partial_sample_dfs.append(_sample_df)

    sample_df = pd.concat(partial_sample_dfs)

    return sample_df
