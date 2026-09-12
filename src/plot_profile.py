import xarray as xr
import matplotlib.pyplot as plt


# Load NOAA CTD profile
ds = xr.open_dataset("data/profile.nc")

# Extract variables
pressure = ds["PRES"].values
temperature = ds["TEMP0"].values
salinity = ds["PSAL0"].values

# Create figure
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Temperature profile
ax[0].plot(temperature, pressure)
ax[0].invert_yaxis()
ax[0].set_xlabel("Temperature (°C)")
ax[0].set_ylabel("Pressure (dbar)")
ax[0].set_title("Temperature Profile")
ax[0].grid(True)

# Salinity profile
ax[1].plot(salinity, pressure)
ax[1].invert_yaxis()
ax[1].set_xlabel("Salinity")
ax[1].set_ylabel("Pressure (dbar)")
ax[1].set_title("Salinity Profile")
ax[1].grid(True)

plt.tight_layout()

# Save figure
plt.savefig(
    "figures/ocean_profile.png",
    dpi=300,
    bbox_inches="tight"
)

print("Analysis complete.")
print("Figure saved to figures/ocean_profile.png")
