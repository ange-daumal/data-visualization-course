# Data Visualization course - Installation Instructions

## Python & python packages installation

* Download the version  `3.7` of Python on the 
[official website](https://www.python.org/downloads/). 
If you're not sure how, you can follow 
[installation steps](https://realpython.com/installing-python/) depending on 
your operating system.
* Open a console / terminal
* Make you sure you have access to the right version using `python -V`. 
You may have to replace `python` by `python3` if you already have Python 2 
installed.
* Upgrade pip and install Pipenv using 
`python -m pip install --upgrade pipenv`. 
Pip should be part of your Python installation if your version is >= `3.4`.
* Open a console / terminal and clone this project using.
`git clone https://github.com/Lyloox/data-visualization-course.git`
* Go in the corresponding directory using `cd data-visualization-course`
* Install required packages using `pipenv install` 
(or `python -m pipenv install`)
* Enter your virtual environment using `pipenv shell`.

Pipenv is a solution to provide both a package manager (like `pip`) and a 
virtual environment (before, we used `virtualenv`). It allows you to have 
several versions of the same package across projects, without them overlapping.


## Jupyter
We will be working with Jupyter to plot our graphs.

Once you have installed pipenv and entered your virtual environment, you can 
use:

* `jupyter notebook` (recommended):  Allow you to edit and create Python 
Notebooks
* `jupyter lab`: It will allow you to edit and create Python Notebooks, but 
also open a terminal, and more functionalities.

Each course will have its own folder.

Once your Jupyter notebook or lab is loaded, you should see a browser window 
open at localhost:8888. Open the `Chapter01` folder and open the `.ipynb` file
titled with `lesson01` to start the first course. Good luck!

