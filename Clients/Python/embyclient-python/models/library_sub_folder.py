# coding: utf-8

"""
    Emby Server REST API
"""

import pprint
import re  # noqa: F401

import six

class LibrarySubFolder(object):
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
        'path': 'str',
        'is_user_access_configurable': 'bool'
    }

    attribute_map = {
        'name': 'Name',
        'id': 'Id',
        'path': 'Path',
        'is_user_access_configurable': 'IsUserAccessConfigurable'
    }

    def __init__(self, name=None, id=None, path=None, is_user_access_configurable=None):  # noqa: E501
        """LibrarySubFolder - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._id = None
        self._path = None
        self._is_user_access_configurable = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if path is not None:
            self.path = path
        if is_user_access_configurable is not None:
            self.is_user_access_configurable = is_user_access_configurable

    @property
    def name(self):
        """Gets the name of this LibrarySubFolder.  # noqa: E501


        :return: The name of this LibrarySubFolder.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LibrarySubFolder.


        :param name: The name of this LibrarySubFolder.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this LibrarySubFolder.  # noqa: E501


        :return: The id of this LibrarySubFolder.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LibrarySubFolder.


        :param id: The id of this LibrarySubFolder.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def path(self):
        """Gets the path of this LibrarySubFolder.  # noqa: E501


        :return: The path of this LibrarySubFolder.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this LibrarySubFolder.


        :param path: The path of this LibrarySubFolder.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def is_user_access_configurable(self):
        """Gets the is_user_access_configurable of this LibrarySubFolder.  # noqa: E501


        :return: The is_user_access_configurable of this LibrarySubFolder.  # noqa: E501
        :rtype: bool
        """
        return self._is_user_access_configurable

    @is_user_access_configurable.setter
    def is_user_access_configurable(self, is_user_access_configurable):
        """Sets the is_user_access_configurable of this LibrarySubFolder.


        :param is_user_access_configurable: The is_user_access_configurable of this LibrarySubFolder.  # noqa: E501
        :type: bool
        """

        self._is_user_access_configurable = is_user_access_configurable

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
        if issubclass(LibrarySubFolder, dict):
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
        if not isinstance(other, LibrarySubFolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other