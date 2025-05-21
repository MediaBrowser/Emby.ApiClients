/*
 * Emby Server REST API
 *
 * Explore the Emby Server API
 *
 */
package embyclient

type EncodingContext string

// List of EncodingContext
const (
	STREAMING_EncodingContext EncodingContext = "Streaming"
	STATIC_EncodingContext EncodingContext = "Static"
)
