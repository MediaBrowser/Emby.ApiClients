//
// SyncJob.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct SyncJob: Codable {

    /** The identifier. */
    public var _id: Int64?
    /** The device identifier. */
    public var targetId: String?
    public var internalTargetId: Int64?
    /** The name of the target. */
    public var targetName: String?
    /** The quality. */
    public var quality: String?
    /** The bitrate. */
    public var bitrate: Int?
    public var container: String?
    public var videoCodec: String?
    public var audioCodec: String?
    /** The profile. */
    public var profile: String?
    public var category: SyncCategory?
    /** The parent identifier. */
    public var parentId: Int64?
    /** The current progress. */
    public var progress: Double?
    /** The name. */
    public var name: String?
    public var status: SyncJobStatus?
    /** The user identifier. */
    public var userId: Int64?
    /** A value indicating whether \\[unwatched only\\]. */
    public var unwatchedOnly: Bool?
    /** A value indicating whether \\[synchronize new content\\]. */
    public var syncNewContent: Bool?
    /** The item limit. */
    public var itemLimit: Int?
    /** The requested item ids. */
    public var requestedItemIds: [Int64]?
    public var itemId: Int64?
    /** The date created. */
    public var dateCreated: Date?
    /** The date last modified. */
    public var dateLastModified: Date?
    /** The item count. */
    public var itemCount: Int?
    public var parentName: String?
    public var primaryImageItemId: String?
    public var primaryImageTag: String?

    public init(_id: Int64? = nil, targetId: String? = nil, internalTargetId: Int64? = nil, targetName: String? = nil, quality: String? = nil, bitrate: Int? = nil, container: String? = nil, videoCodec: String? = nil, audioCodec: String? = nil, profile: String? = nil, category: SyncCategory? = nil, parentId: Int64? = nil, progress: Double? = nil, name: String? = nil, status: SyncJobStatus? = nil, userId: Int64? = nil, unwatchedOnly: Bool? = nil, syncNewContent: Bool? = nil, itemLimit: Int? = nil, requestedItemIds: [Int64]? = nil, itemId: Int64? = nil, dateCreated: Date? = nil, dateLastModified: Date? = nil, itemCount: Int? = nil, parentName: String? = nil, primaryImageItemId: String? = nil, primaryImageTag: String? = nil) {
        self._id = _id
        self.targetId = targetId
        self.internalTargetId = internalTargetId
        self.targetName = targetName
        self.quality = quality
        self.bitrate = bitrate
        self.container = container
        self.videoCodec = videoCodec
        self.audioCodec = audioCodec
        self.profile = profile
        self.category = category
        self.parentId = parentId
        self.progress = progress
        self.name = name
        self.status = status
        self.userId = userId
        self.unwatchedOnly = unwatchedOnly
        self.syncNewContent = syncNewContent
        self.itemLimit = itemLimit
        self.requestedItemIds = requestedItemIds
        self.itemId = itemId
        self.dateCreated = dateCreated
        self.dateLastModified = dateLastModified
        self.itemCount = itemCount
        self.parentName = parentName
        self.primaryImageItemId = primaryImageItemId
        self.primaryImageTag = primaryImageTag
    }

    public enum CodingKeys: String, CodingKey { 
        case _id = "Id"
        case targetId = "TargetId"
        case internalTargetId = "InternalTargetId"
        case targetName = "TargetName"
        case quality = "Quality"
        case bitrate = "Bitrate"
        case container = "Container"
        case videoCodec = "VideoCodec"
        case audioCodec = "AudioCodec"
        case profile = "Profile"
        case category = "Category"
        case parentId = "ParentId"
        case progress = "Progress"
        case name = "Name"
        case status = "Status"
        case userId = "UserId"
        case unwatchedOnly = "UnwatchedOnly"
        case syncNewContent = "SyncNewContent"
        case itemLimit = "ItemLimit"
        case requestedItemIds = "RequestedItemIds"
        case itemId = "ItemId"
        case dateCreated = "DateCreated"
        case dateLastModified = "DateLastModified"
        case itemCount = "ItemCount"
        case parentName = "ParentName"
        case primaryImageItemId = "PrimaryImageItemId"
        case primaryImageTag = "PrimaryImageTag"
    }

}
