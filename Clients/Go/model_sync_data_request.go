/*
 * Emby Server REST API
 *
 * Explore the Emby Server API
 *
 */
package embyclient

type SyncDataRequest struct {
	LocalItemIds []string `json:"LocalItemIds,omitempty"`
	InternalTargetIds []int64 `json:"InternalTargetIds,omitempty"`
}
