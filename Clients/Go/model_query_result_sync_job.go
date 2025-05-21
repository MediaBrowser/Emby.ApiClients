/*
 * Emby Server REST API
 *
 * Explore the Emby Server API
 *
 */
package embyclient

type QueryResultSyncJob struct {
	Items []SyncJob `json:"Items,omitempty"`
	TotalRecordCount int32 `json:"TotalRecordCount,omitempty"`
}
