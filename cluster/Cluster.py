

def RealestateClustering(input_dict):
    import pandas as pd
    from cluster.util_funct.data_processing import LoadData, TransformInput, ConcatAndScale, FindDistanceSortZips
    from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering

    realestate_data = LoadData()

    user_input = TransformInput(input_dict)

    realestate_array = realestate_data.iloc[:,1:8].values

    concat_data = ConcatAndScale(user_input, realestate_array)

    cluster = AgglomerativeClustering(n_clusters=7, affinity='cosine', linkage='complete')

    labels = cluster.fit_predict(concat_data)


    ins = realestate_data['zip_codes'].values
    zip_cluster_vals = pd.DataFrame([ins, labels[1:]],).transpose().values
    zip_cluster = pd.DataFrame(zip_cluster_vals, columns=['zip_code', 'label'])
    zips_predicted = zip_cluster.loc[zip_cluster['label'] == labels[0]]
    zips = zips_predicted['zip_code'].values
    zips_dict = {'zips': list(zips)}

    sorted_zips = FindDistanceSortZips(user_input, realestate_data, zips_dict)

    return sorted_zips


if __name__ == "__main__":
    parks = 7
    price = 100000
    tax = 8
    transportation = 7
    eats = 8
    income = 91000
    shop = 3

    input_dict = {'parks': parks, 'price': price, 'tax': tax,
                'transportation': transportation, 'eats': eats,
                'income': income, 'shop': shop}

    output_zips = RealestateClustering(input_dict)

    print(output_zips)
