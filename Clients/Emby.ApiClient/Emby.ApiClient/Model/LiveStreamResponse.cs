// <copyright file="LiveStreamResponse.cs" company="Emby LLC">
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
    /// LiveStreamResponse.
    /// </summary>
    /// <seealso>MediaBrowser.Model.MediaInfo.LiveStreamResponse</seealso>
    public partial class LiveStreamResponse :  IEquatable<LiveStreamResponse>
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="LiveStreamResponse" /> class.
        /// </summary>
        public LiveStreamResponse()
        {
        }
        
        /// <summary>
        /// Gets or Sets MediaSource
        /// </summary>
        /// <value>The MediaSource.</value>
        public MediaSourceInfo MediaSource { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class LiveStreamResponse {\n");
            sb.Append("  MediaSource: ").Append(MediaSource).Append("\n");
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
            return this.Equals(input as LiveStreamResponse);
        }

        /// <summary>
        /// Returns true if LiveStreamResponse instances are equal
        /// </summary>
        /// <param name="input">Instance of LiveStreamResponse to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(LiveStreamResponse input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.MediaSource == input.MediaSource ||
                    (this.MediaSource != null &&
                    this.MediaSource.Equals(input.MediaSource))
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
                if (this.MediaSource != null)
                    hashCode = hashCode * 59 + this.MediaSource.GetHashCode();
                return hashCode;
            }
        }
    }
}