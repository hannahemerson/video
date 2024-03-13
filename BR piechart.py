import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('microbit_code.csv')

sizes = [0.41666666666,0.25,0.33]
labels = 'yes', 'no', 'sometimes'  
colors = ['pink', 'purple', 'lightskyblue']
explode = (0.1, 0.0, 0.0)  # explode 1st slice

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.title("Piechart")

plt.show()