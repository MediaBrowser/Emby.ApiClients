/**
 * Emby Server REST API
 * Explore the Emby Server API
 *
 * 
 *
 * NOTE: This class is auto generated.
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
/**
* Enum class ProxyHeaderMode.
* @enum {}
* @readonly
*/
export default class ProxyHeaderMode {
        /**
         * value: "None"
         * @const
         */
        None = "None";

        /**
         * value: "LanAddressesOnly"
         * @const
         */
        LanAddressesOnly = "LanAddressesOnly";

        /**
         * value: "RemoteAddressesOnly"
         * @const
         */
        RemoteAddressesOnly = "RemoteAddressesOnly";

        /**
         * value: "AllAddresses"
         * @const
         */
        AllAddresses = "AllAddresses";


    /**
    * Returns a <code>ProxyHeaderMode</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/ProxyHeaderMode} The enum <code>ProxyHeaderMode</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}
