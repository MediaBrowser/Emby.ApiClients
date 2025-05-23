/*
 * Emby Server REST API
 *
 * Explore the Emby Server API
 *
 */
package embyclient

type LibraryRemoveMediaPath struct {
	Id string `json:"Id,omitempty"`
	Path string `json:"Path,omitempty"`
	RefreshLibrary bool `json:"RefreshLibrary,omitempty"`
}
