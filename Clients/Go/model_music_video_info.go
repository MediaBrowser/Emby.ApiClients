/*
 * Emby Server REST API
 *
 * Explore the Emby Server API
 *
 */
package embyclient
import (
	"time"
)

type MusicVideoInfo struct {
	Artists []string `json:"Artists,omitempty"`
	// The name.
	Name string `json:"Name,omitempty"`
	Path string `json:"Path,omitempty"`
	// The metadata language.
	MetadataLanguage string `json:"MetadataLanguage,omitempty"`
	// The metadata country code.
	MetadataCountryCode string `json:"MetadataCountryCode,omitempty"`
	MetadataLanguages []GlobalizationCultureDto `json:"MetadataLanguages,omitempty"`
	ProviderIds *map[string]string `json:"ProviderIds,omitempty"`
	// The year.
	Year int32 `json:"Year,omitempty"`
	IndexNumber int32 `json:"IndexNumber,omitempty"`
	ParentIndexNumber int32 `json:"ParentIndexNumber,omitempty"`
	PremiereDate time.Time `json:"PremiereDate,omitempty"`
	IsAutomated bool `json:"IsAutomated,omitempty"`
	EnableAdultMetadata bool `json:"EnableAdultMetadata,omitempty"`
}
