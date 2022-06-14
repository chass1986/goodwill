import json

import pandas as pd
import numpy as np
from datetime import datetime
from core.models import Territories


def func():
    df_territories = pd.read_csv('territories.csv')
    df_territories = df_territories.replace(np.nan, None, regex=True)
    territories = df_territories.to_dict(orient='records')
    formatted_territories = {row['id']: row for row in territories}

    df_relations = pd.read_csv('territory_parents.csv')
    relations = df_relations.to_dict(orient='records')

    for rel in relations:
        parent_id = rel['parent_id']
        child_id = rel['child_id']
        formatted_territories[child_id]['parent_id'] = parent_id if child_id in formatted_territories else None

    with open('territories_relations3.json', 'w') as f:
        json.dump(list(formatted_territories.values()), f)

    return formatted_territories


def insert_without_foreign_key_value():

    with open('territories_relations3.json', 'r') as f2:
        ter2 = json.load(f2)

    for row in ter2:
        row['created_at'] = datetime.strptime(row['created_at'], '%Y-%m-%d %H:%M:%S.%f')
        row['updated_at'] = datetime.strptime(row['updated_at'], '%Y-%m-%d %H:%M:%S.%f')
        if 'parent_id' in row:
            row.pop('parent_id')

    for idx, row in enumerate(ter2):
        print(f"*********** id: {row['id']}, index: {idx}")
        Territories.objects.create(**row)

    return ter2


def insert_with_foreign_key_value():
    with open('territories_relations3.json', 'r') as f2:
        ter2 = json.load(f2)

    idx = 37378
    for row in ter2[idx:]:
        print(f"*********** id: {row['id']}, index: {idx}")
        Territories.objects.filter(id=row['id']).update(parent_id=row.get('parent_id'))
        idx += 1



if __name__ == '__main__':
    # func()
    print(test())

created_at = datetime.strptime('2019-12-10 12:38:53.752692', '%Y-%m-%d %H:%M:%S.%f')
updated_at = datetime.strptime('2020-06-23 13:14:56.170453', '%Y-%m-%d %H:%M:%S.%f')
obj = {'id': 4, 'code': '240100883', 'name': "CC de la Plaine de l'Ain", 'kind': 'FREPCI', 'created_at': created_at, 'updated_at': updated_at, 'is_current': True, 'population': None, 'official_website_url': 'http://www.cc-plainedelain.fr', 'articles_count': 2, 'admin_docs_count': 2, 'impacters_count': 33, 'websites_count': 34, 'sources_count': 98, 'parent_id': 3}