/*
 * Emby Server REST API
 *
 * Explore the Emby Server API
 *
 */
package embyclient

type ActionsPostbackAction struct {
	TargetEditorId string `json:"TargetEditorId,omitempty"`
	PostbackCommandId string `json:"PostbackCommandId,omitempty"`
	CommandParameterPropertyId string `json:"CommandParameterPropertyId,omitempty"`
}
