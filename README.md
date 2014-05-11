Sample Python Web application
=============================

Webapp that supports the use of either the [Flask](http://flask.pocoo.org) or [bottle](http://bottlepy.org) microframeworks and is intented to test the support for [Python](http://python.org) on [IBM's BlueMix](https://bluemix.net) PaaS.

Deploy to IBM BlueMix
---------------------
Assumes that [cf](http://cli.cloudfoundry.org) has been properly installed.
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
