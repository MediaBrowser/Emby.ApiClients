//
// UserLibraryUpdateUserItemAccess.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct UserLibraryUpdateUserItemAccess: Codable {

    public var itemIds: [String]?
    public var userIds: [String]?
    public var itemAccess: UserItemShareLevel?

    public init(itemIds: [String]? = nil, userIds: [String]? = nil, itemAccess: UserItemShareLevel? = nil) {
        self.itemIds = itemIds
        self.userIds = userIds
        self.itemAccess = itemAccess
    }

    public enum CodingKeys: String, CodingKey { 
        case itemIds = "ItemIds"
        case userIds = "UserIds"
        case itemAccess = "ItemAccess"
    }

}
