//
// ChapterInfo.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation


/** Class ChapterInfo   */

public struct ChapterInfo: Codable {

    /** The start position ticks. */
    public var startPositionTicks: Int64?
    /** The name. */
    public var name: String?
    public var imageTag: String?
    public var markerType: MarkerType?
    public var chapterIndex: Int?

    public init(startPositionTicks: Int64? = nil, name: String? = nil, imageTag: String? = nil, markerType: MarkerType? = nil, chapterIndex: Int? = nil) {
        self.startPositionTicks = startPositionTicks
        self.name = name
        self.imageTag = imageTag
        self.markerType = markerType
        self.chapterIndex = chapterIndex
    }

    public enum CodingKeys: String, CodingKey { 
        case startPositionTicks = "StartPositionTicks"
        case name = "Name"
        case imageTag = "ImageTag"
        case markerType = "MarkerType"
        case chapterIndex = "ChapterIndex"
    }

}
