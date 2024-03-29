//
// CodecConfiguration.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct CodecConfiguration: Codable {

    /** A value indicating whether the codec is enabled. */
    public var isEnabled: Bool?
    /** The selection priority for the codec.    Higher values mean higher priority. */
    public var priority: Int?
    /** The codec identifier. */
    public var codecId: String?

    public init(isEnabled: Bool? = nil, priority: Int? = nil, codecId: String? = nil) {
        self.isEnabled = isEnabled
        self.priority = priority
        self.codecId = codecId
    }

    public enum CodingKeys: String, CodingKey { 
        case isEnabled = "IsEnabled"
        case priority = "Priority"
        case codecId = "CodecId"
    }

}
