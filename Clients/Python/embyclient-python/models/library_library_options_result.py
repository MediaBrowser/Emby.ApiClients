# coding: utf-8

"""
    Emby Server REST API
"""

import pprint
import re  # noqa: F401

import six

class LibraryLibraryOptionsResult(object):
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
        'metadata_savers': 'list[LibraryLibraryOptionInfo]',
        'metadata_readers': 'list[LibraryLibraryOptionInfo]',
        'subtitle_fetchers': 'list[LibraryLibraryOptionInfo]',
        'lyrics_fetchers': 'list[LibraryLibraryOptionInfo]',
        'type_options': 'list[LibraryLibraryTypeOptions]'
    }

    attribute_map = {
        'metadata_savers': 'MetadataSavers',
        'metadata_readers': 'MetadataReaders',
        'subtitle_fetchers': 'SubtitleFetchers',
        'lyrics_fetchers': 'LyricsFetchers',
        'type_options': 'TypeOptions'
    }

    def __init__(self, metadata_savers=None, metadata_readers=None, subtitle_fetchers=None, lyrics_fetchers=None, type_options=None):  # noqa: E501
        """LibraryLibraryOptionsResult - a model defined in Swagger"""  # noqa: E501
        self._metadata_savers = None
        self._metadata_readers = None
        self._subtitle_fetchers = None
        self._lyrics_fetchers = None
        self._type_options = None
        self.discriminator = None
        if metadata_savers is not None:
            self.metadata_savers = metadata_savers
        if metadata_readers is not None:
            self.metadata_readers = metadata_readers
        if subtitle_fetchers is not None:
            self.subtitle_fetchers = subtitle_fetchers
        if lyrics_fetchers is not None:
            self.lyrics_fetchers = lyrics_fetchers
        if type_options is not None:
            self.type_options = type_options

    @property
    def metadata_savers(self):
        """Gets the metadata_savers of this LibraryLibraryOptionsResult.  # noqa: E501


        :return: The metadata_savers of this LibraryLibraryOptionsResult.  # noqa: E501
        :rtype: list[LibraryLibraryOptionInfo]
        """
        return self._metadata_savers

    @metadata_savers.setter
    def metadata_savers(self, metadata_savers):
        """Sets the metadata_savers of this LibraryLibraryOptionsResult.


        :param metadata_savers: The metadata_savers of this LibraryLibraryOptionsResult.  # noqa: E501
        :type: list[LibraryLibraryOptionInfo]
        """

        self._metadata_savers = metadata_savers

    @property
    def metadata_readers(self):
        """Gets the metadata_readers of this LibraryLibraryOptionsResult.  # noqa: E501


        :return: The metadata_readers of this LibraryLibraryOptionsResult.  # noqa: E501
        :rtype: list[LibraryLibraryOptionInfo]
        """
        return self._metadata_readers

    @metadata_readers.setter
    def metadata_readers(self, metadata_readers):
        """Sets the metadata_readers of this LibraryLibraryOptionsResult.


        :param metadata_readers: The metadata_readers of this LibraryLibraryOptionsResult.  # noqa: E501
        :type: list[LibraryLibraryOptionInfo]
        """

        self._metadata_readers = metadata_readers

    @property
    def subtitle_fetchers(self):
        """Gets the subtitle_fetchers of this LibraryLibraryOptionsResult.  # noqa: E501


        :return: The subtitle_fetchers of this LibraryLibraryOptionsResult.  # noqa: E501
        :rtype: list[LibraryLibraryOptionInfo]
        """
        return self._subtitle_fetchers

    @subtitle_fetchers.setter
    def subtitle_fetchers(self, subtitle_fetchers):
        """Sets the subtitle_fetchers of this LibraryLibraryOptionsResult.


        :param subtitle_fetchers: The subtitle_fetchers of this LibraryLibraryOptionsResult.  # noqa: E501
        :type: list[LibraryLibraryOptionInfo]
        """

        self._subtitle_fetchers = subtitle_fetchers

    @property
    def lyrics_fetchers(self):
        """Gets the lyrics_fetchers of this LibraryLibraryOptionsResult.  # noqa: E501


        :return: The lyrics_fetchers of this LibraryLibraryOptionsResult.  # noqa: E501
        :rtype: list[LibraryLibraryOptionInfo]
        """
        return self._lyrics_fetchers

    @lyrics_fetchers.setter
    def lyrics_fetchers(self, lyrics_fetchers):
        """Sets the lyrics_fetchers of this LibraryLibraryOptionsResult.


        :param lyrics_fetchers: The lyrics_fetchers of this LibraryLibraryOptionsResult.  # noqa: E501
        :type: list[LibraryLibraryOptionInfo]
        """

        self._lyrics_fetchers = lyrics_fetchers

    @property
    def type_options(self):
        """Gets the type_options of this LibraryLibraryOptionsResult.  # noqa: E501


        :return: The type_options of this LibraryLibraryOptionsResult.  # noqa: E501
        :rtype: list[LibraryLibraryTypeOptions]
        """
        return self._type_options

    @type_options.setter
    def type_options(self, type_options):
        """Sets the type_options of this LibraryLibraryOptionsResult.


        :param type_options: The type_options of this LibraryLibraryOptionsResult.  # noqa: E501
        :type: list[LibraryLibraryTypeOptions]
        """

        self._type_options = type_options

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
        if issubclass(LibraryLibraryOptionsResult, dict):
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
        if not isinstance(other, LibraryLibraryOptionsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other