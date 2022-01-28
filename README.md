# SpecialMath Web
This project represents a basic implementation of the `specialmath` algorithm
served from a web server.

## Getting Started
Python 3.10 is suggested to run this project and can be
[downloaded here](https://www.python.org/downloads/release/python-3102/).

For development and testing you'll want to
[clone the repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

## Initial Setup
The suggested IDE for this project is [IntelliJ](https://www.jetbrains.com/idea/download) with the [Python plugin](https://www.jetbrains.com/help/idea/plugin-overview.html).

### Create a virtual environment(Mac)
From the root of the project
```
python3.10 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```
This will build and install the required packages in your virtual environment.

### Starting the web server
From the root of the project
```
. venv/bin/activate
export FLASK_APP=special_math
export FLASK_ENV=development
flask run
```
You should see something like
```
 * Serving Flask app 'special_math' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: ###-###-###
```
If not check out some [debugging tips](https://flask.palletsprojects.com/en/2.0.x/quickstart/#what-to-do-if-the-server-does-not-start)
on the flask website.

## Interacting with the Server
The special_math server reacts to http requests on the given IP and port. In this case 127.0.0.1:5000.

Using [curl commands](https://curl.se/docs/manual.html)
you can interact with the server:
```
curl http://127.0.0.1:5000/specialmath/90
```

Which will return a json response with your special math calculation:
```json
{
  "context": {
    "request-id": "f8862894-df9e-4ab4-ab09-c56e032ca8a7", 
    "request-time": "2022-01-28T20:11:22Z"
  }, 
  "response": {
    "special-calculation": 19740274219868223074
  }
}
```

## Running the tests
You can run the tests for this repository like so, again from the root of the repository:
```
. venv/bin/activate
python -m pytest
```

You should see output like:

```
============================= test session starts ==============================
platform darwin -- Python 3.10.2, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /usr/git/SpecialMath, configfile: setup.cfg, testpaths: tests
plugins: mock-3.7.0
collected 18 items                                                             

tests/functional/test_specialmath.py ......                              [ 33%]
tests/unit/test_common_utilities.py .......                              [ 72%]
tests/unit/test_factory.py .....                                         [100%]

============================== 18 passed in 0.10s ==============================
```

### Generating Coverage
This project allows you to generate a coverage report to see what code has active tests.
From the root directory
```
. venv/bin/activate
python -m coverage run -m pytest
```
A successful test run should be presented
```
============================= test session starts ==============================
platform darwin -- Python 3.10.2, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /usr/git/SpecialMath, configfile: setup.cfg, testpaths: tests
plugins: mock-3.7.0
collected 18 items                                                             

tests/functional/test_specialmath.py ......                              [ 33%]
tests/unit/test_common_utilities.py .......                              [ 72%]
tests/unit/test_factory.py .....                                         [100%]

============================== 18 passed in 0.08s ==============================
```
Once results are recorded a coverage report can be generated by running
``` 
coverage html
```

With an expected output of
``` 
Wrote HTML report to htmlcov/index.html
```

A new directory called `htmlcov` will now be present, open the `index.html` file to review coverage results.

## Thanks for checking out my project!