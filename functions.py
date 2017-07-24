import pandas as pd

def create_df():
    return pd.create_df()

def trialTime(block):
    #//requires(type(block) == int)
    #//requires(block > -1 && block < 30)
    timings = [5000, 4500, 4000,
               4500, 4000, 3500,
               4000, 3500, 3000,
               3500, 3000, 2500,
               3000, 2500, 2000,
               2500, 2000, 1500,
               2000, 1500, 1000,
               1500, 1000, 750,
               1000, 750,  500,
               750,  500,  500]
    return timings[block]
