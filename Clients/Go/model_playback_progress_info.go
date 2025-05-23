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

// Class PlaybackProgressInfo.  
type PlaybackProgressInfo struct {
	// A value indicating whether this instance can seek.
	CanSeek bool `json:"CanSeek,omitempty"`
	NowPlayingQueue []QueueItem `json:"NowPlayingQueue,omitempty"`
	PlaylistItemId string `json:"PlaylistItemId,omitempty"`
	// The session id.
	SessionId string `json:"SessionId,omitempty"`
	// The index of the audio stream.
	AudioStreamIndex int32 `json:"AudioStreamIndex,omitempty"`
	// The index of the subtitle stream.
	SubtitleStreamIndex int32 `json:"SubtitleStreamIndex,omitempty"`
	// A value indicating whether this instance is paused.
	IsPaused bool `json:"IsPaused,omitempty"`
	PlaylistIndex int32 `json:"PlaylistIndex,omitempty"`
	PlaylistLength int32 `json:"PlaylistLength,omitempty"`
	// A value indicating whether this instance is muted.
	IsMuted bool `json:"IsMuted,omitempty"`
	RunTimeTicks int64 `json:"RunTimeTicks,omitempty"`
	PlaybackStartTimeTicks int64 `json:"PlaybackStartTimeTicks,omitempty"`
	// The volume level.
	VolumeLevel int32 `json:"VolumeLevel,omitempty"`
	Brightness int32 `json:"Brightness,omitempty"`
	AspectRatio string `json:"AspectRatio,omitempty"`
	EventName *ProgressEvent `json:"EventName,omitempty"`
	PlayMethod *PlayMethod `json:"PlayMethod,omitempty"`
	RepeatMode *RepeatMode `json:"RepeatMode,omitempty"`
	SleepTimerMode *SleepTimerMode `json:"SleepTimerMode,omitempty"`
	SleepTimerEndTime time.Time `json:"SleepTimerEndTime,omitempty"`
	Shuffle bool `json:"Shuffle,omitempty"`
	SubtitleOffset int32 `json:"SubtitleOffset,omitempty"`
	PlaybackRate float64 `json:"PlaybackRate,omitempty"`
	PlaylistItemIds []string `json:"PlaylistItemIds,omitempty"`
	// The play session identifier.
	PlaySessionId string `json:"PlaySessionId,omitempty"`
	// The item identifier.
	ItemId string `json:"ItemId,omitempty"`
	// The live stream identifier.
	LiveStreamId string `json:"LiveStreamId,omitempty"`
	// The media version identifier.
	MediaSourceId string `json:"MediaSourceId,omitempty"`
	Item *BaseItemDto `json:"Item,omitempty"`
	// The position ticks.
	PositionTicks int64 `json:"PositionTicks,omitempty"`
}
