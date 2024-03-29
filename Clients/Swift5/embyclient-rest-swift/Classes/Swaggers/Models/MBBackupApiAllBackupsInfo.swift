//
// MBBackupApiAllBackupsInfo.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct MBBackupApiAllBackupsInfo: Codable {

    public var fullBackupInfo: MBBackupBackupInfo?
    public var lightBackups: [MBBackupBackupInfo]?

    public init(fullBackupInfo: MBBackupBackupInfo? = nil, lightBackups: [MBBackupBackupInfo]? = nil) {
        self.fullBackupInfo = fullBackupInfo
        self.lightBackups = lightBackups
    }

    public enum CodingKeys: String, CodingKey { 
        case fullBackupInfo = "FullBackupInfo"
        case lightBackups = "LightBackups"
    }

}
