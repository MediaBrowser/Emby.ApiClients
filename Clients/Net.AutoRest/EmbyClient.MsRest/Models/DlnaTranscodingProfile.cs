// <auto-generated>
// Code generated by Microsoft (R) AutoRest Code Generator.
// Changes may cause incorrect behavior and will be lost if the code is
// regenerated.
// </auto-generated>

namespace EmbyClient.MsRest.Models
{
    using Newtonsoft.Json;
    using System.Linq;

    public partial class DlnaTranscodingProfile
    {
        /// <summary>
        /// Initializes a new instance of the DlnaTranscodingProfile class.
        /// </summary>
        public DlnaTranscodingProfile()
        {
            CustomInit();
        }

        /// <summary>
        /// Initializes a new instance of the DlnaTranscodingProfile class.
        /// </summary>
        /// <param name="type">Possible values include: 'Audio', 'Video',
        /// 'Photo'</param>
        /// <param name="transcodeSeekInfo">Possible values include: 'Auto',
        /// 'Bytes'</param>
        /// <param name="context">Possible values include: 'Streaming',
        /// 'Static'</param>
        public DlnaTranscodingProfile(string container = default(string), string type = default(string), string videoCodec = default(string), string audioCodec = default(string), string protocol = default(string), bool? estimateContentLength = default(bool?), bool? enableMpegtsM2TsMode = default(bool?), string transcodeSeekInfo = default(string), bool? copyTimestamps = default(bool?), string context = default(string), string maxAudioChannels = default(string), int? minSegments = default(int?), int? segmentLength = default(int?), bool? breakOnNonKeyFrames = default(bool?), bool? allowInterlacedVideoStreamCopy = default(bool?), string manifestSubtitles = default(string), int? maxManifestSubtitles = default(int?))
        {
            Container = container;
            Type = type;
            VideoCodec = videoCodec;
            AudioCodec = audioCodec;
            Protocol = protocol;
            EstimateContentLength = estimateContentLength;
            EnableMpegtsM2TsMode = enableMpegtsM2TsMode;
            TranscodeSeekInfo = transcodeSeekInfo;
            CopyTimestamps = copyTimestamps;
            Context = context;
            MaxAudioChannels = maxAudioChannels;
            MinSegments = minSegments;
            SegmentLength = segmentLength;
            BreakOnNonKeyFrames = breakOnNonKeyFrames;
            AllowInterlacedVideoStreamCopy = allowInterlacedVideoStreamCopy;
            ManifestSubtitles = manifestSubtitles;
            MaxManifestSubtitles = maxManifestSubtitles;
            CustomInit();
        }

        /// <summary>
        /// An initialization method that performs custom operations like setting defaults
        /// </summary>
        partial void CustomInit();

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "Container")]
        public string Container { get; set; }

        /// <summary>
        /// Gets or sets possible values include: 'Audio', 'Video', 'Photo'
        /// </summary>
        [JsonProperty(PropertyName = "Type")]
        public string Type { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "VideoCodec")]
        public string VideoCodec { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "AudioCodec")]
        public string AudioCodec { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "Protocol")]
        public string Protocol { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "EstimateContentLength")]
        public bool? EstimateContentLength { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "EnableMpegtsM2TsMode")]
        public bool? EnableMpegtsM2TsMode { get; set; }

        /// <summary>
        /// Gets or sets possible values include: 'Auto', 'Bytes'
        /// </summary>
        [JsonProperty(PropertyName = "TranscodeSeekInfo")]
        public string TranscodeSeekInfo { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "CopyTimestamps")]
        public bool? CopyTimestamps { get; set; }

        /// <summary>
        /// Gets or sets possible values include: 'Streaming', 'Static'
        /// </summary>
        [JsonProperty(PropertyName = "Context")]
        public string Context { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "MaxAudioChannels")]
        public string MaxAudioChannels { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "MinSegments")]
        public int? MinSegments { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "SegmentLength")]
        public int? SegmentLength { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "BreakOnNonKeyFrames")]
        public bool? BreakOnNonKeyFrames { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "AllowInterlacedVideoStreamCopy")]
        public bool? AllowInterlacedVideoStreamCopy { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "ManifestSubtitles")]
        public string ManifestSubtitles { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "MaxManifestSubtitles")]
        public int? MaxManifestSubtitles { get; set; }

    }
}