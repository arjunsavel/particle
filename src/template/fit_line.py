import numpy as np
from scipy.optimize import curve_fit


def exp_func(x, a, b, c):
    """
	An exponential function.

	
	Inputs:
		x : (1D array) x-values to be input into the exponential function.
		a : (float) multiplicative factor for the exponential.
		b : (float) multiplicative factor for the exponentiated x.
		c : (float) additive factor for the exponential function.


	Outputs:
		y : (1D array) The exponentiated function. Same length as x.

	"""
    y = a * np.exp(-b * x) + c
    return y


def fit_line(xdata, ydata, func):
    """
	Fits a line given data.

	Inputs:
		xdata : (1D array) x-values of observed / provided data.
		ydata : (1D array) y-values of observed / provided data.
		func : (function) functional form of curve to be fit.


	Outputs:
		fit_y : (1D array) y-values computed from applying fit
						function to xdata. Same length as
						xdata and ydata.
		popt : (1D array) best-fit parameters for func.

	"""
    popt, pcov = curve_fit(func, xdata, ydata)
    fit_y = func(xdata, *popt)
    return fit_y, popt
