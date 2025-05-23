// <copyright file="ProgressEvent.cs" company="Emby LLC">
// Emby.ApiClient. Autogenerated Code. No license applied. 
// </copyright>
// <autogenerated />
namespace Emby.ApiClient.Model
{
    using System;
    using System.Linq;
    using System.IO;
    using System.Text;
    using System.Collections;
    using System.Collections.Generic;
    using System.Collections.ObjectModel;
    using System.Runtime.Serialization;

    /// <summary>
    /// Defines ProgressEvent
    /// </summary>
    /// <seealso>MediaBrowser.Model.Session.ProgressEvent</seealso>
    public enum ProgressEvent
    {
        /// <summary>
        /// Enum TimeUpdate for value: TimeUpdate
        /// </summary>
        [EnumMember(Value = "TimeUpdate")]
        TimeUpdate = 1,
        /// <summary>
        /// Enum Pause for value: Pause
        /// </summary>
        [EnumMember(Value = "Pause")]
        Pause = 2,
        /// <summary>
        /// Enum Unpause for value: Unpause
        /// </summary>
        [EnumMember(Value = "Unpause")]
        Unpause = 3,
        /// <summary>
        /// Enum VolumeChange for value: VolumeChange
        /// </summary>
        [EnumMember(Value = "VolumeChange")]
        VolumeChange = 4,
        /// <summary>
        /// Enum RepeatModeChange for value: RepeatModeChange
        /// </summary>
        [EnumMember(Value = "RepeatModeChange")]
        RepeatModeChange = 5,
        /// <summary>
        /// Enum AudioTrackChange for value: AudioTrackChange
        /// </summary>
        [EnumMember(Value = "AudioTrackChange")]
        AudioTrackChange = 6,
        /// <summary>
        /// Enum SubtitleTrackChange for value: SubtitleTrackChange
        /// </summary>
        [EnumMember(Value = "SubtitleTrackChange")]
        SubtitleTrackChange = 7,
        /// <summary>
        /// Enum PlaylistItemMove for value: PlaylistItemMove
        /// </summary>
        [EnumMember(Value = "PlaylistItemMove")]
        PlaylistItemMove = 8,
        /// <summary>
        /// Enum PlaylistItemRemove for value: PlaylistItemRemove
        /// </summary>
        [EnumMember(Value = "PlaylistItemRemove")]
        PlaylistItemRemove = 9,
        /// <summary>
        /// Enum PlaylistItemAdd for value: PlaylistItemAdd
        /// </summary>
        [EnumMember(Value = "PlaylistItemAdd")]
        PlaylistItemAdd = 10,
        /// <summary>
        /// Enum QualityChange for value: QualityChange
        /// </summary>
        [EnumMember(Value = "QualityChange")]
        QualityChange = 11,
        /// <summary>
        /// Enum StateChange for value: StateChange
        /// </summary>
        [EnumMember(Value = "StateChange")]
        StateChange = 12,
        /// <summary>
        /// Enum SubtitleOffsetChange for value: SubtitleOffsetChange
        /// </summary>
        [EnumMember(Value = "SubtitleOffsetChange")]
        SubtitleOffsetChange = 13,
        /// <summary>
        /// Enum PlaybackRateChange for value: PlaybackRateChange
        /// </summary>
        [EnumMember(Value = "PlaybackRateChange")]
        PlaybackRateChange = 14,
        /// <summary>
        /// Enum ShuffleChange for value: ShuffleChange
        /// </summary>
        [EnumMember(Value = "ShuffleChange")]
        ShuffleChange = 15,
        /// <summary>
        /// Enum SleepTimerChange for value: SleepTimerChange
        /// </summary>
        [EnumMember(Value = "SleepTimerChange")]
        SleepTimerChange = 16    }
}