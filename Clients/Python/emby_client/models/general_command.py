# coding: utf-8

"""
    Emby Server REST API (BETA)
"""

import pprint
import re  # noqa: F401

import six

class GeneralCommand(object):
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
        'controlling_user_id': 'str',
        'arguments': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'Name',
        'controlling_user_id': 'ControllingUserId',
        'arguments': 'Arguments'
    }

    def __init__(self, name=None, controlling_user_id=None, arguments=None):  # noqa: E501
        """GeneralCommand - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._controlling_user_id = None
        self._arguments = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if controlling_user_id is not None:
            self.controlling_user_id = controlling_user_id
        if arguments is not None:
            self.arguments = arguments

    @property
    def name(self):
        """Gets the name of this GeneralCommand.  # noqa: E501


        :return: The name of this GeneralCommand.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GeneralCommand.


        :param name: The name of this GeneralCommand.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def controlling_user_id(self):
        """Gets the controlling_user_id of this GeneralCommand.  # noqa: E501


        :return: The controlling_user_id of this GeneralCommand.  # noqa: E501
        :rtype: str
        """
        return self._controlling_user_id

    @controlling_user_id.setter
    def controlling_user_id(self, controlling_user_id):
        """Sets the controlling_user_id of this GeneralCommand.


        :param controlling_user_id: The controlling_user_id of this GeneralCommand.  # noqa: E501
        :type: str
        """

        self._controlling_user_id = controlling_user_id

    @property
    def arguments(self):
        """Gets the arguments of this GeneralCommand.  # noqa: E501


        :return: The arguments of this GeneralCommand.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this GeneralCommand.


        :param arguments: The arguments of this GeneralCommand.  # noqa: E501
        :type: dict(str, str)
        """

        self._arguments = arguments

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
        if issubclass(GeneralCommand, dict):
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
        if not isinstance(other, GeneralCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other