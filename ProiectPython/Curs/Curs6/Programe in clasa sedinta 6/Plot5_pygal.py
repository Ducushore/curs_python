# Program generare grafic pygal
# Explica functiile pygal
# Ion Studentul - 1/26/13

import pygal

bar_chart = pygal.StackedBar()
bar_chart.no_data_text = "Fara Date"
bar_chart.title='Locatie: Bucuresti'
bar_chart.human_readable=True
bar_chart.y_title='Elemente masurate'
bar_chart.x_title='Timp'
bar_chart.add('Bandwindth Voce-Mbps', [5, 7, 1, 0, 8, 12, 3, 8, 13, 20, 24])
bar_chart.add('Bandwindth Date-Mbp', [4, 10, 5, 0, 4, 20, 8, 13, 21, 34, 55])
bar_chart.render_to_file('grafic5.svg') 

raw_input("\n\nApasa <enter> pt a iesi.")