/*
 * Emby Server REST API
 *
 * Explore the Emby Server API
 *
 */
package embyclient

type LibraryRemoveVirtualFolder struct {
	Id string `json:"Id,omitempty"`
	RefreshLibrary bool `json:"RefreshLibrary,omitempty"`
}
