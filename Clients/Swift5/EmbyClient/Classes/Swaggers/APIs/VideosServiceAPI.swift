//
// VideosServiceAPI.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation
import Alamofire


open class VideosServiceAPI {
    /**
     Removes alternate video sources.

     - parameter _id: (path) Item Id 
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func deleteVideosByIdAlternatesources(_id: String, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        deleteVideosByIdAlternatesourcesWithRequestBuilder(_id: _id).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     Removes alternate video sources.
     - DELETE /Videos/{Id}/AlternateSources

     - API Key:
       - type: apiKey api_key (QUERY)
       - name: apikeyauth
     - :
       - type: http
       - name: embyauth
     - parameter _id: (path) Item Id 

     - returns: RequestBuilder<Void> 
     */
    open class func deleteVideosByIdAlternatesourcesWithRequestBuilder(_id: String) -> RequestBuilder<Void> {
        var path = "/Videos/{Id}/AlternateSources"
        let _idPreEscape = "\(_id)"
        let _idPostEscape = _idPreEscape.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed) ?? ""
        path = path.replacingOccurrences(of: "{Id}", with: _idPostEscape, options: .literal, range: nil)
        let URLString = EmbyClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        let url = URLComponents(string: URLString)


        let requestBuilder: RequestBuilder<Void>.Type = EmbyClientAPI.requestBuilderFactory.getNonDecodableBuilder()

        return requestBuilder.init(method: "DELETE", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false)
    }
    /**
     Removes alternate video sources.

     - parameter _id: (path) Item Id 
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func postVideosByIdAlternatesourcesDelete(_id: String, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        postVideosByIdAlternatesourcesDeleteWithRequestBuilder(_id: _id).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     Removes alternate video sources.
     - POST /Videos/{Id}/AlternateSources/Delete

     - API Key:
       - type: apiKey api_key (QUERY)
       - name: apikeyauth
     - :
       - type: http
       - name: embyauth
     - parameter _id: (path) Item Id 

     - returns: RequestBuilder<Void> 
     */
    open class func postVideosByIdAlternatesourcesDeleteWithRequestBuilder(_id: String) -> RequestBuilder<Void> {
        var path = "/Videos/{Id}/AlternateSources/Delete"
        let _idPreEscape = "\(_id)"
        let _idPostEscape = _idPreEscape.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed) ?? ""
        path = path.replacingOccurrences(of: "{Id}", with: _idPostEscape, options: .literal, range: nil)
        let URLString = EmbyClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        let url = URLComponents(string: URLString)


        let requestBuilder: RequestBuilder<Void>.Type = EmbyClientAPI.requestBuilderFactory.getNonDecodableBuilder()

        return requestBuilder.init(method: "POST", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false)
    }
    /**
     Merges videos into a single record

     - parameter ids: (query) Item id list. This allows multiple, comma delimited. (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func postVideosMergeversions(ids: String? = nil, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        postVideosMergeversionsWithRequestBuilder(ids: ids).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     Merges videos into a single record
     - POST /Videos/MergeVersions

     - API Key:
       - type: apiKey api_key (QUERY)
       - name: apikeyauth
     - :
       - type: http
       - name: embyauth
     - parameter ids: (query) Item id list. This allows multiple, comma delimited. (optional)

     - returns: RequestBuilder<Void> 
     */
    open class func postVideosMergeversionsWithRequestBuilder(ids: String? = nil) -> RequestBuilder<Void> {
        let path = "/Videos/MergeVersions"
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
