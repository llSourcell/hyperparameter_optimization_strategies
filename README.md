# hyperparameter_optimization_strategies
This is the Code for "How Do I Find the Best Hyperparameters?- The Math of Intelligence #7" By Siraj Raval on Youtube

# Coding Challenge - Due Date - Thursday, August 3rd, 2017

Use Bayesian Optimization to find the optimal learning rate for a linear regression model. You can use any dataset you like (examples [here](https://www.kaggle.com/datasets)) and you can use any "bayesian optimization library" you like as well. Bonus points are given if you are able to perform Bayesian optimization without using any libraries. Good luck!

## Overview

This is the code for [this](https://youtu.be/ttE0F7fghfk) video on Youtube by Siraj Raval as part of The Math of Intelligence series. I go through 3 strategies (grid search, random search, and bayesian optimization) to find the ideal hyperparameters. You can find a twitter sentiment dataset [here](https://twitter-sentiment-csv.herokuapp.com/) or [here](http://thinknook.com/twitter-sentiment-analysis-training-corpus-dataset-2012-09-22/). 


## Dependencies

* numpy
* matplotlib
* pandas

Install missing dependencies using [pip](https://pip.pypa.io/en/stable/).

## Usage

You can run both the grid search and random search files using `python name_of_file` in terminal. I've got 2 examples of Bayesian Optimization in jupyter notebooks. The first one uses a scikit-learn wrapper to do it, but has great visualizations. The second one uses tensorflow to build the model, but implements bayesian optimization from scratch. You can run them both by typing `jupyter notebook` into terminal and the code will pop up in your browser.

Install jupyter [here](http://jupyter.readthedocs.io/en/latest/install.html). 


## Credits

Credits for this code goes to [David Li-Bland](https://github.com/davidlibland). I've merely created a wrapper to get people started.
