// <copyright file="LibraryAddVirtualFolder.cs" company="Emby LLC">
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
    /// LibraryAddVirtualFolder.
    /// </summary>
    /// <seealso>Emby.Api.Library.AddVirtualFolder</seealso>
    public partial class LibraryAddVirtualFolder :  IEquatable<LibraryAddVirtualFolder>
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="LibraryAddVirtualFolder" /> class.
        /// </summary>
        public LibraryAddVirtualFolder()
        {
        }
        
        /// <summary>
        /// Gets or Sets Name
        /// </summary>
        /// <value>The Name.</value>
        public string Name { get; set; }

        /// <summary>
        /// Gets or Sets CollectionType
        /// </summary>
        /// <value>The CollectionType.</value>
        public string CollectionType { get; set; }

        /// <summary>
        /// Gets or Sets RefreshLibrary
        /// </summary>
        /// <value>The RefreshLibrary.</value>
        public bool? RefreshLibrary { get; set; }

        /// <summary>
        /// Gets or Sets Paths
        /// </summary>
        /// <value>The Paths.</value>
        public List<string> Paths { get; set; }

        /// <summary>
        /// Gets or Sets LibraryOptions
        /// </summary>
        /// <value>The LibraryOptions.</value>
        public LibraryOptions LibraryOptions { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class LibraryAddVirtualFolder {\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  CollectionType: ").Append(CollectionType).Append("\n");
            sb.Append("  RefreshLibrary: ").Append(RefreshLibrary).Append("\n");
            sb.Append("  Paths: ").Append(Paths).Append("\n");
            sb.Append("  LibraryOptions: ").Append(LibraryOptions).Append("\n");
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
            return this.Equals(input as LibraryAddVirtualFolder);
        }

        /// <summary>
        /// Returns true if LibraryAddVirtualFolder instances are equal
        /// </summary>
        /// <param name="input">Instance of LibraryAddVirtualFolder to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(LibraryAddVirtualFolder input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Name == input.Name ||
                    (this.Name != null &&
                    this.Name.Equals(input.Name))
                ) && 
                (
                    this.CollectionType == input.CollectionType ||
                    (this.CollectionType != null &&
                    this.CollectionType.Equals(input.CollectionType))
                ) && 
                (
                    this.RefreshLibrary == input.RefreshLibrary ||
                    (this.RefreshLibrary != null &&
                    this.RefreshLibrary.Equals(input.RefreshLibrary))
                ) && 
                (
                    this.Paths == input.Paths ||
                    this.Paths != null &&
                    input.Paths != null &&
                    this.Paths.SequenceEqual(input.Paths)
                ) && 
                (
                    this.LibraryOptions == input.LibraryOptions ||
                    (this.LibraryOptions != null &&
                    this.LibraryOptions.Equals(input.LibraryOptions))
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
                if (this.Name != null)
                    hashCode = hashCode * 59 + this.Name.GetHashCode();
                if (this.CollectionType != null)
                    hashCode = hashCode * 59 + this.CollectionType.GetHashCode();
                if (this.RefreshLibrary != null)
                    hashCode = hashCode * 59 + this.RefreshLibrary.GetHashCode();
                if (this.Paths != null)
                    hashCode = hashCode * 59 + this.Paths.GetHashCode();
                if (this.LibraryOptions != null)
                    hashCode = hashCode * 59 + this.LibraryOptions.GetHashCode();
                return hashCode;
            }
        }
    }
}