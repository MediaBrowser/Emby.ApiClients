//
// PlaybackInfoRequest.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct PlaybackInfoRequest: Codable {

    public var _id: String?
    public var userId: String?
    public var maxStreamingBitrate: Int64?
    public var startTimeTicks: Int64?
    public var audioStreamIndex: Int?
    public var subtitleStreamIndex: Int?
    public var maxAudioChannels: Int?
    public var mediaSourceId: String?
    public var liveStreamId: String?
    public var deviceProfile: DeviceProfile?
    public var enableDirectPlay: Bool?
    public var enableDirectStream: Bool?
    public var enableTranscoding: Bool?
    public var allowInterlacedVideoStreamCopy: Bool?
    public var allowVideoStreamCopy: Bool?
    public var allowAudioStreamCopy: Bool?
    public var isPlayback: Bool?
    public var autoOpenLiveStream: Bool?
    public var currentPlaySessionId: String?

    public init(_id: String? = nil, userId: String? = nil, maxStreamingBitrate: Int64? = nil, startTimeTicks: Int64? = nil, audioStreamIndex: Int? = nil, subtitleStreamIndex: Int? = nil, maxAudioChannels: Int? = nil, mediaSourceId: String? = nil, liveStreamId: String? = nil, deviceProfile: DeviceProfile? = nil, enableDirectPlay: Bool? = nil, enableDirectStream: Bool? = nil, enableTranscoding: Bool? = nil, allowInterlacedVideoStreamCopy: Bool? = nil, allowVideoStreamCopy: Bool? = nil, allowAudioStreamCopy: Bool? = nil, isPlayback: Bool? = nil, autoOpenLiveStream: Bool? = nil, currentPlaySessionId: String? = nil) {
        self._id = _id
        self.userId = userId
        self.maxStreamingBitrate = maxStreamingBitrate
        self.startTimeTicks = startTimeTicks
        self.audioStreamIndex = audioStreamIndex
        self.subtitleStreamIndex = subtitleStreamIndex
        self.maxAudioChannels = maxAudioChannels
        self.mediaSourceId = mediaSourceId
        self.liveStreamId = liveStreamId
        self.deviceProfile = deviceProfile
        self.enableDirectPlay = enableDirectPlay
        self.enableDirectStream = enableDirectStream
        self.enableTranscoding = enableTranscoding
        self.allowInterlacedVideoStreamCopy = allowInterlacedVideoStreamCopy
        self.allowVideoStreamCopy = allowVideoStreamCopy
        self.allowAudioStreamCopy = allowAudioStreamCopy
        self.isPlayback = isPlayback
        self.autoOpenLiveStream = autoOpenLiveStream
        self.currentPlaySessionId = currentPlaySessionId
    }

    public enum CodingKeys: String, CodingKey { 
        case _id = "Id"
        case userId = "UserId"
        case maxStreamingBitrate = "MaxStreamingBitrate"
        case startTimeTicks = "StartTimeTicks"
        case audioStreamIndex = "AudioStreamIndex"
        case subtitleStreamIndex = "SubtitleStreamIndex"
        case maxAudioChannels = "MaxAudioChannels"
        case mediaSourceId = "MediaSourceId"
        case liveStreamId = "LiveStreamId"
        case deviceProfile = "DeviceProfile"
        case enableDirectPlay = "EnableDirectPlay"
        case enableDirectStream = "EnableDirectStream"
        case enableTranscoding = "EnableTranscoding"
        case allowInterlacedVideoStreamCopy = "AllowInterlacedVideoStreamCopy"
        case allowVideoStreamCopy = "AllowVideoStreamCopy"
        case allowAudioStreamCopy = "AllowAudioStreamCopy"
        case isPlayback = "IsPlayback"
        case autoOpenLiveStream = "AutoOpenLiveStream"
        case currentPlaySessionId = "CurrentPlaySessionId"
    }

}