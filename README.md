# HSE MLwP 2022 Homework 2: Introduction to Jupyter notebooks and Google Colab

This is a template repository for **Machine Learning with Python Assignment 2: Introduction to Jupyter Notebooks**.  All of the assignment instruction are in the Jupyter (.ipynb) notebook. 

## Excercise 1
To begin, open (click) the [jupyter_assignment.ipynb](jupyter_assignment.ipynb) notebook and then click on the blue "Open in Colab" button at the top.  A new tab or window should open in your browser, displaying the notebook in Google Colaboratory.

## Setup and submission

### Google Colab
In order to submit your assignment you'll need to save an editable copy of your notebook.  Click File > Save a copy in Drive and then save your copy of the notebook as `jupyter_assignment.ipynb` (i.e., remove the "`Copy of`" text that gets automatically appended to the beginning of the filename).

The second setup task is to ensure that Colaboratory has access to your private repositories on GitHub. (By default, your assignment repositories will be accessible only to you and the course instructor.) To give Colaboratory access to your private repositories:
- Navigate to [http://colab.research.google.com/github](http://colab.research.google.com/github)
- Make sure the "Include Private Repos" checkbox is checked
- In the popup window, sign into your GitHub account and authorize Colab to read private files

You should do your work on the assignment in the *copied* notebook (i.e., the copied notebook that you have the ability to save and edit). Submitting the assignment entails syncing your copy of the notebook with your GitHub repository (in this case, `<course_name>/<assignment_name>-<username>`, with `<username>` replaced with your GitHub username, e.g. `hse-mlwp-2022/jupyter-intro-markpolyak`). From within Colaboratory, open your notebook and click File > Save a copy in GitHub.  Select your repository name (e.g. `hse-mlwp-2022/jupyter-intro-markpolyak`) from the Repository drop-down menu, and type '`jupyter_assignment.ipynb`' into the File path text box.  Optionally, you may also enter a description into the "Commit message" text box (or you can just leave the default message).  Make sure that the "Include a link to Colaboratory" box is checked, and press "OK".  A new tab or window should open up, displaying your submitted notebook from within your GitHub repository.

### Local python installation with Anaconda
Here are the steps to take in case Google Colab is unavailable due to blockages, internet connectivity issues or other reasons.

1. Download and install Anaconda data science toolkit from [anaconda.com](https://www.anaconda.com/products/individual).
2. Create a local copy of your repository, e.g. by using `git clone ...` command.
3. Open Anaconda Navigator and launch Jupyter Notebook application.
4. From within Jupyter navigate to the local copy of your repository and open the notebook you want to work on (i.e. the `.ipynb` file).
5. Edit the notebook and save the changes by pressing the diskette button in Jupyter.
6. Commit changed notebook(s) to the local copy of your repository, e.g. by issuing `git add <filename>` and `git commit` commands.

## Excercise 2
Proceed to open the [matplotlib_assignment.ipynb](matplotlib_assignment.ipynb) notebook on GitHub and follow to Colab. Or just click this button: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hse-mlwp-2022/assignment2-template/blob/main/matplotlib_assignment.ipynb)