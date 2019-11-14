import pytest
from country import calc_exec_times, countries_to_json, encode_sha1, get_regions, get_first_country_by_region 


def test_get_regions():
    res = get_regions()
    assert res == ['Asia', 'Europe', 'Africa', 'Oceania', 'Americas', 'Polar']

def test_get_country():
    region = 'asia'
    res = get_first_country_by_region('asia')
    assert res['name'] == 'Afghanistan'
    assert res['region'] == 'asia'

def test_encode_sha1_integer():
    res = encode_sha1(1)
    assert 'error' in res.keys() 
    assert res['error'] == 'parameter provided is not a string'

def test_encode_sha1_string():
    res = encode_sha1("test")
    assert type(res) == str
    assert 'keys' not in dir(res)

def test_countries_2_json():
    lst = [1,2,3,4]
    res = countries_to_json(lst)
    import os.path
    assert os.path.exists('data.json') == True

def test_calc_exec_times_wrong_list():
    lst = ['1', 2, 3, 4 ]
    res = calc_exec_times(lst)
    assert res == "error: Dataframe doesn't have the column required"
