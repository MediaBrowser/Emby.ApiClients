/*
 * Emby Server REST API
 *
 * Explore the Emby Server API
 *
 */
package embyclient

type LibraryUserCopyOptions string

// List of Library.UserCopyOptions
const (
	USER_POLICY_LibraryUserCopyOptions LibraryUserCopyOptions = "UserPolicy"
	USER_CONFIGURATION_LibraryUserCopyOptions LibraryUserCopyOptions = "UserConfiguration"
	USER_DATA_LibraryUserCopyOptions LibraryUserCopyOptions = "UserData"
)
