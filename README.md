# PythonLivePlotting
Collection of functions that makes live plotting of data in matplotlib a breeze

## Scope
I have found that I'm rewriting the same code over and over again when trying to easily visualize a stream of data in matplotlib. That's why I've decided to rewrite it piece by piece into a coherent library.
This set of functions was not written with the intent to be applicable to every situation out there, but rather to solve the specific problems I have been encountering personally. By releasing it, I simply hope that the code will help in it's current state. 

That being said, if you think that some specific enhancement would be especially cool, don't hesitate to file an enhancement request or (even better!) a pull request. 

For the time being, I've only included the little amount of functions I currently need.

## Prerequisites
* Python 2.7 (other versions not tested)
* matplotlib
* numpy

## Installation
Currently, this is just a collection of classes in one file. To use, download the file and put it in the directory that you want to use it in, or somewhere on your PYTHONPATH.

This library is maintained and tested in python 2.7 with matplotlib 1.3.1.

## Simple example
A simple example is already given in plot.py. Try the following (e.g. from the python command line):
```     
from plot import *
import random

fig = Figure(10)                        # Create a new figure with an x-axis-length of 10 seconds
    
lp = LinePlot(fig, history=10)          # Add a LinePlot to that figure, keep data of the last 10 seconds stored
vl = VerticalLines(fig, color='r')      # Add some red vertical lines to the figure
   
while True:
    lp.add_value(random.random())       # update the line plot with random numbers
    if random.random() > .9:
        vl.add_value()                  # in 1 out of 10 cases, add a vertical line at the current time
    fig.refresh()                       # redraw the figure
    time.sleep(.1)                      # wait some time
    
```

![Sample output](https://github.com/sharst/PythonLivePlotting/blob/master/animation.gif)

## Planned enhancements
* Enable color, style and linewidth arguments for all plotting elements
* add histogram plot element
* auto-scale plot data history to figure size
