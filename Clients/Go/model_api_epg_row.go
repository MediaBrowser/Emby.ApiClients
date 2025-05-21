/*
 * Emby Server REST API
 *
 * Explore the Emby Server API
 *
 */
package embyclient

type ApiEpgRow struct {
	Channel *BaseItemDto `json:"Channel,omitempty"`
	Programs []BaseItemDto `json:"Programs,omitempty"`
}
