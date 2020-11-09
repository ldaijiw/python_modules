# Python Modules

- Built-in functions
- Python library
- What is pip and how do we use it
- APIs with Python

## Built-in Functions
- Built in functions help us accelerate our development of software

**Task Using Math**
- get user input of a float number
- check if the number is lower than .50 then round the figure to lower end
- check if the number is greater than .51 then round the figure to higher end
- example - num_float = 23.66 - round it to 24, num_float = 23.50 - round it to lower end
- tips - get help online - python library


#### Creating a customised method to add required info and use functionality provided by sys module
```python
def current_system_path():
    print(f"This is your current system paths")
    return sys.path

print(current_system_path())
```

## PIP

**What is pip?**
- pip is a package manager for Python and helps us install external packages 

Syntax:
```
pip install package_name
```

## API
**A**pplication **P**rogramming **I**nterface

### Requests
- Localhost makes an API call to www server
- 