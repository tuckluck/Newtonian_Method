# Newtonian Method and Elasto Plastic Modeling



[![python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
![os](https://img.shields.io/badge/os-ubuntu%20|%20macos%20|%20windows-blue.svg)
[![license](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/sandialabs/sibl#license)


[![codecov](https://codecov.io/gh/tuckluck/Part1/graph/badge.svg?token=TKF4CLV1G5)](https://codecov.io/gh/tuckluck/Part1)
[![tests](https://github.com/tuckluck/Part1/actions/workflows/tests.yml/badge.svg)](https://github.com/tuckluck/Part1/actions)



ME 700 Assignment 1 - Newtonian Method Solver & Elasto Plastic Modeling (Isotropic Hardening and Kinematic Hardening)

This tutorial aims to show a user how to use two distinct sets of functions. The first is a Newtonian Method solver meant to solve difficult, multi-variable, systems of equations. The function, as outlined below, allows the user to enter an equations, and a guess for the solution. The solver will then find the nearest solution to your guess if there are multiple solutions or the single solution if only one exists. 

Example of calling the function:

from Scripts import Newton_and_ElastoPlastic as nm
nm.Newtonian_multi_DOF([3*x+1],[x],[-5])

The second set of functions allows the user to model isotropic hardening or kinematic hardening of a material. The tutorial on those functions will help illustrate how to run it

I used chatGPT while creating these functions to learn how to read symbols from equation strings, to use the sympy library, to perform calculations by subbing in a number for a variable, to plot a basic chart, and to learn how to set up classes in python. Additionally, i used chatGPT to write the basic outline of my pytest functions before going back through them for accuracy. 

I used Professor Lejeune's bisection_method repo as an outline to structure my README file to run test code. 

To install this package, please begin by setting up a conda environment (mamba also works):
```bash
conda create --name tl_Part1-env python=3.12
```
Once the environment has been created, activate it:

```bash
conda activate tl_Part1-env
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
pytest -v --cov=Newton_and_ElastoPlastic --cov-report term-missing
```
Code coverage should be nearly 100%. Now you are prepared to write your own code based on this method and/or run the tutorial. 

If you would like, you can also open python and check to make sure that the import works properly:
```bash
(tl_Newton-env) $ python
Python 3.12.8 | packaged by Anaconda, Inc. | (main, Dec 11 2024, 11:37:13) [Clang 14.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from Scripts import Newton_and_ElastoPlastic as nm
>>> nm.Welcome()
'Welcome to Newtonian Method Solver!'
```
If you are using VSCode to run this code, don't forget to set VSCode virtual environment to bisection-method-env.

Setup juypter notebook for tutorials

```bash
pip install jupyter
```

Run Newtonian Solver Tutorial
```bash
jupyter notebook Newton_tutorial.ipynb
```
Run ElastoPlastic Modeling Tutorial
```bash
jupyter notebook ElastoPlastic_tutorial.ipynb
```
---

