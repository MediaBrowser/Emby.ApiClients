//
// UserLibraryLeaveSharedItems.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct UserLibraryLeaveSharedItems: Codable {

    public var itemIds: [String]?
    public var userId: String?

    public init(itemIds: [String]? = nil, userId: String? = nil) {
        self.itemIds = itemIds
        self.userId = userId
    }

    public enum CodingKeys: String, CodingKey { 
        case itemIds = "ItemIds"
        case userId = "UserId"
    }

}