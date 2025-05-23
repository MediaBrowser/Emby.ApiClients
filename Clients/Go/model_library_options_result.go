/*
 * Emby Server REST API
 *
 * Explore the Emby Server API
 *
 */
package embyclient

type LibraryOptionsResult struct {
	MetadataSavers []LibraryOptionInfo `json:"MetadataSavers,omitempty"`
	MetadataReaders []LibraryOptionInfo `json:"MetadataReaders,omitempty"`
	SubtitleFetchers []LibraryOptionInfo `json:"SubtitleFetchers,omitempty"`
	LyricsFetchers []LibraryOptionInfo `json:"LyricsFetchers,omitempty"`
	TypeOptions []LibraryTypeOptions `json:"TypeOptions,omitempty"`
	DefaultLibraryOptions *LibraryOptions `json:"DefaultLibraryOptions,omitempty"`
}
