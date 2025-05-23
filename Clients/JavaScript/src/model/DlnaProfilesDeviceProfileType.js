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
* Enum class DlnaProfilesDeviceProfileType.
* @enum {}
* @readonly
*/
export default class DlnaProfilesDeviceProfileType {
        /**
         * value: "System"
         * @const
         */
        System = "System";

        /**
         * value: "User"
         * @const
         */
        User = "User";


    /**
    * Returns a <code>DlnaProfilesDeviceProfileType</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/DlnaProfilesDeviceProfileType} The enum <code>DlnaProfilesDeviceProfileType</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}
