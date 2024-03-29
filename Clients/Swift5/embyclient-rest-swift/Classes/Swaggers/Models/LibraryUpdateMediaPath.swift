//
// LibraryUpdateMediaPath.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct LibraryUpdateMediaPath: Codable {

    public var _id: String?
    public var pathInfo: MediaPathInfo?

    public init(_id: String? = nil, pathInfo: MediaPathInfo? = nil) {
        self._id = _id
        self.pathInfo = pathInfo
    }

    public enum CodingKeys: String, CodingKey { 
        case _id = "Id"
        case pathInfo = "PathInfo"
    }

}
