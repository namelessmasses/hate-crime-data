import pandas as pd
from itertools import product
import zipfile

with zipfile.ZipFile('hate_crime.zip') as zf:
    print('Extracting hate_crime.csv from hate_crime.zip')
    hate_crime_csv = zf.extract('hate_crime/hate_crime.csv')
    print('Extracted {}'.format(hate_crime_csv))

# Step 1: Load the CSV file into a DataFrame
print('Reading dataframe from {}'.format(hate_crime_csv))
df = pd.read_csv(hate_crime_csv)
print('Dataframe loaded successfully')
print('Original data contains {} rows'.format(len(df)))

# Count the number of rows in the original data
n_total_rows_processed = 0

# Count the number of rows that were expanded
# i.e., sum of the number of rows generated for each row that was expanded.
n_total_rows_expanded = 0

# Count the total number of expanded rows in the output data (i.e., )
n_expanded_rows = 0

# Step 2: Function to split offense_name and bias_desc, and generate Cartesian product
def split_and_expand(row):
    offenses = row['offense_name'].split(';')
    biases = row['bias_desc'].split(';')
    
    # Generate the Cartesian product of offenses and biases
    combinations = list(product(offenses, biases))

    global n_total_rows_processed
    global n_total_rows_expanded
    global n_expanded_rows
    n_total_rows_processed = n_total_rows_processed + 1
    percent_10ths = int(n_total_rows_processed / len(df) * 1000)
    if percent_10ths % 10 == 0:
        print('\r{}% complete'.format(int(percent_10ths / 10)), end='')
    n_total_rows_expanded = n_total_rows_expanded + [0, 1][len(combinations) > 1]
    n_expanded_rows = n_expanded_rows + [0, len(combinations)][len(combinations) > 1]
          
    # Create a DataFrame for each combination
    return pd.DataFrame({
        'incident_id': [row['incident_id']] * len(combinations),
        'data_year': [row['data_year']] * len(combinations),
        'ori': [row['ori']] * len(combinations),
        'pug_agency_name': [row['pug_agency_name']] * len(combinations),
        'pub_agency_unit': [row['pub_agency_unit']] * len(combinations),
        'agency_type_name': [row['agency_type_name']] * len(combinations),
        'state_abbr': [row['state_abbr']] * len(combinations),
        'state_name': [row['state_name']] * len(combinations),
        'division_name': [row['division_name']] * len(combinations),
        'region_name': [row['region_name']] * len(combinations),
        'population_group_code': [row['population_group_code']] * len(combinations),
        'population_group_description': [row['population_group_description']] * len(combinations),
        'incident_date': [row['incident_date']] * len(combinations),
        'adult_victim_count': [row['adult_victim_count']] * len(combinations),
        'juvenile_victim_count': [row['juvenile_victim_count']] * len(combinations),
        'total_offender_count': [row['total_offender_count']] * len(combinations),
        'adult_offender_count': [row['adult_offender_count']] * len(combinations),
        'juvenile_offender_count': [row['juvenile_offender_count']] * len(combinations),
        'offender_race': [row['offender_race']] * len(combinations),
        'offender_ethnicity': [row['offender_ethnicity']] * len(combinations),
        'victim_count': [row['victim_count']] * len(combinations),
        'offense_name': [combo[0] for combo in combinations],  # First element of the tuple
        'bias_desc': [combo[1] for combo in combinations],  # Second element of the tuple
        'total_individual_victims': [row['total_individual_victims']] * len(combinations),
        'location_name': [row['location_name']] * len(combinations),
        'victim_types': [row['victim_types']] * len(combinations),
        'multiple_offense': [row['multiple_offense']] * len(combinations),
        'multiple_bias': [row['multiple_bias']] * len(combinations)
    })

print('Processing data...')
# Step 3: Apply the function to each row and concatenate the results
df_expanded = pd.concat([split_and_expand(row) for _, row in df.iterrows()], ignore_index=True)
print('\nData processed successfully')
print('Processed {} rows'.format(n_total_rows_processed))
print('Expanded {} rows'.format(n_total_rows_expanded))
print('Expanded by {} rows'.format(n_expanded_rows))
print('Expanded data contains {} rows'.format(len(df_expanded)))
print('Consistency check: {} - {} + {} = {}'.format(len(df_expanded), n_expanded_rows, n_total_rows_expanded, len(df)))
if (len(df_expanded) == len(df) - n_total_rows_expanded + n_expanded_rows):
    print('Consistency check passed')
else:
    raise ValueError('Consistency check failed')

# Step 4: Save the result back to a CSV file
print('Saving the output to hate_crime_expanded.csv')
df_expanded.to_csv('hate_crime_expanded.csv', index=False)

print("Data processing complete. The output is saved as 'hate_crime_expanded.csv'.")
