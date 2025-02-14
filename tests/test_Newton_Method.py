import pytest
import sympy as sp
import numpy as np
from Scripts import Newton_and_ElastoPlastic as nm
   


# --------------------------------
# SYMBOLIC VARIABLES FOR TESTING
# --------------------------------
x, y, z = sp.symbols('x y z')

# Sample function system:
# f1 = x^2 + y^2 - 4, f2 = x*y - 1
function_list  = [3*x+2*y-z-1,2*x-2*y+4*z+2,-x+.5*y-z]
variable_list  = [x, y, z]
guess_list     = [10, 3, 2]

# Expected solution (approximately)
expected_solution = sp.Matrix([1,-2,-2])


# --------------------------------
# BASIC FUNCTION TESTS
# --------------------------------

def test_welcome():
    """Test the Welcome function"""
    assert nm.Welcome() == "Welcome To Newtonian Method Solver!"


# --------------------------------
# VALIDATION FUNCTION TESTS
# --------------------------------

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


# --------------------------------
# MATRIX MANIPULATION TESTS
# --------------------------------

def test_substitution_dictionary():
    """Test substitution dictionary creation"""
    
    variables = sp.Matrix([x, y])
    values    = sp.Matrix([1, 2])
    
    sub_dict  = nm.Substitution_dictionary(variables, values)
    expected  = {x: 1, y: 2}

    assert sub_dict == expected


def test_populate_jacobian():
    """Test Jacobian matrix substitution"""
    
    functions  = sp.Matrix([x**2 + y, x*y])
    variables  = sp.Matrix([x, y])
    values     = sp.Matrix([1, 2])

    jacobian   = functions.jacobian(variables)
    populated  = nm.populate_jacobian(jacobian, variables, values)

    expected   = sp.Matrix([[2*1, 1], [2, 1]])

    assert populated == expected


def test_inverse_jacobian():
    """Test the inverse of a Jacobian matrix"""
    
    matrix        = sp.Matrix([[2, 1], [1, 3]])
    inv_matrix    = nm.inverse_jacobian(matrix)
    expected_inv  = matrix.inv()

    # Should pass
    assert inv_matrix == expected_inv

    # Singular matrix case should raise ValueError
    singular_matrix = sp.Matrix([[1, 2], [2, 4]])
    
    with pytest.raises(ValueError):
        nm.inverse_jacobian(singular_matrix)


# --------------------------------
# NEWTONIAN SOLVER TEST
# --------------------------------

def test_newtonian_multi_DOF():
    """Test Newtonian multi-DOF solver on a simple system"""

    solution = nm.Newtonian_multi_DOF(
        function_list, variable_list, guess_list, tolerance=1e-4, max_iterations=100
    )

    # Convert to float before comparing
    sol_0 = float(solution[0].evalf())
    sol_1 = float(solution[1].evalf())
    sol_2 = float(solution[2].evalf())

    exp_0 = float(expected_solution[0].evalf())
    exp_1 = float(expected_solution[1].evalf())
    exp_2 = float(expected_solution[2].evalf())

    assert sol_0 == pytest.approx(exp_0, rel=1e-4)
    assert sol_1 == pytest.approx(exp_1, rel=1e-4)
    assert sol_2 == pytest.approx(exp_2, rel=1e-4)
