def get_population(country_dict):
  population_dict = {
    '2022':int(country_dict['2022 Population']),
    '2020':int(country_dict['2020 Population']),
    '2015':int(country_dict['2015 Population']),
    '2010':int(country_dict['2010 Population']),
    '2000':int(country_dict['2000 Population']),
    '1990':int(country_dict['1990 Population']),
    '1980':int(country_dict['1980 Population']),
    '1970':int(country_dict['1970 Population'])
  }
  return population_dict.keys(), population_dict.values()



def population_by_conutry(data, country):
  result = list(filter(lambda item: item['Country'] == country, data))
  return result