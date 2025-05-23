/*
 * Emby Server REST API
 *
 * Explore the Emby Server API
 *
 */
package embyclient

type LibraryItemLinkType string

// List of Library.ItemLinkType
const (
	ARTISTS_LibraryItemLinkType LibraryItemLinkType = "Artists"
	ALBUM_ARTISTS_LibraryItemLinkType LibraryItemLinkType = "AlbumArtists"
	GENRES_LibraryItemLinkType LibraryItemLinkType = "Genres"
	STUDIOS_LibraryItemLinkType LibraryItemLinkType = "Studios"
	TAGS_LibraryItemLinkType LibraryItemLinkType = "Tags"
	COMPOSERS_LibraryItemLinkType LibraryItemLinkType = "Composers"
	COLLECTIONS_LibraryItemLinkType LibraryItemLinkType = "Collections"
	ALBUMS_LibraryItemLinkType LibraryItemLinkType = "Albums"
	COLLECTION_FOLDERS_LibraryItemLinkType LibraryItemLinkType = "CollectionFolders"
	LIVE_TV_SERIES_LibraryItemLinkType LibraryItemLinkType = "LiveTVSeries"
	GAME_SYSTEMS_LibraryItemLinkType LibraryItemLinkType = "GameSystems"
)
