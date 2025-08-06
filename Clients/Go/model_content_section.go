/*
 * Emby Server REST API (BETA)
 *
 * Explore the Emby Server API
 *
 */
package embyclient

type ContentSection struct {
	Name string `json:"Name,omitempty"`
	Id string `json:"Id,omitempty"`
	SectionType string `json:"SectionType,omitempty"`
	CollectionType string `json:"CollectionType,omitempty"`
	ViewType string `json:"ViewType,omitempty"`
	Monitor []string `json:"Monitor,omitempty"`
	CardSizeOffset int32 `json:"CardSizeOffset,omitempty"`
	ScrollDirection *ScrollDirection `json:"ScrollDirection,omitempty"`
	ParentItem *BaseItemDto `json:"ParentItem,omitempty"`
}
