=====================
Big Multiplier
=====================
.. image:: https://travis-ci.org/somedanalytics/big-multiplier.svg?branch=master
    :target: https://travis-ci.org/somedanalytics/big-multiplier


This repository created for matrix multiplication.

The purpose is to prevent being out of memory on GPU.

Doing matrix multiplication is a massive calculation for CPU. However generally GPU rams are not enough. Sometimes it is not possible to place the two of the matrix on the GPU ram.

In this implementation you will find a Theano symbolic multiplication. This function will divide your big matrixes to smaller blocks in order to make possible the calculation on GPU.

Just call the method

``result_sparse_matrix = calculate(sparse_matrix_1, sparse_matrix_2)``

Implementation is using scipy lil and csr sparse matrix.

Install
===============

``pip install bigmultiplier``