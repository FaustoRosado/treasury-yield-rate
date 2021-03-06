# Yield Curve Project


The 10-2 Treasury Yield Spread is the difference between the 10 year treasury rate and the 2 year treasury rate. A 10-2 treasury spread that approaches 0 signifies a "flattening" yield curve. A negative 10-2 yield spread has historically been viewed as a precursor to a recessionary period. A negative 10-2 spread has predicted every recession from 1955 to 2018, but has occurred 6-24 months before the recession occurring, and is thus seen as a far-leading indicator. The 10-2 spread reached a high of 2.91% in 2011, and went as low as -2.41% in 1980.

10-2 Year Treasury Yield Spread is at 1.49%, compared to 1.49% the previous market day and 0.44% last year. This is higher than the long term average of 0.93%.

Using data scraped from [United States Treasury.](https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yield')


## Setup

### Forking this repo.

Since forking is not a `git` operation, you can either fork this project on github or simulate a fork manually with the following commands:

```bash
# first make sure you create a repo on github

# then clone this repo
$ git clone https://www.github.com/FaustoRosado/treasury-yield-rate.git

# rename the 'origin' remote to 'upstream'
$ git remote rename origin upstream

# add remote 'origin' pointing to that new repo you created
$ git remote add origin https://github.com/<username>/<repo>.git 

# then use the following to check your git remotes:
$ git remote -v
origin https://github.com/<username>/<repo>.git (fetch)
origin https://github.com/<username>/<repo>.git (push)
upstream   https://github.com/newstudent718/yield-curve.git
upstream   https://github.com/newstudent718/yield-curve.git
```

### Setting up your environment.

Then set up your python environment. If you're using `pyenv`, make sure you're using the right version of python (either set globally or locally for this directory). 

```bash
# this will create a virtual environment in the env/ folder in your repo
$ python -m venv env

# then to activate your virtualenv
$ source env/bin/activate

# you'll see your env is activated
# because there'll be '(env)' written in your terminal prompt
(env) $ 

# to deactivate your env use:
(env) $ deactivate

# you'll see the '(env)' is gone
$ 

```

### Dealing with dependencies

You'll need to install `requests`, `bs4` and `matplotlib`.

```bash
# if your env is activated, you can simply `pip install` to your env
# this will install the minimum requirements
(env) $ pip install requests bs4 matplotlib 

# to populate your 'requirements.txt' file after 
# installing all of your dependencies
(env) $ pip freeze > requirements.txt

# to install from your requirements.txt later on, use:
(env) $ pip install -r requirements.txt
```
### Running the project

With the python virtual environment activated, you can simply run the script. You'll see the following output.
```bash
(env) $ python script.py
scraping
generating matplotlib chart
completed

```


### Using Docker

There is a `Dockerfile` already set up to run your project. The one caveat is that we need to attach a volume so the charts created by the container can be accessed on our local machine. To do this we need two paths, the path to the charts folder on our machine and the path to the charts folder on our container. Our container's chart folder is absolute (`/usr/src/app/charts`) but the folder on your local machine will be the path to `charts/` (on linux/mac you can find this using the `pwd` command inside the `charts/` folder.

If you'd like to use docker to run your project, use the following:

```bash
# this will build your docker container based 
# on the steps written in the Dockerfile
# the -t flag will create your container with the tag that follows
# so you can easily refer to it in the docker cli$ docker built -t yield-curve
$ docker build -t yield-curve .

# then once the docker container is built, you can run it using:
# be sure to fix the path
$ docker run -v ~/path/to/charts:/usr/src/app/charts yield-curve 
```	
notes: 
* We ran 'yield-curve' because that's the tag we gave the container when we built it.
* If you use the docker container, the charts will be saved to your `/charts` folder in the repo folder on your local machine. 

