# coding: utf-8

"""
    Emby Server REST API
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from embyclient.api_client import ApiClient


class DynamicHlsServiceApi(object):
    """NOTE: This class is auto generated.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(self, segment_container, segment_id, id, playlist_id, **kwargs):  # noqa: E501
        """get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(segment_container, segment_id, id, playlist_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str segment_container: (required)
        :param str segment_id: (required)
        :param str id: (required)
        :param str playlist_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer_with_http_info(segment_container, segment_id, id, playlist_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer_with_http_info(segment_container, segment_id, id, playlist_id, **kwargs)  # noqa: E501
            return data

    def get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer_with_http_info(self, segment_container, segment_id, id, playlist_id, **kwargs):  # noqa: E501
        """get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer_with_http_info(segment_container, segment_id, id, playlist_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str segment_container: (required)
        :param str segment_id: (required)
        :param str id: (required)
        :param str playlist_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['segment_container', 'segment_id', 'id', 'playlist_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'segment_container' is set
        if ('segment_container' not in params or
                params['segment_container'] is None):
            raise ValueError("Missing the required parameter `segment_container` when calling `get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer`")  # noqa: E501
        # verify the required parameter 'segment_id' is set
        if ('segment_id' not in params or
                params['segment_id'] is None):
            raise ValueError("Missing the required parameter `segment_id` when calling `get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer`")  # noqa: E501
        # verify the required parameter 'playlist_id' is set
        if ('playlist_id' not in params or
                params['playlist_id'] is None):
            raise ValueError("Missing the required parameter `playlist_id` when calling `get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'segment_container' in params:
            path_params['SegmentContainer'] = params['segment_container']  # noqa: E501
        if 'segment_id' in params:
            path_params['SegmentId'] = params['segment_id']  # noqa: E501
        if 'id' in params:
            path_params['Id'] = params['id']  # noqa: E501
        if 'playlist_id' in params:
            path_params['PlaylistId'] = params['playlist_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apikeyauth', 'embyauth']  # noqa: E501

        return self.api_client.call_api(
            '/Audio/{Id}/hls1/{PlaylistId}/{SegmentId}.{SegmentContainer}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_audio_by_id_live_m3u8(self, id, container, **kwargs):  # noqa: E501
        """get_audio_by_id_live_m3u8  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audio_by_id_live_m3u8(id, container, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Item Id (required)
        :param str container: Container (required)
        :param str device_profile_id: Optional. The dlna device profile id to utilize.
        :param str device_id: The device id of the client requesting. Used to stop encoding processes when needed.
        :param str audio_codec: Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
        :param bool enable_auto_stream_copy: Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
        :param int audio_sample_rate: Optional. Specify a specific audio sample rate, e.g. 44100
        :param int audio_bit_rate: Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
        :param int audio_channels: Optional. Specify a specific number of audio channels to encode to, e.g. 2
        :param int max_audio_channels: Optional. Specify a maximum number of audio channels to encode to, e.g. 2
        :param bool static: Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false
        :param bool copy_timestamps: Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
        :param int start_time_ticks: Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks.
        :param int width: Optional. The fixed horizontal resolution of the encoded video.
        :param int height: Optional. The fixed vertical resolution of the encoded video.
        :param int max_width: Optional. The maximum horizontal resolution of the encoded video.
        :param int max_height: Optional. The maximum vertical resolution of the encoded video.
        :param int video_bit_rate: Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
        :param int subtitle_stream_index: Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
        :param SubtitleDeliveryMethod subtitle_method: Optional. Specify the subtitle delivery method.
        :param int max_video_bit_depth: Optional.
        :param str video_codec: Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv.
        :param int audio_stream_index: Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
        :param int video_stream_index: Optional. The index of the video stream to use. If omitted the first video stream will be used.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_audio_by_id_live_m3u8_with_http_info(id, container, **kwargs)  # noqa: E501
        else:
            (data) = self.get_audio_by_id_live_m3u8_with_http_info(id, container, **kwargs)  # noqa: E501
            return data

    def get_audio_by_id_live_m3u8_with_http_info(self, id, container, **kwargs):  # noqa: E501
        """get_audio_by_id_live_m3u8  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audio_by_id_live_m3u8_with_http_info(id, container, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Item Id (required)
        :param str container: Container (required)
        :param str device_profile_id: Optional. The dlna device profile id to utilize.
        :param str device_id: The device id of the client requesting. Used to stop encoding processes when needed.
        :param str audio_codec: Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
        :param bool enable_auto_stream_copy: Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
        :param int audio_sample_rate: Optional. Specify a specific audio sample rate, e.g. 44100
        :param int audio_bit_rate: Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
        :param int audio_channels: Optional. Specify a specific number of audio channels to encode to, e.g. 2
        :param int max_audio_channels: Optional. Specify a maximum number of audio channels to encode to, e.g. 2
        :param bool static: Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false
        :param bool copy_timestamps: Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
        :param int start_time_ticks: Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks.
        :param int width: Optional. The fixed horizontal resolution of the encoded video.
        :param int height: Optional. The fixed vertical resolution of the encoded video.
        :param int max_width: Optional. The maximum horizontal resolution of the encoded video.
        :param int max_height: Optional. The maximum vertical resolution of the encoded video.
        :param int video_bit_rate: Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
        :param int subtitle_stream_index: Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
        :param SubtitleDeliveryMethod subtitle_method: Optional. Specify the subtitle delivery method.
        :param int max_video_bit_depth: Optional.
        :param str video_codec: Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv.
        :param int audio_stream_index: Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
        :param int video_stream_index: Optional. The index of the video stream to use. If omitted the first video stream will be used.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'container', 'device_profile_id', 'device_id', 'audio_codec', 'enable_auto_stream_copy', 'audio_sample_rate', 'audio_bit_rate', 'audio_channels', 'max_audio_channels', 'static', 'copy_timestamps', 'start_time_ticks', 'width', 'height', 'max_width', 'max_height', 'video_bit_rate', 'subtitle_stream_index', 'subtitle_method', 'max_video_bit_depth', 'video_codec', 'audio_stream_index', 'video_stream_index']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audio_by_id_live_m3u8" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_audio_by_id_live_m3u8`")  # noqa: E501
        # verify the required parameter 'container' is set
        if ('container' not in params or
                params['container'] is None):
            raise ValueError("Missing the required parameter `container` when calling `get_audio_by_id_live_m3u8`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['Id'] = params['id']  # noqa: E501

        query_params = []
        if 'device_profile_id' in params:
            query_params.append(('DeviceProfileId', params['device_profile_id']))  # noqa: E501
        if 'device_id' in params:
            query_params.append(('DeviceId', params['device_id']))  # noqa: E501
        if 'container' in params:
            query_params.append(('Container', params['container']))  # noqa: E501
        if 'audio_codec' in params:
            query_params.append(('AudioCodec', params['audio_codec']))  # noqa: E501
        if 'enable_auto_stream_copy' in params:
            query_params.append(('EnableAutoStreamCopy', params['enable_auto_stream_copy']))  # noqa: E501
        if 'audio_sample_rate' in params:
            query_params.append(('AudioSampleRate', params['audio_sample_rate']))  # noqa: E501
        if 'audio_bit_rate' in params:
            query_params.append(('AudioBitRate', params['audio_bit_rate']))  # noqa: E501
        if 'audio_channels' in params:
            query_params.append(('AudioChannels', params['audio_channels']))  # noqa: E501
        if 'max_audio_channels' in params:
            query_params.append(('MaxAudioChannels', params['max_audio_channels']))  # noqa: E501
        if 'static' in params:
            query_params.append(('Static', params['static']))  # noqa: E501
        if 'copy_timestamps' in params:
            query_params.append(('CopyTimestamps', params['copy_timestamps']))  # noqa: E501
        if 'start_time_ticks' in params:
            query_params.append(('StartTimeTicks', params['start_time_ticks']))  # noqa: E501
        if 'width' in params:
            query_params.append(('Width', params['width']))  # noqa: E501
        if 'height' in params:
            query_params.append(('Height', params['height']))  # noqa: E501
        if 'max_width' in params:
            query_params.append(('MaxWidth', params['max_width']))  # noqa: E501
        if 'max_height' in params:
            query_params.append(('MaxHeight', params['max_height']))  # noqa: E501
        if 'video_bit_rate' in params:
            query_params.append(('VideoBitRate', params['video_bit_rate']))  # noqa: E501
        if 'subtitle_stream_index' in params:
            query_params.append(('SubtitleStreamIndex', params['subtitle_stream_index']))  # noqa: E501
        if 'subtitle_method' in params:
            query_params.append(('SubtitleMethod', params['subtitle_method']))  # noqa: E501
        if 'max_video_bit_depth' in params:
            query_params.append(('MaxVideoBitDepth', params['max_video_bit_depth']))  # noqa: E501
        if 'video_codec' in params:
            query_params.append(('VideoCodec', params['video_codec']))  # noqa: E501
        if 'audio_stream_index' in params:
            query_params.append(('AudioStreamIndex', params['audio_stream_index']))  # noqa: E501
        if 'video_stream_index' in params:
            query_params.append(('VideoStreamIndex', params['video_stream_index']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apikeyauth', 'embyauth']  # noqa: E501

        return self.api_client.call_api(
            '/Audio/{Id}/live.m3u8', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_audio_by_id_main_m3u8(self, id, container, **kwargs):  # noqa: E501
        """Gets an audio stream using HTTP live streaming.  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audio_by_id_main_m3u8(id, container, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Item Id (required)
        :param str container: Container (required)
        :param str device_profile_id: Optional. The dlna device profile id to utilize.
        :param str device_id: The device id of the client requesting. Used to stop encoding processes when needed.
        :param str audio_codec: Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
        :param bool enable_auto_stream_copy: Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
        :param int audio_sample_rate: Optional. Specify a specific audio sample rate, e.g. 44100
        :param int audio_bit_rate: Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
        :param int audio_channels: Optional. Specify a specific number of audio channels to encode to, e.g. 2
        :param int max_audio_channels: Optional. Specify a maximum number of audio channels to encode to, e.g. 2
        :param bool static: Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false
        :param bool copy_timestamps: Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
        :param int start_time_ticks: Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks.
        :param int width: Optional. The fixed horizontal resolution of the encoded video.
        :param int height: Optional. The fixed vertical resolution of the encoded video.
        :param int max_width: Optional. The maximum horizontal resolution of the encoded video.
        :param int max_height: Optional. The maximum vertical resolution of the encoded video.
        :param int video_bit_rate: Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
        :param int subtitle_stream_index: Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
        :param SubtitleDeliveryMethod subtitle_method: Optional. Specify the subtitle delivery method.
        :param int max_video_bit_depth: Optional.
        :param str video_codec: Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv.
        :param int audio_stream_index: Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
        :param int video_stream_index: Optional. The index of the video stream to use. If omitted the first video stream will be used.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_audio_by_id_main_m3u8_with_http_info(id, container, **kwargs)  # noqa: E501
        else:
            (data) = self.get_audio_by_id_main_m3u8_with_http_info(id, container, **kwargs)  # noqa: E501
            return data

    def get_audio_by_id_main_m3u8_with_http_info(self, id, container, **kwargs):  # noqa: E501
        """Gets an audio stream using HTTP live streaming.  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audio_by_id_main_m3u8_with_http_info(id, container, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Item Id (required)
        :param str container: Container (required)
        :param str device_profile_id: Optional. The dlna device profile id to utilize.
        :param str device_id: The device id of the client requesting. Used to stop encoding processes when needed.
        :param str audio_codec: Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
        :param bool enable_auto_stream_copy: Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
        :param int audio_sample_rate: Optional. Specify a specific audio sample rate, e.g. 44100
        :param int audio_bit_rate: Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
        :param int audio_channels: Optional. Specify a specific number of audio channels to encode to, e.g. 2
        :param int max_audio_channels: Optional. Specify a maximum number of audio channels to encode to, e.g. 2
        :param bool static: Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false
        :param bool copy_timestamps: Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
        :param int start_time_ticks: Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks.
        :param int width: Optional. The fixed horizontal resolution of the encoded video.
        :param int height: Optional. The fixed vertical resolution of the encoded video.
        :param int max_width: Optional. The maximum horizontal resolution of the encoded video.
        :param int max_height: Optional. The maximum vertical resolution of the encoded video.
        :param int video_bit_rate: Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
        :param int subtitle_stream_index: Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
        :param SubtitleDeliveryMethod subtitle_method: Optional. Specify the subtitle delivery method.
        :param int max_video_bit_depth: Optional.
        :param str video_codec: Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv.
        :param int audio_stream_index: Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
        :param int video_stream_index: Optional. The index of the video stream to use. If omitted the first video stream will be used.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'container', 'device_profile_id', 'device_id', 'audio_codec', 'enable_auto_stream_copy', 'audio_sample_rate', 'audio_bit_rate', 'audio_channels', 'max_audio_channels', 'static', 'copy_timestamps', 'start_time_ticks', 'width', 'height', 'max_width', 'max_height', 'video_bit_rate', 'subtitle_stream_index', 'subtitle_method', 'max_video_bit_depth', 'video_codec', 'audio_stream_index', 'video_stream_index']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audio_by_id_main_m3u8" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_audio_by_id_main_m3u8`")  # noqa: E501
        # verify the required parameter 'container' is set
        if ('container' not in params or
                params['container'] is None):
            raise ValueError("Missing the required parameter `container` when calling `get_audio_by_id_main_m3u8`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['Id'] = params['id']  # noqa: E501

        query_params = []
        if 'device_profile_id' in params:
            query_params.append(('DeviceProfileId', params['device_profile_id']))  # noqa: E501
        if 'device_id' in params:
            query_params.append(('DeviceId', params['device_id']))  # noqa: E501
        if 'container' in params:
            query_params.append(('Container', params['container']))  # noqa: E501
        if 'audio_codec' in params:
            query_params.append(('AudioCodec', params['audio_codec']))  # noqa: E501
        if 'enable_auto_stream_copy' in params:
            query_params.append(('EnableAutoStreamCopy', params['enable_auto_stream_copy']))  # noqa: E501
        if 'audio_sample_rate' in params:
            query_params.append(('AudioSampleRate', params['audio_sample_rate']))  # noqa: E501
        if 'audio_bit_rate' in params:
            query_params.append(('AudioBitRate', params['audio_bit_rate']))  # noqa: E501
        if 'audio_channels' in params:
            query_params.append(('AudioChannels', params['audio_channels']))  # noqa: E501
        if 'max_audio_channels' in params:
            query_params.append(('MaxAudioChannels', params['max_audio_channels']))  # noqa: E501
        if 'static' in params:
            query_params.append(('Static', params['static']))  # noqa: E501
        if 'copy_timestamps' in params:
            query_params.append(('CopyTimestamps', params['copy_timestamps']))  # noqa: E501
        if 'start_time_ticks' in params:
            query_params.append(('StartTimeTicks', params['start_time_ticks']))  # noqa: E501
        if 'width' in params:
            query_params.append(('Width', params['width']))  # noqa: E501
        if 'height' in params:
            query_params.append(('Height', params['height']))  # noqa: E501
        if 'max_width' in params:
            query_params.append(('MaxWidth', params['max_width']))  # noqa: E501
        if 'max_height' in params:
            query_params.append(('MaxHeight', params['max_height']))  # noqa: E501
        if 'video_bit_rate' in params:
            query_params.append(('VideoBitRate', params['video_bit_rate']))  # noqa: E501
        if 'subtitle_stream_index' in params:
            query_params.append(('SubtitleStreamIndex', params['subtitle_stream_index']))  # noqa: E501
        if 'subtitle_method' in params:
            query_params.append(('SubtitleMethod', params['subtitle_method']))  # noqa: E501
        if 'max_video_bit_depth' in params:
            query_params.append(('MaxVideoBitDepth', params['max_video_bit_depth']))  # noqa: E501
        if 'video_codec' in params:
            query_params.append(('VideoCodec', params['video_codec']))  # noqa: E501
        if 'audio_stream_index' in params:
            query_params.append(('AudioStreamIndex', params['audio_stream_index']))  # noqa: E501
        if 'video_stream_index' in params:
            query_params.append(('VideoStreamIndex', params['video_stream_index']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apikeyauth', 'embyauth']  # noqa: E501

        return self.api_client.call_api(
            '/Audio/{Id}/main.m3u8', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_audio_by_id_master_m3u8(self, id, container, **kwargs):  # noqa: E501
        """Gets an audio stream using HTTP live streaming.  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audio_by_id_master_m3u8(id, container, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Item Id (required)
        :param str container: Container (required)
        :param str device_profile_id: Optional. The dlna device profile id to utilize.
        :param str device_id: The device id of the client requesting. Used to stop encoding processes when needed.
        :param str audio_codec: Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
        :param bool enable_auto_stream_copy: Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
        :param int audio_sample_rate: Optional. Specify a specific audio sample rate, e.g. 44100
        :param int audio_bit_rate: Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
        :param int audio_channels: Optional. Specify a specific number of audio channels to encode to, e.g. 2
        :param int max_audio_channels: Optional. Specify a maximum number of audio channels to encode to, e.g. 2
        :param bool static: Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false
        :param bool copy_timestamps: Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
        :param int start_time_ticks: Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks.
        :param int width: Optional. The fixed horizontal resolution of the encoded video.
        :param int height: Optional. The fixed vertical resolution of the encoded video.
        :param int max_width: Optional. The maximum horizontal resolution of the encoded video.
        :param int max_height: Optional. The maximum vertical resolution of the encoded video.
        :param int video_bit_rate: Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
        :param int subtitle_stream_index: Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
        :param SubtitleDeliveryMethod subtitle_method: Optional. Specify the subtitle delivery method.
        :param int max_video_bit_depth: Optional.
        :param str video_codec: Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv.
        :param int audio_stream_index: Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
        :param int video_stream_index: Optional. The index of the video stream to use. If omitted the first video stream will be used.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_audio_by_id_master_m3u8_with_http_info(id, container, **kwargs)  # noqa: E501
        else:
            (data) = self.get_audio_by_id_master_m3u8_with_http_info(id, container, **kwargs)  # noqa: E501
            return data

    def get_audio_by_id_master_m3u8_with_http_info(self, id, container, **kwargs):  # noqa: E501
        """Gets an audio stream using HTTP live streaming.  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audio_by_id_master_m3u8_with_http_info(id, container, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Item Id (required)
        :param str container: Container (required)
        :param str device_profile_id: Optional. The dlna device profile id to utilize.
        :param str device_id: The device id of the client requesting. Used to stop encoding processes when needed.
        :param str audio_codec: Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
        :param bool enable_auto_stream_copy: Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
        :param int audio_sample_rate: Optional. Specify a specific audio sample rate, e.g. 44100
        :param int audio_bit_rate: Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
        :param int audio_channels: Optional. Specify a specific number of audio channels to encode to, e.g. 2
        :param int max_audio_channels: Optional. Specify a maximum number of audio channels to encode to, e.g. 2
        :param bool static: Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false
        :param bool copy_timestamps: Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
        :param int start_time_ticks: Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks.
        :param int width: Optional. The fixed horizontal resolution of the encoded video.
        :param int height: Optional. The fixed vertical resolution of the encoded video.
        :param int max_width: Optional. The maximum horizontal resolution of the encoded video.
        :param int max_height: Optional. The maximum vertical resolution of the encoded video.
        :param int video_bit_rate: Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
        :param int subtitle_stream_index: Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
        :param SubtitleDeliveryMethod subtitle_method: Optional. Specify the subtitle delivery method.
        :param int max_video_bit_depth: Optional.
        :param str video_codec: Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv.
        :param int audio_stream_index: Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
        :param int video_stream_index: Optional. The index of the video stream to use. If omitted the first video stream will be used.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'container', 'device_profile_id', 'device_id', 'audio_codec', 'enable_auto_stream_copy', 'audio_sample_rate', 'audio_bit_rate', 'audio_channels', 'max_audio_channels', 'static', 'copy_timestamps', 'start_time_ticks', 'width', 'height', 'max_width', 'max_height', 'video_bit_rate', 'subtitle_stream_index', 'subtitle_method', 'max_video_bit_depth', 'video_codec', 'audio_stream_index', 'video_stream_index']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audio_by_id_master_m3u8" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_audio_by_id_master_m3u8`")  # noqa: E501
        # verify the required parameter 'container' is set
        if ('container' not in params or
                params['container'] is None):
            raise ValueError("Missing the required parameter `container` when calling `get_audio_by_id_master_m3u8`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['Id'] = params['id']  # noqa: E501

        query_params = []
        if 'device_profile_id' in params:
            query_params.append(('DeviceProfileId', params['device_profile_id']))  # noqa: E501
        if 'device_id' in params:
            query_params.append(('DeviceId', params['device_id']))  # noqa: E501
        if 'container' in params:
            query_params.append(('Container', params['container']))  # noqa: E501
        if 'audio_codec' in params:
            query_params.append(('AudioCodec', params['audio_codec']))  # noqa: E501
        if 'enable_auto_stream_copy' in params:
            query_params.append(('EnableAutoStreamCopy', params['enable_auto_stream_copy']))  # noqa: E501
        if 'audio_sample_rate' in params:
            query_params.append(('AudioSampleRate', params['audio_sample_rate']))  # noqa: E501
        if 'audio_bit_rate' in params:
            query_params.append(('AudioBitRate', params['audio_bit_rate']))  # noqa: E501
        if 'audio_channels' in params:
            query_params.append(('AudioChannels', params['audio_channels']))  # noqa: E501
        if 'max_audio_channels' in params:
            query_params.append(('MaxAudioChannels', params['max_audio_channels']))  # noqa: E501
        if 'static' in params:
            query_params.append(('Static', params['static']))  # noqa: E501
        if 'copy_timestamps' in params:
            query_params.append(('CopyTimestamps', params['copy_timestamps']))  # noqa: E501
        if 'start_time_ticks' in params:
            query_params.append(('StartTimeTicks', params['start_time_ticks']))  # noqa: E501
        if 'width' in params:
            query_params.append(('Width', params['width']))  # noqa: E501
        if 'height' in params:
            query_params.append(('Height', params['height']))  # noqa: E501
        if 'max_width' in params:
            query_params.append(('MaxWidth', params['max_width']))  # noqa: E501
        if 'max_height' in params:
            query_params.append(('MaxHeight', params['max_height']))  # noqa: E501
        if 'video_bit_rate' in params:
            query_params.append(('VideoBitRate', params['video_bit_rate']))  # noqa: E501
        if 'subtitle_stream_index' in params:
            query_params.append(('SubtitleStreamIndex', params['subtitle_stream_index']))  # noqa: E501
        if 'subtitle_method' in params:
            query_params.append(('SubtitleMethod', params['subtitle_method']))  # noqa: E501
        if 'max_video_bit_depth' in params:
            query_params.append(('MaxVideoBitDepth', params['max_video_bit_depth']))  # noqa: E501
        if 'video_codec' in params:
            query_params.append(('VideoCodec', params['video_codec']))  # noqa: E501
        if 'audio_stream_index' in params:
            query_params.append(('AudioStreamIndex', params['audio_stream_index']))  # noqa: E501
        if 'video_stream_index' in params:
            query_params.append(('VideoStreamIndex', params['video_stream_index']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apikeyauth', 'embyauth']  # noqa: E501

        return self.api_client.call_api(
            '/Audio/{Id}/master.m3u8', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(self, segment_container, segment_id, id, playlist_id, **kwargs):  # noqa: E501
        """get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(segment_container, segment_id, id, playlist_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str segment_container: (required)
        :param str segment_id: (required)
        :param str id: (required)
        :param str playlist_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer_with_http_info(segment_container, segment_id, id, playlist_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer_with_http_info(segment_container, segment_id, id, playlist_id, **kwargs)  # noqa: E501
            return data

    def get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer_with_http_info(self, segment_container, segment_id, id, playlist_id, **kwargs):  # noqa: E501
        """get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer_with_http_info(segment_container, segment_id, id, playlist_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str segment_container: (required)
        :param str segment_id: (required)
        :param str id: (required)
        :param str playlist_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['segment_container', 'segment_id', 'id', 'playlist_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'segment_container' is set
        if ('segment_container' not in params or
                params['segment_container'] is None):
            raise ValueError("Missing the required parameter `segment_container` when calling `get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer`")  # noqa: E501
        # verify the required parameter 'segment_id' is set
        if ('segment_id' not in params or
                params['segment_id'] is None):
            raise ValueError("Missing the required parameter `segment_id` when calling `get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer`")  # noqa: E501
        # verify the required parameter 'playlist_id' is set
        if ('playlist_id' not in params or
                params['playlist_id'] is None):
            raise ValueError("Missing the required parameter `playlist_id` when calling `get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'segment_container' in params:
            path_params['SegmentContainer'] = params['segment_container']  # noqa: E501
        if 'segment_id' in params:
            path_params['SegmentId'] = params['segment_id']  # noqa: E501
        if 'id' in params:
            path_params['Id'] = params['id']  # noqa: E501
        if 'playlist_id' in params:
            path_params['PlaylistId'] = params['playlist_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apikeyauth', 'embyauth']  # noqa: E501

        return self.api_client.call_api(
            '/Videos/{Id}/hls1/{PlaylistId}/{SegmentId}.{SegmentContainer}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_videos_by_id_live_m3u8(self, id, container, **kwargs):  # noqa: E501
        """get_videos_by_id_live_m3u8  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_videos_by_id_live_m3u8(id, container, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Item Id (required)
        :param str container: Container (required)
        :param str device_profile_id: Optional. The dlna device profile id to utilize.
        :param str device_id: The device id of the client requesting. Used to stop encoding processes when needed.
        :param str audio_codec: Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
        :param bool enable_auto_stream_copy: Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
        :param int audio_sample_rate: Optional. Specify a specific audio sample rate, e.g. 44100
        :param int audio_bit_rate: Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
        :param int audio_channels: Optional. Specify a specific number of audio channels to encode to, e.g. 2
        :param int max_audio_channels: Optional. Specify a maximum number of audio channels to encode to, e.g. 2
        :param bool static: Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false
        :param bool copy_timestamps: Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
        :param int start_time_ticks: Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks.
        :param int width: Optional. The fixed horizontal resolution of the encoded video.
        :param int height: Optional. The fixed vertical resolution of the encoded video.
        :param int max_width: Optional. The maximum horizontal resolution of the encoded video.
        :param int max_height: Optional. The maximum vertical resolution of the encoded video.
        :param int video_bit_rate: Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
        :param int subtitle_stream_index: Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
        :param SubtitleDeliveryMethod subtitle_method: Optional. Specify the subtitle delivery method.
        :param int max_video_bit_depth: Optional.
        :param str video_codec: Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv.
        :param int audio_stream_index: Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
        :param int video_stream_index: Optional. The index of the video stream to use. If omitted the first video stream will be used.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_videos_by_id_live_m3u8_with_http_info(id, container, **kwargs)  # noqa: E501
        else:
            (data) = self.get_videos_by_id_live_m3u8_with_http_info(id, container, **kwargs)  # noqa: E501
            return data

    def get_videos_by_id_live_m3u8_with_http_info(self, id, container, **kwargs):  # noqa: E501
        """get_videos_by_id_live_m3u8  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_videos_by_id_live_m3u8_with_http_info(id, container, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Item Id (required)
        :param str container: Container (required)
        :param str device_profile_id: Optional. The dlna device profile id to utilize.
        :param str device_id: The device id of the client requesting. Used to stop encoding processes when needed.
        :param str audio_codec: Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
        :param bool enable_auto_stream_copy: Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
        :param int audio_sample_rate: Optional. Specify a specific audio sample rate, e.g. 44100
        :param int audio_bit_rate: Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
        :param int audio_channels: Optional. Specify a specific number of audio channels to encode to, e.g. 2
        :param int max_audio_channels: Optional. Specify a maximum number of audio channels to encode to, e.g. 2
        :param bool static: Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false
        :param bool copy_timestamps: Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
        :param int start_time_ticks: Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks.
        :param int width: Optional. The fixed horizontal resolution of the encoded video.
        :param int height: Optional. The fixed vertical resolution of the encoded video.
        :param int max_width: Optional. The maximum horizontal resolution of the encoded video.
        :param int max_height: Optional. The maximum vertical resolution of the encoded video.
        :param int video_bit_rate: Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
        :param int subtitle_stream_index: Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
        :param SubtitleDeliveryMethod subtitle_method: Optional. Specify the subtitle delivery method.
        :param int max_video_bit_depth: Optional.
        :param str video_codec: Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv.
        :param int audio_stream_index: Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
        :param int video_stream_index: Optional. The index of the video stream to use. If omitted the first video stream will be used.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'container', 'device_profile_id', 'device_id', 'audio_codec', 'enable_auto_stream_copy', 'audio_sample_rate', 'audio_bit_rate', 'audio_channels', 'max_audio_channels', 'static', 'copy_timestamps', 'start_time_ticks', 'width', 'height', 'max_width', 'max_height', 'video_bit_rate', 'subtitle_stream_index', 'subtitle_method', 'max_video_bit_depth', 'video_codec', 'audio_stream_index', 'video_stream_index']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_videos_by_id_live_m3u8" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_videos_by_id_live_m3u8`")  # noqa: E501
        # verify the required parameter 'container' is set
        if ('container' not in params or
                params['container'] is None):
            raise ValueError("Missing the required parameter `container` when calling `get_videos_by_id_live_m3u8`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['Id'] = params['id']  # noqa: E501

        query_params = []
        if 'device_profile_id' in params:
            query_params.append(('DeviceProfileId', params['device_profile_id']))  # noqa: E501
        if 'device_id' in params:
            query_params.append(('DeviceId', params['device_id']))  # noqa: E501
        if 'container' in params:
            query_params.append(('Container', params['container']))  # noqa: E501
        if 'audio_codec' in params:
            query_params.append(('AudioCodec', params['audio_codec']))  # noqa: E501
        if 'enable_auto_stream_copy' in params:
            query_params.append(('EnableAutoStreamCopy', params['enable_auto_stream_copy']))  # noqa: E501
        if 'audio_sample_rate' in params:
            query_params.append(('AudioSampleRate', params['audio_sample_rate']))  # noqa: E501
        if 'audio_bit_rate' in params:
            query_params.append(('AudioBitRate', params['audio_bit_rate']))  # noqa: E501
        if 'audio_channels' in params:
            query_params.append(('AudioChannels', params['audio_channels']))  # noqa: E501
        if 'max_audio_channels' in params:
            query_params.append(('MaxAudioChannels', params['max_audio_channels']))  # noqa: E501
        if 'static' in params:
            query_params.append(('Static', params['static']))  # noqa: E501
        if 'copy_timestamps' in params:
            query_params.append(('CopyTimestamps', params['copy_timestamps']))  # noqa: E501
        if 'start_time_ticks' in params:
            query_params.append(('StartTimeTicks', params['start_time_ticks']))  # noqa: E501
        if 'width' in params:
            query_params.append(('Width', params['width']))  # noqa: E501
        if 'height' in params:
            query_params.append(('Height', params['height']))  # noqa: E501
        if 'max_width' in params:
            query_params.append(('MaxWidth', params['max_width']))  # noqa: E501
        if 'max_height' in params:
            query_params.append(('MaxHeight', params['max_height']))  # noqa: E501
        if 'video_bit_rate' in params:
            query_params.append(('VideoBitRate', params['video_bit_rate']))  # noqa: E501
        if 'subtitle_stream_index' in params:
            query_params.append(('SubtitleStreamIndex', params['subtitle_stream_index']))  # noqa: E501
        if 'subtitle_method' in params:
            query_params.append(('SubtitleMethod', params['subtitle_method']))  # noqa: E501
        if 'max_video_bit_depth' in params:
            query_params.append(('MaxVideoBitDepth', params['max_video_bit_depth']))  # noqa: E501
        if 'video_codec' in params:
            query_params.append(('VideoCodec', params['video_codec']))  # noqa: E501
        if 'audio_stream_index' in params:
            query_params.append(('AudioStreamIndex', params['audio_stream_index']))  # noqa: E501
        if 'video_stream_index' in params:
            query_params.append(('VideoStreamIndex', params['video_stream_index']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apikeyauth', 'embyauth']  # noqa: E501

        return self.api_client.call_api(
            '/Videos/{Id}/live.m3u8', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_videos_by_id_live_subtitles_m3u8(self, id, subtitle_segment_length, manifest_subtitles, **kwargs):  # noqa: E501
        """Gets an HLS subtitle playlist.  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_videos_by_id_live_subtitles_m3u8(id, subtitle_segment_length, manifest_subtitles, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Item Id (required)
        :param int subtitle_segment_length: The subtitle segment length (required)
        :param str manifest_subtitles: The subtitle segment format (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_videos_by_id_live_subtitles_m3u8_with_http_info(id, subtitle_segment_length, manifest_subtitles, **kwargs)  # noqa: E501
        else:
            (data) = self.get_videos_by_id_live_subtitles_m3u8_with_http_info(id, subtitle_segment_length, manifest_subtitles, **kwargs)  # noqa: E501
            return data

    def get_videos_by_id_live_subtitles_m3u8_with_http_info(self, id, subtitle_segment_length, manifest_subtitles, **kwargs):  # noqa: E501
        """Gets an HLS subtitle playlist.  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_videos_by_id_live_subtitles_m3u8_with_http_info(id, subtitle_segment_length, manifest_subtitles, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Item Id (required)
        :param int subtitle_segment_length: The subtitle segment length (required)
        :param str manifest_subtitles: The subtitle segment format (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'subtitle_segment_length', 'manifest_subtitles']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_videos_by_id_live_subtitles_m3u8" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_videos_by_id_live_subtitles_m3u8`")  # noqa: E501
        # verify the required parameter 'subtitle_segment_length' is set
        if ('subtitle_segment_length' not in params or
                params['subtitle_segment_length'] is None):
            raise ValueError("Missing the required parameter `subtitle_segment_length` when calling `get_videos_by_id_live_subtitles_m3u8`")  # noqa: E501
        # verify the required parameter 'manifest_subtitles' is set
        if ('manifest_subtitles' not in params or
                params['manifest_subtitles'] is None):
            raise ValueError("Missing the required parameter `manifest_subtitles` when calling `get_videos_by_id_live_subtitles_m3u8`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['Id'] = params['id']  # noqa: E501

        query_params = []
        if 'subtitle_segment_length' in params:
            query_params.append(('SubtitleSegmentLength', params['subtitle_segment_length']))  # noqa: E501
        if 'manifest_subtitles' in params:
            query_params.append(('ManifestSubtitles', params['manifest_subtitles']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apikeyauth', 'embyauth']  # noqa: E501

        return self.api_client.call_api(
            '/Videos/{Id}/live_subtitles.m3u8', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_videos_by_id_main_m3u8(self, id, container, **kwargs):  # noqa: E501
        """Gets a video stream using HTTP live streaming.  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_videos_by_id_main_m3u8(id, container, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Item Id (required)
        :param str container: Container (required)
        :param str device_profile_id: Optional. The dlna device profile id to utilize.
        :param str device_id: The device id of the client requesting. Used to stop encoding processes when needed.
        :param str audio_codec: Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
        :param bool enable_auto_stream_copy: Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
        :param int audio_sample_rate: Optional. Specify a specific audio sample rate, e.g. 44100
        :param int audio_bit_rate: Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
        :param int audio_channels: Optional. Specify a specific number of audio channels to encode to, e.g. 2
        :param int max_audio_channels: Optional. Specify a maximum number of audio channels to encode to, e.g. 2
        :param bool static: Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false
        :param bool copy_timestamps: Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
        :param int start_time_ticks: Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks.
        :param int width: Optional. The fixed horizontal resolution of the encoded video.
        :param int height: Optional. The fixed vertical resolution of the encoded video.
        :param int max_width: Optional. The maximum horizontal resolution of the encoded video.
        :param int max_height: Optional. The maximum vertical resolution of the encoded video.
        :param int video_bit_rate: Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
        :param int subtitle_stream_index: Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
        :param SubtitleDeliveryMethod subtitle_method: Optional. Specify the subtitle delivery method.
        :param int max_video_bit_depth: Optional.
        :param str video_codec: Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv.
        :param int audio_stream_index: Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
        :param int video_stream_index: Optional. The index of the video stream to use. If omitted the first video stream will be used.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_videos_by_id_main_m3u8_with_http_info(id, container, **kwargs)  # noqa: E501
        else:
            (data) = self.get_videos_by_id_main_m3u8_with_http_info(id, container, **kwargs)  # noqa: E501
            return data

    def get_videos_by_id_main_m3u8_with_http_info(self, id, container, **kwargs):  # noqa: E501
        """Gets a video stream using HTTP live streaming.  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_videos_by_id_main_m3u8_with_http_info(id, container, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Item Id (required)
        :param str container: Container (required)
        :param str device_profile_id: Optional. The dlna device profile id to utilize.
        :param str device_id: The device id of the client requesting. Used to stop encoding processes when needed.
        :param str audio_codec: Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
        :param bool enable_auto_stream_copy: Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
        :param int audio_sample_rate: Optional. Specify a specific audio sample rate, e.g. 44100
        :param int audio_bit_rate: Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
        :param int audio_channels: Optional. Specify a specific number of audio channels to encode to, e.g. 2
        :param int max_audio_channels: Optional. Specify a maximum number of audio channels to encode to, e.g. 2
        :param bool static: Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false
        :param bool copy_timestamps: Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
        :param int start_time_ticks: Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks.
        :param int width: Optional. The fixed horizontal resolution of the encoded video.
        :param int height: Optional. The fixed vertical resolution of the encoded video.
        :param int max_width: Optional. The maximum horizontal resolution of the encoded video.
        :param int max_height: Optional. The maximum vertical resolution of the encoded video.
        :param int video_bit_rate: Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
        :param int subtitle_stream_index: Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
        :param SubtitleDeliveryMethod subtitle_method: Optional. Specify the subtitle delivery method.
        :param int max_video_bit_depth: Optional.
        :param str video_codec: Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv.
        :param int audio_stream_index: Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
        :param int video_stream_index: Optional. The index of the video stream to use. If omitted the first video stream will be used.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'container', 'device_profile_id', 'device_id', 'audio_codec', 'enable_auto_stream_copy', 'audio_sample_rate', 'audio_bit_rate', 'audio_channels', 'max_audio_channels', 'static', 'copy_timestamps', 'start_time_ticks', 'width', 'height', 'max_width', 'max_height', 'video_bit_rate', 'subtitle_stream_index', 'subtitle_method', 'max_video_bit_depth', 'video_codec', 'audio_stream_index', 'video_stream_index']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_videos_by_id_main_m3u8" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_videos_by_id_main_m3u8`")  # noqa: E501
        # verify the required parameter 'container' is set
        if ('container' not in params or
                params['container'] is None):
            raise ValueError("Missing the required parameter `container` when calling `get_videos_by_id_main_m3u8`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['Id'] = params['id']  # noqa: E501

        query_params = []
        if 'device_profile_id' in params:
            query_params.append(('DeviceProfileId', params['device_profile_id']))  # noqa: E501
        if 'device_id' in params:
            query_params.append(('DeviceId', params['device_id']))  # noqa: E501
        if 'container' in params:
            query_params.append(('Container', params['container']))  # noqa: E501
        if 'audio_codec' in params:
            query_params.append(('AudioCodec', params['audio_codec']))  # noqa: E501
        if 'enable_auto_stream_copy' in params:
            query_params.append(('EnableAutoStreamCopy', params['enable_auto_stream_copy']))  # noqa: E501
        if 'audio_sample_rate' in params:
            query_params.append(('AudioSampleRate', params['audio_sample_rate']))  # noqa: E501
        if 'audio_bit_rate' in params:
            query_params.append(('AudioBitRate', params['audio_bit_rate']))  # noqa: E501
        if 'audio_channels' in params:
            query_params.append(('AudioChannels', params['audio_channels']))  # noqa: E501
        if 'max_audio_channels' in params:
            query_params.append(('MaxAudioChannels', params['max_audio_channels']))  # noqa: E501
        if 'static' in params:
            query_params.append(('Static', params['static']))  # noqa: E501
        if 'copy_timestamps' in params:
            query_params.append(('CopyTimestamps', params['copy_timestamps']))  # noqa: E501
        if 'start_time_ticks' in params:
            query_params.append(('StartTimeTicks', params['start_time_ticks']))  # noqa: E501
        if 'width' in params:
            query_params.append(('Width', params['width']))  # noqa: E501
        if 'height' in params:
            query_params.append(('Height', params['height']))  # noqa: E501
        if 'max_width' in params:
            query_params.append(('MaxWidth', params['max_width']))  # noqa: E501
        if 'max_height' in params:
            query_params.append(('MaxHeight', params['max_height']))  # noqa: E501
        if 'video_bit_rate' in params:
            query_params.append(('VideoBitRate', params['video_bit_rate']))  # noqa: E501
        if 'subtitle_stream_index' in params:
            query_params.append(('SubtitleStreamIndex', params['subtitle_stream_index']))  # noqa: E501
        if 'subtitle_method' in params:
            query_params.append(('SubtitleMethod', params['subtitle_method']))  # noqa: E501
        if 'max_video_bit_depth' in params:
            query_params.append(('MaxVideoBitDepth', params['max_video_bit_depth']))  # noqa: E501
        if 'video_codec' in params:
            query_params.append(('VideoCodec', params['video_codec']))  # noqa: E501
        if 'audio_stream_index' in params:
            query_params.append(('AudioStreamIndex', params['audio_stream_index']))  # noqa: E501
        if 'video_stream_index' in params:
            query_params.append(('VideoStreamIndex', params['video_stream_index']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apikeyauth', 'embyauth']  # noqa: E501

        return self.api_client.call_api(
            '/Videos/{Id}/main.m3u8', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_videos_by_id_master_m3u8(self, id, container, **kwargs):  # noqa: E501
        """Gets a video stream using HTTP live streaming.  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_videos_by_id_master_m3u8(id, container, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Item Id (required)
        :param str container: Container (required)
        :param str device_profile_id: Optional. The dlna device profile id to utilize.
        :param str device_id: The device id of the client requesting. Used to stop encoding processes when needed.
        :param str audio_codec: Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
        :param bool enable_auto_stream_copy: Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
        :param int audio_sample_rate: Optional. Specify a specific audio sample rate, e.g. 44100
        :param int audio_bit_rate: Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
        :param int audio_channels: Optional. Specify a specific number of audio channels to encode to, e.g. 2
        :param int max_audio_channels: Optional. Specify a maximum number of audio channels to encode to, e.g. 2
        :param bool static: Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false
        :param bool copy_timestamps: Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
        :param int start_time_ticks: Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks.
        :param int width: Optional. The fixed horizontal resolution of the encoded video.
        :param int height: Optional. The fixed vertical resolution of the encoded video.
        :param int max_width: Optional. The maximum horizontal resolution of the encoded video.
        :param int max_height: Optional. The maximum vertical resolution of the encoded video.
        :param int video_bit_rate: Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
        :param int subtitle_stream_index: Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
        :param SubtitleDeliveryMethod subtitle_method: Optional. Specify the subtitle delivery method.
        :param int max_video_bit_depth: Optional.
        :param str video_codec: Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv.
        :param int audio_stream_index: Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
        :param int video_stream_index: Optional. The index of the video stream to use. If omitted the first video stream will be used.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_videos_by_id_master_m3u8_with_http_info(id, container, **kwargs)  # noqa: E501
        else:
            (data) = self.get_videos_by_id_master_m3u8_with_http_info(id, container, **kwargs)  # noqa: E501
            return data

    def get_videos_by_id_master_m3u8_with_http_info(self, id, container, **kwargs):  # noqa: E501
        """Gets a video stream using HTTP live streaming.  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_videos_by_id_master_m3u8_with_http_info(id, container, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Item Id (required)
        :param str container: Container (required)
        :param str device_profile_id: Optional. The dlna device profile id to utilize.
        :param str device_id: The device id of the client requesting. Used to stop encoding processes when needed.
        :param str audio_codec: Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
        :param bool enable_auto_stream_copy: Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
        :param int audio_sample_rate: Optional. Specify a specific audio sample rate, e.g. 44100
        :param int audio_bit_rate: Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
        :param int audio_channels: Optional. Specify a specific number of audio channels to encode to, e.g. 2
        :param int max_audio_channels: Optional. Specify a maximum number of audio channels to encode to, e.g. 2
        :param bool static: Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false
        :param bool copy_timestamps: Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
        :param int start_time_ticks: Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks.
        :param int width: Optional. The fixed horizontal resolution of the encoded video.
        :param int height: Optional. The fixed vertical resolution of the encoded video.
        :param int max_width: Optional. The maximum horizontal resolution of the encoded video.
        :param int max_height: Optional. The maximum vertical resolution of the encoded video.
        :param int video_bit_rate: Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
        :param int subtitle_stream_index: Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
        :param SubtitleDeliveryMethod subtitle_method: Optional. Specify the subtitle delivery method.
        :param int max_video_bit_depth: Optional.
        :param str video_codec: Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv.
        :param int audio_stream_index: Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
        :param int video_stream_index: Optional. The index of the video stream to use. If omitted the first video stream will be used.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'container', 'device_profile_id', 'device_id', 'audio_codec', 'enable_auto_stream_copy', 'audio_sample_rate', 'audio_bit_rate', 'audio_channels', 'max_audio_channels', 'static', 'copy_timestamps', 'start_time_ticks', 'width', 'height', 'max_width', 'max_height', 'video_bit_rate', 'subtitle_stream_index', 'subtitle_method', 'max_video_bit_depth', 'video_codec', 'audio_stream_index', 'video_stream_index']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_videos_by_id_master_m3u8" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_videos_by_id_master_m3u8`")  # noqa: E501
        # verify the required parameter 'container' is set
        if ('container' not in params or
                params['container'] is None):
            raise ValueError("Missing the required parameter `container` when calling `get_videos_by_id_master_m3u8`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['Id'] = params['id']  # noqa: E501

        query_params = []
        if 'device_profile_id' in params:
            query_params.append(('DeviceProfileId', params['device_profile_id']))  # noqa: E501
        if 'device_id' in params:
            query_params.append(('DeviceId', params['device_id']))  # noqa: E501
        if 'container' in params:
            query_params.append(('Container', params['container']))  # noqa: E501
        if 'audio_codec' in params:
            query_params.append(('AudioCodec', params['audio_codec']))  # noqa: E501
        if 'enable_auto_stream_copy' in params:
            query_params.append(('EnableAutoStreamCopy', params['enable_auto_stream_copy']))  # noqa: E501
        if 'audio_sample_rate' in params:
            query_params.append(('AudioSampleRate', params['audio_sample_rate']))  # noqa: E501
        if 'audio_bit_rate' in params:
            query_params.append(('AudioBitRate', params['audio_bit_rate']))  # noqa: E501
        if 'audio_channels' in params:
            query_params.append(('AudioChannels', params['audio_channels']))  # noqa: E501
        if 'max_audio_channels' in params:
            query_params.append(('MaxAudioChannels', params['max_audio_channels']))  # noqa: E501
        if 'static' in params:
            query_params.append(('Static', params['static']))  # noqa: E501
        if 'copy_timestamps' in params:
            query_params.append(('CopyTimestamps', params['copy_timestamps']))  # noqa: E501
        if 'start_time_ticks' in params:
            query_params.append(('StartTimeTicks', params['start_time_ticks']))  # noqa: E501
        if 'width' in params:
            query_params.append(('Width', params['width']))  # noqa: E501
        if 'height' in params:
            query_params.append(('Height', params['height']))  # noqa: E501
        if 'max_width' in params:
            query_params.append(('MaxWidth', params['max_width']))  # noqa: E501
        if 'max_height' in params:
            query_params.append(('MaxHeight', params['max_height']))  # noqa: E501
        if 'video_bit_rate' in params:
            query_params.append(('VideoBitRate', params['video_bit_rate']))  # noqa: E501
        if 'subtitle_stream_index' in params:
            query_params.append(('SubtitleStreamIndex', params['subtitle_stream_index']))  # noqa: E501
        if 'subtitle_method' in params:
            query_params.append(('SubtitleMethod', params['subtitle_method']))  # noqa: E501
        if 'max_video_bit_depth' in params:
            query_params.append(('MaxVideoBitDepth', params['max_video_bit_depth']))  # noqa: E501
        if 'video_codec' in params:
            query_params.append(('VideoCodec', params['video_codec']))  # noqa: E501
        if 'audio_stream_index' in params:
            query_params.append(('AudioStreamIndex', params['audio_stream_index']))  # noqa: E501
        if 'video_stream_index' in params:
            query_params.append(('VideoStreamIndex', params['video_stream_index']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apikeyauth', 'embyauth']  # noqa: E501

        return self.api_client.call_api(
            '/Videos/{Id}/master.m3u8', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_videos_by_id_subtitles_m3u8(self, id, subtitle_segment_length, manifest_subtitles, **kwargs):  # noqa: E501
        """Gets an HLS subtitle playlist.  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_videos_by_id_subtitles_m3u8(id, subtitle_segment_length, manifest_subtitles, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Item Id (required)
        :param int subtitle_segment_length: The subtitle segment length (required)
        :param str manifest_subtitles: The subtitle segment format (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_videos_by_id_subtitles_m3u8_with_http_info(id, subtitle_segment_length, manifest_subtitles, **kwargs)  # noqa: E501
        else:
            (data) = self.get_videos_by_id_subtitles_m3u8_with_http_info(id, subtitle_segment_length, manifest_subtitles, **kwargs)  # noqa: E501
            return data

    def get_videos_by_id_subtitles_m3u8_with_http_info(self, id, subtitle_segment_length, manifest_subtitles, **kwargs):  # noqa: E501
        """Gets an HLS subtitle playlist.  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_videos_by_id_subtitles_m3u8_with_http_info(id, subtitle_segment_length, manifest_subtitles, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Item Id (required)
        :param int subtitle_segment_length: The subtitle segment length (required)
        :param str manifest_subtitles: The subtitle segment format (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'subtitle_segment_length', 'manifest_subtitles']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_videos_by_id_subtitles_m3u8" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_videos_by_id_subtitles_m3u8`")  # noqa: E501
        # verify the required parameter 'subtitle_segment_length' is set
        if ('subtitle_segment_length' not in params or
                params['subtitle_segment_length'] is None):
            raise ValueError("Missing the required parameter `subtitle_segment_length` when calling `get_videos_by_id_subtitles_m3u8`")  # noqa: E501
        # verify the required parameter 'manifest_subtitles' is set
        if ('manifest_subtitles' not in params or
                params['manifest_subtitles'] is None):
            raise ValueError("Missing the required parameter `manifest_subtitles` when calling `get_videos_by_id_subtitles_m3u8`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['Id'] = params['id']  # noqa: E501

        query_params = []
        if 'subtitle_segment_length' in params:
            query_params.append(('SubtitleSegmentLength', params['subtitle_segment_length']))  # noqa: E501
        if 'manifest_subtitles' in params:
            query_params.append(('ManifestSubtitles', params['manifest_subtitles']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apikeyauth', 'embyauth']  # noqa: E501

        return self.api_client.call_api(
            '/Videos/{Id}/subtitles.m3u8', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(self, segment_container, segment_id, id, playlist_id, **kwargs):  # noqa: E501
        """head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(segment_container, segment_id, id, playlist_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str segment_container: (required)
        :param str segment_id: (required)
        :param str id: (required)
        :param str playlist_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer_with_http_info(segment_container, segment_id, id, playlist_id, **kwargs)  # noqa: E501
        else:
            (data) = self.head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer_with_http_info(segment_container, segment_id, id, playlist_id, **kwargs)  # noqa: E501
            return data

    def head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer_with_http_info(self, segment_container, segment_id, id, playlist_id, **kwargs):  # noqa: E501
        """head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer_with_http_info(segment_container, segment_id, id, playlist_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str segment_container: (required)
        :param str segment_id: (required)
        :param str id: (required)
        :param str playlist_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['segment_container', 'segment_id', 'id', 'playlist_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'segment_container' is set
        if ('segment_container' not in params or
                params['segment_container'] is None):
            raise ValueError("Missing the required parameter `segment_container` when calling `head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer`")  # noqa: E501
        # verify the required parameter 'segment_id' is set
        if ('segment_id' not in params or
                params['segment_id'] is None):
            raise ValueError("Missing the required parameter `segment_id` when calling `head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer`")  # noqa: E501
        # verify the required parameter 'playlist_id' is set
        if ('playlist_id' not in params or
                params['playlist_id'] is None):
            raise ValueError("Missing the required parameter `playlist_id` when calling `head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'segment_container' in params:
            path_params['SegmentContainer'] = params['segment_container']  # noqa: E501
        if 'segment_id' in params:
            path_params['SegmentId'] = params['segment_id']  # noqa: E501
        if 'id' in params:
            path_params['Id'] = params['id']  # noqa: E501
        if 'playlist_id' in params:
            path_params['PlaylistId'] = params['playlist_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apikeyauth', 'embyauth']  # noqa: E501

        return self.api_client.call_api(
            '/Audio/{Id}/hls1/{PlaylistId}/{SegmentId}.{SegmentContainer}', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_audio_by_id_master_m3u8(self, id, container, **kwargs):  # noqa: E501
        """Gets an audio stream using HTTP live streaming.  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_audio_by_id_master_m3u8(id, container, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Item Id (required)
        :param str container: Container (required)
        :param str device_profile_id: Optional. The dlna device profile id to utilize.
        :param str device_id: The device id of the client requesting. Used to stop encoding processes when needed.
        :param str audio_codec: Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
        :param bool enable_auto_stream_copy: Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
        :param int audio_sample_rate: Optional. Specify a specific audio sample rate, e.g. 44100
        :param int audio_bit_rate: Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
        :param int audio_channels: Optional. Specify a specific number of audio channels to encode to, e.g. 2
        :param int max_audio_channels: Optional. Specify a maximum number of audio channels to encode to, e.g. 2
        :param bool static: Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false
        :param bool copy_timestamps: Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
        :param int start_time_ticks: Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks.
        :param int width: Optional. The fixed horizontal resolution of the encoded video.
        :param int height: Optional. The fixed vertical resolution of the encoded video.
        :param int max_width: Optional. The maximum horizontal resolution of the encoded video.
        :param int max_height: Optional. The maximum vertical resolution of the encoded video.
        :param int video_bit_rate: Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
        :param int subtitle_stream_index: Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
        :param SubtitleDeliveryMethod subtitle_method: Optional. Specify the subtitle delivery method.
        :param int max_video_bit_depth: Optional.
        :param str video_codec: Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv.
        :param int audio_stream_index: Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
        :param int video_stream_index: Optional. The index of the video stream to use. If omitted the first video stream will be used.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_audio_by_id_master_m3u8_with_http_info(id, container, **kwargs)  # noqa: E501
        else:
            (data) = self.head_audio_by_id_master_m3u8_with_http_info(id, container, **kwargs)  # noqa: E501
            return data

    def head_audio_by_id_master_m3u8_with_http_info(self, id, container, **kwargs):  # noqa: E501
        """Gets an audio stream using HTTP live streaming.  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_audio_by_id_master_m3u8_with_http_info(id, container, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Item Id (required)
        :param str container: Container (required)
        :param str device_profile_id: Optional. The dlna device profile id to utilize.
        :param str device_id: The device id of the client requesting. Used to stop encoding processes when needed.
        :param str audio_codec: Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
        :param bool enable_auto_stream_copy: Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
        :param int audio_sample_rate: Optional. Specify a specific audio sample rate, e.g. 44100
        :param int audio_bit_rate: Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
        :param int audio_channels: Optional. Specify a specific number of audio channels to encode to, e.g. 2
        :param int max_audio_channels: Optional. Specify a maximum number of audio channels to encode to, e.g. 2
        :param bool static: Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false
        :param bool copy_timestamps: Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
        :param int start_time_ticks: Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks.
        :param int width: Optional. The fixed horizontal resolution of the encoded video.
        :param int height: Optional. The fixed vertical resolution of the encoded video.
        :param int max_width: Optional. The maximum horizontal resolution of the encoded video.
        :param int max_height: Optional. The maximum vertical resolution of the encoded video.
        :param int video_bit_rate: Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
        :param int subtitle_stream_index: Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
        :param SubtitleDeliveryMethod subtitle_method: Optional. Specify the subtitle delivery method.
        :param int max_video_bit_depth: Optional.
        :param str video_codec: Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv.
        :param int audio_stream_index: Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
        :param int video_stream_index: Optional. The index of the video stream to use. If omitted the first video stream will be used.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'container', 'device_profile_id', 'device_id', 'audio_codec', 'enable_auto_stream_copy', 'audio_sample_rate', 'audio_bit_rate', 'audio_channels', 'max_audio_channels', 'static', 'copy_timestamps', 'start_time_ticks', 'width', 'height', 'max_width', 'max_height', 'video_bit_rate', 'subtitle_stream_index', 'subtitle_method', 'max_video_bit_depth', 'video_codec', 'audio_stream_index', 'video_stream_index']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_audio_by_id_master_m3u8" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `head_audio_by_id_master_m3u8`")  # noqa: E501
        # verify the required parameter 'container' is set
        if ('container' not in params or
                params['container'] is None):
            raise ValueError("Missing the required parameter `container` when calling `head_audio_by_id_master_m3u8`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['Id'] = params['id']  # noqa: E501

        query_params = []
        if 'device_profile_id' in params:
            query_params.append(('DeviceProfileId', params['device_profile_id']))  # noqa: E501
        if 'device_id' in params:
            query_params.append(('DeviceId', params['device_id']))  # noqa: E501
        if 'container' in params:
            query_params.append(('Container', params['container']))  # noqa: E501
        if 'audio_codec' in params:
            query_params.append(('AudioCodec', params['audio_codec']))  # noqa: E501
        if 'enable_auto_stream_copy' in params:
            query_params.append(('EnableAutoStreamCopy', params['enable_auto_stream_copy']))  # noqa: E501
        if 'audio_sample_rate' in params:
            query_params.append(('AudioSampleRate', params['audio_sample_rate']))  # noqa: E501
        if 'audio_bit_rate' in params:
            query_params.append(('AudioBitRate', params['audio_bit_rate']))  # noqa: E501
        if 'audio_channels' in params:
            query_params.append(('AudioChannels', params['audio_channels']))  # noqa: E501
        if 'max_audio_channels' in params:
            query_params.append(('MaxAudioChannels', params['max_audio_channels']))  # noqa: E501
        if 'static' in params:
            query_params.append(('Static', params['static']))  # noqa: E501
        if 'copy_timestamps' in params:
            query_params.append(('CopyTimestamps', params['copy_timestamps']))  # noqa: E501
        if 'start_time_ticks' in params:
            query_params.append(('StartTimeTicks', params['start_time_ticks']))  # noqa: E501
        if 'width' in params:
            query_params.append(('Width', params['width']))  # noqa: E501
        if 'height' in params:
            query_params.append(('Height', params['height']))  # noqa: E501
        if 'max_width' in params:
            query_params.append(('MaxWidth', params['max_width']))  # noqa: E501
        if 'max_height' in params:
            query_params.append(('MaxHeight', params['max_height']))  # noqa: E501
        if 'video_bit_rate' in params:
            query_params.append(('VideoBitRate', params['video_bit_rate']))  # noqa: E501
        if 'subtitle_stream_index' in params:
            query_params.append(('SubtitleStreamIndex', params['subtitle_stream_index']))  # noqa: E501
        if 'subtitle_method' in params:
            query_params.append(('SubtitleMethod', params['subtitle_method']))  # noqa: E501
        if 'max_video_bit_depth' in params:
            query_params.append(('MaxVideoBitDepth', params['max_video_bit_depth']))  # noqa: E501
        if 'video_codec' in params:
            query_params.append(('VideoCodec', params['video_codec']))  # noqa: E501
        if 'audio_stream_index' in params:
            query_params.append(('AudioStreamIndex', params['audio_stream_index']))  # noqa: E501
        if 'video_stream_index' in params:
            query_params.append(('VideoStreamIndex', params['video_stream_index']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apikeyauth', 'embyauth']  # noqa: E501

        return self.api_client.call_api(
            '/Audio/{Id}/master.m3u8', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(self, segment_container, segment_id, id, playlist_id, **kwargs):  # noqa: E501
        """head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(segment_container, segment_id, id, playlist_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str segment_container: (required)
        :param str segment_id: (required)
        :param str id: (required)
        :param str playlist_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer_with_http_info(segment_container, segment_id, id, playlist_id, **kwargs)  # noqa: E501
        else:
            (data) = self.head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer_with_http_info(segment_container, segment_id, id, playlist_id, **kwargs)  # noqa: E501
            return data

    def head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer_with_http_info(self, segment_container, segment_id, id, playlist_id, **kwargs):  # noqa: E501
        """head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer_with_http_info(segment_container, segment_id, id, playlist_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str segment_container: (required)
        :param str segment_id: (required)
        :param str id: (required)
        :param str playlist_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['segment_container', 'segment_id', 'id', 'playlist_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'segment_container' is set
        if ('segment_container' not in params or
                params['segment_container'] is None):
            raise ValueError("Missing the required parameter `segment_container` when calling `head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer`")  # noqa: E501
        # verify the required parameter 'segment_id' is set
        if ('segment_id' not in params or
                params['segment_id'] is None):
            raise ValueError("Missing the required parameter `segment_id` when calling `head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer`")  # noqa: E501
        # verify the required parameter 'playlist_id' is set
        if ('playlist_id' not in params or
                params['playlist_id'] is None):
            raise ValueError("Missing the required parameter `playlist_id` when calling `head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'segment_container' in params:
            path_params['SegmentContainer'] = params['segment_container']  # noqa: E501
        if 'segment_id' in params:
            path_params['SegmentId'] = params['segment_id']  # noqa: E501
        if 'id' in params:
            path_params['Id'] = params['id']  # noqa: E501
        if 'playlist_id' in params:
            path_params['PlaylistId'] = params['playlist_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apikeyauth', 'embyauth']  # noqa: E501

        return self.api_client.call_api(
            '/Videos/{Id}/hls1/{PlaylistId}/{SegmentId}.{SegmentContainer}', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_videos_by_id_master_m3u8(self, id, container, **kwargs):  # noqa: E501
        """Gets a video stream using HTTP live streaming.  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_videos_by_id_master_m3u8(id, container, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Item Id (required)
        :param str container: Container (required)
        :param str device_profile_id: Optional. The dlna device profile id to utilize.
        :param str device_id: The device id of the client requesting. Used to stop encoding processes when needed.
        :param str audio_codec: Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
        :param bool enable_auto_stream_copy: Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
        :param int audio_sample_rate: Optional. Specify a specific audio sample rate, e.g. 44100
        :param int audio_bit_rate: Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
        :param int audio_channels: Optional. Specify a specific number of audio channels to encode to, e.g. 2
        :param int max_audio_channels: Optional. Specify a maximum number of audio channels to encode to, e.g. 2
        :param bool static: Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false
        :param bool copy_timestamps: Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
        :param int start_time_ticks: Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks.
        :param int width: Optional. The fixed horizontal resolution of the encoded video.
        :param int height: Optional. The fixed vertical resolution of the encoded video.
        :param int max_width: Optional. The maximum horizontal resolution of the encoded video.
        :param int max_height: Optional. The maximum vertical resolution of the encoded video.
        :param int video_bit_rate: Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
        :param int subtitle_stream_index: Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
        :param SubtitleDeliveryMethod subtitle_method: Optional. Specify the subtitle delivery method.
        :param int max_video_bit_depth: Optional.
        :param str video_codec: Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv.
        :param int audio_stream_index: Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
        :param int video_stream_index: Optional. The index of the video stream to use. If omitted the first video stream will be used.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_videos_by_id_master_m3u8_with_http_info(id, container, **kwargs)  # noqa: E501
        else:
            (data) = self.head_videos_by_id_master_m3u8_with_http_info(id, container, **kwargs)  # noqa: E501
            return data

    def head_videos_by_id_master_m3u8_with_http_info(self, id, container, **kwargs):  # noqa: E501
        """Gets a video stream using HTTP live streaming.  # noqa: E501

        Requires authentication as user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_videos_by_id_master_m3u8_with_http_info(id, container, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Item Id (required)
        :param str container: Container (required)
        :param str device_profile_id: Optional. The dlna device profile id to utilize.
        :param str device_id: The device id of the client requesting. Used to stop encoding processes when needed.
        :param str audio_codec: Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
        :param bool enable_auto_stream_copy: Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
        :param int audio_sample_rate: Optional. Specify a specific audio sample rate, e.g. 44100
        :param int audio_bit_rate: Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
        :param int audio_channels: Optional. Specify a specific number of audio channels to encode to, e.g. 2
        :param int max_audio_channels: Optional. Specify a maximum number of audio channels to encode to, e.g. 2
        :param bool static: Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false
        :param bool copy_timestamps: Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
        :param int start_time_ticks: Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks.
        :param int width: Optional. The fixed horizontal resolution of the encoded video.
        :param int height: Optional. The fixed vertical resolution of the encoded video.
        :param int max_width: Optional. The maximum horizontal resolution of the encoded video.
        :param int max_height: Optional. The maximum vertical resolution of the encoded video.
        :param int video_bit_rate: Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
        :param int subtitle_stream_index: Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
        :param SubtitleDeliveryMethod subtitle_method: Optional. Specify the subtitle delivery method.
        :param int max_video_bit_depth: Optional.
        :param str video_codec: Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv.
        :param int audio_stream_index: Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
        :param int video_stream_index: Optional. The index of the video stream to use. If omitted the first video stream will be used.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'container', 'device_profile_id', 'device_id', 'audio_codec', 'enable_auto_stream_copy', 'audio_sample_rate', 'audio_bit_rate', 'audio_channels', 'max_audio_channels', 'static', 'copy_timestamps', 'start_time_ticks', 'width', 'height', 'max_width', 'max_height', 'video_bit_rate', 'subtitle_stream_index', 'subtitle_method', 'max_video_bit_depth', 'video_codec', 'audio_stream_index', 'video_stream_index']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_videos_by_id_master_m3u8" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `head_videos_by_id_master_m3u8`")  # noqa: E501
        # verify the required parameter 'container' is set
        if ('container' not in params or
                params['container'] is None):
            raise ValueError("Missing the required parameter `container` when calling `head_videos_by_id_master_m3u8`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['Id'] = params['id']  # noqa: E501

        query_params = []
        if 'device_profile_id' in params:
            query_params.append(('DeviceProfileId', params['device_profile_id']))  # noqa: E501
        if 'device_id' in params:
            query_params.append(('DeviceId', params['device_id']))  # noqa: E501
        if 'container' in params:
            query_params.append(('Container', params['container']))  # noqa: E501
        if 'audio_codec' in params:
            query_params.append(('AudioCodec', params['audio_codec']))  # noqa: E501
        if 'enable_auto_stream_copy' in params:
            query_params.append(('EnableAutoStreamCopy', params['enable_auto_stream_copy']))  # noqa: E501
        if 'audio_sample_rate' in params:
            query_params.append(('AudioSampleRate', params['audio_sample_rate']))  # noqa: E501
        if 'audio_bit_rate' in params:
            query_params.append(('AudioBitRate', params['audio_bit_rate']))  # noqa: E501
        if 'audio_channels' in params:
            query_params.append(('AudioChannels', params['audio_channels']))  # noqa: E501
        if 'max_audio_channels' in params:
            query_params.append(('MaxAudioChannels', params['max_audio_channels']))  # noqa: E501
        if 'static' in params:
            query_params.append(('Static', params['static']))  # noqa: E501
        if 'copy_timestamps' in params:
            query_params.append(('CopyTimestamps', params['copy_timestamps']))  # noqa: E501
        if 'start_time_ticks' in params:
            query_params.append(('StartTimeTicks', params['start_time_ticks']))  # noqa: E501
        if 'width' in params:
            query_params.append(('Width', params['width']))  # noqa: E501
        if 'height' in params:
            query_params.append(('Height', params['height']))  # noqa: E501
        if 'max_width' in params:
            query_params.append(('MaxWidth', params['max_width']))  # noqa: E501
        if 'max_height' in params:
            query_params.append(('MaxHeight', params['max_height']))  # noqa: E501
        if 'video_bit_rate' in params:
            query_params.append(('VideoBitRate', params['video_bit_rate']))  # noqa: E501
        if 'subtitle_stream_index' in params:
            query_params.append(('SubtitleStreamIndex', params['subtitle_stream_index']))  # noqa: E501
        if 'subtitle_method' in params:
            query_params.append(('SubtitleMethod', params['subtitle_method']))  # noqa: E501
        if 'max_video_bit_depth' in params:
            query_params.append(('MaxVideoBitDepth', params['max_video_bit_depth']))  # noqa: E501
        if 'video_codec' in params:
            query_params.append(('VideoCodec', params['video_codec']))  # noqa: E501
        if 'audio_stream_index' in params:
            query_params.append(('AudioStreamIndex', params['audio_stream_index']))  # noqa: E501
        if 'video_stream_index' in params:
            query_params.append(('VideoStreamIndex', params['video_stream_index']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apikeyauth', 'embyauth']  # noqa: E501

        return self.api_client.call_api(
            '/Videos/{Id}/master.m3u8', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
