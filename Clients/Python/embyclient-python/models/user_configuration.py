# coding: utf-8

"""
    Emby Server REST API
"""

import pprint
import re  # noqa: F401

import six

class UserConfiguration(object):
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
        'audio_language_preference': 'str',
        'play_default_audio_track': 'bool',
        'subtitle_language_preference': 'str',
        'profile_pin': 'str',
        'display_missing_episodes': 'bool',
        'subtitle_mode': 'SubtitlePlaybackMode',
        'ordered_views': 'list[str]',
        'latest_items_excludes': 'list[str]',
        'my_media_excludes': 'list[str]',
        'hide_played_in_latest': 'bool',
        'hide_played_in_more_like_this': 'bool',
        'hide_played_in_suggestions': 'bool',
        'remember_audio_selections': 'bool',
        'remember_subtitle_selections': 'bool',
        'enable_next_episode_auto_play': 'bool',
        'resume_rewind_seconds': 'int',
        'intro_skip_mode': 'SegmentSkipMode',
        'enable_local_password': 'bool'
    }

    attribute_map = {
        'audio_language_preference': 'AudioLanguagePreference',
        'play_default_audio_track': 'PlayDefaultAudioTrack',
        'subtitle_language_preference': 'SubtitleLanguagePreference',
        'profile_pin': 'ProfilePin',
        'display_missing_episodes': 'DisplayMissingEpisodes',
        'subtitle_mode': 'SubtitleMode',
        'ordered_views': 'OrderedViews',
        'latest_items_excludes': 'LatestItemsExcludes',
        'my_media_excludes': 'MyMediaExcludes',
        'hide_played_in_latest': 'HidePlayedInLatest',
        'hide_played_in_more_like_this': 'HidePlayedInMoreLikeThis',
        'hide_played_in_suggestions': 'HidePlayedInSuggestions',
        'remember_audio_selections': 'RememberAudioSelections',
        'remember_subtitle_selections': 'RememberSubtitleSelections',
        'enable_next_episode_auto_play': 'EnableNextEpisodeAutoPlay',
        'resume_rewind_seconds': 'ResumeRewindSeconds',
        'intro_skip_mode': 'IntroSkipMode',
        'enable_local_password': 'EnableLocalPassword'
    }

    def __init__(self, audio_language_preference=None, play_default_audio_track=None, subtitle_language_preference=None, profile_pin=None, display_missing_episodes=None, subtitle_mode=None, ordered_views=None, latest_items_excludes=None, my_media_excludes=None, hide_played_in_latest=None, hide_played_in_more_like_this=None, hide_played_in_suggestions=None, remember_audio_selections=None, remember_subtitle_selections=None, enable_next_episode_auto_play=None, resume_rewind_seconds=None, intro_skip_mode=None, enable_local_password=None):  # noqa: E501
        """UserConfiguration - a model defined in Swagger"""  # noqa: E501
        self._audio_language_preference = None
        self._play_default_audio_track = None
        self._subtitle_language_preference = None
        self._profile_pin = None
        self._display_missing_episodes = None
        self._subtitle_mode = None
        self._ordered_views = None
        self._latest_items_excludes = None
        self._my_media_excludes = None
        self._hide_played_in_latest = None
        self._hide_played_in_more_like_this = None
        self._hide_played_in_suggestions = None
        self._remember_audio_selections = None
        self._remember_subtitle_selections = None
        self._enable_next_episode_auto_play = None
        self._resume_rewind_seconds = None
        self._intro_skip_mode = None
        self._enable_local_password = None
        self.discriminator = None
        if audio_language_preference is not None:
            self.audio_language_preference = audio_language_preference
        if play_default_audio_track is not None:
            self.play_default_audio_track = play_default_audio_track
        if subtitle_language_preference is not None:
            self.subtitle_language_preference = subtitle_language_preference
        if profile_pin is not None:
            self.profile_pin = profile_pin
        if display_missing_episodes is not None:
            self.display_missing_episodes = display_missing_episodes
        if subtitle_mode is not None:
            self.subtitle_mode = subtitle_mode
        if ordered_views is not None:
            self.ordered_views = ordered_views
        if latest_items_excludes is not None:
            self.latest_items_excludes = latest_items_excludes
        if my_media_excludes is not None:
            self.my_media_excludes = my_media_excludes
        if hide_played_in_latest is not None:
            self.hide_played_in_latest = hide_played_in_latest
        if hide_played_in_more_like_this is not None:
            self.hide_played_in_more_like_this = hide_played_in_more_like_this
        if hide_played_in_suggestions is not None:
            self.hide_played_in_suggestions = hide_played_in_suggestions
        if remember_audio_selections is not None:
            self.remember_audio_selections = remember_audio_selections
        if remember_subtitle_selections is not None:
            self.remember_subtitle_selections = remember_subtitle_selections
        if enable_next_episode_auto_play is not None:
            self.enable_next_episode_auto_play = enable_next_episode_auto_play
        if resume_rewind_seconds is not None:
            self.resume_rewind_seconds = resume_rewind_seconds
        if intro_skip_mode is not None:
            self.intro_skip_mode = intro_skip_mode
        if enable_local_password is not None:
            self.enable_local_password = enable_local_password

    @property
    def audio_language_preference(self):
        """Gets the audio_language_preference of this UserConfiguration.  # noqa: E501

        The audio language preference.  # noqa: E501

        :return: The audio_language_preference of this UserConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._audio_language_preference

    @audio_language_preference.setter
    def audio_language_preference(self, audio_language_preference):
        """Sets the audio_language_preference of this UserConfiguration.

        The audio language preference.  # noqa: E501

        :param audio_language_preference: The audio_language_preference of this UserConfiguration.  # noqa: E501
        :type: str
        """

        self._audio_language_preference = audio_language_preference

    @property
    def play_default_audio_track(self):
        """Gets the play_default_audio_track of this UserConfiguration.  # noqa: E501

        A value indicating whether \\[play default audio track\\].  # noqa: E501

        :return: The play_default_audio_track of this UserConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._play_default_audio_track

    @play_default_audio_track.setter
    def play_default_audio_track(self, play_default_audio_track):
        """Sets the play_default_audio_track of this UserConfiguration.

        A value indicating whether \\[play default audio track\\].  # noqa: E501

        :param play_default_audio_track: The play_default_audio_track of this UserConfiguration.  # noqa: E501
        :type: bool
        """

        self._play_default_audio_track = play_default_audio_track

    @property
    def subtitle_language_preference(self):
        """Gets the subtitle_language_preference of this UserConfiguration.  # noqa: E501

        The subtitle language preference.  # noqa: E501

        :return: The subtitle_language_preference of this UserConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._subtitle_language_preference

    @subtitle_language_preference.setter
    def subtitle_language_preference(self, subtitle_language_preference):
        """Sets the subtitle_language_preference of this UserConfiguration.

        The subtitle language preference.  # noqa: E501

        :param subtitle_language_preference: The subtitle_language_preference of this UserConfiguration.  # noqa: E501
        :type: str
        """

        self._subtitle_language_preference = subtitle_language_preference

    @property
    def profile_pin(self):
        """Gets the profile_pin of this UserConfiguration.  # noqa: E501


        :return: The profile_pin of this UserConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._profile_pin

    @profile_pin.setter
    def profile_pin(self, profile_pin):
        """Sets the profile_pin of this UserConfiguration.


        :param profile_pin: The profile_pin of this UserConfiguration.  # noqa: E501
        :type: str
        """

        self._profile_pin = profile_pin

    @property
    def display_missing_episodes(self):
        """Gets the display_missing_episodes of this UserConfiguration.  # noqa: E501


        :return: The display_missing_episodes of this UserConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._display_missing_episodes

    @display_missing_episodes.setter
    def display_missing_episodes(self, display_missing_episodes):
        """Sets the display_missing_episodes of this UserConfiguration.


        :param display_missing_episodes: The display_missing_episodes of this UserConfiguration.  # noqa: E501
        :type: bool
        """

        self._display_missing_episodes = display_missing_episodes

    @property
    def subtitle_mode(self):
        """Gets the subtitle_mode of this UserConfiguration.  # noqa: E501


        :return: The subtitle_mode of this UserConfiguration.  # noqa: E501
        :rtype: SubtitlePlaybackMode
        """
        return self._subtitle_mode

    @subtitle_mode.setter
    def subtitle_mode(self, subtitle_mode):
        """Sets the subtitle_mode of this UserConfiguration.


        :param subtitle_mode: The subtitle_mode of this UserConfiguration.  # noqa: E501
        :type: SubtitlePlaybackMode
        """

        self._subtitle_mode = subtitle_mode

    @property
    def ordered_views(self):
        """Gets the ordered_views of this UserConfiguration.  # noqa: E501


        :return: The ordered_views of this UserConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._ordered_views

    @ordered_views.setter
    def ordered_views(self, ordered_views):
        """Sets the ordered_views of this UserConfiguration.


        :param ordered_views: The ordered_views of this UserConfiguration.  # noqa: E501
        :type: list[str]
        """

        self._ordered_views = ordered_views

    @property
    def latest_items_excludes(self):
        """Gets the latest_items_excludes of this UserConfiguration.  # noqa: E501


        :return: The latest_items_excludes of this UserConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._latest_items_excludes

    @latest_items_excludes.setter
    def latest_items_excludes(self, latest_items_excludes):
        """Sets the latest_items_excludes of this UserConfiguration.


        :param latest_items_excludes: The latest_items_excludes of this UserConfiguration.  # noqa: E501
        :type: list[str]
        """

        self._latest_items_excludes = latest_items_excludes

    @property
    def my_media_excludes(self):
        """Gets the my_media_excludes of this UserConfiguration.  # noqa: E501


        :return: The my_media_excludes of this UserConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._my_media_excludes

    @my_media_excludes.setter
    def my_media_excludes(self, my_media_excludes):
        """Sets the my_media_excludes of this UserConfiguration.


        :param my_media_excludes: The my_media_excludes of this UserConfiguration.  # noqa: E501
        :type: list[str]
        """

        self._my_media_excludes = my_media_excludes

    @property
    def hide_played_in_latest(self):
        """Gets the hide_played_in_latest of this UserConfiguration.  # noqa: E501


        :return: The hide_played_in_latest of this UserConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._hide_played_in_latest

    @hide_played_in_latest.setter
    def hide_played_in_latest(self, hide_played_in_latest):
        """Sets the hide_played_in_latest of this UserConfiguration.


        :param hide_played_in_latest: The hide_played_in_latest of this UserConfiguration.  # noqa: E501
        :type: bool
        """

        self._hide_played_in_latest = hide_played_in_latest

    @property
    def hide_played_in_more_like_this(self):
        """Gets the hide_played_in_more_like_this of this UserConfiguration.  # noqa: E501


        :return: The hide_played_in_more_like_this of this UserConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._hide_played_in_more_like_this

    @hide_played_in_more_like_this.setter
    def hide_played_in_more_like_this(self, hide_played_in_more_like_this):
        """Sets the hide_played_in_more_like_this of this UserConfiguration.


        :param hide_played_in_more_like_this: The hide_played_in_more_like_this of this UserConfiguration.  # noqa: E501
        :type: bool
        """

        self._hide_played_in_more_like_this = hide_played_in_more_like_this

    @property
    def hide_played_in_suggestions(self):
        """Gets the hide_played_in_suggestions of this UserConfiguration.  # noqa: E501


        :return: The hide_played_in_suggestions of this UserConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._hide_played_in_suggestions

    @hide_played_in_suggestions.setter
    def hide_played_in_suggestions(self, hide_played_in_suggestions):
        """Sets the hide_played_in_suggestions of this UserConfiguration.


        :param hide_played_in_suggestions: The hide_played_in_suggestions of this UserConfiguration.  # noqa: E501
        :type: bool
        """

        self._hide_played_in_suggestions = hide_played_in_suggestions

    @property
    def remember_audio_selections(self):
        """Gets the remember_audio_selections of this UserConfiguration.  # noqa: E501


        :return: The remember_audio_selections of this UserConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._remember_audio_selections

    @remember_audio_selections.setter
    def remember_audio_selections(self, remember_audio_selections):
        """Sets the remember_audio_selections of this UserConfiguration.


        :param remember_audio_selections: The remember_audio_selections of this UserConfiguration.  # noqa: E501
        :type: bool
        """

        self._remember_audio_selections = remember_audio_selections

    @property
    def remember_subtitle_selections(self):
        """Gets the remember_subtitle_selections of this UserConfiguration.  # noqa: E501


        :return: The remember_subtitle_selections of this UserConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._remember_subtitle_selections

    @remember_subtitle_selections.setter
    def remember_subtitle_selections(self, remember_subtitle_selections):
        """Sets the remember_subtitle_selections of this UserConfiguration.


        :param remember_subtitle_selections: The remember_subtitle_selections of this UserConfiguration.  # noqa: E501
        :type: bool
        """

        self._remember_subtitle_selections = remember_subtitle_selections

    @property
    def enable_next_episode_auto_play(self):
        """Gets the enable_next_episode_auto_play of this UserConfiguration.  # noqa: E501


        :return: The enable_next_episode_auto_play of this UserConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._enable_next_episode_auto_play

    @enable_next_episode_auto_play.setter
    def enable_next_episode_auto_play(self, enable_next_episode_auto_play):
        """Sets the enable_next_episode_auto_play of this UserConfiguration.


        :param enable_next_episode_auto_play: The enable_next_episode_auto_play of this UserConfiguration.  # noqa: E501
        :type: bool
        """

        self._enable_next_episode_auto_play = enable_next_episode_auto_play

    @property
    def resume_rewind_seconds(self):
        """Gets the resume_rewind_seconds of this UserConfiguration.  # noqa: E501


        :return: The resume_rewind_seconds of this UserConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._resume_rewind_seconds

    @resume_rewind_seconds.setter
    def resume_rewind_seconds(self, resume_rewind_seconds):
        """Sets the resume_rewind_seconds of this UserConfiguration.


        :param resume_rewind_seconds: The resume_rewind_seconds of this UserConfiguration.  # noqa: E501
        :type: int
        """

        self._resume_rewind_seconds = resume_rewind_seconds

    @property
    def intro_skip_mode(self):
        """Gets the intro_skip_mode of this UserConfiguration.  # noqa: E501


        :return: The intro_skip_mode of this UserConfiguration.  # noqa: E501
        :rtype: SegmentSkipMode
        """
        return self._intro_skip_mode

    @intro_skip_mode.setter
    def intro_skip_mode(self, intro_skip_mode):
        """Sets the intro_skip_mode of this UserConfiguration.


        :param intro_skip_mode: The intro_skip_mode of this UserConfiguration.  # noqa: E501
        :type: SegmentSkipMode
        """

        self._intro_skip_mode = intro_skip_mode

    @property
    def enable_local_password(self):
        """Gets the enable_local_password of this UserConfiguration.  # noqa: E501


        :return: The enable_local_password of this UserConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._enable_local_password

    @enable_local_password.setter
    def enable_local_password(self, enable_local_password):
        """Sets the enable_local_password of this UserConfiguration.


        :param enable_local_password: The enable_local_password of this UserConfiguration.  # noqa: E501
        :type: bool
        """

        self._enable_local_password = enable_local_password

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
        if issubclass(UserConfiguration, dict):
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
        if not isinstance(other, UserConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
