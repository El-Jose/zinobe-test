import pytest
from run import get_regions, get_first_country_by_region  


def test_get_regions():
    res = get_regions()
    assert res == ['Asia', 'Europe', 'Africa', 'Oceania', 'Americas', 'Polar']

def test_get_country():
    region = 'asia'
    res = get_first_country_by_region('asia')
    assert res == {'name': 'Afghanistan'}
