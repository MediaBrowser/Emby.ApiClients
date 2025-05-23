# coding: utf-8

"""
    Emby Server REST API
"""

import pprint
import re  # noqa: F401

import six

class ApiBaseItemsRequest(object):
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
        'is_special_episode': 'bool',
        'is4_k': 'bool',
        'enable_total_record_count': 'bool',
        'is_duplicate': 'bool',
        'name': 'str',
        'recording_keyword': 'str',
        'recording_keyword_type': 'LiveTvKeywordType',
        'random_seed': 'int',
        'genre_ids': 'str',
        'collection_ids': 'str',
        'tag_ids': 'str',
        'exclude_tag_ids': 'str',
        'item_person_types': 'list[PersonType]',
        'exclude_artist_ids': 'str',
        'album_artist_ids': 'str',
        'composer_artist_ids': 'str',
        'contributing_artist_ids': 'str',
        'album_ids': 'str',
        'outer_ids': 'str',
        'list_item_ids': 'str',
        'audio_languages': 'str',
        'subtitle_languages': 'str',
        'can_edit_items': 'bool',
        'group_items_into': 'LibraryItemLinkType',
        'is_standalone_special': 'bool',
        'min_width': 'int',
        'min_height': 'int',
        'max_width': 'int',
        'max_height': 'int',
        'group_programs_by_series': 'bool',
        'air_days': 'list[DayOfWeek]',
        'is_airing': 'bool',
        'has_aired': 'bool',
        'collection_types': 'str',
        'exclude_sources': 'list[str]'
    }

    attribute_map = {
        'is_special_episode': 'IsSpecialEpisode',
        'is4_k': 'Is4K',
        'enable_total_record_count': 'EnableTotalRecordCount',
        'is_duplicate': 'IsDuplicate',
        'name': 'Name',
        'recording_keyword': 'RecordingKeyword',
        'recording_keyword_type': 'RecordingKeywordType',
        'random_seed': 'RandomSeed',
        'genre_ids': 'GenreIds',
        'collection_ids': 'CollectionIds',
        'tag_ids': 'TagIds',
        'exclude_tag_ids': 'ExcludeTagIds',
        'item_person_types': 'ItemPersonTypes',
        'exclude_artist_ids': 'ExcludeArtistIds',
        'album_artist_ids': 'AlbumArtistIds',
        'composer_artist_ids': 'ComposerArtistIds',
        'contributing_artist_ids': 'ContributingArtistIds',
        'album_ids': 'AlbumIds',
        'outer_ids': 'OuterIds',
        'list_item_ids': 'ListItemIds',
        'audio_languages': 'AudioLanguages',
        'subtitle_languages': 'SubtitleLanguages',
        'can_edit_items': 'CanEditItems',
        'group_items_into': 'GroupItemsInto',
        'is_standalone_special': 'IsStandaloneSpecial',
        'min_width': 'MinWidth',
        'min_height': 'MinHeight',
        'max_width': 'MaxWidth',
        'max_height': 'MaxHeight',
        'group_programs_by_series': 'GroupProgramsBySeries',
        'air_days': 'AirDays',
        'is_airing': 'IsAiring',
        'has_aired': 'HasAired',
        'collection_types': 'CollectionTypes',
        'exclude_sources': 'ExcludeSources'
    }

    def __init__(self, is_special_episode=None, is4_k=None, enable_total_record_count=None, is_duplicate=None, name=None, recording_keyword=None, recording_keyword_type=None, random_seed=None, genre_ids=None, collection_ids=None, tag_ids=None, exclude_tag_ids=None, item_person_types=None, exclude_artist_ids=None, album_artist_ids=None, composer_artist_ids=None, contributing_artist_ids=None, album_ids=None, outer_ids=None, list_item_ids=None, audio_languages=None, subtitle_languages=None, can_edit_items=None, group_items_into=None, is_standalone_special=None, min_width=None, min_height=None, max_width=None, max_height=None, group_programs_by_series=None, air_days=None, is_airing=None, has_aired=None, collection_types=None, exclude_sources=None):  # noqa: E501
        """ApiBaseItemsRequest - a model defined in Swagger"""  # noqa: E501
        self._is_special_episode = None
        self._is4_k = None
        self._enable_total_record_count = None
        self._is_duplicate = None
        self._name = None
        self._recording_keyword = None
        self._recording_keyword_type = None
        self._random_seed = None
        self._genre_ids = None
        self._collection_ids = None
        self._tag_ids = None
        self._exclude_tag_ids = None
        self._item_person_types = None
        self._exclude_artist_ids = None
        self._album_artist_ids = None
        self._composer_artist_ids = None
        self._contributing_artist_ids = None
        self._album_ids = None
        self._outer_ids = None
        self._list_item_ids = None
        self._audio_languages = None
        self._subtitle_languages = None
        self._can_edit_items = None
        self._group_items_into = None
        self._is_standalone_special = None
        self._min_width = None
        self._min_height = None
        self._max_width = None
        self._max_height = None
        self._group_programs_by_series = None
        self._air_days = None
        self._is_airing = None
        self._has_aired = None
        self._collection_types = None
        self._exclude_sources = None
        self.discriminator = None
        if is_special_episode is not None:
            self.is_special_episode = is_special_episode
        if is4_k is not None:
            self.is4_k = is4_k
        if enable_total_record_count is not None:
            self.enable_total_record_count = enable_total_record_count
        if is_duplicate is not None:
            self.is_duplicate = is_duplicate
        if name is not None:
            self.name = name
        if recording_keyword is not None:
            self.recording_keyword = recording_keyword
        if recording_keyword_type is not None:
            self.recording_keyword_type = recording_keyword_type
        if random_seed is not None:
            self.random_seed = random_seed
        if genre_ids is not None:
            self.genre_ids = genre_ids
        if collection_ids is not None:
            self.collection_ids = collection_ids
        if tag_ids is not None:
            self.tag_ids = tag_ids
        if exclude_tag_ids is not None:
            self.exclude_tag_ids = exclude_tag_ids
        if item_person_types is not None:
            self.item_person_types = item_person_types
        if exclude_artist_ids is not None:
            self.exclude_artist_ids = exclude_artist_ids
        if album_artist_ids is not None:
            self.album_artist_ids = album_artist_ids
        if composer_artist_ids is not None:
            self.composer_artist_ids = composer_artist_ids
        if contributing_artist_ids is not None:
            self.contributing_artist_ids = contributing_artist_ids
        if album_ids is not None:
            self.album_ids = album_ids
        if outer_ids is not None:
            self.outer_ids = outer_ids
        if list_item_ids is not None:
            self.list_item_ids = list_item_ids
        if audio_languages is not None:
            self.audio_languages = audio_languages
        if subtitle_languages is not None:
            self.subtitle_languages = subtitle_languages
        if can_edit_items is not None:
            self.can_edit_items = can_edit_items
        if group_items_into is not None:
            self.group_items_into = group_items_into
        if is_standalone_special is not None:
            self.is_standalone_special = is_standalone_special
        if min_width is not None:
            self.min_width = min_width
        if min_height is not None:
            self.min_height = min_height
        if max_width is not None:
            self.max_width = max_width
        if max_height is not None:
            self.max_height = max_height
        if group_programs_by_series is not None:
            self.group_programs_by_series = group_programs_by_series
        if air_days is not None:
            self.air_days = air_days
        if is_airing is not None:
            self.is_airing = is_airing
        if has_aired is not None:
            self.has_aired = has_aired
        if collection_types is not None:
            self.collection_types = collection_types
        if exclude_sources is not None:
            self.exclude_sources = exclude_sources

    @property
    def is_special_episode(self):
        """Gets the is_special_episode of this ApiBaseItemsRequest.  # noqa: E501


        :return: The is_special_episode of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_special_episode

    @is_special_episode.setter
    def is_special_episode(self, is_special_episode):
        """Sets the is_special_episode of this ApiBaseItemsRequest.


        :param is_special_episode: The is_special_episode of this ApiBaseItemsRequest.  # noqa: E501
        :type: bool
        """

        self._is_special_episode = is_special_episode

    @property
    def is4_k(self):
        """Gets the is4_k of this ApiBaseItemsRequest.  # noqa: E501


        :return: The is4_k of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is4_k

    @is4_k.setter
    def is4_k(self, is4_k):
        """Sets the is4_k of this ApiBaseItemsRequest.


        :param is4_k: The is4_k of this ApiBaseItemsRequest.  # noqa: E501
        :type: bool
        """

        self._is4_k = is4_k

    @property
    def enable_total_record_count(self):
        """Gets the enable_total_record_count of this ApiBaseItemsRequest.  # noqa: E501


        :return: The enable_total_record_count of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_total_record_count

    @enable_total_record_count.setter
    def enable_total_record_count(self, enable_total_record_count):
        """Sets the enable_total_record_count of this ApiBaseItemsRequest.


        :param enable_total_record_count: The enable_total_record_count of this ApiBaseItemsRequest.  # noqa: E501
        :type: bool
        """

        self._enable_total_record_count = enable_total_record_count

    @property
    def is_duplicate(self):
        """Gets the is_duplicate of this ApiBaseItemsRequest.  # noqa: E501


        :return: The is_duplicate of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_duplicate

    @is_duplicate.setter
    def is_duplicate(self, is_duplicate):
        """Sets the is_duplicate of this ApiBaseItemsRequest.


        :param is_duplicate: The is_duplicate of this ApiBaseItemsRequest.  # noqa: E501
        :type: bool
        """

        self._is_duplicate = is_duplicate

    @property
    def name(self):
        """Gets the name of this ApiBaseItemsRequest.  # noqa: E501


        :return: The name of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiBaseItemsRequest.


        :param name: The name of this ApiBaseItemsRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def recording_keyword(self):
        """Gets the recording_keyword of this ApiBaseItemsRequest.  # noqa: E501


        :return: The recording_keyword of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: str
        """
        return self._recording_keyword

    @recording_keyword.setter
    def recording_keyword(self, recording_keyword):
        """Sets the recording_keyword of this ApiBaseItemsRequest.


        :param recording_keyword: The recording_keyword of this ApiBaseItemsRequest.  # noqa: E501
        :type: str
        """

        self._recording_keyword = recording_keyword

    @property
    def recording_keyword_type(self):
        """Gets the recording_keyword_type of this ApiBaseItemsRequest.  # noqa: E501


        :return: The recording_keyword_type of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: LiveTvKeywordType
        """
        return self._recording_keyword_type

    @recording_keyword_type.setter
    def recording_keyword_type(self, recording_keyword_type):
        """Sets the recording_keyword_type of this ApiBaseItemsRequest.


        :param recording_keyword_type: The recording_keyword_type of this ApiBaseItemsRequest.  # noqa: E501
        :type: LiveTvKeywordType
        """

        self._recording_keyword_type = recording_keyword_type

    @property
    def random_seed(self):
        """Gets the random_seed of this ApiBaseItemsRequest.  # noqa: E501


        :return: The random_seed of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: int
        """
        return self._random_seed

    @random_seed.setter
    def random_seed(self, random_seed):
        """Sets the random_seed of this ApiBaseItemsRequest.


        :param random_seed: The random_seed of this ApiBaseItemsRequest.  # noqa: E501
        :type: int
        """

        self._random_seed = random_seed

    @property
    def genre_ids(self):
        """Gets the genre_ids of this ApiBaseItemsRequest.  # noqa: E501


        :return: The genre_ids of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: str
        """
        return self._genre_ids

    @genre_ids.setter
    def genre_ids(self, genre_ids):
        """Sets the genre_ids of this ApiBaseItemsRequest.


        :param genre_ids: The genre_ids of this ApiBaseItemsRequest.  # noqa: E501
        :type: str
        """

        self._genre_ids = genre_ids

    @property
    def collection_ids(self):
        """Gets the collection_ids of this ApiBaseItemsRequest.  # noqa: E501


        :return: The collection_ids of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: str
        """
        return self._collection_ids

    @collection_ids.setter
    def collection_ids(self, collection_ids):
        """Sets the collection_ids of this ApiBaseItemsRequest.


        :param collection_ids: The collection_ids of this ApiBaseItemsRequest.  # noqa: E501
        :type: str
        """

        self._collection_ids = collection_ids

    @property
    def tag_ids(self):
        """Gets the tag_ids of this ApiBaseItemsRequest.  # noqa: E501


        :return: The tag_ids of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: str
        """
        return self._tag_ids

    @tag_ids.setter
    def tag_ids(self, tag_ids):
        """Sets the tag_ids of this ApiBaseItemsRequest.


        :param tag_ids: The tag_ids of this ApiBaseItemsRequest.  # noqa: E501
        :type: str
        """

        self._tag_ids = tag_ids

    @property
    def exclude_tag_ids(self):
        """Gets the exclude_tag_ids of this ApiBaseItemsRequest.  # noqa: E501


        :return: The exclude_tag_ids of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: str
        """
        return self._exclude_tag_ids

    @exclude_tag_ids.setter
    def exclude_tag_ids(self, exclude_tag_ids):
        """Sets the exclude_tag_ids of this ApiBaseItemsRequest.


        :param exclude_tag_ids: The exclude_tag_ids of this ApiBaseItemsRequest.  # noqa: E501
        :type: str
        """

        self._exclude_tag_ids = exclude_tag_ids

    @property
    def item_person_types(self):
        """Gets the item_person_types of this ApiBaseItemsRequest.  # noqa: E501


        :return: The item_person_types of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: list[PersonType]
        """
        return self._item_person_types

    @item_person_types.setter
    def item_person_types(self, item_person_types):
        """Sets the item_person_types of this ApiBaseItemsRequest.


        :param item_person_types: The item_person_types of this ApiBaseItemsRequest.  # noqa: E501
        :type: list[PersonType]
        """

        self._item_person_types = item_person_types

    @property
    def exclude_artist_ids(self):
        """Gets the exclude_artist_ids of this ApiBaseItemsRequest.  # noqa: E501


        :return: The exclude_artist_ids of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: str
        """
        return self._exclude_artist_ids

    @exclude_artist_ids.setter
    def exclude_artist_ids(self, exclude_artist_ids):
        """Sets the exclude_artist_ids of this ApiBaseItemsRequest.


        :param exclude_artist_ids: The exclude_artist_ids of this ApiBaseItemsRequest.  # noqa: E501
        :type: str
        """

        self._exclude_artist_ids = exclude_artist_ids

    @property
    def album_artist_ids(self):
        """Gets the album_artist_ids of this ApiBaseItemsRequest.  # noqa: E501


        :return: The album_artist_ids of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: str
        """
        return self._album_artist_ids

    @album_artist_ids.setter
    def album_artist_ids(self, album_artist_ids):
        """Sets the album_artist_ids of this ApiBaseItemsRequest.


        :param album_artist_ids: The album_artist_ids of this ApiBaseItemsRequest.  # noqa: E501
        :type: str
        """

        self._album_artist_ids = album_artist_ids

    @property
    def composer_artist_ids(self):
        """Gets the composer_artist_ids of this ApiBaseItemsRequest.  # noqa: E501


        :return: The composer_artist_ids of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: str
        """
        return self._composer_artist_ids

    @composer_artist_ids.setter
    def composer_artist_ids(self, composer_artist_ids):
        """Sets the composer_artist_ids of this ApiBaseItemsRequest.


        :param composer_artist_ids: The composer_artist_ids of this ApiBaseItemsRequest.  # noqa: E501
        :type: str
        """

        self._composer_artist_ids = composer_artist_ids

    @property
    def contributing_artist_ids(self):
        """Gets the contributing_artist_ids of this ApiBaseItemsRequest.  # noqa: E501


        :return: The contributing_artist_ids of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: str
        """
        return self._contributing_artist_ids

    @contributing_artist_ids.setter
    def contributing_artist_ids(self, contributing_artist_ids):
        """Sets the contributing_artist_ids of this ApiBaseItemsRequest.


        :param contributing_artist_ids: The contributing_artist_ids of this ApiBaseItemsRequest.  # noqa: E501
        :type: str
        """

        self._contributing_artist_ids = contributing_artist_ids

    @property
    def album_ids(self):
        """Gets the album_ids of this ApiBaseItemsRequest.  # noqa: E501


        :return: The album_ids of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: str
        """
        return self._album_ids

    @album_ids.setter
    def album_ids(self, album_ids):
        """Sets the album_ids of this ApiBaseItemsRequest.


        :param album_ids: The album_ids of this ApiBaseItemsRequest.  # noqa: E501
        :type: str
        """

        self._album_ids = album_ids

    @property
    def outer_ids(self):
        """Gets the outer_ids of this ApiBaseItemsRequest.  # noqa: E501


        :return: The outer_ids of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: str
        """
        return self._outer_ids

    @outer_ids.setter
    def outer_ids(self, outer_ids):
        """Sets the outer_ids of this ApiBaseItemsRequest.


        :param outer_ids: The outer_ids of this ApiBaseItemsRequest.  # noqa: E501
        :type: str
        """

        self._outer_ids = outer_ids

    @property
    def list_item_ids(self):
        """Gets the list_item_ids of this ApiBaseItemsRequest.  # noqa: E501


        :return: The list_item_ids of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: str
        """
        return self._list_item_ids

    @list_item_ids.setter
    def list_item_ids(self, list_item_ids):
        """Sets the list_item_ids of this ApiBaseItemsRequest.


        :param list_item_ids: The list_item_ids of this ApiBaseItemsRequest.  # noqa: E501
        :type: str
        """

        self._list_item_ids = list_item_ids

    @property
    def audio_languages(self):
        """Gets the audio_languages of this ApiBaseItemsRequest.  # noqa: E501


        :return: The audio_languages of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: str
        """
        return self._audio_languages

    @audio_languages.setter
    def audio_languages(self, audio_languages):
        """Sets the audio_languages of this ApiBaseItemsRequest.


        :param audio_languages: The audio_languages of this ApiBaseItemsRequest.  # noqa: E501
        :type: str
        """

        self._audio_languages = audio_languages

    @property
    def subtitle_languages(self):
        """Gets the subtitle_languages of this ApiBaseItemsRequest.  # noqa: E501


        :return: The subtitle_languages of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: str
        """
        return self._subtitle_languages

    @subtitle_languages.setter
    def subtitle_languages(self, subtitle_languages):
        """Sets the subtitle_languages of this ApiBaseItemsRequest.


        :param subtitle_languages: The subtitle_languages of this ApiBaseItemsRequest.  # noqa: E501
        :type: str
        """

        self._subtitle_languages = subtitle_languages

    @property
    def can_edit_items(self):
        """Gets the can_edit_items of this ApiBaseItemsRequest.  # noqa: E501


        :return: The can_edit_items of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._can_edit_items

    @can_edit_items.setter
    def can_edit_items(self, can_edit_items):
        """Sets the can_edit_items of this ApiBaseItemsRequest.


        :param can_edit_items: The can_edit_items of this ApiBaseItemsRequest.  # noqa: E501
        :type: bool
        """

        self._can_edit_items = can_edit_items

    @property
    def group_items_into(self):
        """Gets the group_items_into of this ApiBaseItemsRequest.  # noqa: E501


        :return: The group_items_into of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: LibraryItemLinkType
        """
        return self._group_items_into

    @group_items_into.setter
    def group_items_into(self, group_items_into):
        """Sets the group_items_into of this ApiBaseItemsRequest.


        :param group_items_into: The group_items_into of this ApiBaseItemsRequest.  # noqa: E501
        :type: LibraryItemLinkType
        """

        self._group_items_into = group_items_into

    @property
    def is_standalone_special(self):
        """Gets the is_standalone_special of this ApiBaseItemsRequest.  # noqa: E501


        :return: The is_standalone_special of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_standalone_special

    @is_standalone_special.setter
    def is_standalone_special(self, is_standalone_special):
        """Sets the is_standalone_special of this ApiBaseItemsRequest.


        :param is_standalone_special: The is_standalone_special of this ApiBaseItemsRequest.  # noqa: E501
        :type: bool
        """

        self._is_standalone_special = is_standalone_special

    @property
    def min_width(self):
        """Gets the min_width of this ApiBaseItemsRequest.  # noqa: E501


        :return: The min_width of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: int
        """
        return self._min_width

    @min_width.setter
    def min_width(self, min_width):
        """Sets the min_width of this ApiBaseItemsRequest.


        :param min_width: The min_width of this ApiBaseItemsRequest.  # noqa: E501
        :type: int
        """

        self._min_width = min_width

    @property
    def min_height(self):
        """Gets the min_height of this ApiBaseItemsRequest.  # noqa: E501


        :return: The min_height of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: int
        """
        return self._min_height

    @min_height.setter
    def min_height(self, min_height):
        """Sets the min_height of this ApiBaseItemsRequest.


        :param min_height: The min_height of this ApiBaseItemsRequest.  # noqa: E501
        :type: int
        """

        self._min_height = min_height

    @property
    def max_width(self):
        """Gets the max_width of this ApiBaseItemsRequest.  # noqa: E501


        :return: The max_width of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_width

    @max_width.setter
    def max_width(self, max_width):
        """Sets the max_width of this ApiBaseItemsRequest.


        :param max_width: The max_width of this ApiBaseItemsRequest.  # noqa: E501
        :type: int
        """

        self._max_width = max_width

    @property
    def max_height(self):
        """Gets the max_height of this ApiBaseItemsRequest.  # noqa: E501


        :return: The max_height of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_height

    @max_height.setter
    def max_height(self, max_height):
        """Sets the max_height of this ApiBaseItemsRequest.


        :param max_height: The max_height of this ApiBaseItemsRequest.  # noqa: E501
        :type: int
        """

        self._max_height = max_height

    @property
    def group_programs_by_series(self):
        """Gets the group_programs_by_series of this ApiBaseItemsRequest.  # noqa: E501


        :return: The group_programs_by_series of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._group_programs_by_series

    @group_programs_by_series.setter
    def group_programs_by_series(self, group_programs_by_series):
        """Sets the group_programs_by_series of this ApiBaseItemsRequest.


        :param group_programs_by_series: The group_programs_by_series of this ApiBaseItemsRequest.  # noqa: E501
        :type: bool
        """

        self._group_programs_by_series = group_programs_by_series

    @property
    def air_days(self):
        """Gets the air_days of this ApiBaseItemsRequest.  # noqa: E501


        :return: The air_days of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: list[DayOfWeek]
        """
        return self._air_days

    @air_days.setter
    def air_days(self, air_days):
        """Sets the air_days of this ApiBaseItemsRequest.


        :param air_days: The air_days of this ApiBaseItemsRequest.  # noqa: E501
        :type: list[DayOfWeek]
        """

        self._air_days = air_days

    @property
    def is_airing(self):
        """Gets the is_airing of this ApiBaseItemsRequest.  # noqa: E501


        :return: The is_airing of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_airing

    @is_airing.setter
    def is_airing(self, is_airing):
        """Sets the is_airing of this ApiBaseItemsRequest.


        :param is_airing: The is_airing of this ApiBaseItemsRequest.  # noqa: E501
        :type: bool
        """

        self._is_airing = is_airing

    @property
    def has_aired(self):
        """Gets the has_aired of this ApiBaseItemsRequest.  # noqa: E501


        :return: The has_aired of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._has_aired

    @has_aired.setter
    def has_aired(self, has_aired):
        """Sets the has_aired of this ApiBaseItemsRequest.


        :param has_aired: The has_aired of this ApiBaseItemsRequest.  # noqa: E501
        :type: bool
        """

        self._has_aired = has_aired

    @property
    def collection_types(self):
        """Gets the collection_types of this ApiBaseItemsRequest.  # noqa: E501


        :return: The collection_types of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: str
        """
        return self._collection_types

    @collection_types.setter
    def collection_types(self, collection_types):
        """Sets the collection_types of this ApiBaseItemsRequest.


        :param collection_types: The collection_types of this ApiBaseItemsRequest.  # noqa: E501
        :type: str
        """

        self._collection_types = collection_types

    @property
    def exclude_sources(self):
        """Gets the exclude_sources of this ApiBaseItemsRequest.  # noqa: E501


        :return: The exclude_sources of this ApiBaseItemsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._exclude_sources

    @exclude_sources.setter
    def exclude_sources(self, exclude_sources):
        """Sets the exclude_sources of this ApiBaseItemsRequest.


        :param exclude_sources: The exclude_sources of this ApiBaseItemsRequest.  # noqa: E501
        :type: list[str]
        """

        self._exclude_sources = exclude_sources

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
        if issubclass(ApiBaseItemsRequest, dict):
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
        if not isinstance(other, ApiBaseItemsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
