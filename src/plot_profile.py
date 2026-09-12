import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

# Load NOAA CTD profile
ds = xr.open_dataset("data/profile.nc")

# Extract variables
pressure = ds["PRES"].values
temperature = ds["TEMP0"].values
salinity = ds["PSAL0"].values

# Remove missing values
valid_temp = ~np.isnan(temperature)
valid_sal = ~np.isnan(salinity)

pressure_temp = pressure[valid_temp]
temperature = temperature[valid_temp]

pressure_sal = pressure[valid_sal]
salinity = salinity[valid_sal]

# Calculate temperature gradient
temp_gradient = np.gradient(temperature, pressure_temp)
strongest_temp_index = np.argmax(np.abs(temp_gradient))
thermocline_pressure = pressure_temp[strongest_temp_index]

# Create figure
fig, ax = plt.subplots(1, 2, figsize=(12, 7))

# Temperature profile
ax[0].plot(temperature, pressure_temp, linewidth=2)
ax[0].axhline(
    thermocline_pressure,
    linestyle="--",
    linewidth=1.5,
    label=f"Strongest gradient: {thermocline_pressure:.0f} dbar"
)

ax[0].invert_yaxis()
ax[0].set_xlabel("Temperature (°C)")
ax[0].set_ylabel("Pressure (dbar)")
ax[0].set_title("Temperature Profile")
ax[0].grid(True, alpha=0.3)
ax[0].legend()

# Salinity profile
ax[1].plot(salinity, pressure_sal, linewidth=2)

ax[1].invert_yaxis()
ax[1].set_xlabel("Salinity")
ax[1].set_ylabel("Pressure (dbar)")
ax[1].set_title("Salinity Profile")
ax[1].grid(True, alpha=0.3)

plt.suptitle(
    "NOAA CTD Temperature and Salinity Profile\n"
    "TAO Site KA-09-01 | 2.02°N, 155°W",
    fontsize=14
)

plt.tight_layout()

# Save figure
plt.savefig(
    "figures/ocean_profile.png",
    dpi=300,
    bbox_inches="tight"
)

print("Updated figure saved to figures/ocean_profile.png")
print(f"Strongest temperature gradient: {thermocline_pressure:.0f} dbar")
