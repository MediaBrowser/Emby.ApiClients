/*
 * Emby Server REST API
 *
 * Explore the Emby Server API
 *
 */
package embyclient

type QueryResultDevicesDeviceInfo struct {
	Items []DevicesDeviceInfo `json:"Items,omitempty"`
	TotalRecordCount int32 `json:"TotalRecordCount,omitempty"`
}
