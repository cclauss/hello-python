Sample Python Web application
=============================

The sample is using [Flask microframework](http://flask.pocoo.org/) and is intented to test the Python support on [IBM's BlueMix](https://bluemix.net/).

Deploy to IBM BlueMix
---------------------
```script
git clone <URL_OF_THIS_REPO>
cd hello-python
cf push
```

Notes
-----
2014/02/18: The offical Heroku buildpack seems not to be working with Cloud Foundry.

Python Versions
---------------
Edit __runtime.txt__ to select desired runtime: __python-2.7.6__ or __python-3.4.0__ or __pypy-1.9__

NOTE: `pypy-2.3` does not yet seem to work on BlueMix.
