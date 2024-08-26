import pandas as pd
from itertools import product

# Step 1: Load the CSV file into a DataFrame
df = pd.read_csv('hate_crime_source.csv')

# Step 2: Function to split offense_name and bias_desc, and generate Cartesian product
def split_and_expand(row):
    offenses = row['offense_name'].split(';')
    biases = row['bias_desc'].split(';')
    
    # Generate the Cartesian product of offenses and biases
    combinations = list(product(offenses, biases))
    
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

# Step 3: Apply the function to each row and concatenate the results
df_expanded = pd.concat([split_and_expand(row) for _, row in df.iterrows()], ignore_index=True)

# Step 4: Save the result back to a CSV file
df_expanded.to_csv('hate_crime_expanded.csv', index=False)

print("Data processing complete. The output is saved as 'hate_crime_expanded.csv'.")
