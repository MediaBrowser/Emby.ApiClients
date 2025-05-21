/*
 * Emby Server REST API
 *
 * Explore the Emby Server API
 *
 */
package embyclient

type EditObjectContainer struct {
	Object *interface{} `json:"Object,omitempty"`
	DefaultObject *interface{} `json:"DefaultObject,omitempty"`
	TypeName string `json:"TypeName,omitempty"`
	EditorRoot *EditorsEditorRoot `json:"EditorRoot,omitempty"`
}
