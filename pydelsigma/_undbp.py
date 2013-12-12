# -*- coding: utf-8 -*-
# _undbp.py
# This module provides the undbp function.
# Copyright 2013 Giuseppe Venturini
# This file is part of python-deltasigma.
#
# python-deltasigma is a 1:1 Python replacement of Richard Schreier's 
# MATLAB delta sigma toolbox (aka "delsigma"), upon which it is heavily based.
# The delta sigma toolbox is (c) 2009, Richard Schreier.
#
# python-deltasigma is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# LICENSE file for the licensing terms.

"""This module provides the undbp() function.
"""
from __future__ import division
import numpy as np

from ._utils import carray, save_input_form, restore_input_form

def undbp(x):
	"""Convert ``x`` from dB to a power, according to the relationship:

	.. math::

	    P_{\\mathrm{RMS}} = 10^{x/10}

	**Parameters:**

	x : scalar or sequence
	    The signal in dB to be converted.

	**Returns:**

	Prms : scalar or sequence
	       The RMS power corresponding to x.
	"""
	iform = save_input_form(x)
	x = carray(x)
	up = 10.**(x/10.)
	return restore_input_form(up, iform)
	
def test_undbp():
	"""Test function for undbp()"""
	assert np.allclose([undbp(53.05)], [201836.636368], rtol=1e-05, atol=1e-08)
	assert np.allclose([undbp(3)], [1.99526231497], rtol=1e-05, atol=1e-08)

