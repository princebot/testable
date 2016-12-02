testable
========
Show the difference between testable and untestable code.  

This slapdash little repo briefly illustrates the concept for a friend re a
conversation from this morning (where I clumsily attempted to explain the
limitations of shell scripting).


Explanation
-----------
Shell scripts (and other executable files) are essentially untestable. They’re
black boxes: You run them — and that’s it. You can check the before-state and
the after-state, but you cannot easily verify what happens in between.  

Libraries (and other importable files) **can** be tested. You simply import the
library and try its functions to verify they do what you expect.  

Some languages offer ways to do both in the same program allowing you to make
files that can either be launched as scripts or imported as libraries.  

This matters because [testability is extremely important](http://docs.python-guide.org/en/latest/writing/tests/)
for writing correct, maintainable code that …
* does what you expect,
* can be reasoned about, and
* can be included in other projects without incurring [technical debt](https://www.wikiwand.com/en/Technical_debt).


Files
-----
name | description
:---- | :-----------
`standalone.py` | can only run as a script
`importable.py` | can run as a script or be imported as a library
`importable_test.py` | unit tests for `importable.py`


Requirements
------------
* Python 3.x
* [pytest](http://doc.pytest.org/en/latest/)


Usage
-----
```bash
# Clone the repo.
git clone https://github.com/princebot/testable
cd testable

# Ensure pytest package is installed.
pip install --upgrade pytest

# See what the scripts do.
python standalone.py
python importable.py

# Run the unit tests for importable.py
pytest
```
