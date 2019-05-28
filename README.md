# swagger_client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2017-03-02T13:53:08Z
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: oAuth_2_0
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str |  (optional)

try:
    api_response = api_instance.test_delete(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->test_delete: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://d3kndyx4n9.execute-api.us-east-1.amazonaws.com/pre_alpha*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**test_delete**](docs/DefaultApi.md#test_delete) | **DELETE** /Test | 
*DefaultApi* | [**test_get**](docs/DefaultApi.md#test_get) | **GET** /Test | 
*DefaultApi* | [**test_options**](docs/DefaultApi.md#test_options) | **OPTIONS** /Test | 
*DefaultApi* | [**test_put**](docs/DefaultApi.md#test_put) | **PUT** /Test | 
*DefaultApi* | [**tests_get**](docs/DefaultApi.md#tests_get) | **GET** /Tests | 
*DefaultApi* | [**tests_options**](docs/DefaultApi.md#tests_options) | **OPTIONS** /Tests | 


## Documentation For Models

 - [Empty](docs/Empty.md)
 - [Test](docs/Test.md)
 - [TestMarkers](docs/TestMarkers.md)
 - [Tests](docs/Tests.md)


## Documentation For Authorization


## oAuth_2_0

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author


