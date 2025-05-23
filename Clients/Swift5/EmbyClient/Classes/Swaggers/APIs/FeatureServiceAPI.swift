//
// FeatureServiceAPI.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation
import Alamofire


open class FeatureServiceAPI {
    /**
     Gets a list of installed features

     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func getFeatures(completion: @escaping ((_ data: [FeatureInfo]?,_ error: Error?) -> Void)) {
        getFeaturesWithRequestBuilder().execute { (response, error) -> Void in
            completion(response?.body, error)
        }
    }


    /**
     Gets a list of installed features
     - GET /Features

     - API Key:
       - type: apiKey api_key (QUERY)
       - name: apikeyauth
     - :
       - type: http
       - name: embyauth
     - examples: [{contentType=application/json, example=[ {
  "FeatureType" : "System",
  "Id" : "Id",
  "Name" : "Name"
}, {
  "FeatureType" : "System",
  "Id" : "Id",
  "Name" : "Name"
} ]}]

     - returns: RequestBuilder<[FeatureInfo]> 
     */
    open class func getFeaturesWithRequestBuilder() -> RequestBuilder<[FeatureInfo]> {
        let path = "/Features"
        let URLString = EmbyClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        let url = URLComponents(string: URLString)


        let requestBuilder: RequestBuilder<[FeatureInfo]>.Type = EmbyClientAPI.requestBuilderFactory.getBuilder()

        return requestBuilder.init(method: "GET", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false)
    }
}
