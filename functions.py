import pandas as pd

def createDataDict():
    # creates the dataframe for data storage
    #//ensures(is_empty_data_dict(@return))
    parameters = ["conf", "level", "block", "resp", "rt"]
    data_dict = dict( (param,[]) for param in parameters)
    return data_dict

def fill_trial(dataDict, data):
    #//requires(type(data) == list && type(dataDict) == dict)
    # let's have all of the data be put in a 1D list called data that is 
    # passed into this function in the format: 
    # [configuration, level, block, response, rt]
    # configuration: 'congruent', 'incongruent'
    # response: 'correct', 'incorrect', 'toolong'
    dataDict["conf"].append(data[0])
    dataDict["level"].append(data[1])
    dataDict["block"].append(data[2])
    dataDict["resp"].append(data[3])
    dataDict["rt"].append(data[4])
    return dataDict

def createCSV(dataDict, name="temp"):
    #//requires(type(name) == str)
    #//requires(!is_empty(dataDict))
    output_name = name + ".csv"
    df = pd.DataFrame.from_dict(dataDict)
    df.to_csv(output_name)
    #void function

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
