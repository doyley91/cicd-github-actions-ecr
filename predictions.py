import pandas as pd
#import sklearn
#import xgboost as xgb


def handler(event, context):
    message = []
    #message.append('The xgboost version is {}.'.format(xgb.__version__))
    #message.append('The scikit-learn version is {}.'.format(sklearn.__version__))
    message.append('The pandas version is {}.'.format(pd.__version__))
    return message