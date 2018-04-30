zips = pd.read_csv('zips', sep=',')
zips.head()
## Make sure to change the name of the object you're assigning the zip codes to:

## community zip codes:
df_ana_3 = pd.merge(df_ana_2, zips, how='left', left_on='CommunityZipCode', right_on='ZIP')
df_ana_3.rename(columns={'LAT': 'community-lat', 'LNG': 'community-long'}, inplace=True)
df_ana_3.head()

## customer zip codes:
df_ana_4 = pd.merge(df_ana_3, zips, how='left', left_on='ZipCode', right_on='ZIP')
df_ana_4.rename(columns={'LAT': 'customer-lat', 'LNG': 'customer-long'}, inplace=True)


df_ana_4.columns.values

def haversine_np(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)

    All args must be of equal length.    

    """
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2

    c = 2 * np.arcsin(np.sqrt(a))
    km = 6367 * c
    return km

df_ana_4.loc[df_ana_4['ZipCode'] == 85373.0].head()

#df_ana_4[['community-long', 'community-lat', 'customer-long', 'customer-lat']].apply(haversine_np, axis=1)
df_ana_4['distance'] = df_ana_4.apply(lambda row: 
                                      haversine_np(
                                        row['community-long'], 
                                        row['community-lat'],
                                        row['customer-long'], 
                                        row['customer-lat']
                                       ), axis=1)

df_ana_4.distance.value_counts()