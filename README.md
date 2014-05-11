Sample Python Web application
=============================

Sample [Python](http://python.org) webapp that supports using either the [Flask](http://flask.pocoo.org) or [bottle](http://bottlepy.org) microframeworks.  This webapp is intented to test the Python support on [IBM's BlueMix](https://bluemix.net).

Deploy to IBM BlueMix (assumes that [cf](http://cli.cloudfoundry.org) has been properly installed)
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
Edit `runtime.txt` to select desired runtime: `python-2.7.6` or `python-3.4.0` or `pypy-1.9`

NOTE: `pypy-2.3` does not yet seem to work on BlueMix.
