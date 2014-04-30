Sample Python Web application
=============================

The sample is using [Flask microframework](http://flask.pocoo.org/) and is intented to test the Python support on [IBM's BlueMix](https://bluemix.net/).

Deploy to IBM BlueMix
---------------------
```script
cf push <YOUR_APP_NAME>
```

Notes
-----
2014/02/18: The offical Heroku buildpack seems not to be working with Cloud Foundry.

Python Versions
---------------
Edit __runtime.txt__ to select desired runtime: python-2.7.6 __or__ python-3.4.0 __or__ pypy-1.9

NOTE: pypy-2.2.1 did not work for me on BlueMix.
