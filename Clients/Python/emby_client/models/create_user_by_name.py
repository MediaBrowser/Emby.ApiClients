# coding: utf-8

"""
    Emby Server REST API (BETA)
"""

import pprint
import re  # noqa: F401

import six

class CreateUserByName(object):
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
        'copy_from_user_id': 'str',
        'user_copy_options': 'list[LibraryUserCopyOptions]'
    }

    attribute_map = {
        'name': 'Name',
        'copy_from_user_id': 'CopyFromUserId',
        'user_copy_options': 'UserCopyOptions'
    }

    def __init__(self, name=None, copy_from_user_id=None, user_copy_options=None):  # noqa: E501
        """CreateUserByName - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._copy_from_user_id = None
        self._user_copy_options = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if copy_from_user_id is not None:
            self.copy_from_user_id = copy_from_user_id
        if user_copy_options is not None:
            self.user_copy_options = user_copy_options

    @property
    def name(self):
        """Gets the name of this CreateUserByName.  # noqa: E501


        :return: The name of this CreateUserByName.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateUserByName.


        :param name: The name of this CreateUserByName.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def copy_from_user_id(self):
        """Gets the copy_from_user_id of this CreateUserByName.  # noqa: E501


        :return: The copy_from_user_id of this CreateUserByName.  # noqa: E501
        :rtype: str
        """
        return self._copy_from_user_id

    @copy_from_user_id.setter
    def copy_from_user_id(self, copy_from_user_id):
        """Sets the copy_from_user_id of this CreateUserByName.


        :param copy_from_user_id: The copy_from_user_id of this CreateUserByName.  # noqa: E501
        :type: str
        """

        self._copy_from_user_id = copy_from_user_id

    @property
    def user_copy_options(self):
        """Gets the user_copy_options of this CreateUserByName.  # noqa: E501


        :return: The user_copy_options of this CreateUserByName.  # noqa: E501
        :rtype: list[LibraryUserCopyOptions]
        """
        return self._user_copy_options

    @user_copy_options.setter
    def user_copy_options(self, user_copy_options):
        """Sets the user_copy_options of this CreateUserByName.


        :param user_copy_options: The user_copy_options of this CreateUserByName.  # noqa: E501
        :type: list[LibraryUserCopyOptions]
        """

        self._user_copy_options = user_copy_options

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
        if issubclass(CreateUserByName, dict):
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
        if not isinstance(other, CreateUserByName):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other