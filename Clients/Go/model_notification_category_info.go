/*
 * Emby Server REST API
 *
 * Explore the Emby Server API
 *
 */
package embyclient

type NotificationCategoryInfo struct {
	Name string `json:"Name,omitempty"`
	Id string `json:"Id,omitempty"`
	Events []NotificationTypeInfo `json:"Events,omitempty"`
}
