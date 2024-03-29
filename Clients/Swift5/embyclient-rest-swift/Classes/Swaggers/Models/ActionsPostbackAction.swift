//
// ActionsPostbackAction.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct ActionsPostbackAction: Codable {

    public var targetEditorId: String?
    public var postbackCommandId: String?
    public var commandParameterPropertyId: String?

    public init(targetEditorId: String? = nil, postbackCommandId: String? = nil, commandParameterPropertyId: String? = nil) {
        self.targetEditorId = targetEditorId
        self.postbackCommandId = postbackCommandId
        self.commandParameterPropertyId = commandParameterPropertyId
    }

    public enum CodingKeys: String, CodingKey { 
        case targetEditorId = "TargetEditorId"
        case postbackCommandId = "PostbackCommandId"
        case commandParameterPropertyId = "CommandParameterPropertyId"
    }

}
