//
// SubtitleProfile.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct SubtitleProfile: Codable {

    public var format: String?
    public var method: SubtitleDeliveryMethod?
    public var didlMode: String?
    public var language: String?
    public var container: String?
    public var _protocol: String?

    public init(format: String? = nil, method: SubtitleDeliveryMethod? = nil, didlMode: String? = nil, language: String? = nil, container: String? = nil, _protocol: String? = nil) {
        self.format = format
        self.method = method
        self.didlMode = didlMode
        self.language = language
        self.container = container
        self._protocol = _protocol
    }

    public enum CodingKeys: String, CodingKey { 
        case format = "Format"
        case method = "Method"
        case didlMode = "DidlMode"
        case language = "Language"
        case container = "Container"
        case _protocol = "Protocol"
    }

}
