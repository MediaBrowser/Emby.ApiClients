/*
 * Emby Server REST API
 *
 * Explore the Emby Server API
 *
 */
package embyclient

type LibraryUpdateLibraryOptions struct {
	Id string `json:"Id,omitempty"`
	LibraryOptions *LibraryOptions `json:"LibraryOptions,omitempty"`
}
