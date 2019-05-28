# swagger_client.DefaultApi

All URIs are relative to *https://d3kndyx4n9.execute-api.us-east-1.amazonaws.com/pre_alpha*

Method | HTTP request | Description
------------- | ------------- | -------------
[**test_delete**](DefaultApi.md#test_delete) | **DELETE** /Test | 
[**test_get**](DefaultApi.md#test_get) | **GET** /Test | 
[**test_options**](DefaultApi.md#test_options) | **OPTIONS** /Test | 
[**test_put**](DefaultApi.md#test_put) | **PUT** /Test | 
[**tests_get**](DefaultApi.md#tests_get) | **GET** /Tests | 
[**tests_options**](DefaultApi.md#tests_options) | **OPTIONS** /Tests | 


# **test_delete**
> Empty test_delete(name=name)



### Example 
```python
from __future__ import print_statement
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[oAuth_2_0](../README.md#oAuth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_get**
> Test test_get(name=name)



### Example 
```python
from __future__ import print_statement
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
    api_response = api_instance.test_get(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->test_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

[**Test**](Test.md)

### Authorization

[oAuth_2_0](../README.md#oAuth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_options**
> Empty test_options()



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try: 
    api_response = api_instance.test_options()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->test_options: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Empty**](Empty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_put**
> Empty test_put(test)



### Example 
```python
from __future__ import print_statement
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
test = swagger_client.Test() # Test | 

try: 
    api_response = api_instance.test_put(test)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->test_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test** | [**Test**](Test.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[oAuth_2_0](../README.md#oAuth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tests_get**
> Tests tests_get(prefix=prefix, tags=tags)



### Example 
```python
from __future__ import print_statement
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
prefix = 'prefix_example' # str |  (optional)
tags = 'tags_example' # str |  (optional)

try: 
    api_response = api_instance.tests_get(prefix=prefix, tags=tags)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->tests_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**|  | [optional] 
 **tags** | **str**|  | [optional] 

### Return type

[**Tests**](Tests.md)

### Authorization

[oAuth_2_0](../README.md#oAuth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tests_options**
> Empty tests_options()



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try: 
    api_response = api_instance.tests_options()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->tests_options: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Empty**](Empty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

