/*
 * Emby Server REST API
 *
 * Explore the Emby Server API
 *
 */
package embyclient

type DevicesContentUploadHistory struct {
	DeviceId string `json:"DeviceId,omitempty"`
	FilesUploaded []DevicesLocalFileInfo `json:"FilesUploaded,omitempty"`
}
