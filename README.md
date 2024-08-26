Based on the United States Federal Bureau of Investigation "Hate Crime" dataset. 

# Downloading the dataset
1. Go to https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/downloads#datasets
1. Select "Hate Crime"
1. Select "Download"
1. Save the downloaded `hate_crime.zip` file to the root directory of this repository.

# Data Massaging - convert.py
The FBI dataset is a CSV file. Two columns need a little data massaging to 
make the data more accesible using query tools.

The downloaded file is a zip file that contains 
```
hate_crime.zip
|
+-- hate_crime/
|   |
|   +-- hate_crime.csv
|
+-- Hate_Crime_<last update year>_Methodology.pdf
```

`hate_crime.csv` is a CSV file with rows uniquely identified by `incident_id`. Some columns contain semi-colon separated lists of values. 

The repository provides a Python script, `convert.py`, to convert the CSV to multiple rows for each incident_id where there are columns with semi-colon separated values. Each row with columns of semi-colon separated values is converted to the cartesian product of the values number of rows. E.g., if a row has one column 3 semi-colon separated values, and another column with 4 semi-colon separated values, the row is converted to 12 rows.
    
`convert.py`
1. Extracts `hate_crime.csv` from the downloaded zip file.
1. Converts the CSV file to a new CSV file, `hate_crime_converted.csv`, with the semi-colon separated column values converted to multiple rows.

## Column: offense_name
The `offense_name` column contains a semi-colon separated list of offenses.

## Column: bias_desc
The `bias_desc` column contains a semi-colon separated list of bias classes of offenders against victim(s).