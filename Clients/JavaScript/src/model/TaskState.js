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
* Enum class TaskState.
* @enum {}
* @readonly
*/
export default class TaskState {
        /**
         * value: "Idle"
         * @const
         */
        Idle = "Idle";

        /**
         * value: "Cancelling"
         * @const
         */
        Cancelling = "Cancelling";

        /**
         * value: "Running"
         * @const
         */
        Running = "Running";


    /**
    * Returns a <code>TaskState</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/TaskState} The enum <code>TaskState</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}
