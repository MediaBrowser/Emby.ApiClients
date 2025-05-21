/*
 * Emby Server REST API
 *
 * Explore the Emby Server API
 *
 */
package embyclient

type LibraryUpdateMediaPath struct {
	Id string `json:"Id,omitempty"`
	PathInfo *MediaPathInfo `json:"PathInfo,omitempty"`
}
