API Reference
=============

Package Structure
-----------------
The package structure is simple, with 5 main modules:
   1. `io`: Translating from custom & proprietary microscope formats to HDF5.
   2. `processing`: Multivariate Statistics, Machine Learning, and Filtering.
   3. `analysis`: Model-dependent analysis of image information.
   4. `viz`: Visualization and interactive slicing of high-dimensional data by lightweight Qt viewers.
   5. `core`: Core components that handle the file I/O, processing framework and visualization utilities

.. currentmodule:: pycroscopy

.. automodule:: pycroscopy
    :no-members:
    :no-inherited-members:

:py:mod:`pycroscopy`:

.. autosummary::
    :toctree: _autosummary/
    :template: module.rst

    pycroscopy.core
    pycroscopy.analysis
    pycroscopy.io
    pycroscopy.processing
    pycroscopy.viz
