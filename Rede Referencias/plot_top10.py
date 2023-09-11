# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 01:03:02 2023

@author: danie
"""

import pandas as pd
import matplotlib.pyplot as plt

d1 = pd.read_csv('94-98.csv')
d2 = pd.read_csv('99-02.csv')
d3 = pd.read_csv('03-06.csv')
d4 = pd.read_csv('07-10.csv')
d5 = pd.read_csv('11-14.csv')
d6 = pd.read_csv('15-18.csv')
d7 = pd.read_csv('19-22.csv')

def merge_dataframes_by_id(dataframes):
    if len(dataframes) == 0:
        return None

    merged_df = dataframes[0]

    for df in dataframes[1:]:
        merged_df = pd.merge(merged_df, df, on='Id', how='inner')

    return merged_df

dataframes = [d1,d2,d3,d4,d5,d6,d7]
datas = ['1994-1998','1999-2002','2003-2006','2007-2010','2011-2014','2015-2018','2019-2022']

for df in dataframes:
    df['porcentagem'] = (df['indegree']/(df['outdegree'] > 0).sum())*100

absolutos = []
for i,df in enumerate(dataframes):
    df=df[['Id','indegree']]
    df.rename(columns={'indegree':datas[i]},inplace=True)
    absolutos.append(df)
    
percentuais = []
for i,df in enumerate(dataframes):
    df=df[['Id','porcentagem']]
    df.rename(columns={'porcentagem':datas[i]},inplace=True)
    percentuais.append(df)

merged_absolutos = merge_dataframes_by_id(absolutos)
merged_percentuais = merge_dataframes_by_id(percentuais)

merged_absolutos.set_index('Id', inplace=True)
merged_percentuais.set_index('Id', inplace=True)

#%%PLOT ABSOLUTOS
for column in list(merged_absolutos.columns):
    
    merged_absolutos.sort_values(by=[column], ascending=False, inplace=True) 

    merged_absolutos.head(10).T.plot(kind='line', marker='o')
    plt.title(f'Evolução dos autores mais mencionados \n no período {column}\npor volume total de menções')
    plt.ylabel('Menções')
    plt.legend(title='Autores',loc='upper left', bbox_to_anchor=(1, 1))
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.savefig(f'./Resultados/Absolutos/{column}.png',dpi=300,bbox_inches='tight')
    plt.show()

#%%PLOT PERCENTUAIS

for column in list(merged_percentuais.columns):
    
    merged_percentuais.sort_values(by=[column], ascending=False, inplace=True) 

    merged_percentuais.head(10).T.plot(kind='line', marker='o')
    plt.title(f'Evolução dos autores mais mencionados \n no período {column}\npor percentual de trabalhos onde é mencionado')
    plt.ylabel('Percentual')
    plt.legend(title='Autores',loc='upper left', bbox_to_anchor=(1, 1))
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.savefig(f'./Resultados/Percentuais/{column}.png',dpi=300,bbox_inches='tight')
    plt.show()
