
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
