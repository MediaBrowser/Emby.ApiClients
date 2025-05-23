//
// DisplayPreferencesServiceAPI.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation
import Alamofire


open class DisplayPreferencesServiceAPI {
    /**
     Gets a user's display preferences for an item

     - parameter _id: (path) Item Id 
     - parameter userId: (query) User Id 
     - parameter client: (query) Client 
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func getDisplaypreferencesById(_id: String, userId: String, client: String, completion: @escaping ((_ data: DisplayPreferences?,_ error: Error?) -> Void)) {
        getDisplaypreferencesByIdWithRequestBuilder(_id: _id, userId: userId, client: client).execute { (response, error) -> Void in
            completion(response?.body, error)
        }
    }


    /**
     Gets a user's display preferences for an item
     - GET /DisplayPreferences/{Id}

     - API Key:
       - type: apiKey api_key (QUERY)
       - name: apikeyauth
     - :
       - type: http
       - name: embyauth
     - examples: [{contentType=application/json, example={
  "SortBy" : "SortBy",
  "SortOrder" : "Ascending",
  "Id" : "Id",
  "Client" : "Client",
  "CustomPrefs" : {
    "key" : "CustomPrefs"
  }
}}]
     - parameter _id: (path) Item Id 
     - parameter userId: (query) User Id 
     - parameter client: (query) Client 

     - returns: RequestBuilder<DisplayPreferences> 
     */
    open class func getDisplaypreferencesByIdWithRequestBuilder(_id: String, userId: String, client: String) -> RequestBuilder<DisplayPreferences> {
        var path = "/DisplayPreferences/{Id}"
        let _idPreEscape = "\(_id)"
        let _idPostEscape = _idPreEscape.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed) ?? ""
        path = path.replacingOccurrences(of: "{Id}", with: _idPostEscape, options: .literal, range: nil)
        let URLString = EmbyClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "UserId": userId, 
                        "Client": client
        ])


        let requestBuilder: RequestBuilder<DisplayPreferences>.Type = EmbyClientAPI.requestBuilderFactory.getBuilder()

        return requestBuilder.init(method: "GET", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false)
    }
    /**
     Gets user settings

     - parameter userId: (path) User Id 
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func getUsersettingsByUserid(userId: String, completion: @escaping ((_ data: [String:String]?,_ error: Error?) -> Void)) {
        getUsersettingsByUseridWithRequestBuilder(userId: userId).execute { (response, error) -> Void in
            completion(response?.body, error)
        }
    }


    /**
     Gets user settings
     - GET /UserSettings/{UserId}

     - API Key:
       - type: apiKey api_key (QUERY)
       - name: apikeyauth
     - :
       - type: http
       - name: embyauth
     - examples: [{contentType=application/json, example={
  "key" : ""
}}]
     - parameter userId: (path) User Id 

     - returns: RequestBuilder<[String:String]> 
     */
    open class func getUsersettingsByUseridWithRequestBuilder(userId: String) -> RequestBuilder<[String:String]> {
        var path = "/UserSettings/{UserId}"
        let userIdPreEscape = "\(userId)"
        let userIdPostEscape = userIdPreEscape.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed) ?? ""
        path = path.replacingOccurrences(of: "{UserId}", with: userIdPostEscape, options: .literal, range: nil)
        let URLString = EmbyClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        let url = URLComponents(string: URLString)


        let requestBuilder: RequestBuilder<[String:String]>.Type = EmbyClientAPI.requestBuilderFactory.getBuilder()

        return requestBuilder.init(method: "GET", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false)
    }
    /**
     Updates a user's display preferences for an item

     - parameter body: (body) DisplayPreferences:  
     - parameter userId: (query) User Id 
     - parameter displayPreferencesId: (path) DisplayPreferences Id 
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func postDisplaypreferencesByDisplaypreferencesid(body: DisplayPreferences, userId: String, displayPreferencesId: String, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        postDisplaypreferencesByDisplaypreferencesidWithRequestBuilder(body: body, userId: userId, displayPreferencesId: displayPreferencesId).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     Updates a user's display preferences for an item
     - POST /DisplayPreferences/{DisplayPreferencesId}

     - API Key:
       - type: apiKey api_key (QUERY)
       - name: apikeyauth
     - :
       - type: http
       - name: embyauth
     - parameter body: (body) DisplayPreferences:  
     - parameter userId: (query) User Id 
     - parameter displayPreferencesId: (path) DisplayPreferences Id 

     - returns: RequestBuilder<Void> 
     */
    open class func postDisplaypreferencesByDisplaypreferencesidWithRequestBuilder(body: DisplayPreferences, userId: String, displayPreferencesId: String) -> RequestBuilder<Void> {
        var path = "/DisplayPreferences/{DisplayPreferencesId}"
        let displayPreferencesIdPreEscape = "\(displayPreferencesId)"
        let displayPreferencesIdPostEscape = displayPreferencesIdPreEscape.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed) ?? ""
        path = path.replacingOccurrences(of: "{DisplayPreferencesId}", with: displayPreferencesIdPostEscape, options: .literal, range: nil)
        let URLString = EmbyClientAPI.basePath + path
        let parameters = JSONEncodingHelper.encodingParameters(forEncodableObject: body)
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "UserId": userId
        ])


        let requestBuilder: RequestBuilder<Void>.Type = EmbyClientAPI.requestBuilderFactory.getNonDecodableBuilder()

        return requestBuilder.init(method: "POST", URLString: (url?.string ?? URLString), parameters: parameters, isBody: true)
    }
    /**
     Updates a user's display preferences for an item

     - parameter body: (body) UserSettings:  
     - parameter userId: (path) User Id 
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func postUsersettingsByUserid(body: [String], userId: String, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        postUsersettingsByUseridWithRequestBuilder(body: body, userId: userId).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     Updates a user's display preferences for an item
     - POST /UserSettings/{UserId}

     - API Key:
       - type: apiKey api_key (QUERY)
       - name: apikeyauth
     - :
       - type: http
       - name: embyauth
     - parameter body: (body) UserSettings:  
     - parameter userId: (path) User Id 

     - returns: RequestBuilder<Void> 
     */
    open class func postUsersettingsByUseridWithRequestBuilder(body: [String], userId: String) -> RequestBuilder<Void> {
        var path = "/UserSettings/{UserId}"
        let userIdPreEscape = "\(userId)"
        let userIdPostEscape = userIdPreEscape.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed) ?? ""
        path = path.replacingOccurrences(of: "{UserId}", with: userIdPostEscape, options: .literal, range: nil)
        let URLString = EmbyClientAPI.basePath + path
        let parameters = JSONEncodingHelper.encodingParameters(forEncodableObject: body)
        let url = URLComponents(string: URLString)


        let requestBuilder: RequestBuilder<Void>.Type = EmbyClientAPI.requestBuilderFactory.getNonDecodableBuilder()

        return requestBuilder.init(method: "POST", URLString: (url?.string ?? URLString), parameters: parameters, isBody: true)
    }
    /**
     Updates a user's display preferences for an item

     - parameter body: (body) Binary stream 
     - parameter userId: (path) User Id 
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func postUsersettingsByUseridPartial(body: Object, userId: String, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        postUsersettingsByUseridPartialWithRequestBuilder(body: body, userId: userId).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     Updates a user's display preferences for an item
     - POST /UserSettings/{UserId}/Partial

     - API Key:
       - type: apiKey api_key (QUERY)
       - name: apikeyauth
     - :
       - type: http
       - name: embyauth
     - parameter body: (body) Binary stream 
     - parameter userId: (path) User Id 

     - returns: RequestBuilder<Void> 
     */
    open class func postUsersettingsByUseridPartialWithRequestBuilder(body: Object, userId: String) -> RequestBuilder<Void> {
        var path = "/UserSettings/{UserId}/Partial"
        let userIdPreEscape = "\(userId)"
        let userIdPostEscape = userIdPreEscape.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed) ?? ""
        path = path.replacingOccurrences(of: "{UserId}", with: userIdPostEscape, options: .literal, range: nil)
        let URLString = EmbyClientAPI.basePath + path
        let parameters = JSONEncodingHelper.encodingParameters(forEncodableObject: body)
        let url = URLComponents(string: URLString)


        let requestBuilder: RequestBuilder<Void>.Type = EmbyClientAPI.requestBuilderFactory.getNonDecodableBuilder()

        return requestBuilder.init(method: "POST", URLString: (url?.string ?? URLString), parameters: parameters, isBody: true)
    }
}
