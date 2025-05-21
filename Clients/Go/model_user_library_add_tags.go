/*
 * Emby Server REST API
 *
 * Explore the Emby Server API
 *
 */
package embyclient

type UserLibraryAddTags struct {
	Tags []NameIdPair `json:"Tags,omitempty"`
}
