//
// SystemInfo.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation


/** Class SystemInfo   */

public struct SystemInfo: Codable {

    public var systemUpdateLevel: PackageVersionClass?
    /** The display name of the operating system. */
    public var operatingSystemDisplayName: String?
    public var packageName: String?
    /** A value indicating whether this instance has pending restart. */
    public var hasPendingRestart: Bool?
    public var isShuttingDown: Bool?
    public var hasImageEnhancers: Bool?
    /** The operating sytem. */
    public var operatingSystem: String?
    /** A value indicating whether \\[supports library monitor\\]. */
    public var supportsLibraryMonitor: Bool?
    public var supportsLocalPortConfiguration: Bool?
    public var supportsWakeServer: Bool?
    /** The web socket port number. */
    public var webSocketPortNumber: Int?
    /** The completed installations. */
    public var completedInstallations: [InstallationInfo]?
    /** A value indicating whether this instance can self restart. */
    public var canSelfRestart: Bool?
    /** A value indicating whether this instance can self update. */
    public var canSelfUpdate: Bool?
    public var canLaunchWebBrowser: Bool?
    /** The program data path. */
    public var programDataPath: String?
    /** The items by name path. */
    public var itemsByNamePath: String?
    /** The cache path. */
    public var cachePath: String?
    /** The log path. */
    public var logPath: String?
    /** The internal metadata path. */
    public var internalMetadataPath: String?
    /** The transcoding temporary path. */
    public var transcodingTempPath: String?
    /** The HTTP server port number. */
    public var httpServerPortNumber: Int?
    /** A value indicating whether \\[enable HTTPS\\]. */
    public var supportsHttps: Bool?
    /** The HTTPS server port number. */
    public var httpsPortNumber: Int?
    /** A value indicating whether this instance has update available. */
    public var hasUpdateAvailable: Bool?
    /** A value indicating whether \\[supports automatic run at startup\\]. */
    public var supportsAutoRunAtStartup: Bool?
    public var hardwareAccelerationRequiresPremiere: Bool?
    public var wakeOnLanInfo: [WakeOnLanInfo]?
    /** The local address. */
    public var localAddress: String?
    public var localAddresses: [String]?
    /** The wan address. */
    public var wanAddress: String?
    public var remoteAddresses: [String]?
    /** The name of the server. */
    public var serverName: String?
    /** The version. */
    public var version: String?
    /** The id. */
    public var _id: String?

    public init(systemUpdateLevel: PackageVersionClass? = nil, operatingSystemDisplayName: String? = nil, packageName: String? = nil, hasPendingRestart: Bool? = nil, isShuttingDown: Bool? = nil, hasImageEnhancers: Bool? = nil, operatingSystem: String? = nil, supportsLibraryMonitor: Bool? = nil, supportsLocalPortConfiguration: Bool? = nil, supportsWakeServer: Bool? = nil, webSocketPortNumber: Int? = nil, completedInstallations: [InstallationInfo]? = nil, canSelfRestart: Bool? = nil, canSelfUpdate: Bool? = nil, canLaunchWebBrowser: Bool? = nil, programDataPath: String? = nil, itemsByNamePath: String? = nil, cachePath: String? = nil, logPath: String? = nil, internalMetadataPath: String? = nil, transcodingTempPath: String? = nil, httpServerPortNumber: Int? = nil, supportsHttps: Bool? = nil, httpsPortNumber: Int? = nil, hasUpdateAvailable: Bool? = nil, supportsAutoRunAtStartup: Bool? = nil, hardwareAccelerationRequiresPremiere: Bool? = nil, wakeOnLanInfo: [WakeOnLanInfo]? = nil, localAddress: String? = nil, localAddresses: [String]? = nil, wanAddress: String? = nil, remoteAddresses: [String]? = nil, serverName: String? = nil, version: String? = nil, _id: String? = nil) {
        self.systemUpdateLevel = systemUpdateLevel
        self.operatingSystemDisplayName = operatingSystemDisplayName
        self.packageName = packageName
        self.hasPendingRestart = hasPendingRestart
        self.isShuttingDown = isShuttingDown
        self.hasImageEnhancers = hasImageEnhancers
        self.operatingSystem = operatingSystem
        self.supportsLibraryMonitor = supportsLibraryMonitor
        self.supportsLocalPortConfiguration = supportsLocalPortConfiguration
        self.supportsWakeServer = supportsWakeServer
        self.webSocketPortNumber = webSocketPortNumber
        self.completedInstallations = completedInstallations
        self.canSelfRestart = canSelfRestart
        self.canSelfUpdate = canSelfUpdate
        self.canLaunchWebBrowser = canLaunchWebBrowser
        self.programDataPath = programDataPath
        self.itemsByNamePath = itemsByNamePath
        self.cachePath = cachePath
        self.logPath = logPath
        self.internalMetadataPath = internalMetadataPath
        self.transcodingTempPath = transcodingTempPath
        self.httpServerPortNumber = httpServerPortNumber
        self.supportsHttps = supportsHttps
        self.httpsPortNumber = httpsPortNumber
        self.hasUpdateAvailable = hasUpdateAvailable
        self.supportsAutoRunAtStartup = supportsAutoRunAtStartup
        self.hardwareAccelerationRequiresPremiere = hardwareAccelerationRequiresPremiere
        self.wakeOnLanInfo = wakeOnLanInfo
        self.localAddress = localAddress
        self.localAddresses = localAddresses
        self.wanAddress = wanAddress
        self.remoteAddresses = remoteAddresses
        self.serverName = serverName
        self.version = version
        self._id = _id
    }

    public enum CodingKeys: String, CodingKey { 
        case systemUpdateLevel = "SystemUpdateLevel"
        case operatingSystemDisplayName = "OperatingSystemDisplayName"
        case packageName = "PackageName"
        case hasPendingRestart = "HasPendingRestart"
        case isShuttingDown = "IsShuttingDown"
        case hasImageEnhancers = "HasImageEnhancers"
        case operatingSystem = "OperatingSystem"
        case supportsLibraryMonitor = "SupportsLibraryMonitor"
        case supportsLocalPortConfiguration = "SupportsLocalPortConfiguration"
        case supportsWakeServer = "SupportsWakeServer"
        case webSocketPortNumber = "WebSocketPortNumber"
        case completedInstallations = "CompletedInstallations"
        case canSelfRestart = "CanSelfRestart"
        case canSelfUpdate = "CanSelfUpdate"
        case canLaunchWebBrowser = "CanLaunchWebBrowser"
        case programDataPath = "ProgramDataPath"
        case itemsByNamePath = "ItemsByNamePath"
        case cachePath = "CachePath"
        case logPath = "LogPath"
        case internalMetadataPath = "InternalMetadataPath"
        case transcodingTempPath = "TranscodingTempPath"
        case httpServerPortNumber = "HttpServerPortNumber"
        case supportsHttps = "SupportsHttps"
        case httpsPortNumber = "HttpsPortNumber"
        case hasUpdateAvailable = "HasUpdateAvailable"
        case supportsAutoRunAtStartup = "SupportsAutoRunAtStartup"
        case hardwareAccelerationRequiresPremiere = "HardwareAccelerationRequiresPremiere"
        case wakeOnLanInfo = "WakeOnLanInfo"
        case localAddress = "LocalAddress"
        case localAddresses = "LocalAddresses"
        case wanAddress = "WanAddress"
        case remoteAddresses = "RemoteAddresses"
        case serverName = "ServerName"
        case version = "Version"
        case _id = "Id"
    }

}