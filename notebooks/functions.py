#stat calculations for numerical variables
def calc_stat(df, columns):
    # Initialize an empty list to store the stats for each column
    stats_list = []
    
    # Loop through each column in the list
    for column in columns:
        # Calculate the required statistics
        mean_column = df[column].mean()
        median_column = df[column].median()
        mode_column = df[column].mode().iloc[0]
        var_column = df[column].var()
        std_column = df[column].std()
        max_column = df[column].max()
        min_column = df[column].min()
        range_column = df[column].max() - df[column].min()
        quantiles_column = df[column].quantile([0.25, 0.5, 0.75]).to_list()
        
        # Append the results to the stats_list
        stats_list.append({
            'Column': column,
            'Mean': mean_column,
            'Median': median_column,
            'Mode': mode_column,
            'Variance': var_column,
            'Standard Deviation': std_column,
            'Maximal': max_column,
            'Minimal': min_column,          
            'Range': range_column,
            '25th Percentile': quantiles_column[0],
            '50th Percentile': quantiles_column[1],
            '75th Percentile': quantiles_column[2]
        })

    # Convert the stats_list to a DataFrame for better presentation
    stats_df = pd.DataFrame(stats_list)
    
    return stats_df


#Testing sample set vs population
def ttest_1samp-AB(population_df, sample_df, column_name):  
 
   # Extract the column of interest from the population and sample dataframes  
   population_values = population_df[column_name]  
   sample_values = sample_df[column_name]  
  
   # Perform the one-sample t-test  
   t_stat, p_val = stats.ttest_1samp(sample_values, population_values.mean())  
  
   return t_stat, p_val

#Testing two samples from the same population population

def ttest_ttest_ind-AB(population_df, sample_df, column_name):  
 
   # Extract the column of interest from the population and sample dataframes  
   population_values = population_df[column_name]  
   sample_values = sample_df[column_name]  
  
   # Perform the one-sample t-test  
   t_stat, p_val = stats.ttest_ttest_ind(sample_values, population_values.mean())  
  
   return t_stat, p_val

#Function to perform chi2tests between columns
from scipy.stats import chi2_contingency 
def chi2_test(df, col1, col2):
    # Create a contingency table between the two specified columns
    contingency_table = pd.crosstab(df[col1], df[col2])
    
    # Perform the chi-squared test
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    
    # Create a DataFrame to store the results
    results_df = pd.DataFrame({
        'column1': [col1],
        'column2': [col2],
        'p-value': [p],
        'statistic': [chi2],
        'dof': [dof]
    })

