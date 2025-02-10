
#Newtonian method with multiple degrees of freedom
from NewtonMethod import Newton_Method as nm
import pytest
import sympy as sp
import numpy as np


)

# Define symbolic variables for testing
x, y = sp.symbols('x y')

# Sample function system: f1 = x^2 + y^2 - 4, f2 = x*y - 1
function_list = [x**2 + y**2 - 4, x*y - 1]
variable_list = [x, y]
guess_list = [2, 0.5]

# Expected solution (approximately)
expected_solution = sp.Matrix([sp.sqrt(2), 1/sp.sqrt(2)])

# ----------------------------------------------
# TESTS
# ----------------------------------------------

def test_welcome():
    """Test Welcome function output"""
    assert nm.Welcome() == "Welcome To Newtonian Method Solver!"

def test_all_lists():
    """Test all_lists function for correct type validation"""
    # Should pass without raising an error
    nm.all_lists([x+y, x**2], [x, y], [1, 2])

    # Should raise ValueError for incorrect types
    with pytest.raises(ValueError):
        nm.all_lists("not a list", [x, y], [1, 2])

def test_num_eqs_equal_num_variable():
    """Test that function, variable, and guess lists have the same length"""
    # Should pass
    nm.num_eqs_equal_num_variable([x+y, x**2], [x, y], [1, 2])

    # Should raise ValueError if lengths mismatch
    with pytest.raises(ValueError):
        nm.num_eqs_equal_num_variable([x+y, x**2], [x], [1, 2])

def test_max_iterations_reached():
    """Test the max_iterations_reached function"""
    # Should pass
    nm.max_iterations_reached(10, 5)

    # Should raise ValueError when iteration count exceeds max
    with pytest.raises(ValueError):
        nm.max_iterations_reached(10, 15)

def test_substitution_dictionary():
    """Test substitution dictionary creation"""
    variables = sp.Matrix([x, y])
    values = sp.Matrix([1, 2])
    sub_dict = nm.Substitution_dictionary(variables, values)

    expected_dict = {x: 1, y: 2}
    assert sub_dict == expected_dict

def test_populate_jacobian():
    """Test Jacobian matrix substitution"""
    functions = sp.Matrix([x**2 + y, x*y])
    variables = sp.Matrix([x, y])
    values = sp.Matrix([1, 2])

    jacobian = functions.jacobian(variables)
    populated = nm.populate_jacobian(jacobian, variables, values)

    expected_jacobian = sp.Matrix([[2*1, 1], [2, 1]])
    assert populated == expected_jacobian

def test_inverse_jacobian():
    """Test the inverse of a Jacobian matrix"""
    matrix = sp.Matrix([[2, 1], [1, 3]])
    
    # Should pass
    inv_matrix = nm.inverse_jacobian(matrix)
    expected_inv = matrix.inv()
    assert inv_matrix == expected_inv

    # Singular matrix case should raise ValueError
    singular_matrix = sp.Matrix([[1, 2], [2, 4]])
    with pytest.raises(ValueError):
        nm.inverse_jacobian(singular_matrix)

def test_newtonian_solver():
    """Test Newtonian multi-DOF solver on a simple system"""
    solution = nm.Newtonian_multi_DOF(function_list, variable_list, guess_list, tolerance=1e-4)

    # Check if solution is close to expected
    assert solution[0].evalf() == pytest.approx(expected_solution[0].evalf(), rel=1e-4)
    assert solution[1].evalf() == pytest.approx(expected_solution[1].evalf(), rel=1e-4)
