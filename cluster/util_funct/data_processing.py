''' Data Processing toolbox: contains pre and post processing function for
    cluster analysis of realestate data.'''

def LoadData():
    ''' loads data from csv file to dataframe '''
    import pandas as pd

    input_df = pd.read_csv('zip_data.csv')
    input_df.drop('Unnamed: 0', axis=1, inplace=True)
    return input_df

def TransformInput(input_dict):
    import pickle
    max_vals = pickle.load( open( "max_vals.p", "rb" ) )
    parks = (input_dict['parks']/10)*max_vals['recreation']
    eats = (input_dict['eats']/10)*max_vals['eating-drinking']
    shop = (input_dict['shop']/10)*max_vals['shopping']
    transportation = (input_dict['transportation']/10)*max_vals['trwpublic']
    tax = ((10 - input_dict['tax'])/10)*max_vals['avg_prop_tax']
    input_list = [parks, eats, shop, input_dict['income'], input_dict['price'], transportation, tax]
    input_list = [input_list]
    return input_list

def ConcatAndScale(Transformed_user_input, data):
    ''' concatenates and scales data with x1 concatenated on top of x2 '''
    import numpy as np
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    data_std = scaler.fit_transform(data)
    input_std = scaler.transform(Transformed_user_input)
    input_concat = np.concatenate((input_std, data_std), axis=0)
    return input_concat



def FindDistanceSortZips(x1, x2, zips_dict):
    ''' finds distance '''
    from sklearn.neighbors import DistanceMetric
    from sklearn.preprocessing import StandardScaler
    import pandas as pd
    import numpy as np
    x2_predicted = x2.loc[x2['zip_codes'] == zips_dict['zips'][0]].values
    for i in range(len(zips_dict['zips'])-1):
        vector = x2.loc[x2['zip_codes'] == zips_dict['zips'][i+1]].values
        x2_predicted = np.concatenate((x2_predicted, vector), axis=0)
    x2_array = x2_predicted[:,1:]
    scaler = StandardScaler()
    x2_std = scaler.fit_transform(x2_array)
    x1_std = scaler.transform(x1)
    X = np.concatenate((x1_std, x2_std))
    dist = DistanceMetric.get_metric('euclidean')
    distance = dist.pairwise(X)
    distance = distance[0]
    distance_dict = {'distance': list(distance)[1:]}
    zip_dist = {**zips_dict, **distance_dict}
    zip_dist_df = pd.DataFrame(zip_dist)
    zip_dist_df.sort_values('distance', axis=0, ascending=True, inplace=True)
    zip_codes_sorted = zip_dist_df['zips'].values.astype(str)
    zip_codes_sorted_dict = {'zip_codes': list(zip_codes_sorted)}
    return zip_codes_sorted_dict
