# Data Visualization course - Installation Instructions

The installation will take place in three steps:
1. Get **Python 3.7** and **Pipenv** to install necessary packages
1. Get **Git** & clone this repository
1. Open **Jupyter Notebook** and open the first lesson

Each step will have subparts depending on your Operating System.

## 1. Get Python 3.7 

* Download the version  `3.7` of Python on the 
[official website](https://www.python.org/downloads/).  
If you're not sure how, you can follow 
[installation steps](https://realpython.com/installing-python/) depending on 
your operating system.

### On Linux & MacOS Only 

* Open a console / terminal
* Make you sure you have access to the right version using `python -V`. 
You may have to replace `python` by `python3` if you already have Python 2 
installed.
* Upgrade pip and install Pipenv using 
`python -m pip install --upgrade pipenv`. 
Pip should be part of your Python installation if your version is >= `3.4`.

Pipenv is a solution to provide both a package manager (like `pip`) and a 
virtual environment (before, we used `virtualenv`). It allows you to have 
several versions of the same package across projects, without them overlapping.

### On Windows, Linux & MacOs

Anaconda requires 3GB of free hard drive space.

* Download the [Anaconda Distribution](https://www.anaconda.com/distribution/) 
for **Python 3.7**.
* You can now access *Anaconda Prompt* and *Anaconda Navigator* softwares.
* Open *Anaconda Prompt* **with administrator rights**, using right click. 
It will open a command-line interface. 
* Type `conda install -c conda-forge pipenv ` to install pipenv.

## 2. Get Git & clone this repository 

### On Linux & MacOs 

* Open a console / terminal
* On *Debian-based Linux*, install git using **apt-get**:
```
sudo apt update
sudo apt upgrade
sudo apt install git
```
* On *Red Hat-based Linux*, install git using **yum**:
```
sudo yum upgrade
sudo yum install git
```
* On *MacOs*, install git using **HomeBrew**:
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew doctor
```
You will be offered to install the Command Line Developer Tools from Apple. 
Confirm by clicking Install.  
After the installation finished, continue installing Homebrew by hitting 
Return.

Then install Git using:
`brew install git`

* Clone this project using
`git clone https://github.com/Lyloox/data-visualization-course.git`

### On Windows

* Install [Git](https://git-scm.com/) from their official website.
* Open the installation file **with administrator rights** too.
* On the screen *Select Components*, let default settings
* On the screen *Adjusting your PATH environnment*, select « Use Git from the Windows Command Prompt »
* On the screen *Configuring the line ending conversions*, select  « Checkout as-is, commit Unix-style line endings »
* Open *Git Bash* software. Make sure git is installed by typing `git --version`
* Close this project using 
`git clone https://github.com/Lyloox/data-visualization-course.git`


## 3. Use Jupyter
We will be working with Jupyter to plot our graphs.

### On Linux & MacOs 
* Go in the corresponding directory using `cd data-visualization-course`
* Install required packages using `pipenv install` 
(or `python -m pipenv install`)
* Enter your virtual environment using `pipenv shell`.
* Type `jupyter notebook` 

### On Windows
* Open `Anaconda Navigator`
* Launch `Jupyter Notebook`
* Navigate to the place where you clone *data-visualization-course*.

Each course will have its own folder.

Once your Jupyter notebook is loaded, you should see a browser window 
open at localhost:8888.  
Open the `Chapter01` folder and open the `.ipynb` file
titled with `lesson01` to start the first course. Good luck!

