import pytest

from jupyter_assignment import READ_INTRODUCTION, LEARNED_ABOUT_JUPYTER, ACCESS_COLABORATORY, CREATED_GITHUB_ACCOUNT, github_username, my_name, greet

from matplotlib_assignment import Student_ID, task_id, my_function

    
#from test_image import CNT_Values
CNT_Values = 3
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
        
#def test_values():    
    #global score
    #global CNT_Values
   # try:
        #from matplotlib_assignment import a,b,c,d,x,y
    #except ImportError:
        #pass
    #CNT_Values = 3
    #tmp = globals()
   # print("globals!=%s",tmp)
    #from test_image import CNT_Values
   # if CNT_Values >= 1:
     #   assert 'a' in tmp,f"Problems a 'a'={tmp}"
     #   assert 'a' not in tmp,f"lll={tmp}"
        #and (isinstance(tmp['a'],(int, float)) )
        #CNT_Values = CNT_Values - 1
        #if CNT_Values >= 1:
            #assert ( ('b' in tmp) and (isinstance(tmp['b'],(int, float)) ),f"Problems a 'b'"
            #CNT_Values -= 1
            #if CNT_Values >= 1 :
                #assert ( 'c' in tmp ) and (type(tmp['c']) == int or float),f"Problems a 'c'"
                #CNT_Values -= 1
                #if CNT_Values >= 1 :
                    #assert ( 'd' in tmp ) and (type(tmp['d']) == int or float),f"Problems a 'd'"

    #assert ( 'x' in tmp ) and ( isinstance(tmp['x'], (list, tuple, np.array)) ),f"Problems a 'x'"
    #assert ( 'y' in tmp ) and ( isinstance(tmp['y'], (list, tuple, np.array)) ),f"Problems a 'y'"
   # score += 1
def test_value():
    global score
    param=["a","b","c","d","x","y"]
    #for t in param:
       # try:
       #     exec("from matplotlib_assignment import "+str(t))
       # except ImportError:
       #     print("ggggggg=")
       #     print(t)
    del param[CNT_Values:4]
    for t in param:
        assert exec("from matplotlib_assignment import "+str(t))==None,f"Create a variable '{t}'!Don't forget to initialize it"
        if (t not "x") and (t not "y"):
            assert (isinstance(t,(int, float)),f"The variable '{t}' is not an int or float!"
        else:
            assert (isinstance(t,(list, tuple, np.array)),f"The variable '{t}' is not an array!"
    score += 1
        
#def test_create_images():
    #if task_id is not None:
        #assert subprocess.call("pytest --mpl-generate-path=baseline Create_img_"+str(task_id)+".py", shell=True)
        
def test_maths():
    if Student_ID is not None:
        import numpy as np
        import math
        if task_id == 1:
            assert my_function(np.array([1]),1,1,1,1) == 4
            assert my_function(np.array([2]),2,2,2,2) == 78
        elif task_id == 2:
            assert math.isclose(my_function(np.array([0]),2,2,0,0), 0)
            assert math.isclose(my_function(np.array([0]),2,2,0,-10), 0)
    


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
