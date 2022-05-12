# Code Challenge
You are given an integer array height of length n. There are n vertical lines drawn such that the
two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the area is the biggest.
Return the maximum container area.

Notice that you may not slant the container.

## Examples

### Example 1
**Input**: height = [1,8,6,2,5,4,8,3,7]

**Output**: 49

Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case,
the max area of the container is 49.

### Example 2

**Input**: height = [1,1]

**Output**: 1


## Required

* Unit Testing
* Any Python Version
* Expose it as Rest Api - Flask
* Upload the Code to Github and share the link

## Requirements

* Python 3.8+
* Flask 2.1.2
* Pytest 7.1.2

## Usage

Once python 3.8 environemnt is ready to be used, install requirements:

```bash
$ pip install -r requirements.txt
```

Set environment variables properly, you can use *.env.sample* as reference

Run Flask application:
```bash
$ flask run
```

Run tests (simple execution):
```bash
$ python -m pytest
```
Run tests with test coverage:
```bash
$ python -m pytest --cov=my_app
```

Expected result:
```
plugins: cov-3.0.0
collected 6 items

my_app/tests/functional/test_calculate_api.py ....                        [ 66%]
my_app/tests/unit/test_calculate.py ..                                    [100%]

---------- coverage: platform darwin, python 3.10.4-final-0 ----------
Name                                            Stmts   Miss  Cover
-------------------------------------------------------------------
my_app/__init__.py                                  7      0   100%
my_app/calculate.py                                14      0   100%
my_app/settings.py                                  3      0   100%
my_app/tests/__init__.py                            0      0   100%
my_app/tests/conftest.py                            8      0   100%
my_app/tests/functional/__init__.py                 0      0   100%
my_app/tests/functional/test_calculate_api.py      15      0   100%
my_app/tests/unit/__init__.py                       0      0   100%
my_app/tests/unit/test_calculate.py                15      0   100%
my_app/views.py                                    15      0   100%
-------------------------------------------------------------------
TOTAL                                              77      0   100%
```