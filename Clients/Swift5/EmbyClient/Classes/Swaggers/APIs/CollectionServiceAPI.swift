//
// CollectionServiceAPI.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation
import Alamofire


open class CollectionServiceAPI {
    /**
     Removes items from a collection

     - parameter ids: (query) Item id, comma delimited 
     - parameter _id: (path)  
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func deleteCollectionsByIdItems(ids: String, _id: String, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        deleteCollectionsByIdItemsWithRequestBuilder(ids: ids, _id: _id).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     Removes items from a collection
     - DELETE /Collections/{Id}/Items

     - API Key:
       - type: apiKey api_key (QUERY)
       - name: apikeyauth
     - :
       - type: http
       - name: embyauth
     - parameter ids: (query) Item id, comma delimited 
     - parameter _id: (path)  

     - returns: RequestBuilder<Void> 
     */
    open class func deleteCollectionsByIdItemsWithRequestBuilder(ids: String, _id: String) -> RequestBuilder<Void> {
        var path = "/Collections/{Id}/Items"
        let _idPreEscape = "\(_id)"
        let _idPostEscape = _idPreEscape.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed) ?? ""
        path = path.replacingOccurrences(of: "{Id}", with: _idPostEscape, options: .literal, range: nil)
        let URLString = EmbyClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "Ids": ids
        ])


        let requestBuilder: RequestBuilder<Void>.Type = EmbyClientAPI.requestBuilderFactory.getNonDecodableBuilder()

        return requestBuilder.init(method: "DELETE", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false)
    }
    /**
     Creates a new collection

     - parameter isLocked: (query) Whether or not to lock the new collection. (optional)
     - parameter name: (query) The name of the new collection. (optional)
     - parameter parentId: (query) Optional - create the collection within a specific folder (optional)
     - parameter ids: (query) Item Ids to add to the collection (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func postCollections(isLocked: Bool? = nil, name: String? = nil, parentId: String? = nil, ids: String? = nil, completion: @escaping ((_ data: CollectionsCollectionCreationResult?,_ error: Error?) -> Void)) {
        postCollectionsWithRequestBuilder(isLocked: isLocked, name: name, parentId: parentId, ids: ids).execute { (response, error) -> Void in
            completion(response?.body, error)
        }
    }


    /**
     Creates a new collection
     - POST /Collections

     - API Key:
       - type: apiKey api_key (QUERY)
       - name: apikeyauth
     - :
       - type: http
       - name: embyauth
     - examples: [{contentType=application/json, example={
  "Id" : "Id",
  "Name" : "Name"
}}]
     - parameter isLocked: (query) Whether or not to lock the new collection. (optional)
     - parameter name: (query) The name of the new collection. (optional)
     - parameter parentId: (query) Optional - create the collection within a specific folder (optional)
     - parameter ids: (query) Item Ids to add to the collection (optional)

     - returns: RequestBuilder<CollectionsCollectionCreationResult> 
     */
    open class func postCollectionsWithRequestBuilder(isLocked: Bool? = nil, name: String? = nil, parentId: String? = nil, ids: String? = nil) -> RequestBuilder<CollectionsCollectionCreationResult> {
        let path = "/Collections"
        let URLString = EmbyClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "IsLocked": isLocked, 
                        "Name": name, 
                        "ParentId": parentId, 
                        "Ids": ids
        ])


        let requestBuilder: RequestBuilder<CollectionsCollectionCreationResult>.Type = EmbyClientAPI.requestBuilderFactory.getBuilder()

        return requestBuilder.init(method: "POST", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false)
    }
    /**
     Adds items to a collection

     - parameter ids: (query) Item id, comma delimited 
     - parameter _id: (path)  
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func postCollectionsByIdItems(ids: String, _id: String, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        postCollectionsByIdItemsWithRequestBuilder(ids: ids, _id: _id).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     Adds items to a collection
     - POST /Collections/{Id}/Items

     - API Key:
       - type: apiKey api_key (QUERY)
       - name: apikeyauth
     - :
       - type: http
       - name: embyauth
     - parameter ids: (query) Item id, comma delimited 
     - parameter _id: (path)  

     - returns: RequestBuilder<Void> 
     */
    open class func postCollectionsByIdItemsWithRequestBuilder(ids: String, _id: String) -> RequestBuilder<Void> {
        var path = "/Collections/{Id}/Items"
        let _idPreEscape = "\(_id)"
        let _idPostEscape = _idPreEscape.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed) ?? ""
        path = path.replacingOccurrences(of: "{Id}", with: _idPostEscape, options: .literal, range: nil)
        let URLString = EmbyClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "Ids": ids
        ])


        let requestBuilder: RequestBuilder<Void>.Type = EmbyClientAPI.requestBuilderFactory.getNonDecodableBuilder()

        return requestBuilder.init(method: "POST", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false)
    }
    /**
     Removes items from a collection

     - parameter ids: (query) Item id, comma delimited 
     - parameter _id: (path)  
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func postCollectionsByIdItemsDelete(ids: String, _id: String, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        postCollectionsByIdItemsDeleteWithRequestBuilder(ids: ids, _id: _id).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     Removes items from a collection
     - POST /Collections/{Id}/Items/Delete

     - API Key:
       - type: apiKey api_key (QUERY)
       - name: apikeyauth
     - :
       - type: http
       - name: embyauth
     - parameter ids: (query) Item id, comma delimited 
     - parameter _id: (path)  

     - returns: RequestBuilder<Void> 
     */
    open class func postCollectionsByIdItemsDeleteWithRequestBuilder(ids: String, _id: String) -> RequestBuilder<Void> {
        var path = "/Collections/{Id}/Items/Delete"
        let _idPreEscape = "\(_id)"
        let _idPostEscape = _idPreEscape.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed) ?? ""
        path = path.replacingOccurrences(of: "{Id}", with: _idPostEscape, options: .literal, range: nil)
        let URLString = EmbyClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "Ids": ids
        ])


        let requestBuilder: RequestBuilder<Void>.Type = EmbyClientAPI.requestBuilderFactory.getNonDecodableBuilder()

        return requestBuilder.init(method: "POST", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false)
    }
}
