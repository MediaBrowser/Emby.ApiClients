// <copyright file="SubtitleDeliveryMethod.cs" company="Emby LLC">
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
    /// Defines SubtitleDeliveryMethod
    /// </summary>
    /// <seealso>MediaBrowser.Model.Dlna.SubtitleDeliveryMethod</seealso>
    public enum SubtitleDeliveryMethod
    {
        /// <summary>
        /// Enum Encode for value: Encode
        /// </summary>
        [EnumMember(Value = "Encode")]
        Encode = 1,
        /// <summary>
        /// Enum Embed for value: Embed
        /// </summary>
        [EnumMember(Value = "Embed")]
        Embed = 2,
        /// <summary>
        /// Enum External for value: External
        /// </summary>
        [EnumMember(Value = "External")]
        External = 3,
        /// <summary>
        /// Enum Hls for value: Hls
        /// </summary>
        [EnumMember(Value = "Hls")]
        Hls = 4,
        /// <summary>
        /// Enum VideoSideData for value: VideoSideData
        /// </summary>
        [EnumMember(Value = "VideoSideData")]
        VideoSideData = 5    }
}