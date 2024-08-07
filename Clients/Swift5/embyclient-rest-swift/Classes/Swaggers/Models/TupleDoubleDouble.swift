//
// TupleDoubleDouble.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct TupleDoubleDouble: Codable {

    public var item1: Double?
    public var item2: Double?

    public init(item1: Double? = nil, item2: Double? = nil) {
        self.item1 = item1
        self.item2 = item2
    }

    public enum CodingKeys: String, CodingKey { 
        case item1 = "Item1"
        case item2 = "Item2"
    }

}
