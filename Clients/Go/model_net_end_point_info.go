/*
 * Emby Server REST API
 *
 * Explore the Emby Server API
 *
 */
package embyclient

type NetEndPointInfo struct {
	IsLocal bool `json:"IsLocal,omitempty"`
	IsInNetwork bool `json:"IsInNetwork,omitempty"`
}
