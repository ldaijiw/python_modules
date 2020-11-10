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
- Finds if web is live
- Handle user as per as per response from web

**HTTP/HTTPS Protocols**
- GET
- POST
- REQUEST

**CRUD**
- Create
- Read
- Update
- Delete

## Postcode Task

- research how to convert this data into dictionary
- hint - python json library
- iterate through data and print results
- print longitude and latitude

**SOLUTION**
- 2 Functions
- ``postcode_response`` to ask user input for postcode and return the response
- ``get_coordinates`` to extract coordinates (longitude, latitude) from response and return tuple

The datatype of the response is _bytes_. In order to extract the useful information from the response

``response.json()`` converts response into dictionary format with 2 items
- status: _int_ status code from response
- result: _dict_ dictionary of all the result contents

Can extract specific information from result dictionary:
```python
response_results = response.json()["results"]
response_results["specific_info"]
```

## JSON Basics

JSON is used heavily in the industry for reading/writing/parsing/converting data

- JavaScript Object Notation
- Use cases - browser data
- Data is in key value pairs
- JSON encoding from dictionary
- JSON decoding into dictionary
- Handling/creating files with python
- writing to file
- reading from file

Using JSON with Python

- ``json.dumps()``- serialises json to a formatted string
```python

car_data_json_string = json.dumps(car_data)
print(type(car_data_json_string))
```

- json.dump() creates a stream object and accept a file object to write to
- "w" gives write permissions
```python
with open("new_json_file.json", "w") as jsonfile:
    json.dump(car_data, jsonfile)
```


- json.load() copies data and stores into variable
- "r" gives read permissions
```python
with open("new_json_file.json", "r") as jsonfile:
    car = json.load(jsonfile)
```

## Using Try/Except

Can use try/except to attempt to run blocks and perform a different action if an error occurs.

The control flow is as follows:
- **TRY**: Attempts to execute main block
- **EXCEPT** _specificError_: If a certain error occurs then executes this block, raising an error
- **ELSE**: If no error occurs then runs this block
- **FINALLY**: Will execute regardless of success or failure
