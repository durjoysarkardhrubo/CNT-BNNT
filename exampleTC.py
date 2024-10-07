#!/usr/bin/env amspython
from scm.plams import *
import numpy as np


def main():
    # Unit conversion factors
    eV_to_J = Units.convert(1.0, "eV", "J")
    fs_to_s = Units.convert(1.0, "fs", "s")
    ang_to_m = Units.convert(1.0, "angstrom", "m")

    # length L and cross-sectional area S
    L = 36.15 * ang_to_m  # m
    S = 281.9 * ang_to_m**2  # m^2

    # manually calculated slope and delta_T
    dEdt = 4.41e-5 * eV_to_J / fs_to_s  # J s^-1 = W
    delta_T = 20  # K

    # automatically calculated slope
    # job = AMSJob.load_external("jobname.results")
    # dEdt = get_slope(job, min_time_fs=100000)
    # delta_T = get_delta_T(job)

    # calculate thermal conductivity k
    k = (dEdt * L) / (2 * S * delta_T)

    print(f"Thermal conductivity: {k:.3f} W m^-1 K^-1")


def get_slope(job, min_time_fs=0):
    """
    Calculates the (absolute value of the) slope of NHCTstat2Energy.

    Discards the first min_time_fs from the trajectory.

    Returns: float. The slope in W ( = J/s)
    """
    from scipy.stats import linregress

    time = job.results.get_history_property("Time", history_section="MDHistory")
    time = np.array(time)  # time in fs

    nhctstatenergy = job.results.get_history_property("NHCTstat2Energy", history_section="MDHistory")
    nhctstatenergy = np.array(nhctstatenergy)  # energy in hartree

    ind = time >= min_time_fs
    time = time[ind]
    nhctstatenergy = nhctstatenergy[ind]

    result = linregress(time, nhctstatenergy)

    # take absolute value, convert to watt (J/s)
    slope = np.abs(result.slope) * Units.convert(1.0, "hartree", "J") / Units.convert(1.0, "fs", "s")

    return slope


def get_delta_T(job):
    """
    Assume there are two Thermostats and take the difference of their temperatures

    Returns: float. The difference in temperature in Kelvin
    """
    t = job.settings.input.ams.MolecularDynamics.Thermostat
    assert isinstance(t, list) and len(t) == 2, f"get_delta_T can only be called if there are exactly two thermostats"

    delta_T = abs(float(t[0].Temperature) - float(t[1].Temperature))
    return delta_T


if __name__ == "__main__":
    main()