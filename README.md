# Newtonian_Method



[![python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
![os](https://img.shields.io/badge/os-ubuntu%20|%20macos%20|%20windows-blue.svg)
[![license](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/sandialabs/sibl#license)





ME 700 Assignment 1 - Newton Solver 

This tutorial aims to show a user how to use the "bisect_warmup" function to solve difficult, single variable ("x"), algebraic equations using the bisect method. The function, as outlined below, allows the user to enter an equation, a lower bound estimate for the possible solution and an upper bound estimate for the possible solution. The user should enter the equation as a string using quotations (ex. "3*x = 3"). 

Example of calling the function:
from tl_bisect import bisect_warmup
bisect_warmup("3*x=3",0,2)

I used chatGPT while creating this function to learn how to read symbols from equation strings, to use the sympy library and to perform calculations by subbing in a number for a variable.

To install this package, please begin by setting up a conda environment (mamba also works):
```bash
conda create --name tl_Newton-env python=3.12
```
Once the environment has been created, activate it:

```bash
conda activate tl_Newton-env
```
Double check that python is version 3.12 in the environment:
```bash
python --version
```
Ensure that pip is using the most up to date version of setuptools:
```bash
pip install --upgrade pip setuptools wheel
```
Create an editable install of the Newtonian method code (note: you must be in the correct directory):
```bash
pip install -e .
```


Test that the code is working with pytest:
```bash
pytest -v --cov=Newtonian_Method --cov-report term-missing
```
Code coverage should be 100%. Now you are prepared to write your own code based on this method and/or run the tutorial. 

If you would like, you can also open python and check to make sure that the import works properly:
```bash
(tl_Newton-env) $ python
Python 3.12.8 | packaged by Anaconda, Inc. | (main, Dec 11 2024, 11:37:13) [Clang 14.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from NewtonMethod import Newton_Method as nm
>>> nm.Welcome()
'Welcome to Newtonian Method Solver!'
```
If you are using VSCode to run this code, don't forget to set VSCode virtual environment to bisection-method-env.

Open in Juypter

```bash
pip install jupyter
```

```bash
jupyter notebook Newton_tutorial.ipynb
```
---

