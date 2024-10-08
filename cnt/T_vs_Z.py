import pandas as pd
import matplotlib.pyplot as plt

# Read the tz.txt file, assuming columns are space-separated
file_path = 'tz.txt'  # Provide the correct file path if needed
# Reading the data while skipping possible non-data lines
df = pd.read_csv(file_path, delim_whitespace=True, header=None)

# Naming columns based on the structure you provided (chunk number, z, Ncount, temperature)
df.columns = ['Chunk', 'z', 'Ncount', 'Temperature']

# Convert z distance to angstroms (if it's not already in angstroms, specify conversion here if needed)
# Assuming the z distance is already in angstroms, no need to convert

# Plotting T (Temperature) vs z (Distance along z-axis)
plt.figure(figsize=(8, 6))
plt.plot(df['z'], df['Temperature'], marker='o', linestyle='-', color='r')
plt.title('Z (Distance Along Z-Axis) vs Temperature')
plt.xlabel('Z (Distance Along Z-Axis) [Angstrom]')
plt.ylabel('Temperature (K)')
plt.grid(True)
plt.show()
