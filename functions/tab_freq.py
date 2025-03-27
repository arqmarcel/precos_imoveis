def tab_freq(df, col):
    tab_freq = df[col].value_counts().reset_index()
    tab_freq.columns = [col, 'Frequência_Absoluta']

    # Freq. Relativa
    tab_freq['Frequência_Relativa'] = (100 * (tab_freq['Frequência_Absoluta'] / tab_freq['Frequência_Absoluta'].sum())).round(2)
    
    # Contagem Acumulada
    tab_freq['Frequência_Acumulada'] = tab_freq['Frequência_Absoluta'].cumsum()

    # Percentual Acumulado
    tab_freq['% Acumulado'] = tab_freq['Frequência_Relativa'].cumsum().round(2)

    return tab_freq