//
// UserLibraryOfficialRatingItem.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct UserLibraryOfficialRatingItem: Codable {

    public var name: String?

    public init(name: String? = nil) {
        self.name = name
    }

    public enum CodingKeys: String, CodingKey { 
        case name = "Name"
    }

}
