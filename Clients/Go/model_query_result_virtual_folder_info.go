/*
 * Emby Server REST API
 *
 * Explore the Emby Server API
 *
 */
package embyclient

type QueryResultVirtualFolderInfo struct {
	Items []VirtualFolderInfo `json:"Items,omitempty"`
	TotalRecordCount int32 `json:"TotalRecordCount,omitempty"`
}
