// <copyright file="QueueItem.cs" company="Emby LLC">
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
    /// QueueItem.
    /// </summary>
    /// <seealso>MediaBrowser.Model.Session.QueueItem</seealso>
    public partial class QueueItem :  IEquatable<QueueItem>
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="QueueItem" /> class.
        /// </summary>
        public QueueItem()
        {
        }
        
        /// <summary>
        /// Gets or Sets Id
        /// </summary>
        /// <value>The Id.</value>
        public long? Id { get; set; }

        /// <summary>
        /// Gets or Sets PlaylistItemId
        /// </summary>
        /// <value>The PlaylistItemId.</value>
        public string PlaylistItemId { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class QueueItem {\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  PlaylistItemId: ").Append(PlaylistItemId).Append("\n");
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
            return this.Equals(input as QueueItem);
        }

        /// <summary>
        /// Returns true if QueueItem instances are equal
        /// </summary>
        /// <param name="input">Instance of QueueItem to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(QueueItem input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Id == input.Id ||
                    (this.Id != null &&
                    this.Id.Equals(input.Id))
                ) && 
                (
                    this.PlaylistItemId == input.PlaylistItemId ||
                    (this.PlaylistItemId != null &&
                    this.PlaylistItemId.Equals(input.PlaylistItemId))
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
                if (this.Id != null)
                    hashCode = hashCode * 59 + this.Id.GetHashCode();
                if (this.PlaylistItemId != null)
                    hashCode = hashCode * 59 + this.PlaylistItemId.GetHashCode();
                return hashCode;
            }
        }
    }
}