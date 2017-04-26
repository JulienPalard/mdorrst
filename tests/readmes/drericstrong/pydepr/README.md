# PyDePr
![PyDePr](https://github.com/drericstrong/pydepr/blob/master/images/pydepr_small.jpg)

[![PyPI version](https://badge.fury.io/py/pydepr.svg)](https://badge.fury.io/py/pydepr)
[![Documentation Status](https://readthedocs.org/projects/pydepr/badge/?version=latest)](http://pydepr.readthedocs.io/en/latest/?badge=latest)

PyDePr ("pie-deeper") is a toolkit designed to facilitate the preprocessing and validation of 
machine learning models. What does that mean? Machine learning models are often 
specialized, requiring years of experience to correctly configure. The hardest 
step is often preprocessing the dataset to be analyzed. An old joke in machine
learning is that 90% of the work is cleaning the dataset, while only 10% is 
actual data analysis.

Keeping that in mind, PyDePr is meant to ease the initial step of model-building
by automatically preprocessing some very specific types of machine learning models.
PyDePr is not meant to build machine learning models for you (there are plenty of
Python libraries for that purpose), and it is not meant to be some sort of  
catch-all solution for all types of machine learning models. However, support for
additional model types will be added as PyDePr is developed.

## Getting Started
PyDePr can be installed using pip:

**pip install pydepr**

**Other required libraries**: matplotlib, numpy, pandas, seaborn, scipy, 
scikit-learn, sympy, statsmodels

PyDePr is integrated tightly with PyeDNA, with static helper functions for 
pulling data directly from eDNA. PyeDNA is not required for most functions
in PyDePr, but it will be loaded if necessary.

## Documentation
Current documentation can be found [here](https://pydepr.readthedocs.io/en/latest/).

## Regression
PyDePr supports the construction of regression models, with built-in
visual model validation. The following features are available:

* Initialize data from either a pandas DataFrame or eDNA
* Automatically perform Ridge Regression
* Calculate model performance metrics
* Build the model equation in a user-friendly form
* Create a series of plots for model validation and visualization

![Regression](/images/Regression.jpg)

## Inference
Inference can be accomplished using time-series evidence within this 
PyDePr module.

* Assign evidence to a conclusion
* Use fuzzy logic to interpolate between conclusions