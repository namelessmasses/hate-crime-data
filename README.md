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

# Support for VSCode DevContainers

The repository supports development using VSCode DevContainers. The repository contains a `.devcontainer` directory with a `devcontainer.json` file. The devcontainer sets up the correct container in order to run Jupyter, and installs the necessary Python packages to run the `convert.py` script. Cloning the repository and opening the clone folder on the host in a devcontainer, or having the devcontainer clone the repository should provide a fully functional Jupyter Datascience Notebook development environment.

1. Open the repository in VSCode.
1. VSCode should detect the `.devcontainer` directory and prompt to "Reopen in Container".
1. Select "Reopen in Container".
1. The devcontainer will build and start.
1. Open a terminal in VSCode.
1. Run `python convert.py` to convert the CSV file to a new CSV file with the semi-colon separated values converted to multiple rows.
1. Select the VSCode terminal session `Configuring...` and look for the Jupyter Notebook URL to open in a browser. E.g., ` http://127.0.0.1:8888/tree?token=e56c6b057bfcd902abbf1b93cd5e005f37059d1c2bcb2f5d`. Copy this URL.
    1. If no `Configuring...` terminal session exists, then run `jupyter notebook list` and copy the URL.
1. Open the Jupyter Notebook `HateCrime.ipynb`.
1. If VSCode does not detect the correct kernel, then Selecting the Kernel menu, and selecting the `Existing Kernel` option, and pasting the URL copied in the previous step should allow the Jupyter Notebook to run in the correct kernel.
