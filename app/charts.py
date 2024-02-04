import matplotlib.pyplot as plt

def generater_bar_chart():
  labels =['a', 'b', 'c']
  values = [50,100,150]
  fig, ax = plt.subplots()
  ax.bar(labels,values)
  plt.savefig('bar.png')
  plt.close() 

def generat_pie_chart():
  labels =['a', 'b', 'c']
  values = [50,100,150]
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close() 

if __name__ == '__main__':
  generater_bar_chart()