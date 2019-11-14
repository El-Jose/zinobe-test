import json
import pandas as pd
import requests
import timeit
from hashlib import sha1

def calc_exec_times(lst):
    df = pd.DataFrame(lst)
    try:
        total_tm, avrg_tm =  df["time"].sum(), df["time"].mean()
        min_tm, max_tm = df["time"].min(), df["time"].max()
    except KeyError:
        return "error: Dataframe doesn't have the column required"
    return total_tm, avrg_tm, min_tm, max_tm

def countries_to_json(lst):
    with open('data.json', 'w') as json_file:
        json.dump(lst, json_file)

def encode_sha1(string, encoding='utf-8'):
    try:
        res = sha1(string.encode(encoding)).hexdigest()
    except AttributeError:
        res = {'error': 'parameter provided is not a string'}
    return res

def get_regions():
    regions = []
    headers = {"x-rapidapi-host": "restcountries-v1.p.rapidapi.com","x-rapidapi-key": "a82c94aee6msh71eba262c237aeep12db28jsn2c05be2f6d20"}
    res = requests.get('https://restcountries-v1.p.rapidapi.com/all', headers=headers)
    res = res.json()
    for i in res:
        if i['region']  not in regions and i['region'] is not '':
            regions.append(i['region'])
    return regions

def get_first_country_by_region(region):
    start = timeit.timeit()
    region = region
    res = requests.get(f'https://restcountries.eu/rest/v2/region/{region}')
    res = res.json()
    end = timeit.timeit()
    total_time = (end-start)*1000
    country = {'region': region,'name': res[0]['name'], 'language': encode_sha1(res[0]['languages'][0]['name']), 'time': total_time}
    return country
