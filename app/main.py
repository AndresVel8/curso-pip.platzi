import mod
import app.read_csv as read_csv
import charts


def run():
  data =   read_csv.read_csv('./app/data.csv')
  country = input('Type Country =>')

  result = mod.population_by_conutry(data,country)

  if len(result) > 0:
    country = result[0]
    keys, values = mod.get_population(country)
    charts.generater_bar_chart(labels, values)