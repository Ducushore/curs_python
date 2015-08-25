# Program generare grafic pygal
# Explica functiile pygal
# Ion Studentul - 1/26/13

import pygal

bar_chart = pygal.Bar(title='Locatie: Bucuresti',x_title='Timp',
         y_title='Elemente masurate',title_font_size=24)
bar_chart.add('Bandwindth-Mbps', [0.5, 7, 1, 0, 0.8, 12, 3, 8, 13, 20, 24])
bar_chart.add('Latency-ms', [4, 10, 5, 0, 4, 20, 8, 13, 21, 34, 55])
bar_chart.render_to_file('grafic2.svg') 

raw_input("\n\nApasa <enter> pt a iesi.")