def eliminaDecimales(df, col):
    df[col + "_sin_decimales"] = df[col].astype(int) # convertim a tipus enter aíxi no tenim decimals i aquesta expressió trunca no arrodoneix
    return df


def calculaRatio(df, col1, col2):
    try:
        ratio = df[col1] / df[col2] # això és una columna amb els ratios per a cada observació
        if (ratio > 1).any(): # any() mira si hi ha al manco 1 observació
            print("Hi ha algun valor major que 1")
        return ratio
    except:
        print("Error!") # col2 pot tenir alguna observació que sigui 0!
    


