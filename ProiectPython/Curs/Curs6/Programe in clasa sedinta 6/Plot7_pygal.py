# Program generare grafic pygal
# Explica functiile pygal
# Ion Studentul - 1/26/13

import pygal


worldmap_chart = pygal.Worldmap()
worldmap_chart.title = 'Some countries'
worldmap_chart.add('Orange countries', ['fr', 'fi','ro'])
worldmap_chart.add('Vodafone countries', ['ma', 'mc', 'md', 'me', 'mg',
                                   'mk', 'ml', 'mm', 'mn', 'mo',
                                   'mr', 'mt', 'mu', 'mv', 'mw',
                                   'mx', 'my', 'mz'])
worldmap_chart.add('U countries', ['ca', 'uc', 'ro', 'uy', 'uz'])
worldmap_chart.render_to_file('grafic7.svg') 

raw_input("\n\nApasa <enter> pt a iesi.")