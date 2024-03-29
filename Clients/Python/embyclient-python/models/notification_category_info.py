# coding: utf-8

"""
    Emby Server REST API
"""

import pprint
import re  # noqa: F401

import six

class NotificationCategoryInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'id': 'str',
        'events': 'list[NotificationTypeInfo]'
    }

    attribute_map = {
        'name': 'Name',
        'id': 'Id',
        'events': 'Events'
    }

    def __init__(self, name=None, id=None, events=None):  # noqa: E501
        """NotificationCategoryInfo - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._id = None
        self._events = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if events is not None:
            self.events = events

    @property
    def name(self):
        """Gets the name of this NotificationCategoryInfo.  # noqa: E501


        :return: The name of this NotificationCategoryInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NotificationCategoryInfo.


        :param name: The name of this NotificationCategoryInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this NotificationCategoryInfo.  # noqa: E501


        :return: The id of this NotificationCategoryInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NotificationCategoryInfo.


        :param id: The id of this NotificationCategoryInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def events(self):
        """Gets the events of this NotificationCategoryInfo.  # noqa: E501


        :return: The events of this NotificationCategoryInfo.  # noqa: E501
        :rtype: list[NotificationTypeInfo]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this NotificationCategoryInfo.


        :param events: The events of this NotificationCategoryInfo.  # noqa: E501
        :type: list[NotificationTypeInfo]
        """

        self._events = events

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(NotificationCategoryInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NotificationCategoryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
