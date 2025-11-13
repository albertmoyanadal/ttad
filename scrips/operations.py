def normalize(df, col):
    df_norm = df.copy()
    df_norm[col] = (df_norm[col] - df_norm[col].mean()) / df_norm[col].std()

    return df_norm




