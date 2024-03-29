// <copyright file="LibraryPostUpdatedMedia.cs" company="Emby LLC">
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
    /// LibraryPostUpdatedMedia.
    /// </summary>
    /// <seealso>Emby.Api.Library.PostUpdatedMedia</seealso>
    public partial class LibraryPostUpdatedMedia :  IEquatable<LibraryPostUpdatedMedia>
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="LibraryPostUpdatedMedia" /> class.
        /// </summary>
        public LibraryPostUpdatedMedia()
        {
        }
        
        /// <summary>
        /// Gets or Sets Updates
        /// </summary>
        /// <value>The Updates.</value>
        public List<LibraryMediaUpdateInfo> Updates { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class LibraryPostUpdatedMedia {\n");
            sb.Append("  Updates: ").Append(Updates).Append("\n");
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
            return this.Equals(input as LibraryPostUpdatedMedia);
        }

        /// <summary>
        /// Returns true if LibraryPostUpdatedMedia instances are equal
        /// </summary>
        /// <param name="input">Instance of LibraryPostUpdatedMedia to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(LibraryPostUpdatedMedia input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Updates == input.Updates ||
                    this.Updates != null &&
                    input.Updates != null &&
                    this.Updates.SequenceEqual(input.Updates)
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
                if (this.Updates != null)
                    hashCode = hashCode * 59 + this.Updates.GetHashCode();
                return hashCode;
            }
        }
    }
}