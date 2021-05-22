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
