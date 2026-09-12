# Oceanographic Temperature & Salinity Profile Analysis

## Overview

This project analyzes a publicly available NOAA oceanographic CTD profile using Python in a Linux/WSL environment.

The analysis examines how temperature and salinity vary with pressure through the sampled ocean water column.

## Dataset

The dataset is a CTD profile from NOAA's National Data Buoy Center (NDBC).

## Methodology

1. Load the NOAA CTD NetCDF dataset using `xarray`.
2. Extract pressure, temperature, and salinity measurements.
3. Convert pressure to approximate depth using the TEOS-10 Gibbs SeaWater (`gsw`) library and the profile latitude.
4. Calculate temperature and salinity gradients with respect to pressure.
5. Identify the pressure corresponding to the strongest temperature gradient.
6. Visualize temperature and salinity profiles against approximate depth.
7. Save the resulting visualization as a high-resolution PNG.- Platform: TAO mooring
- Site: KA-09-01
- Location: 2.02°N, 155°W
- Date: 11 May 2009
- Measurement type: CTD
- Data format: NetCDF

The dataset contains pressure, temperature, and salinity measurements.
## Technologies

- Python
- xarray
- NumPy
- Matplotlib
- NetCDF
- Gibbs SeaWater (GSW / TEOS-10)
- Linux / WSL2
## Results

The analyzed CTD profile spans a pressure range of 2–1001 dbar, corresponding to an approximate depth range of 2–993 m.

### Temperature

- Surface temperature: 28.23 °C
- Deepest measured temperature: 4.57 °C
- Maximum temperature: 28.24 °C
- Minimum temperature: 4.57 °C
- Strongest temperature gradient: -0.6530 °C/dbar at 122 dbar
- Approximate depth of strongest temperature gradient: 121 m

The pronounced temperature transition around 121 m indicates a strong thermocline-region structure in the sampled upper ocean.

### Salinity

- Surface salinity: 35.01
- Deepest salinity: 34.56
- Minimum salinity: 34.55
- Maximum salinity: 35.14
- Strongest salinity gradient: -0.0305/dbar at approximately 118 dbar

The temperature and salinity profiles both exhibit pronounced changes in approximately the same upper-ocean pressure range.

![Oceanographic Profiles](figures/ocean_profile.png)
## Project Structure

```text
ocean-profile/
├── data/
│   └── profile.nc
├── figures/
│   └── ocean_profile.png
├── src/
│   └── plot_profile.py
├── requirements.txt
├── .gitignore
└── README.md
