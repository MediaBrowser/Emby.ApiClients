//
// PlaybackInfoResponse.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct PlaybackInfoResponse: Codable {

    /** The media sources. */
    public var mediaSources: [MediaSourceInfo]?
    /** The play session identifier. */
    public var playSessionId: String?
    public var errorCode: PlaybackErrorCode?

    public init(mediaSources: [MediaSourceInfo]? = nil, playSessionId: String? = nil, errorCode: PlaybackErrorCode? = nil) {
        self.mediaSources = mediaSources
        self.playSessionId = playSessionId
        self.errorCode = errorCode
    }

    public enum CodingKeys: String, CodingKey { 
        case mediaSources = "MediaSources"
        case playSessionId = "PlaySessionId"
        case errorCode = "ErrorCode"
    }

}
