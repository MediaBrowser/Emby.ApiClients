//
// LibraryOptionsResult.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct LibraryOptionsResult: Codable {

    public var metadataSavers: [LibraryOptionInfo]?
    public var metadataReaders: [LibraryOptionInfo]?
    public var subtitleFetchers: [LibraryOptionInfo]?
    public var lyricsFetchers: [LibraryOptionInfo]?
    public var typeOptions: [LibraryTypeOptions]?

    public init(metadataSavers: [LibraryOptionInfo]? = nil, metadataReaders: [LibraryOptionInfo]? = nil, subtitleFetchers: [LibraryOptionInfo]? = nil, lyricsFetchers: [LibraryOptionInfo]? = nil, typeOptions: [LibraryTypeOptions]? = nil) {
        self.metadataSavers = metadataSavers
        self.metadataReaders = metadataReaders
        self.subtitleFetchers = subtitleFetchers
        self.lyricsFetchers = lyricsFetchers
        self.typeOptions = typeOptions
    }

    public enum CodingKeys: String, CodingKey { 
        case metadataSavers = "MetadataSavers"
        case metadataReaders = "MetadataReaders"
        case subtitleFetchers = "SubtitleFetchers"
        case lyricsFetchers = "LyricsFetchers"
        case typeOptions = "TypeOptions"
    }

}