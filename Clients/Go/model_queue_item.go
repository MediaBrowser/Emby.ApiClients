/*
 * Emby Server REST API
 *
 * Explore the Emby Server API
 *
 */
package embyclient

type QueueItem struct {
	Id int64 `json:"Id,omitempty"`
	PlaylistItemId string `json:"PlaylistItemId,omitempty"`
}
