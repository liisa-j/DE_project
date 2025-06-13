import numpy as np
import pandas as pd
from datetime import datetime
from pyproj import Transformer

# Loeme andmed sisse failist
onnetus = pd.read_csv('lo_2011_2025.csv', sep=';')

## Toimumisaeg stringist datetime'iks
onnetus['Toimumisaeg_dt'] = pd.to_datetime(onnetus['Toimumisaeg'])
#kontroll
#onnetus['Toimumisaeg_dt'][0].year

## Lihtsustame valgusolud (valge / pime valgustuseta / pime valgustusega / teadmata) 
#print(onnetus['Valgustus (detailne)'].unique())
onnetus['Valgustus!'] = onnetus['Valgustus (detailne)']
onnetus['Valgustus!'] = onnetus['Valgustus!'].replace('Valge aeg', 'Valge')
onnetus['Valgustus!'] = onnetus['Valgustus!'].replace(('Pimeda ajal valgustus ei põle', 'Pimeda ajal valgustus puudub'), 'Pime')
onnetus['Valgustus!'] = onnetus['Valgustus!'].replace(('Teadmine puudub', np.nan), 'Teadmata')
onnetus['Valgustus!'] = onnetus['Valgustus!'].replace(('Pimeda ajal valgustus põleb'), 'Pime aeg, valgustatud')
#onnetus['Valgustus!'].unique()

## Lihtsustame teeolud (libe / mittelibe / teadmata)
#print(onnetus['Teekatte seisund'].unique())
onnetus['Teekatte seisund!'] = onnetus['Teekatte seisund']
onnetus['Teekatte seisund!'] = onnetus['Teekatte seisund!'].replace(('Pole teada', np.nan, 'Muu'), 'Teadmata')
onnetus['Teekatte seisund!'] = onnetus['Teekatte seisund!'].replace(('Lumelörts, soolalumine segu', 'Sõidujäljed puhtad, sõidujälgede vahe lumine', 
                                                                    'Kohev lahtine lumi', 'Töötlemata pinnaga kinnisõidetud lumi', 
                                                                     'Töötlemata pinnaga jäätunud märg kate, jäide', 'Töödeldud pinnaga jäätunud kate',
                                                                     'Töödeldud pinnaga kinnisõidetud lumi','Töötlemata pinnaga jäätunud kuiv kate',
                                                                     'Lumi, jää - tavalised libeduse põhjustajad'), 'Lumi/lörts/jää')
onnetus['Teekatte seisund!'] = onnetus['Teekatte seisund!'].replace(('Märg', 'Pori, saaste', 'Muu libedus - lehed, liiv, muda, õli'), 'Märg/pori/liiv/õli/saaste')

#print(onnetus['Teekatte seisund!'].unique())


## Siin transformeerime X ja Y koordinaadid (algse Eesti koordinaatsüsteemistiku L-EST97 peame Superseti jaoks transformeerima GPSi koordinaatideks)
transformer = Transformer.from_crs("EPSG:3301", "EPSG:4326", always_xy=True)
onnetus[['lon', 'lat']] = onnetus.apply(lambda row: pd.Series(transformer.transform(row['Y koordinaat'], row['X koordinaat'])), axis=1)


onnetus.to_parquet('onnetus.parquet', index=False)