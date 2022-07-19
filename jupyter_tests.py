import pytest
import numpy as np
import subprocess
####
import sys,os
####
from jupyter_assignment import READ_INTRODUCTION, LEARNED_ABOUT_JUPYTER, ACCESS_COLABORATORY, CREATED_GITHUB_ACCOUNT, github_username, my_name, greet
from matplotlib_assignment import Student_ID, task_id, my_function

    
#from test_image import CNT_Values
CNT_argv=[4,3,3,3,3,
          4,4,4,3,4,
          2,3,3,0,4,
          3,2,3,4,3,
          4,3,3,4,3]
import os


score = 0.0


def test_read_introduction():
    global score
    assert READ_INTRODUCTION == True, "Please, read the instruction!"
    score += 0.1
    # print(f"Score is {score}")


def test_learn_jupyter():
    global score
    assert LEARNED_ABOUT_JUPYTER == True, "Please, learn about Jupyter!"
    score += 0.1
    # print(f"Score is {score}")


def test_access_colaboratory():
    global score
    assert ACCESS_COLABORATORY == True, "Please, configure Google Colab!"
    score += 0.1


def test_create_github():
    global score
    assert CREATED_GITHUB_ACCOUNT == True, "Please, create a GitHub Account!"
    score += 0.1
    

def test_greet():
    global score
    assert greet(my_name) == f"Hello, {my_name}!"
    assert greet("Test User") == "Hello, Test User!"
    score += 0.6


def test_github():
    # print(os.getenv('GITHUB_REPOSITORY'))
    # print(github_username)
    assert os.getenv('GITHUB_REPOSITORY', '').endswith(github_username), f"Your GitHub username doesn't match. Did you forget to update 'github_username' variable or are you trying to cheat by submitting someone else's work?"

#File tests matplotlib_assignment.py
def test_student_id():
    if Student_ID is not None:
        assert Student_ID > 0 and Student_ID < 100, "Invalid Student ID!"


def test_task_id():
    if Student_ID is not None:
        assert task_id > 0 and task_id <= 25, "Invalid task ID!"
        
def test_value():
    global score
    param=["a","b","c","d","x","y"]
    del param[CNT_argv[task_id-1]:4]
    for t in param:
        assert exec("from matplotlib_assignment import "+str(t))==None,f"Create a variable '{t}'!Don't forget to initialize it"
        if (t != "x") and (t != "y"):
            assert isinstance( eval(t), (int, float) ),f"The variable '{t}' is not an int or float!"
        else:
            assert isinstance( eval(t), (list,tuple,np.ndarray) ),f"The variable '{t}' is not an array!"
    score += 1
        
#def test_create_images():
    #global score
    #c=subprocess.run("pytest --mpl-generate-path=images_of_graphs Add_img_13.py", shell=True)
    #assert c.returncode==0,"Image not generate!"
    #score += 1
    
#def test_formula():
    #global score
    #c=subprocess.run("pytest --mpl test_formula_img.py", shell=True)
    #assert c.returncode==0,"Incorrect formula in my_function!"
    #score += 1 
    
def test_images():
    global score
    c=subprocess.run("pytest --mpl test_img.py", shell=True)
    assert c.returncode==0,"Incorrect image!"
    score += 1
    
def test_Latex_formula():
    global score
    c=subprocess.run("pytest --mpl test_Latex.py", shell=True)
    assert c.returncode==0,"Incorrect Latex formula!"
    score += 1   
  
def test_maths():
    if Student_ID is not None:
        import numpy as np
        import math
        if task_id == 1:
            assert my_function(np.array([1]),1,1,1,1) == 4,"Incorrect formula in my_function!"
            assert my_function(np.array([2]),2,2,2,2) == 78,"Incorrect formula in my_function!"
        elif task_id == 2:
            assert math.isclose(my_function(np.array([0]),2,2,3),0.28, abs_tol = 0.1),"Incorrect formula in my_function!"
            assert math.isclose(my_function(np.array([2]),2,1,2),-1.51, abs_tol = 0.1),"Incorrect formula in my_function!"
        elif task_id == 3:
            assert math.isclose(my_function(np.array([0]),3,2,1),1.56, abs_tol = 0.1),"Incorrect formula in my_function!"
            assert math.isclose(my_function(np.array([1]),1,2,0),-0.14, abs_tol = 0.1),"Incorrect formula in my_function!"
        elif task_id == 4:
            assert math.isclose(my_function(np.array([0]),2,1,3),0, abs_tol = 0.1),"Incorrect formula in my_function!"
            assert math.isclose(my_function(np.array([1]),2,3,0),2.2, abs_tol = 0.1),"Incorrect formula in my_function!"
        elif task_id == 5:
            assert math.isclose(my_function(np.array([1]),5,2,4),-8.96, abs_tol = 0.1),"Incorrect formula in my_function!"
            assert math.isclose(my_function(np.array([2]),2,1,2),-1.83, abs_tol = 0.1),"Incorrect formula in my_function!"
        elif task_id == 6:
            assert math.isclose(my_function(np.array([0]),3,4,2,10),0.3, abs_tol = 0.1),"Incorrect formula in my_function!"
            assert math.isclose(my_function(np.array([2]),1,1,0,2),2.58, abs_tol = 0.1),"Incorrect formula in my_function!"
        elif task_id == 7:
            assert math.isclose(my_function(np.array([0]),3,3,2,2),4, abs_tol = 0.1),"Incorrect formula in my_function!"
            assert math.isclose(my_function(np.array([1]),4,3,1,2),256, abs_tol = 0.1),"Incorrect formula in my_function!"
        elif task_id == 8:
            assert math.isclose(my_function(np.array([1]),10,10,5,1),-0.11, abs_tol = 0.1),"Incorrect formula in my_function!"
            assert math.isclose(my_function(np.array([3]),2,5,4,1),0.67, abs_tol = 0.1),"Incorrect formula in my_function!"
        elif task_id == 9:
            assert math.isclose(my_function(np.array([0]),4,-2,4), 0.34, abs_tol = 0.1),"Incorrect formula in my_function!"
            assert math.isclose(my_function(np.array([1]),5,-2,4), 0.13, abs_tol = 0.1),"Incorrect formula in my_function!"
        elif task_id == 10:
            assert math.isclose(my_function(np.array([0]),1,1,1,1), 0, abs_tol = 0.1),"Incorrect formula in my_function!"
            assert math.isclose(my_function(np.array([1]),0,5,2,2), 1.82, abs_tol = 0.1),"Incorrect formula in my_function!"
        elif task_id == 11:
            assert math.isclose(my_function(np.array([1]),8,1), 6.73, abs_tol = 0.1),"Incorrect formula in my_function!"
            assert math.isclose(my_function(np.array([2]),2,2), -6.05, abs_tol = 0.1),"Incorrect formula in my_function!"
        elif task_id == 12:
            assert math.isclose(my_function(np.array([1]),1,6,2), 1.72, abs_tol = 0.1),"Incorrect formula in my_function!"
            assert math.isclose(my_function(np.array([2]),3,32,2), 3.38, abs_tol = 0.1),"Incorrect formula in my_function!"
        elif task_id == 13:
            assert math.isclose(my_function(np.array([0]),1,1,2), 2, abs_tol = 0.1),"Incorrect formula in my_function!"
            assert math.isclose(my_function(np.array([2]),2,1,3), 1, abs_tol = 0.1),"Incorrect formula in my_function!"
        elif task_id == 14:
            tmp=my_function(np.array([0]))
            assert math.isclose(tmp[0][0],0, abs_tol = 0.1) and math.isclose(tmp[0][1],-np.pi, abs_tol = 0.1),"Incorrect formula in my_function!"
            tmp=my_function(np.array([1]))
            assert math.isclose(tmp[0][0],1, abs_tol = 0.1) and math.isclose(tmp[0][1],-1.57, abs_tol = 0.1),"Incorrect formula in my_function!"
        elif task_id == 15:
            assert math.isclose(my_function(np.array([1]),1,1,1,1), 4, abs_tol = 0.1),"Incorrect formula in my_function!"
            assert math.isclose(my_function(np.array([2]),0,1,2,0), 8, abs_tol = 0.1),"Incorrect formula in my_function!"
        elif task_id == 16:
            assert math.isclose(my_function(np.array([0]),3,3,3), 0, abs_tol = 0.1),"Incorrect formula in my_function!"
            assert math.isclose(my_function(np.array([2]),4,1,2), 8.27, abs_tol = 0.1),"Incorrect formula in my_function!"
        elif task_id == 17:
            assert math.isclose(my_function(np.array([-1]),5,1), 2.7, abs_tol = 0.1),"Incorrect formula in my_function!"
            assert math.isclose(my_function(np.array([1]),4,2), -1.66, abs_tol = 0.1),"Incorrect formula in my_function!"
        elif task_id == 18:
            assert math.isclose(my_function(np.array([0]),1.5,0.5,1), 0.81, abs_tol = 0.1),"Incorrect formula in my_function!"
            assert math.isclose(my_function(np.array([1]),4,0.5,2), -3.2, abs_tol = 0.1),"Incorrect formula in my_function!"
        elif task_id == 19:
            assert math.isclose(my_function(np.array([0]),1,1,1,1), 1, abs_tol = 0.1),"Incorrect formula in my_function!"
            assert math.isclose(my_function(np.array([1]),0.5,2,5,3), -4.5, abs_tol = 0.1),"Incorrect formula in my_function!"
        elif task_id == 20:
            assert math.isclose(my_function(np.array([1]),5,-3,1), -3.95, abs_tol = 0.1),"Incorrect formula in my_function!"
            assert math.isclose(my_function(np.array([2]),5,-3,1), 3.4, abs_tol = 0.1),"Incorrect formula in my_function!"
        elif task_id == 21:
            assert math.isclose(my_function(np.array([1]),1,1,1,1), 4, abs_tol = 0.1),"Incorrect formula in my_function!"
            assert math.isclose(my_function(np.array([2]),1,-3,1,2), -4, abs_tol = 0.1),"Incorrect formula in my_function!"
        elif task_id == 22:
            assert math.isclose(my_function(np.array([1],dtype=float),6,2,2), 6, abs_tol = 0.1),"Incorrect formula in my_function!"
            assert math.isclose(my_function(np.array([2]),5,1,-10), 320, abs_tol = 0.1),"Incorrect formula in my_function!"
        elif task_id == 23:
            assert math.isclose(my_function(np.array([2]),10,2,1), 0.26, abs_tol = 0.1),"Incorrect formula in my_function!"
            assert math.isclose(my_function(np.array([0.03]),2,7,10), 1.05, abs_tol = 0.1),"Incorrect formula in my_function!"
        elif task_id == 24:
            assert math.isclose(my_function(np.array([0.05]),5,2,1,1), -26.74, abs_tol = 0.1),"Incorrect formula in my_function!"
            assert math.isclose(my_function(np.array([1]),4,1,2,1), -4.39, abs_tol = 0.1),"Incorrect formula in my_function!"
        elif task_id == 25:
            assert math.isclose(my_function(np.array([0]),2,3,2), -0.46, abs_tol = 0.1),"Incorrect formula in my_function!"
            assert math.isclose(my_function(np.array([1]),3,4,5), -1.57, abs_tol = 0.1),"Incorrect formula in my_function!"


@pytest.fixture(scope="session", autouse=True)
def cleanup(request):
    def print_score():
        global score
        if greet(3.14) == "Hello, 3.14!" and greet(42) == "Hello, 42!":
            score += 0.15
        if greet(['Alice']) == "Hello, Alice!":
            score += 0.15
        if greet(['Alice', 'Bob', 'Charlie']) == "Hello, Alice, Bob and Charlie!":
            score += 0.3
        if greet(['Alice', 3.14, {'key'}]) == "Hello, Alice, 3.14 and {'key'}!":
            score += 0.4
        print(f"\nScore is {score}")
    request.addfinalizer(print_score)
# def pytest_report_header(config):
#     return f"Score is {score}"
    
# print(f"Score is {score}")
