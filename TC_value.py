# Constants for unit conversion
eV_to_J = 1.60218e-19      # Energy: 1 eV = 1.60218e-19 J
ps_to_s = 1e-12            # Time: 1 ps = 1e-12 s
A_to_m = 1e-10             # Length: 1 Å = 1e-10 m

# Take inputs from the user
dqdt_eV_ps = float(input("Enter the heat flux rate (dq/dt) in eV/ps: "))
dTdz_K_per_A = float(input("Enter the temperature gradient (dT/dZ) in K/Å: "))
A_A2 = float(input("Enter the cross-sectional area (A) in Å²: "))

# Convert dq/dt from eV/ps to J/s (Watts)
dqdt_J_s = dqdt_eV_ps * eV_to_J / ps_to_s

# Convert dT/dZ from K/Å to K/m
dTdz_K_m = dTdz_K_per_A * 1e10   # Since 1 Å = 1e-10 m, so 1 K/Å = 1e10 K/m

# Convert A from Å² to m²
A_m2 = A_A2 * (A_to_m)**2

# Calculate thermal conductivity k using Fourier's Law
# k = (dq/dt) / ( (dT/dZ) * A )
k = dqdt_J_s / (dTdz_K_m * A_m2)

# Display the result
print(f"\nThe thermal conductivity k is: {k:.4f} W/(m·K)")
