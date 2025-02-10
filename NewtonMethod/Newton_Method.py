
#Newtonian method with multiple degrees of freedom

import numpy as np
import sympy as sp

q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m = sp.symbols('q w e r t y u i o p a s d f g h j k l z x c v b n m')
symb_matrix = sp.Matrix([q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m])
#sets up all possible letters as possible variables so the user has flexibility with how they want to set up their equations


def Welcome(): 
    #function purpose is to test to make sure import worked correctly
    return "Welcome To Newtonian Method Solver!"

def all_lists(function_list,variable_list,guess_list):
    #tests to make sure all input variables are lists
    if type(function_list) == type(variable_list) == type(guess_list) == list:
        return
    else:
        raise ValueError("All inputs must be type: lists ex. [3*x,3*z],[x,z],[1,2]") 

def max_iterations_reached(maximum,current):
    # function tests to make sure the while loop within the function does not run indefinitly, so a user can check for issues
    if current > maximum:
        raise ValueError("Maximum Iterations Rearched, your guess or equations may be incorrect")
    return        

def num_eqs_equal_num_variable(function_list,variable_list,guess_list):
    # function tests to make sure all input lists are of the same length
    if len(function_list) == len(variable_list) == len(guess_list):
        return
    else:
        raise ValueError("All input lists must be the same length, number of equations should match number of unknown variables")

def Substitution_dictionary(variables,values):
    # function sets up a dictionary which assigns each variable to the current guess for that variable
    # the function is used for subbing values into the function matrix and jacobian matrix which are 
    # filled with variables
    variables_T = variables.T
    values_T = values.T
    sub_dict = {variables_T[i]: values_T[i] for i in range(variables_T.shape[1])}
    return sub_dict

def populate_jacobian(jacobian,variables,values):
    #function is used to populate the jacobian matrix with values instead of variables, the substituion
    #dictionary function helps with choosing the correct value to sub in for each variable
    jacobian_values = jacobian.subs(Substitution_dictionary(variables,values))
    return jacobian_values

def populate_functions(functions,variables,values):
    #this function is used to populate the function matrix with values instead of variables, similar to 
    #the jacobian matrix, it subs in values using the substitution dictionary
    F_values = functions.subs(Substitution_dictionary(variables,values))
    return F_values

def inverse_jacobian(jacobian_new):
    #this funciton takes the inverse of the jacobian for the calculation in the while loop in the main function
    #this function will spit out an error if the inverse of the jacobian is not possible
    if jacobian_new.det()!=0:
        inv_jacobian = jacobian_new.inv()
        return inv_jacobian
    else:
        raise ValueError("Maximum Iterations Rearched, your guess or equations may be incorrect")
        
    
def Newtonian_multi_DOF(function_list,variable_list,guess_list,tolerance = .1, max_iterations = 100):
    num_eqs_equal_num_variable(function_list,variable_list,guess_list)   #tests to make sure all lists are of same length
    all_lists(function_list,variable_list,guess_list) #tests to make sure all inputs are lists
    functions = sp.Matrix(function_list)              #turns list into matrix
    variables = sp.Matrix(variable_list)              #turns list into matrix
    guesses = sp.Matrix(guess_list)                   #turns list into matrix
    var_jacobian = functions.jacobian(variables)      #creates the jacobian matrix from the function and variavbles chosen
    
    xn = guesses                                    # initializes xn matrix with our initial guesses
    F = populate_functions(functions,variables,xn)  #F is the function matrix with guesses subbed in for variables
    count = 0                                       # initialize the count to break out of the while loop if too many iterations
    while F.norm() > tolerance:                     # compares value to chosen tolerance
        val_jacobian = populate_jacobian(var_jacobian,variables,xn)   #fills variable jacobian with current guesses
        F = populate_functions(functions,variables,xn)                #fills variable functions with current guesses
        del_x = -inverse_jacobian(val_jacobian)*F                     #calculates delta x
        xn = xn + del_x                                               #improves guess list
        count = count+1                                               #updates count
        max_iterations_reached(max_iterations,count)                  #breaks out of while loop if max iterations reached
        
    solution_float = xn.evalf()
    
    return solution_float
    
    
    
    
    
    
