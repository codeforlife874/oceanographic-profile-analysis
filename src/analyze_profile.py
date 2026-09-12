import xarray as xr
import numpy as np
import gsw
# Load dataset
ds = xr.open_dataset("data/profile.nc")

# Extract data
pressure = ds["PRES"].values
temperature = ds["TEMP0"].values
salinity = ds["PSAL0"].values
# Convert pressure to approximate depth using TEOS-10
latitude = float(ds["LATITUDE"].values.squeeze())
depth = -gsw.z_from_p(pressure, latitude)
# Remove missing values
valid_temp = ~np.isnan(temperature)
valid_sal = ~np.isnan(salinity)

pressure_temp = pressure[valid_temp]
temperature = temperature[valid_temp]

pressure_sal = pressure[valid_sal]
salinity = salinity[valid_sal]

# Surface and deepest measurements
surface_temp = temperature[0]
deep_temp = temperature[-1]

surface_sal = salinity[0]
deep_sal = salinity[-1]

# Basic statistics
print("\n--- Oceanographic Profile Analysis ---\n")

print(f"Pressure range: {pressure.min():.1f} - {pressure.max():.1f} dbar")
print(f"Approximate depth range: {depth.min():.1f} - {depth.max():.1f} m")
print(f"\nTemperature:")
print(f"  Surface: {surface_temp:.2f} °C")
print(f"  Deepest: {deep_temp:.2f} °C")
print(f"  Minimum: {temperature.min():.2f} °C")
print(f"  Maximum: {temperature.max():.2f} °C")

print(f"\nSalinity:")
print(f"  Surface: {surface_sal:.2f}")
print(f"  Deepest: {deep_sal:.2f}")
print(f"  Minimum: {salinity.min():.2f}")
print(f"  Maximum: {salinity.max():.2f}")

# Approximate temperature gradient
temp_gradient = np.gradient(temperature, pressure_temp)

strongest_gradient_index = np.argmax(np.abs(temp_gradient))

print("\nStrongest temperature gradient:")
print(
    f"  Pressure: {pressure_temp[strongest_gradient_index]:.1f} dbar"
)
print(
    f"  Gradient: {temp_gradient[strongest_gradient_index]:.4f} °C/dbar"
)

print("\nAnalysis complete.")
# Temperature gradient
temp_gradient = np.gradient(temperature, pressure_temp)

strongest_temp_index = np.argmax(np.abs(temp_gradient))

print("\nStrongest temperature gradient:")
print(
    f"  Pressure: {pressure_temp[strongest_temp_index]:.1f} dbar"
)
print(
    f"  Gradient: {temp_gradient[strongest_temp_index]:.4f} °C/dbar"
)

# Salinity gradient
sal_gradient = np.gradient(salinity, pressure_sal)

strongest_sal_index = np.argmax(np.abs(sal_gradient))

print("\nStrongest salinity gradient:")
print(
    f"  Pressure: {pressure_sal[strongest_sal_index]:.1f} dbar"
)
print(
    f"  Gradient: {sal_gradient[strongest_sal_index]:.4f} /dbar"
)
