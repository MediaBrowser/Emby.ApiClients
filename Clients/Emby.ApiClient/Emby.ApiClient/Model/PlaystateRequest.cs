// <copyright file="PlaystateRequest.cs" company="Emby LLC">
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
    /// PlaystateRequest.
    /// </summary>
    /// <seealso>MediaBrowser.Model.Session.PlaystateRequest</seealso>
    public partial class PlaystateRequest :  IEquatable<PlaystateRequest>
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="PlaystateRequest" /> class.
        /// </summary>
        public PlaystateRequest()
        {
        }
        
        /// <summary>
        /// Gets or Sets Command
        /// </summary>
        /// <value>The Command.</value>
        public PlaystateCommand Command { get; set; }

        /// <summary>
        /// Gets or Sets SeekPositionTicks
        /// </summary>
        /// <value>The SeekPositionTicks.</value>
        public long? SeekPositionTicks { get; set; }

        /// <summary>
        /// The controlling user identifier.
        /// </summary>
        /// <value>The ControllingUserId.</value>
        public string ControllingUserId { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class PlaystateRequest {\n");
            sb.Append("  Command: ").Append(Command).Append("\n");
            sb.Append("  SeekPositionTicks: ").Append(SeekPositionTicks).Append("\n");
            sb.Append("  ControllingUserId: ").Append(ControllingUserId).Append("\n");
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
            return this.Equals(input as PlaystateRequest);
        }

        /// <summary>
        /// Returns true if PlaystateRequest instances are equal
        /// </summary>
        /// <param name="input">Instance of PlaystateRequest to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(PlaystateRequest input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Command == input.Command ||
                    (this.Command != null &&
                    this.Command.Equals(input.Command))
                ) && 
                (
                    this.SeekPositionTicks == input.SeekPositionTicks ||
                    (this.SeekPositionTicks != null &&
                    this.SeekPositionTicks.Equals(input.SeekPositionTicks))
                ) && 
                (
                    this.ControllingUserId == input.ControllingUserId ||
                    (this.ControllingUserId != null &&
                    this.ControllingUserId.Equals(input.ControllingUserId))
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
                if (this.Command != null)
                    hashCode = hashCode * 59 + this.Command.GetHashCode();
                if (this.SeekPositionTicks != null)
                    hashCode = hashCode * 59 + this.SeekPositionTicks.GetHashCode();
                if (this.ControllingUserId != null)
                    hashCode = hashCode * 59 + this.ControllingUserId.GetHashCode();
                return hashCode;
            }
        }
    }
}