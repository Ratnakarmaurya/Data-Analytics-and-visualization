import numpy as np
from pandas import Series,DataFrame
import pandas as pd

# Heres an example of what a JSON (JavaScript Object Notation) looks like:
json_obj = """
{   "zoo_animal": "Lion",
    "food": ["Meat", "Veggies", "Honey"],
    "fur": "Golden",
    "clothes": null, 
    "diet": [{"zoo_animal": "Gazelle", "food":"grass", "fur": "Brown"}]
}
"""
import json
data = json.loads(json_obj)#converts json object(string) into dictionery
data
type(data)
type(json_obj)
converting_back=json.dumps(data)# .dumps converts dict to json string
type(converting_back)
converting_back

#loading json data in dataframe
#We can simply open JSON data after loading with a DataFrame
dframe = DataFrame(data["diet"])
dframe
