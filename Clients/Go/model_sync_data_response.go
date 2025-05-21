/*
 * Emby Server REST API
 *
 * Explore the Emby Server API
 *
 */
package embyclient

type SyncDataResponse struct {
	ItemIdsToRemove []string `json:"ItemIdsToRemove,omitempty"`
}
