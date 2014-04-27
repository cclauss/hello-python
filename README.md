Sample Python Web application
=============================

The sample is using [Flask microframework](http://flask.pocoo.org/) and is intented to test the Python support on [Pivotal's Cloud Foundry](https://run.pivotal.io/).

Deploy to Cloud Foundry
-----------------------
```script
cf push <YOUR_APP_NAME> -m 128M -b https://github.com/heroku/heroku-buildpack-python.git
```
or
```script
cf push <YOUR_APP_NAME> -m 128M -b https://github.com/joshuamckenty/heroku-buildpack-python.git
```
or
```script
cf push <YOUR_APP_NAME> -m 128M -b https://github.com/ephoning/heroku-buildpack-python.git
````

Notes
-----
2014/02/18: The offical Heroku buildpack seems not to be working with Cloud Foundry.

Question
--------
Have you tried using Python 3? If I edit runtime.txt, I can upgrade to python-2.7.6 on IBM BlueMix with no problems.

However if I attempt python-3.4.0 or 3.3.0 I get the message File “/tmp/buildpacks/heroku-buildpack-python/vendor/bpwatch/bpwatch.zip/bp_cli.py”, line 37
print get_state()

The problem is that print() is a function in Python3 so the syntax must be print(get_state()) for Python3 to be happy. (e.g. In Python3 the parentheses are not optional).

