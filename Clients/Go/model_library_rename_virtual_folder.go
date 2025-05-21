/*
 * Emby Server REST API
 *
 * Explore the Emby Server API
 *
 */
package embyclient

type LibraryRenameVirtualFolder struct {
	Id string `json:"Id,omitempty"`
	NewName string `json:"NewName,omitempty"`
}
