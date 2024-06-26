//
// AuthenticationAuthenticationResult.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct AuthenticationAuthenticationResult: Codable {

    public var user: UserDto?
    public var sessionInfo: SessionSessionInfo?
    /** The authentication token. */
    public var accessToken: String?
    /** The server identifier. */
    public var serverId: String?

    public init(user: UserDto? = nil, sessionInfo: SessionSessionInfo? = nil, accessToken: String? = nil, serverId: String? = nil) {
        self.user = user
        self.sessionInfo = sessionInfo
        self.accessToken = accessToken
        self.serverId = serverId
    }

    public enum CodingKeys: String, CodingKey { 
        case user = "User"
        case sessionInfo = "SessionInfo"
        case accessToken = "AccessToken"
        case serverId = "ServerId"
    }

}
