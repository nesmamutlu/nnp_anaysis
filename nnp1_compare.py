import pandas as pd
import matplotlib.pyplot as plt

# Define the path to your CSV file
file_path = '/home/esma/Documents/nnp1_nnp2.csv'

# Load the data from the CSV file
data = pd.read_csv(file_path)

# Extract relevant columns for plotting
nnp1_validation_rmse = data['nnp1_validation_psavg_f_rmse']
nnp2_validation_rmse = data['nnp2_validation_psavg_f_rmse']

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(nnp1_validation_rmse, label='nnp1_validation_psavg_f_rmse', marker='o')
plt.plot(nnp2_validation_rmse, label='nnp2_validation_psavg_f_rmse', marker='x')

# Labeling the axes
plt.xlabel('Index')
plt.ylabel('Validation RMSE')
plt.title('Comparison of nnp1 and nnp2 Validation RMSE')

# Adding a legend
plt.legend()

# Display the plot
plt.show()

