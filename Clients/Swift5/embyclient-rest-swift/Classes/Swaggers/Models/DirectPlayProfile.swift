//
// DirectPlayProfile.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct DirectPlayProfile: Codable {

    public var container: String?
    public var audioCodec: String?
    public var videoCodec: String?
    public var type: DlnaProfileType?

    public init(container: String? = nil, audioCodec: String? = nil, videoCodec: String? = nil, type: DlnaProfileType? = nil) {
        self.container = container
        self.audioCodec = audioCodec
        self.videoCodec = videoCodec
        self.type = type
    }

    public enum CodingKeys: String, CodingKey { 
        case container = "Container"
        case audioCodec = "AudioCodec"
        case videoCodec = "VideoCodec"
        case type = "Type"
    }

}
