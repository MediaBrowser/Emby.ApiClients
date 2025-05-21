/*
 * Emby Server REST API
 *
 * Explore the Emby Server API
 *
 */
package embyclient

type GenericEditIEditObjectContainer struct {
	Object *interface{} `json:"Object,omitempty"`
	DefaultObject *interface{} `json:"DefaultObject,omitempty"`
	TypeName string `json:"TypeName,omitempty"`
}
