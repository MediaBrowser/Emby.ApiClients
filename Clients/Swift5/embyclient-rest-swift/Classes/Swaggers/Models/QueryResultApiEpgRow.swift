//
// QueryResultApiEpgRow.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct QueryResultApiEpgRow: Codable {

    public var items: [ApiEpgRow]?
    public var totalRecordCount: Int?

    public init(items: [ApiEpgRow]? = nil, totalRecordCount: Int? = nil) {
        self.items = items
        self.totalRecordCount = totalRecordCount
    }

    public enum CodingKeys: String, CodingKey { 
        case items = "Items"
        case totalRecordCount = "TotalRecordCount"
    }

}
