# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

def price_percent_cut(df_NEW, col):
    price_low = np.percentile(df_NEW[col].values, 1)
    price_high = np.percentile(df_NEW[col].values, 99)

    df_NEW = df_NEW.drop(df_NEW[df_NEW.col < price_low].index)
    df_NEW = df_NEW.drop(df_NEW[df_NEW.col > price_high].index)

    return df_NEW

# Datetime object and number of photos feature engineering
def clean_preprocess(initial_df):
    # convert created column into datetime type
    try:
        initial_df['DateTime'] = pd.to_datetime(initial_df.created)
        initial_df.drop('created', axis=1, inplace=True)

        # create feature for number of photos
        initial_df['num_of_photos'] = initial_df.photos.map(len)
    except:
        print("Clean_Preprocessed function skipped as it can only be run once")
    return initial_df

# Remove prices outside of defined range
def remove_outlier_prices(df_NEW, price_low, price_high):
    df_NEW = df_NEW.drop(df_NEW[df_NEW.price < price_low].index)
    df_NEW = df_NEW.drop(df_NEW[df_NEW.price > price_high].index)
    return df_NEW

# Remove locations outside of New York
def remove_nonNY_coords(df_NEW, ny_boundaries):
    #Removing out of bounds longitude
    df_NEW = df_NEW.drop(df_NEW[df_NEW.longitude < ny_boundaries[0]].index)
    df_NEW = df_NEW.drop(df_NEW[df_NEW.longitude > ny_boundaries[1]].index)

    #Removing out of bounds latitude
    df_NEW = df_NEW.drop(df_NEW[df_NEW.latitude < ny_boundaries[2]].index)
    df_NEW = df_NEW.drop(df_NEW[df_NEW.latitude > ny_boundaries[3]].index)

    return df_NEW