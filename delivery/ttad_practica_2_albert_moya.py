def eliminaDecimales(df, col):
    df[col + "_sin_decimales"] = df[col].astype(int) # convertim a tipus enter aíxi no tenim decimals i aquesta expressió trunca no arrodoneix
    return df





