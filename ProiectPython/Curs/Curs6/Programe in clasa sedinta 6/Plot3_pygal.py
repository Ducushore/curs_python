# Program generare grafic pygal
# Explica functiile pygal
# Ion Studentul - 1/26/13

import pygal

bar_chart = pygal.Bar(title='Locatie: Bucuresti',x_title='Timp',
         y_title='Elemente masurate',title_font_size=24,human_readable=True)
bar_chart.add('Bandwindth-bps', [500000, 7000000, 1000000, 0, 800000, 12000000, 3000000, 8000000, 13000000, 20000000, 24000000])
bar_chart.add('Latency-ms', [4, 10, 5, 0, 4, 20, 8, 13, 21, 34, 55])
bar_chart.x_labels = [
    '10:15:10',
    '10:15:20',
    '10:15:30',
    '10:15:40']

bar_chart.render_to_file('grafic3.svg') 


raw_input("\n\nApasa <enter> pt a iesi.")