# DE_project

This repository contains information and code on various parts of the Data Engineering Project. 

Code and setup: 
1. Superset_build catalogue - information on how Superset was set up.
2. Downloaddata.py - Python code on reading in the data file, modifying and transforming data.
3. Dashboard_export.zip - information on how the Superset dashboard was created, downloaded from Superset

Data files: 
1. lo_2011_2025.csv - original .csv file downloaded from https://avaandmed.eesti.ee/datasets/inimkannatanutega-liiklusonnetuste-andmed
2. onnetus.parquet - a transformed data file (output of downloaddata.py, input to Superset)

Other important files: 
1. 'Projekti raport.pdf' and 'Projekti raport.md' - files containing the report of the project.
2. dashboard_liiklus.jpg - a .jpg view of the dashboard created in Superset based on the abovementioned dataset (please note, that some of the charts' date range has been slightly modified in this view due to the fact that a charts cannot be scrolled and to show the most important part of charts).
