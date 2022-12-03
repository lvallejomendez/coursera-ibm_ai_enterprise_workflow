

import os
import sys
import getopt
import pandas as pd
import numpy as np
import sqlite3

DATA_DIR = os.path.join("..","data")


def connect_db(file_path):
    """
    function to connection to aavail database
    INPUT : the file path of the data base
    OUTPUT : the sqlite connection to the database
    """
    ## YOUR CODE HERE
    try:
      conn = sqlite3.connect(file_path)
      print("...successfully connected to db\n")
    except Error as e:
      print("...unsuccessful connection\n",e)
    
    return(conn)

def ingest_db_data(conn):
    """
    load and clean the db data
    INPUT : the sqlite connection to the database
    OUPUT : the customer dataframe
    """
    ## YOUR CODE HERE
    customer_df = conn.execute(
        'SELECT customer_id, last_name, first_name, DOB, city, state, country_name, gender \
        FROM CUSTOMER \
        INNER JOIN COUNTRY ON CUSTOMER.country_id = COUNTRY.country_id;')

    columns_name = ['customer_id', 'last_name', 'first_name', 'DOB', 'city', 'state', 'country_name', 'gender']

    customer_df = pd.DataFrame(customer_df, columns=columns_name)

    
    # Remove duplicates
    size_before = len(customer_df)
    customer_df.drop_duplicates(inplace=True)
    size_after = len(customer_df)
    print("... removed {} duplicate rows in customer data".format(size_before-size_after))
    return customer_df
    

def ingest_stream_data(file_path):
    """
    load and clean the stream data
    INPUT : the file path of the stream csv
    OUTPUT : the streams dataframe and a mapping of the customers that churned
    """
    ## YOUR CODE HERE
    df_streams = pd.read_csv(file_path)
    size_before = len(df_streams)
    df_streams = df_streams[~df_streams['stream_id'].isna()]
    size_after = len(df_streams)
    print("... removed {} missing stream ids".format(size_before-size_after))

    has_stopped = df_streams.groupby("customer_id").apply(lambda x : True if x['subscription_stopped'].max() > 0 else False)

    return df_streams, has_stopped
    

def process_dataframes(customer_df, df_streams, has_stopped, conn):
    """
    create the target dataset from the different data imported 
    INPUT : the customer dataframe, the stream data frame, the map of churned customers and the connection to the database
    OUTPUT : the cleaned data set as described question 4
    """
    ## YOUR CODE HERE
    df_comb = pd.DataFrame()
    df_comb['customer_id'] = customer_df.customer_id
    df_comb['customer_name'] = customer_df.first_name + ' ' + customer_df.last_name

    # Create age column from DOB
    now = pd.Timestamp('now')
    dob = pd.to_datetime(customer_df.DOB, infer_datetime_format=True)
    dob = dob.where(dob < now, dob - np.timedelta64(100, 'Y'))
    customer_age = (now - dob).astype('timedelta64[Y]')
    customer_age
    df_comb['customer_age'] = customer_age.astype(int)

    df_comb['country'] = customer_df.country_name
    df_comb['is_subscriber'] = df_streams.groupby("customer_id").max().subscription_stopped.values
    df_comb['subscriber_type'] = df_streams.groupby("customer_id").max().invoice_item_id.values.astype(int)
    df_comb['num_streams'] = df_streams.groupby('customer_id').size().values

    return (df_comb)
    
    
def update_target(target_file, df_comb, overwrite=False):
    """
    write the clean data in a target file located in the working directory.
    Overwrite the existing target file if overwrite is false, otherwise append the clean data to the target file
    INPUT : the name of the target file, the cleaned dataframe and an overwrite flag
    OUPUT : None
    """
    ## YOUR CODE HERE
    if overwrite or not os.path.exists(target_file):
        df_comb.to_csv(target_file, index=False)   
    else:
        df_comb.to_csv(target_file, mode='a', header=False, index=False)
    
        
if __name__ == "__main__":
  
    ## collect and handle arguments with getopt or argparse
    ## YOUR CODE HERE

    ## collect args
    arg_string = "%s -d db_filepath -s streams_filepath"%sys.argv[0]
    try:
        optlist, args = getopt.getopt(sys.argv[1:],'d:s:')
    except getopt.GetoptError:
        print(getopt.GetoptError)
        raise Exception(arg_string)

    ## handle args
    streams_file = None
    db_file = None
    for o, a in optlist:
        if o == '-d':
            db_file = a
        if o == '-s':
            streams_file = a
    streams_file = os.path.join(DATA_DIR,streams_file)
    db_file = os.path.join(DATA_DIR,db_file)
    target_file = os.path.join(DATA_DIR, "aavail-subscribers.csv")
    
    ## make the connection to the database
    ## YOUR CODE HERE
    conn = connect_db(db_file)

    ## ingest the data and transform it
    ## YOUR CODE HERE
    customer_df = ingest_db_data(conn)
    df_streams, df_churn = ingest_stream_data(streams_file)
    df_comb = process_dataframes(customer_df, df_streams, df_churn, conn)
    
    ## write the transformed data to a csv
    ## YOUR CODE HERE
    update_target(target_file, df_comb, overwrite=False)
    print("done")

    