df2_piv = pd.pivot_table(df2, index='ProspectID', columns=['Activity'], aggfunc=np.size, fill_value=0)

df2_piv.reset_index(inplace=True)

df2_grp = df2_piv.groupby('ProspectID').sum()