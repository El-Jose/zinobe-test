from country import calc_exec_times, countries_to_json, get_first_country_by_region, get_regions
from database import insert_countries


if __name__ == "__main__":
    countries = []
    # get regions from API service
    regions = get_regions()
    # Start to Build each country info
    for i in regions:
        country = get_first_country_by_region(i)
        countries.append(country)
    # show execution times to user
    total_tm, avrg_tm, min_tm, max_tm = calc_exec_times(countries)
    print(f'Total time: {total_tm} ms\nMean time: {avrg_tm} ms\n')
    print(f'Minimum time: {min_tm} ms\nMaximum time: {max_tm} ms\n')
    
    # insert country info into database
    insert_countries(countries)
    # export country info to JSON file
    countries_to_json(countries)
