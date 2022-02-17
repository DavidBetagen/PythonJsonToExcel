import json
import pandas

# TEST FROM DATA
data = {
            'superheroes': [
                {
                    'firstname':'Bruce',
                    'lastname':'Wayne',
                    'country':'England'
                },
                {
                    'firstname':'Steve ',
                    'lastname':'Rogers',
                    'country':'America'
                }
            ]
        }
        
data = pandas.DataFrame(data['superheroes'])
data.to_excel('superheroes.xlsx')


# TEST FROM FILE.json
with open('employees.json') as json_file:
    data = json.load(json_file)
    data = pandas.DataFrame(data['employees'])
    data.to_excel('employees.xlsx')
    