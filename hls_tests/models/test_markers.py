# coding: utf-8

"""
    HLS - Tests

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2017-03-02T13:53:08Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TestMarkers(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description=None, timestamp=None, tags=None):
        """
        TestMarkers - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'timestamp': 'float',
            'tags': 'object'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'timestamp': 'timestamp',
            'tags': 'tags'
        }

        self._name = name
        self._description = description
        self._timestamp = timestamp
        self._tags = tags

    @property
    def name(self):
        """
        Gets the name of this TestMarkers.

        :return: The name of this TestMarkers.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TestMarkers.

        :param name: The name of this TestMarkers.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this TestMarkers.

        :return: The description of this TestMarkers.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TestMarkers.

        :param description: The description of this TestMarkers.
        :type: str
        """

        self._description = description

    @property
    def timestamp(self):
        """
        Gets the timestamp of this TestMarkers.

        :return: The timestamp of this TestMarkers.
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this TestMarkers.

        :param timestamp: The timestamp of this TestMarkers.
        :type: float
        """

        self._timestamp = timestamp

    @property
    def tags(self):
        """
        Gets the tags of this TestMarkers.

        :return: The tags of this TestMarkers.
        :rtype: object
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this TestMarkers.

        :param tags: The tags of this TestMarkers.
        :type: object
        """

        self._tags = tags

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
