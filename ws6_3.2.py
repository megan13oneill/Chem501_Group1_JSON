import json 
import os

data = {'Molecule1' : 
            {'CompoundName' : 'Haloperidol',
             'MolecularFormula' : 'C21H23CIFNO2',
             'inchikey' : 'LNEPOXFFQSENCJ-UHFFFAOYSA-N',

            'synonyms': [
                {
                'synonym': 'Haldol',
                'source': 'PubChem',
                },
                {
                'synonym': 'Haloperidol',
                'source': 'PunChem',
                }
            ]  
            }
        }

output_file = './chemdata.json'

# Write the combined data to a single output file
with open(output_file, 'w') as outfile:
    json.dump(data, outfile, indent=4)

data