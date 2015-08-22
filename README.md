Recommendation
===============

Recommendation is a Python command line application to provide recommendation of similar items based on provided user data and list of sample items.


Getting Started
===============

Requirements
------------

* Python 2.7


Installation sets up recommendation command
********************************************

Situation before installation::

    $ recommendation
    bash: recommendation: command not found

Installation right from the source tree::

    $ python setup.py install

Now, the ``recommendation`` command is available::
	
	$ recommendation -help
    $ recommendation <input_movies> <file_path> [count]
    

On Unix-like systems, the installation places a ``recommendation`` script into a
centralized ``bin`` directory, which should be in your ``PATH``. On Windows,
``recommendation.exe`` is placed into a centralized ``Scripts`` directory which
should also be in your ``PATH``.

Basic Usage as Package
======================

After installation, Recommendation classes can be imported from the package:

```
$ python
>>> import recommendation
>>> recommendation.__version__
>>> from recommendation.recommendation import Recommendation
```

Run Tests
=========

Test needs "data" directory to run. Make sure its in same place where tests resides. 

	
	$ cd Recommendation\recommendation 
    $ python -m unittest discover


