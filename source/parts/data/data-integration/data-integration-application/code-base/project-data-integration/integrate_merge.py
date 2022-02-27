#merge.py

# batch_merge.py
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

import os
import glob
import pandas as pd
import datetime
import json
import urllib.request

"""
merges csv and json files according to user preferences defined in a yaml file
"""
def batch_merge(dictionary: dict):
    """
    merges in batches
    """
    
    input_directory = dictionary['directories']['input_directory']
    #output_directory = cwd + dictionary['output_directory']
    os.chdir(dictionary['directories']['input_directory'])
    print("Reading Files From : {}".format(input_directory))

    #getting files from directory
    files_to_merge = dictionary['files']['files_to_merge']

    print("Files to Merge: {}".format(files_to_merge))
    #combine all files in the list
 
    master_chunksize = dictionary['vars']['master_chunksize']
    chunksize = master_chunksize
    extra_chunk = None # Initialize the extra chunk.
    
    for file in files_to_merge:
        csv_file = file

        # Alter chunksize if extra chunk is not None.
        if extra_chunk is not None:
            chunksize = master_chunksize - extra_chunk.shape[0]

        for chunk in pd.read_csv(csv_file, chunksize=chunksize):
            if extra_chunk is not None: 
                # Concatenate last small chunk of previous file with altered first chunk of next file.
                chunk = pd.concat([chunk, extra_chunk], sort=True)
                extra_chunk = None
                chunksize = master_chunksize # Reset chunksize.
            elif chunk.shape[0] < chunksize:
                # If last chunk is less than chunk size, set is as the extra bit.
                extra_chunk = chunk
                break

            yield chunk
    os.chdir(dictionary['directories']['cwd'])

def dumb_merge(dictionary: dict):
    """
    Merges en masse.  Memory inefficient
    """
    os.chdir(dictionary['directories']['input_directory'])
    dumb_merge = pd.concat([pd.read_csv(f) for f in dictionary['files']['files_to_merge'] ],sort=True)
    os.chdir(dictionary['directories']['cwd'])
    return dumb_merge

def load_json_files(dictionary: dict):
    """
    Json files to merge
    """ 
    os.chdir(dictionary['directories']['input_directory'])
    #f = dictionary['files']['files_to_merge'][2]
    #with open(f) as d:
    #    data = json.load(d)
    #    #print(data['results'][0])
    #df = pd.DataFrame(data['results'])
    #print(df)
    #print(len(data['results']))
    #print(f)
    json_df = pd.DataFrame()
    for f in dictionary['files']['files_to_merge']:
        with open(f) as d:
            data = json.load(d)
        df = pd.DataFrame(data["results"])
        
        json_df = pd.concat([json_df,df],ignore_index=True )

    
    
    #print(json_df['resources'][0][0]['pdf'])
    #print(json_df['item'][0])
    #print(type(json_df['item'][0]))

    os.chdir(dictionary['directories']['cwd'])

    return json_df

    
    

