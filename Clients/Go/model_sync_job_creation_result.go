/*
 * Emby Server REST API
 *
 * Explore the Emby Server API
 *
 */
package embyclient

type SyncJobCreationResult struct {
	Job *SyncJob `json:"Job,omitempty"`
	JobItems []SyncJobItem `json:"JobItems,omitempty"`
}
