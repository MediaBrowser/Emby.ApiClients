/*
 * Emby Server REST API
 *
 * Explore the Emby Server API
 *
 */
package embyclient

type LibraryPostUpdatedMedia struct {
	Updates []LibraryMediaUpdateInfo `json:"Updates,omitempty"`
}
