//
// ProgressEvent.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation


public enum ProgressEvent: String, Codable {
    case timeUpdate = "TimeUpdate"
    case pause = "Pause"
    case unpause = "Unpause"
    case volumeChange = "VolumeChange"
    case repeatModeChange = "RepeatModeChange"
    case audioTrackChange = "AudioTrackChange"
    case subtitleTrackChange = "SubtitleTrackChange"
    case playlistItemMove = "PlaylistItemMove"
    case playlistItemRemove = "PlaylistItemRemove"
    case playlistItemAdd = "PlaylistItemAdd"
    case qualityChange = "QualityChange"
    case stateChange = "StateChange"
    case subtitleOffsetChange = "SubtitleOffsetChange"
    case playbackRateChange = "PlaybackRateChange"
    case shuffleChange = "ShuffleChange"
}