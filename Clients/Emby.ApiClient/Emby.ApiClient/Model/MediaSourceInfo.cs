// <copyright file="MediaSourceInfo.cs" company="Emby LLC">
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
    /// MediaSourceInfo.
    /// </summary>
    /// <seealso>MediaBrowser.Model.Dto.MediaSourceInfo</seealso>
    public partial class MediaSourceInfo :  IEquatable<MediaSourceInfo>
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="MediaSourceInfo" /> class.
        /// </summary>
        public MediaSourceInfo()
        {
        }
        
        /// <summary>
        /// Gets or Sets Chapters
        /// </summary>
        /// <value>The Chapters.</value>
        public List<ChapterInfo> Chapters { get; set; }

        /// <summary>
        /// Gets or Sets Protocol
        /// </summary>
        /// <value>The Protocol.</value>
        public MediaProtocol Protocol { get; set; }

        /// <summary>
        /// Gets or Sets Id
        /// </summary>
        /// <value>The Id.</value>
        public string Id { get; set; }

        /// <summary>
        /// Gets or Sets Path
        /// </summary>
        /// <value>The Path.</value>
        public string Path { get; set; }

        /// <summary>
        /// Gets or Sets EncoderPath
        /// </summary>
        /// <value>The EncoderPath.</value>
        public string EncoderPath { get; set; }

        /// <summary>
        /// Gets or Sets EncoderProtocol
        /// </summary>
        /// <value>The EncoderProtocol.</value>
        public MediaProtocol EncoderProtocol { get; set; }

        /// <summary>
        /// Gets or Sets Type
        /// </summary>
        /// <value>The Type.</value>
        public MediaSourceType Type { get; set; }

        /// <summary>
        /// Gets or Sets ProbePath
        /// </summary>
        /// <value>The ProbePath.</value>
        public string ProbePath { get; set; }

        /// <summary>
        /// Gets or Sets ProbeProtocol
        /// </summary>
        /// <value>The ProbeProtocol.</value>
        public MediaProtocol ProbeProtocol { get; set; }

        /// <summary>
        /// Gets or Sets Container
        /// </summary>
        /// <value>The Container.</value>
        public string Container { get; set; }

        /// <summary>
        /// Gets or Sets Size
        /// </summary>
        /// <value>The Size.</value>
        public long? Size { get; set; }

        /// <summary>
        /// Gets or Sets Name
        /// </summary>
        /// <value>The Name.</value>
        public string Name { get; set; }

        /// <summary>
        /// Gets or Sets SortName
        /// </summary>
        /// <value>The SortName.</value>
        public string SortName { get; set; }

        /// <summary>
        /// Differentiate internet url vs local network
        /// </summary>
        /// <value>The IsRemote.</value>
        public bool? IsRemote { get; set; }

        /// <summary>
        /// Gets or Sets HasMixedProtocols
        /// </summary>
        /// <value>The HasMixedProtocols.</value>
        public bool? HasMixedProtocols { get; set; }

        /// <summary>
        /// Gets or Sets RunTimeTicks
        /// </summary>
        /// <value>The RunTimeTicks.</value>
        public long? RunTimeTicks { get; set; }

        /// <summary>
        /// Gets or Sets ContainerStartTimeTicks
        /// </summary>
        /// <value>The ContainerStartTimeTicks.</value>
        public long? ContainerStartTimeTicks { get; set; }

        /// <summary>
        /// Gets or Sets SupportsTranscoding
        /// </summary>
        /// <value>The SupportsTranscoding.</value>
        public bool? SupportsTranscoding { get; set; }

        /// <summary>
        /// Gets or Sets TrancodeLiveStartIndex
        /// </summary>
        /// <value>The TrancodeLiveStartIndex.</value>
        public int? TrancodeLiveStartIndex { get; set; }

        /// <summary>
        /// Gets or Sets WallClockStart
        /// </summary>
        /// <value>The WallClockStart.</value>
        public DateTimeOffset? WallClockStart { get; set; }

        /// <summary>
        /// Gets or Sets SupportsDirectStream
        /// </summary>
        /// <value>The SupportsDirectStream.</value>
        public bool? SupportsDirectStream { get; set; }

        /// <summary>
        /// Gets or Sets SupportsDirectPlay
        /// </summary>
        /// <value>The SupportsDirectPlay.</value>
        public bool? SupportsDirectPlay { get; set; }

        /// <summary>
        /// Gets or Sets IsInfiniteStream
        /// </summary>
        /// <value>The IsInfiniteStream.</value>
        public bool? IsInfiniteStream { get; set; }

        /// <summary>
        /// Gets or Sets RequiresOpening
        /// </summary>
        /// <value>The RequiresOpening.</value>
        public bool? RequiresOpening { get; set; }

        /// <summary>
        /// Gets or Sets OpenToken
        /// </summary>
        /// <value>The OpenToken.</value>
        public string OpenToken { get; set; }

        /// <summary>
        /// Gets or Sets RequiresClosing
        /// </summary>
        /// <value>The RequiresClosing.</value>
        public bool? RequiresClosing { get; set; }

        /// <summary>
        /// Gets or Sets LiveStreamId
        /// </summary>
        /// <value>The LiveStreamId.</value>
        public string LiveStreamId { get; set; }

        /// <summary>
        /// Gets or Sets BufferMs
        /// </summary>
        /// <value>The BufferMs.</value>
        public int? BufferMs { get; set; }

        /// <summary>
        /// Gets or Sets RequiresLooping
        /// </summary>
        /// <value>The RequiresLooping.</value>
        public bool? RequiresLooping { get; set; }

        /// <summary>
        /// Gets or Sets SupportsProbing
        /// </summary>
        /// <value>The SupportsProbing.</value>
        public bool? SupportsProbing { get; set; }

        /// <summary>
        /// Gets or Sets Video3DFormat
        /// </summary>
        /// <value>The Video3DFormat.</value>
        public Video3DFormat Video3DFormat { get; set; }

        /// <summary>
        /// Gets or Sets MediaStreams
        /// </summary>
        /// <value>The MediaStreams.</value>
        public List<MediaStream> MediaStreams { get; set; }

        /// <summary>
        /// Gets or Sets Formats
        /// </summary>
        /// <value>The Formats.</value>
        public List<string> Formats { get; set; }

        /// <summary>
        /// Gets or Sets Bitrate
        /// </summary>
        /// <value>The Bitrate.</value>
        public int? Bitrate { get; set; }

        /// <summary>
        /// Gets or Sets Timestamp
        /// </summary>
        /// <value>The Timestamp.</value>
        public TransportStreamTimestamp Timestamp { get; set; }

        /// <summary>
        /// Gets or Sets RequiredHttpHeaders
        /// </summary>
        /// <value>The RequiredHttpHeaders.</value>
        public Dictionary<string, string> RequiredHttpHeaders { get; set; }

        /// <summary>
        /// Gets or Sets DirectStreamUrl
        /// </summary>
        /// <value>The DirectStreamUrl.</value>
        public string DirectStreamUrl { get; set; }

        /// <summary>
        /// Gets or Sets AddApiKeyToDirectStreamUrl
        /// </summary>
        /// <value>The AddApiKeyToDirectStreamUrl.</value>
        public bool? AddApiKeyToDirectStreamUrl { get; set; }

        /// <summary>
        /// Gets or Sets TranscodingUrl
        /// </summary>
        /// <value>The TranscodingUrl.</value>
        public string TranscodingUrl { get; set; }

        /// <summary>
        /// Gets or Sets TranscodingSubProtocol
        /// </summary>
        /// <value>The TranscodingSubProtocol.</value>
        public string TranscodingSubProtocol { get; set; }

        /// <summary>
        /// Gets or Sets TranscodingContainer
        /// </summary>
        /// <value>The TranscodingContainer.</value>
        public string TranscodingContainer { get; set; }

        /// <summary>
        /// Gets or Sets AnalyzeDurationMs
        /// </summary>
        /// <value>The AnalyzeDurationMs.</value>
        public int? AnalyzeDurationMs { get; set; }

        /// <summary>
        /// Gets or Sets ReadAtNativeFramerate
        /// </summary>
        /// <value>The ReadAtNativeFramerate.</value>
        public bool? ReadAtNativeFramerate { get; set; }

        /// <summary>
        /// Gets or Sets DefaultAudioStreamIndex
        /// </summary>
        /// <value>The DefaultAudioStreamIndex.</value>
        public int? DefaultAudioStreamIndex { get; set; }

        /// <summary>
        /// Gets or Sets DefaultSubtitleStreamIndex
        /// </summary>
        /// <value>The DefaultSubtitleStreamIndex.</value>
        public int? DefaultSubtitleStreamIndex { get; set; }

        /// <summary>
        /// Used only by our Windows app. Not used by Emby Server. The id of the item that this mediasource belongs to, if there is one Also used by Emby for Kodi
        /// </summary>
        /// <value>The ItemId.</value>
        public string ItemId { get; set; }

        /// <summary>
        /// Used only by our Windows app. Not used by Emby Server.
        /// </summary>
        /// <value>The ServerId.</value>
        public string ServerId { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class MediaSourceInfo {\n");
            sb.Append("  Chapters: ").Append(Chapters).Append("\n");
            sb.Append("  Protocol: ").Append(Protocol).Append("\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  Path: ").Append(Path).Append("\n");
            sb.Append("  EncoderPath: ").Append(EncoderPath).Append("\n");
            sb.Append("  EncoderProtocol: ").Append(EncoderProtocol).Append("\n");
            sb.Append("  Type: ").Append(Type).Append("\n");
            sb.Append("  ProbePath: ").Append(ProbePath).Append("\n");
            sb.Append("  ProbeProtocol: ").Append(ProbeProtocol).Append("\n");
            sb.Append("  Container: ").Append(Container).Append("\n");
            sb.Append("  Size: ").Append(Size).Append("\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  SortName: ").Append(SortName).Append("\n");
            sb.Append("  IsRemote: ").Append(IsRemote).Append("\n");
            sb.Append("  HasMixedProtocols: ").Append(HasMixedProtocols).Append("\n");
            sb.Append("  RunTimeTicks: ").Append(RunTimeTicks).Append("\n");
            sb.Append("  ContainerStartTimeTicks: ").Append(ContainerStartTimeTicks).Append("\n");
            sb.Append("  SupportsTranscoding: ").Append(SupportsTranscoding).Append("\n");
            sb.Append("  TrancodeLiveStartIndex: ").Append(TrancodeLiveStartIndex).Append("\n");
            sb.Append("  WallClockStart: ").Append(WallClockStart).Append("\n");
            sb.Append("  SupportsDirectStream: ").Append(SupportsDirectStream).Append("\n");
            sb.Append("  SupportsDirectPlay: ").Append(SupportsDirectPlay).Append("\n");
            sb.Append("  IsInfiniteStream: ").Append(IsInfiniteStream).Append("\n");
            sb.Append("  RequiresOpening: ").Append(RequiresOpening).Append("\n");
            sb.Append("  OpenToken: ").Append(OpenToken).Append("\n");
            sb.Append("  RequiresClosing: ").Append(RequiresClosing).Append("\n");
            sb.Append("  LiveStreamId: ").Append(LiveStreamId).Append("\n");
            sb.Append("  BufferMs: ").Append(BufferMs).Append("\n");
            sb.Append("  RequiresLooping: ").Append(RequiresLooping).Append("\n");
            sb.Append("  SupportsProbing: ").Append(SupportsProbing).Append("\n");
            sb.Append("  Video3DFormat: ").Append(Video3DFormat).Append("\n");
            sb.Append("  MediaStreams: ").Append(MediaStreams).Append("\n");
            sb.Append("  Formats: ").Append(Formats).Append("\n");
            sb.Append("  Bitrate: ").Append(Bitrate).Append("\n");
            sb.Append("  Timestamp: ").Append(Timestamp).Append("\n");
            sb.Append("  RequiredHttpHeaders: ").Append(RequiredHttpHeaders).Append("\n");
            sb.Append("  DirectStreamUrl: ").Append(DirectStreamUrl).Append("\n");
            sb.Append("  AddApiKeyToDirectStreamUrl: ").Append(AddApiKeyToDirectStreamUrl).Append("\n");
            sb.Append("  TranscodingUrl: ").Append(TranscodingUrl).Append("\n");
            sb.Append("  TranscodingSubProtocol: ").Append(TranscodingSubProtocol).Append("\n");
            sb.Append("  TranscodingContainer: ").Append(TranscodingContainer).Append("\n");
            sb.Append("  AnalyzeDurationMs: ").Append(AnalyzeDurationMs).Append("\n");
            sb.Append("  ReadAtNativeFramerate: ").Append(ReadAtNativeFramerate).Append("\n");
            sb.Append("  DefaultAudioStreamIndex: ").Append(DefaultAudioStreamIndex).Append("\n");
            sb.Append("  DefaultSubtitleStreamIndex: ").Append(DefaultSubtitleStreamIndex).Append("\n");
            sb.Append("  ItemId: ").Append(ItemId).Append("\n");
            sb.Append("  ServerId: ").Append(ServerId).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as MediaSourceInfo);
        }

        /// <summary>
        /// Returns true if MediaSourceInfo instances are equal
        /// </summary>
        /// <param name="input">Instance of MediaSourceInfo to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(MediaSourceInfo input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Chapters == input.Chapters ||
                    this.Chapters != null &&
                    input.Chapters != null &&
                    this.Chapters.SequenceEqual(input.Chapters)
                ) && 
                (
                    this.Protocol == input.Protocol ||
                    (this.Protocol != null &&
                    this.Protocol.Equals(input.Protocol))
                ) && 
                (
                    this.Id == input.Id ||
                    (this.Id != null &&
                    this.Id.Equals(input.Id))
                ) && 
                (
                    this.Path == input.Path ||
                    (this.Path != null &&
                    this.Path.Equals(input.Path))
                ) && 
                (
                    this.EncoderPath == input.EncoderPath ||
                    (this.EncoderPath != null &&
                    this.EncoderPath.Equals(input.EncoderPath))
                ) && 
                (
                    this.EncoderProtocol == input.EncoderProtocol ||
                    (this.EncoderProtocol != null &&
                    this.EncoderProtocol.Equals(input.EncoderProtocol))
                ) && 
                (
                    this.Type == input.Type ||
                    (this.Type != null &&
                    this.Type.Equals(input.Type))
                ) && 
                (
                    this.ProbePath == input.ProbePath ||
                    (this.ProbePath != null &&
                    this.ProbePath.Equals(input.ProbePath))
                ) && 
                (
                    this.ProbeProtocol == input.ProbeProtocol ||
                    (this.ProbeProtocol != null &&
                    this.ProbeProtocol.Equals(input.ProbeProtocol))
                ) && 
                (
                    this.Container == input.Container ||
                    (this.Container != null &&
                    this.Container.Equals(input.Container))
                ) && 
                (
                    this.Size == input.Size ||
                    (this.Size != null &&
                    this.Size.Equals(input.Size))
                ) && 
                (
                    this.Name == input.Name ||
                    (this.Name != null &&
                    this.Name.Equals(input.Name))
                ) && 
                (
                    this.SortName == input.SortName ||
                    (this.SortName != null &&
                    this.SortName.Equals(input.SortName))
                ) && 
                (
                    this.IsRemote == input.IsRemote ||
                    (this.IsRemote != null &&
                    this.IsRemote.Equals(input.IsRemote))
                ) && 
                (
                    this.HasMixedProtocols == input.HasMixedProtocols ||
                    (this.HasMixedProtocols != null &&
                    this.HasMixedProtocols.Equals(input.HasMixedProtocols))
                ) && 
                (
                    this.RunTimeTicks == input.RunTimeTicks ||
                    (this.RunTimeTicks != null &&
                    this.RunTimeTicks.Equals(input.RunTimeTicks))
                ) && 
                (
                    this.ContainerStartTimeTicks == input.ContainerStartTimeTicks ||
                    (this.ContainerStartTimeTicks != null &&
                    this.ContainerStartTimeTicks.Equals(input.ContainerStartTimeTicks))
                ) && 
                (
                    this.SupportsTranscoding == input.SupportsTranscoding ||
                    (this.SupportsTranscoding != null &&
                    this.SupportsTranscoding.Equals(input.SupportsTranscoding))
                ) && 
                (
                    this.TrancodeLiveStartIndex == input.TrancodeLiveStartIndex ||
                    (this.TrancodeLiveStartIndex != null &&
                    this.TrancodeLiveStartIndex.Equals(input.TrancodeLiveStartIndex))
                ) && 
                (
                    this.WallClockStart == input.WallClockStart ||
                    (this.WallClockStart != null &&
                    this.WallClockStart.Equals(input.WallClockStart))
                ) && 
                (
                    this.SupportsDirectStream == input.SupportsDirectStream ||
                    (this.SupportsDirectStream != null &&
                    this.SupportsDirectStream.Equals(input.SupportsDirectStream))
                ) && 
                (
                    this.SupportsDirectPlay == input.SupportsDirectPlay ||
                    (this.SupportsDirectPlay != null &&
                    this.SupportsDirectPlay.Equals(input.SupportsDirectPlay))
                ) && 
                (
                    this.IsInfiniteStream == input.IsInfiniteStream ||
                    (this.IsInfiniteStream != null &&
                    this.IsInfiniteStream.Equals(input.IsInfiniteStream))
                ) && 
                (
                    this.RequiresOpening == input.RequiresOpening ||
                    (this.RequiresOpening != null &&
                    this.RequiresOpening.Equals(input.RequiresOpening))
                ) && 
                (
                    this.OpenToken == input.OpenToken ||
                    (this.OpenToken != null &&
                    this.OpenToken.Equals(input.OpenToken))
                ) && 
                (
                    this.RequiresClosing == input.RequiresClosing ||
                    (this.RequiresClosing != null &&
                    this.RequiresClosing.Equals(input.RequiresClosing))
                ) && 
                (
                    this.LiveStreamId == input.LiveStreamId ||
                    (this.LiveStreamId != null &&
                    this.LiveStreamId.Equals(input.LiveStreamId))
                ) && 
                (
                    this.BufferMs == input.BufferMs ||
                    (this.BufferMs != null &&
                    this.BufferMs.Equals(input.BufferMs))
                ) && 
                (
                    this.RequiresLooping == input.RequiresLooping ||
                    (this.RequiresLooping != null &&
                    this.RequiresLooping.Equals(input.RequiresLooping))
                ) && 
                (
                    this.SupportsProbing == input.SupportsProbing ||
                    (this.SupportsProbing != null &&
                    this.SupportsProbing.Equals(input.SupportsProbing))
                ) && 
                (
                    this.Video3DFormat == input.Video3DFormat ||
                    (this.Video3DFormat != null &&
                    this.Video3DFormat.Equals(input.Video3DFormat))
                ) && 
                (
                    this.MediaStreams == input.MediaStreams ||
                    this.MediaStreams != null &&
                    input.MediaStreams != null &&
                    this.MediaStreams.SequenceEqual(input.MediaStreams)
                ) && 
                (
                    this.Formats == input.Formats ||
                    this.Formats != null &&
                    input.Formats != null &&
                    this.Formats.SequenceEqual(input.Formats)
                ) && 
                (
                    this.Bitrate == input.Bitrate ||
                    (this.Bitrate != null &&
                    this.Bitrate.Equals(input.Bitrate))
                ) && 
                (
                    this.Timestamp == input.Timestamp ||
                    (this.Timestamp != null &&
                    this.Timestamp.Equals(input.Timestamp))
                ) && 
                (
                    this.RequiredHttpHeaders == input.RequiredHttpHeaders ||
                    this.RequiredHttpHeaders != null &&
                    input.RequiredHttpHeaders != null &&
                    this.RequiredHttpHeaders.SequenceEqual(input.RequiredHttpHeaders)
                ) && 
                (
                    this.DirectStreamUrl == input.DirectStreamUrl ||
                    (this.DirectStreamUrl != null &&
                    this.DirectStreamUrl.Equals(input.DirectStreamUrl))
                ) && 
                (
                    this.AddApiKeyToDirectStreamUrl == input.AddApiKeyToDirectStreamUrl ||
                    (this.AddApiKeyToDirectStreamUrl != null &&
                    this.AddApiKeyToDirectStreamUrl.Equals(input.AddApiKeyToDirectStreamUrl))
                ) && 
                (
                    this.TranscodingUrl == input.TranscodingUrl ||
                    (this.TranscodingUrl != null &&
                    this.TranscodingUrl.Equals(input.TranscodingUrl))
                ) && 
                (
                    this.TranscodingSubProtocol == input.TranscodingSubProtocol ||
                    (this.TranscodingSubProtocol != null &&
                    this.TranscodingSubProtocol.Equals(input.TranscodingSubProtocol))
                ) && 
                (
                    this.TranscodingContainer == input.TranscodingContainer ||
                    (this.TranscodingContainer != null &&
                    this.TranscodingContainer.Equals(input.TranscodingContainer))
                ) && 
                (
                    this.AnalyzeDurationMs == input.AnalyzeDurationMs ||
                    (this.AnalyzeDurationMs != null &&
                    this.AnalyzeDurationMs.Equals(input.AnalyzeDurationMs))
                ) && 
                (
                    this.ReadAtNativeFramerate == input.ReadAtNativeFramerate ||
                    (this.ReadAtNativeFramerate != null &&
                    this.ReadAtNativeFramerate.Equals(input.ReadAtNativeFramerate))
                ) && 
                (
                    this.DefaultAudioStreamIndex == input.DefaultAudioStreamIndex ||
                    (this.DefaultAudioStreamIndex != null &&
                    this.DefaultAudioStreamIndex.Equals(input.DefaultAudioStreamIndex))
                ) && 
                (
                    this.DefaultSubtitleStreamIndex == input.DefaultSubtitleStreamIndex ||
                    (this.DefaultSubtitleStreamIndex != null &&
                    this.DefaultSubtitleStreamIndex.Equals(input.DefaultSubtitleStreamIndex))
                ) && 
                (
                    this.ItemId == input.ItemId ||
                    (this.ItemId != null &&
                    this.ItemId.Equals(input.ItemId))
                ) && 
                (
                    this.ServerId == input.ServerId ||
                    (this.ServerId != null &&
                    this.ServerId.Equals(input.ServerId))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.Chapters != null)
                    hashCode = hashCode * 59 + this.Chapters.GetHashCode();
                if (this.Protocol != null)
                    hashCode = hashCode * 59 + this.Protocol.GetHashCode();
                if (this.Id != null)
                    hashCode = hashCode * 59 + this.Id.GetHashCode();
                if (this.Path != null)
                    hashCode = hashCode * 59 + this.Path.GetHashCode();
                if (this.EncoderPath != null)
                    hashCode = hashCode * 59 + this.EncoderPath.GetHashCode();
                if (this.EncoderProtocol != null)
                    hashCode = hashCode * 59 + this.EncoderProtocol.GetHashCode();
                if (this.Type != null)
                    hashCode = hashCode * 59 + this.Type.GetHashCode();
                if (this.ProbePath != null)
                    hashCode = hashCode * 59 + this.ProbePath.GetHashCode();
                if (this.ProbeProtocol != null)
                    hashCode = hashCode * 59 + this.ProbeProtocol.GetHashCode();
                if (this.Container != null)
                    hashCode = hashCode * 59 + this.Container.GetHashCode();
                if (this.Size != null)
                    hashCode = hashCode * 59 + this.Size.GetHashCode();
                if (this.Name != null)
                    hashCode = hashCode * 59 + this.Name.GetHashCode();
                if (this.SortName != null)
                    hashCode = hashCode * 59 + this.SortName.GetHashCode();
                if (this.IsRemote != null)
                    hashCode = hashCode * 59 + this.IsRemote.GetHashCode();
                if (this.HasMixedProtocols != null)
                    hashCode = hashCode * 59 + this.HasMixedProtocols.GetHashCode();
                if (this.RunTimeTicks != null)
                    hashCode = hashCode * 59 + this.RunTimeTicks.GetHashCode();
                if (this.ContainerStartTimeTicks != null)
                    hashCode = hashCode * 59 + this.ContainerStartTimeTicks.GetHashCode();
                if (this.SupportsTranscoding != null)
                    hashCode = hashCode * 59 + this.SupportsTranscoding.GetHashCode();
                if (this.TrancodeLiveStartIndex != null)
                    hashCode = hashCode * 59 + this.TrancodeLiveStartIndex.GetHashCode();
                if (this.WallClockStart != null)
                    hashCode = hashCode * 59 + this.WallClockStart.GetHashCode();
                if (this.SupportsDirectStream != null)
                    hashCode = hashCode * 59 + this.SupportsDirectStream.GetHashCode();
                if (this.SupportsDirectPlay != null)
                    hashCode = hashCode * 59 + this.SupportsDirectPlay.GetHashCode();
                if (this.IsInfiniteStream != null)
                    hashCode = hashCode * 59 + this.IsInfiniteStream.GetHashCode();
                if (this.RequiresOpening != null)
                    hashCode = hashCode * 59 + this.RequiresOpening.GetHashCode();
                if (this.OpenToken != null)
                    hashCode = hashCode * 59 + this.OpenToken.GetHashCode();
                if (this.RequiresClosing != null)
                    hashCode = hashCode * 59 + this.RequiresClosing.GetHashCode();
                if (this.LiveStreamId != null)
                    hashCode = hashCode * 59 + this.LiveStreamId.GetHashCode();
                if (this.BufferMs != null)
                    hashCode = hashCode * 59 + this.BufferMs.GetHashCode();
                if (this.RequiresLooping != null)
                    hashCode = hashCode * 59 + this.RequiresLooping.GetHashCode();
                if (this.SupportsProbing != null)
                    hashCode = hashCode * 59 + this.SupportsProbing.GetHashCode();
                if (this.Video3DFormat != null)
                    hashCode = hashCode * 59 + this.Video3DFormat.GetHashCode();
                if (this.MediaStreams != null)
                    hashCode = hashCode * 59 + this.MediaStreams.GetHashCode();
                if (this.Formats != null)
                    hashCode = hashCode * 59 + this.Formats.GetHashCode();
                if (this.Bitrate != null)
                    hashCode = hashCode * 59 + this.Bitrate.GetHashCode();
                if (this.Timestamp != null)
                    hashCode = hashCode * 59 + this.Timestamp.GetHashCode();
                if (this.RequiredHttpHeaders != null)
                    hashCode = hashCode * 59 + this.RequiredHttpHeaders.GetHashCode();
                if (this.DirectStreamUrl != null)
                    hashCode = hashCode * 59 + this.DirectStreamUrl.GetHashCode();
                if (this.AddApiKeyToDirectStreamUrl != null)
                    hashCode = hashCode * 59 + this.AddApiKeyToDirectStreamUrl.GetHashCode();
                if (this.TranscodingUrl != null)
                    hashCode = hashCode * 59 + this.TranscodingUrl.GetHashCode();
                if (this.TranscodingSubProtocol != null)
                    hashCode = hashCode * 59 + this.TranscodingSubProtocol.GetHashCode();
                if (this.TranscodingContainer != null)
                    hashCode = hashCode * 59 + this.TranscodingContainer.GetHashCode();
                if (this.AnalyzeDurationMs != null)
                    hashCode = hashCode * 59 + this.AnalyzeDurationMs.GetHashCode();
                if (this.ReadAtNativeFramerate != null)
                    hashCode = hashCode * 59 + this.ReadAtNativeFramerate.GetHashCode();
                if (this.DefaultAudioStreamIndex != null)
                    hashCode = hashCode * 59 + this.DefaultAudioStreamIndex.GetHashCode();
                if (this.DefaultSubtitleStreamIndex != null)
                    hashCode = hashCode * 59 + this.DefaultSubtitleStreamIndex.GetHashCode();
                if (this.ItemId != null)
                    hashCode = hashCode * 59 + this.ItemId.GetHashCode();
                if (this.ServerId != null)
                    hashCode = hashCode * 59 + this.ServerId.GetHashCode();
                return hashCode;
            }
        }
    }
}