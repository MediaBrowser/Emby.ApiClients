//
// UniversalAudioServiceAPI.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation
import Alamofire


open class UniversalAudioServiceAPI {
    /**
     Gets an audio stream

     - parameter _id: (path) Item Id 
     - parameter deviceId: (query) The device id of the client requesting. Used to stop encoding processes when needed. (optional)
     - parameter startTimeTicks: (query) Optional. Specify a starting offset, in ticks. 1ms &#x3D; 10000 ticks. (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func getAudioByIdUniversal(_id: String, deviceId: String? = nil, startTimeTicks: Int64? = nil, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        getAudioByIdUniversalWithRequestBuilder(_id: _id, deviceId: deviceId, startTimeTicks: startTimeTicks).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     Gets an audio stream
     - GET /Audio/{Id}/universal

     - API Key:
       - type: apiKey api_key (QUERY)
       - name: apikeyauth
     - :
       - type: http
       - name: embyauth
     - parameter _id: (path) Item Id 
     - parameter deviceId: (query) The device id of the client requesting. Used to stop encoding processes when needed. (optional)
     - parameter startTimeTicks: (query) Optional. Specify a starting offset, in ticks. 1ms &#x3D; 10000 ticks. (optional)

     - returns: RequestBuilder<Void> 
     */
    open class func getAudioByIdUniversalWithRequestBuilder(_id: String, deviceId: String? = nil, startTimeTicks: Int64? = nil) -> RequestBuilder<Void> {
        var path = "/Audio/{Id}/universal"
        let _idPreEscape = "\(_id)"
        let _idPostEscape = _idPreEscape.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed) ?? ""
        path = path.replacingOccurrences(of: "{Id}", with: _idPostEscape, options: .literal, range: nil)
        let URLString = EmbyClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "DeviceId": deviceId, 
                        "StartTimeTicks": startTimeTicks?.encodeToJSON()
        ])


        let requestBuilder: RequestBuilder<Void>.Type = EmbyClientAPI.requestBuilderFactory.getNonDecodableBuilder()

        return requestBuilder.init(method: "GET", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false)
    }
    /**
     Gets an audio stream

     - parameter _id: (path) Item Id 
     - parameter container: (path)  
     - parameter deviceId: (query) The device id of the client requesting. Used to stop encoding processes when needed. (optional)
     - parameter startTimeTicks: (query) Optional. Specify a starting offset, in ticks. 1ms &#x3D; 10000 ticks. (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func getAudioByIdUniversalByContainer(_id: String, container: String, deviceId: String? = nil, startTimeTicks: Int64? = nil, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        getAudioByIdUniversalByContainerWithRequestBuilder(_id: _id, container: container, deviceId: deviceId, startTimeTicks: startTimeTicks).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     Gets an audio stream
     - GET /Audio/{Id}/universal.{Container}

     - API Key:
       - type: apiKey api_key (QUERY)
       - name: apikeyauth
     - :
       - type: http
       - name: embyauth
     - parameter _id: (path) Item Id 
     - parameter container: (path)  
     - parameter deviceId: (query) The device id of the client requesting. Used to stop encoding processes when needed. (optional)
     - parameter startTimeTicks: (query) Optional. Specify a starting offset, in ticks. 1ms &#x3D; 10000 ticks. (optional)

     - returns: RequestBuilder<Void> 
     */
    open class func getAudioByIdUniversalByContainerWithRequestBuilder(_id: String, container: String, deviceId: String? = nil, startTimeTicks: Int64? = nil) -> RequestBuilder<Void> {
        var path = "/Audio/{Id}/universal.{Container}"
        let _idPreEscape = "\(_id)"
        let _idPostEscape = _idPreEscape.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed) ?? ""
        path = path.replacingOccurrences(of: "{Id}", with: _idPostEscape, options: .literal, range: nil)
        let containerPreEscape = "\(container)"
        let containerPostEscape = containerPreEscape.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed) ?? ""
        path = path.replacingOccurrences(of: "{Container}", with: containerPostEscape, options: .literal, range: nil)
        let URLString = EmbyClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "DeviceId": deviceId, 
                        "StartTimeTicks": startTimeTicks?.encodeToJSON()
        ])


        let requestBuilder: RequestBuilder<Void>.Type = EmbyClientAPI.requestBuilderFactory.getNonDecodableBuilder()

        return requestBuilder.init(method: "GET", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false)
    }
    /**
     Gets an audio stream

     - parameter _id: (path) Item Id 
     - parameter deviceId: (query) The device id of the client requesting. Used to stop encoding processes when needed. (optional)
     - parameter startTimeTicks: (query) Optional. Specify a starting offset, in ticks. 1ms &#x3D; 10000 ticks. (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func headAudioByIdUniversal(_id: String, deviceId: String? = nil, startTimeTicks: Int64? = nil, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        headAudioByIdUniversalWithRequestBuilder(_id: _id, deviceId: deviceId, startTimeTicks: startTimeTicks).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     Gets an audio stream
     - HEAD /Audio/{Id}/universal

     - API Key:
       - type: apiKey api_key (QUERY)
       - name: apikeyauth
     - :
       - type: http
       - name: embyauth
     - parameter _id: (path) Item Id 
     - parameter deviceId: (query) The device id of the client requesting. Used to stop encoding processes when needed. (optional)
     - parameter startTimeTicks: (query) Optional. Specify a starting offset, in ticks. 1ms &#x3D; 10000 ticks. (optional)

     - returns: RequestBuilder<Void> 
     */
    open class func headAudioByIdUniversalWithRequestBuilder(_id: String, deviceId: String? = nil, startTimeTicks: Int64? = nil) -> RequestBuilder<Void> {
        var path = "/Audio/{Id}/universal"
        let _idPreEscape = "\(_id)"
        let _idPostEscape = _idPreEscape.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed) ?? ""
        path = path.replacingOccurrences(of: "{Id}", with: _idPostEscape, options: .literal, range: nil)
        let URLString = EmbyClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "DeviceId": deviceId, 
                        "StartTimeTicks": startTimeTicks?.encodeToJSON()
        ])


        let requestBuilder: RequestBuilder<Void>.Type = EmbyClientAPI.requestBuilderFactory.getNonDecodableBuilder()

        return requestBuilder.init(method: "HEAD", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false)
    }
    /**
     Gets an audio stream

     - parameter _id: (path) Item Id 
     - parameter container: (path)  
     - parameter deviceId: (query) The device id of the client requesting. Used to stop encoding processes when needed. (optional)
     - parameter startTimeTicks: (query) Optional. Specify a starting offset, in ticks. 1ms &#x3D; 10000 ticks. (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func headAudioByIdUniversalByContainer(_id: String, container: String, deviceId: String? = nil, startTimeTicks: Int64? = nil, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        headAudioByIdUniversalByContainerWithRequestBuilder(_id: _id, container: container, deviceId: deviceId, startTimeTicks: startTimeTicks).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     Gets an audio stream
     - HEAD /Audio/{Id}/universal.{Container}

     - API Key:
       - type: apiKey api_key (QUERY)
       - name: apikeyauth
     - :
       - type: http
       - name: embyauth
     - parameter _id: (path) Item Id 
     - parameter container: (path)  
     - parameter deviceId: (query) The device id of the client requesting. Used to stop encoding processes when needed. (optional)
     - parameter startTimeTicks: (query) Optional. Specify a starting offset, in ticks. 1ms &#x3D; 10000 ticks. (optional)

     - returns: RequestBuilder<Void> 
     */
    open class func headAudioByIdUniversalByContainerWithRequestBuilder(_id: String, container: String, deviceId: String? = nil, startTimeTicks: Int64? = nil) -> RequestBuilder<Void> {
        var path = "/Audio/{Id}/universal.{Container}"
        let _idPreEscape = "\(_id)"
        let _idPostEscape = _idPreEscape.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed) ?? ""
        path = path.replacingOccurrences(of: "{Id}", with: _idPostEscape, options: .literal, range: nil)
        let containerPreEscape = "\(container)"
        let containerPostEscape = containerPreEscape.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed) ?? ""
        path = path.replacingOccurrences(of: "{Container}", with: containerPostEscape, options: .literal, range: nil)
        let URLString = EmbyClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "DeviceId": deviceId, 
                        "StartTimeTicks": startTimeTicks?.encodeToJSON()
        ])


        let requestBuilder: RequestBuilder<Void>.Type = EmbyClientAPI.requestBuilderFactory.getNonDecodableBuilder()

        return requestBuilder.init(method: "HEAD", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false)
    }
}
