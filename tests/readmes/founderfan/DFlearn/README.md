[![Latest Release](https://img.shields.io/pypi/v/dflearn.svg)](https://pypi.python.org/pypi/dflearn/)
[![License](https://img.shields.io/pypi/l/dflearn.svg)](https://pypi.python.org/pypi/dflearn/)
[![Build Status](https://travis-ci.org/founderfan/DFlearn.svg?branch=master)](https://travis-ci.org/founderfan/DFlearn)

A data analysis and machine-learning toolset using pandas DataFrame and scikit-learn models.

## Install

```sh
pip install dflearn
```

## Dependencies

- [numpy](http://www.numpy.org): 1.11.0 or higher
- [scipy](https://www.scipy.org/): 0.18.0 or higher
- [pandas](http://pandas.pydata.org/): 0.19.0 or higher
- [statsmodels](http://www.statsmodels.org/): 0.6.0 or higher
- [scikit-learn](http://scikit-learn.org/): 0.18.0 or higher
- [nltk](http://www.nltk.org/): 3.0.0 or higher

## Contents

- MLtools: machine learning tools, main toolset
    - Whole dataset
        - Data summary
            - Variable type, NA/non-NA values, numeric summary statistics, most frequent values.
        - Data cleaning
            - Categorical variables transformation into dummy variables.
            - Numeric variables standarzation/normalization with imputation.
            - Sparse variables deletion.
            - Collinear variables deletion.
    - Machine learning
        - Training/validation set creation
            - Single training/validation set split.
            - Cross-validation set creation.
            - Cross-join with different models.
        - Model training
            - Scikit-learn like regression/classification.
        - Variable analysis
            - Variable importance inference (tree models, random forest interactions)
            - Bayesian inference of high-dimensional linear coefficients summary.
        - Validation and error analysis
            - Model effects inference on cross-validation loss with linear mixed model

- NLtools: natural language tools, waiting for development
    - Clean text
    - Word tokenize

- SNPtools: used for genetic SNP data, not general
    - [PLINK](https://www.cog-genomics.org/plink2) binary data reading
    - Risk score calculation

## License

MIT license