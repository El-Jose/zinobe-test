import database as db
import pandas as pd
import requests
import timeit
from hashlib import sha1

def calc_exec_times(lst):
    df = pd.DataFrame(lst)
    total_tm, avrg_tm, min_tm, max_tm = df["time"].sum(), df["time"].mean(), df["time"].min(), df["time"].max()
    return total_tm, avrg_tm, min_tm, max_tm

def encode_sha1(s, encoding='utf-8'):
    return sha1(s.encode(encoding)).hexdigest()

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

def save_countries_db(lst):
    conn = db.conn
    for i in lst:
        conn.execute('INSERT INTO country VALUES(?, ?, ?, ?);', (i['region'], i['name'], i['language'], i['time']));
        conn.commit()

if __name__ == "__main__":
    countries = []
    regions = get_regions()
    for i in regions:
        country = get_first_country_by_region(i)
        countries.append(country)
    calc_exec_times(countries)
    save_countries_db(countries)
