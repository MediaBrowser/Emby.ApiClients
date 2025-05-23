//
// RemoteImageServiceAPI.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation
import Alamofire


open class RemoteImageServiceAPI {
    /**
     Gets a remote image

     - parameter imageUrl: (query) The image url 
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func getImagesRemote(imageUrl: String, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        getImagesRemoteWithRequestBuilder(imageUrl: imageUrl).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     Gets a remote image
     - GET /Images/Remote

     - API Key:
       - type: apiKey api_key (QUERY)
       - name: apikeyauth
     - :
       - type: http
       - name: embyauth
     - parameter imageUrl: (query) The image url 

     - returns: RequestBuilder<Void> 
     */
    open class func getImagesRemoteWithRequestBuilder(imageUrl: String) -> RequestBuilder<Void> {
        let path = "/Images/Remote"
        let URLString = EmbyClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "ImageUrl": imageUrl
        ])


        let requestBuilder: RequestBuilder<Void>.Type = EmbyClientAPI.requestBuilderFactory.getNonDecodableBuilder()

        return requestBuilder.init(method: "GET", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false)
    }
    /**
     Gets available remote images for an item

     - parameter _id: (path) Item Id 
     - parameter type: (query) The image type (optional)
     - parameter startIndex: (query) Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
     - parameter limit: (query) Optional. The maximum number of records to return (optional)
     - parameter providerName: (query) Optional. The image provider to use (optional)
     - parameter includeAllLanguages: (query) Optional. (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func getItemsByIdRemoteimages(_id: String, type: ImageType? = nil, startIndex: Int? = nil, limit: Int? = nil, providerName: String? = nil, includeAllLanguages: Bool? = nil, completion: @escaping ((_ data: RemoteImageResult?,_ error: Error?) -> Void)) {
        getItemsByIdRemoteimagesWithRequestBuilder(_id: _id, type: type, startIndex: startIndex, limit: limit, providerName: providerName, includeAllLanguages: includeAllLanguages).execute { (response, error) -> Void in
            completion(response?.body, error)
        }
    }


    /**
     Gets available remote images for an item
     - GET /Items/{Id}/RemoteImages

     - API Key:
       - type: apiKey api_key (QUERY)
       - name: apikeyauth
     - :
       - type: http
       - name: embyauth
     - examples: [{contentType=application/json, example={
  "TotalRecordCount" : 5,
  "Images" : [ {
    "ProviderName" : "ProviderName",
    "DisplayLanguage" : "DisplayLanguage",
    "Type" : "Primary",
    "ThumbnailUrl" : "ThumbnailUrl",
    "Language" : "Language",
    "RatingType" : "Score",
    "VoteCount" : 5,
    "CommunityRating" : 1.4658129805029452,
    "Height" : 0,
    "Width" : 6,
    "Url" : "Url"
  }, {
    "ProviderName" : "ProviderName",
    "DisplayLanguage" : "DisplayLanguage",
    "Type" : "Primary",
    "ThumbnailUrl" : "ThumbnailUrl",
    "Language" : "Language",
    "RatingType" : "Score",
    "VoteCount" : 5,
    "CommunityRating" : 1.4658129805029452,
    "Height" : 0,
    "Width" : 6,
    "Url" : "Url"
  } ],
  "Providers" : [ "Providers", "Providers" ]
}}]
     - parameter _id: (path) Item Id 
     - parameter type: (query) The image type (optional)
     - parameter startIndex: (query) Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
     - parameter limit: (query) Optional. The maximum number of records to return (optional)
     - parameter providerName: (query) Optional. The image provider to use (optional)
     - parameter includeAllLanguages: (query) Optional. (optional)

     - returns: RequestBuilder<RemoteImageResult> 
     */
    open class func getItemsByIdRemoteimagesWithRequestBuilder(_id: String, type: ImageType? = nil, startIndex: Int? = nil, limit: Int? = nil, providerName: String? = nil, includeAllLanguages: Bool? = nil) -> RequestBuilder<RemoteImageResult> {
        var path = "/Items/{Id}/RemoteImages"
        let _idPreEscape = "\(_id)"
        let _idPostEscape = _idPreEscape.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed) ?? ""
        path = path.replacingOccurrences(of: "{Id}", with: _idPostEscape, options: .literal, range: nil)
        let URLString = EmbyClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "Type": type, 
                        "StartIndex": startIndex?.encodeToJSON(), 
                        "Limit": limit?.encodeToJSON(), 
                        "ProviderName": providerName, 
                        "IncludeAllLanguages": includeAllLanguages
        ])


        let requestBuilder: RequestBuilder<RemoteImageResult>.Type = EmbyClientAPI.requestBuilderFactory.getBuilder()

        return requestBuilder.init(method: "GET", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false)
    }
    /**
     Gets available remote image providers for an item

     - parameter _id: (path) Item Id 
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func getItemsByIdRemoteimagesProviders(_id: String, completion: @escaping ((_ data: [ImageProviderInfo]?,_ error: Error?) -> Void)) {
        getItemsByIdRemoteimagesProvidersWithRequestBuilder(_id: _id).execute { (response, error) -> Void in
            completion(response?.body, error)
        }
    }


    /**
     Gets available remote image providers for an item
     - GET /Items/{Id}/RemoteImages/Providers

     - API Key:
       - type: apiKey api_key (QUERY)
       - name: apikeyauth
     - :
       - type: http
       - name: embyauth
     - examples: [{contentType=application/json, example=[ {
  "SupportedImages" : [ "Primary", "Primary" ],
  "Name" : "Name"
}, {
  "SupportedImages" : [ "Primary", "Primary" ],
  "Name" : "Name"
} ]}]
     - parameter _id: (path) Item Id 

     - returns: RequestBuilder<[ImageProviderInfo]> 
     */
    open class func getItemsByIdRemoteimagesProvidersWithRequestBuilder(_id: String) -> RequestBuilder<[ImageProviderInfo]> {
        var path = "/Items/{Id}/RemoteImages/Providers"
        let _idPreEscape = "\(_id)"
        let _idPostEscape = _idPreEscape.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed) ?? ""
        path = path.replacingOccurrences(of: "{Id}", with: _idPostEscape, options: .literal, range: nil)
        let URLString = EmbyClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        let url = URLComponents(string: URLString)


        let requestBuilder: RequestBuilder<[ImageProviderInfo]>.Type = EmbyClientAPI.requestBuilderFactory.getBuilder()

        return requestBuilder.init(method: "GET", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false)
    }
    /**
     Downloads a remote image for an item

     - parameter body: (body) BaseDownloadRemoteImage:  
     - parameter type: (query) The image type 
     - parameter _id: (path) Item Id 
     - parameter providerName: (query) The image provider (optional)
     - parameter imageUrl: (query) The image url (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func postItemsByIdRemoteimagesDownload(body: ImagesBaseDownloadRemoteImage, type: ImageType, _id: String, providerName: String? = nil, imageUrl: String? = nil, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        postItemsByIdRemoteimagesDownloadWithRequestBuilder(body: body, type: type, _id: _id, providerName: providerName, imageUrl: imageUrl).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     Downloads a remote image for an item
     - POST /Items/{Id}/RemoteImages/Download

     - API Key:
       - type: apiKey api_key (QUERY)
       - name: apikeyauth
     - :
       - type: http
       - name: embyauth
     - parameter body: (body) BaseDownloadRemoteImage:  
     - parameter type: (query) The image type 
     - parameter _id: (path) Item Id 
     - parameter providerName: (query) The image provider (optional)
     - parameter imageUrl: (query) The image url (optional)

     - returns: RequestBuilder<Void> 
     */
    open class func postItemsByIdRemoteimagesDownloadWithRequestBuilder(body: ImagesBaseDownloadRemoteImage, type: ImageType, _id: String, providerName: String? = nil, imageUrl: String? = nil) -> RequestBuilder<Void> {
        var path = "/Items/{Id}/RemoteImages/Download"
        let _idPreEscape = "\(_id)"
        let _idPostEscape = _idPreEscape.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed) ?? ""
        path = path.replacingOccurrences(of: "{Id}", with: _idPostEscape, options: .literal, range: nil)
        let URLString = EmbyClientAPI.basePath + path
        let parameters = JSONEncodingHelper.encodingParameters(forEncodableObject: body)
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "Type": type, 
                        "ProviderName": providerName, 
                        "ImageUrl": imageUrl
        ])


        let requestBuilder: RequestBuilder<Void>.Type = EmbyClientAPI.requestBuilderFactory.getNonDecodableBuilder()

        return requestBuilder.init(method: "POST", URLString: (url?.string ?? URLString), parameters: parameters, isBody: true)
    }
}
