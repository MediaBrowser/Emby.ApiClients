// <copyright file="VirtualFolderInfo.cs" company="Emby LLC">
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
    /// Used to hold information about a user's list of configured virtual folders  .
    /// </summary>
    /// <seealso>MediaBrowser.Model.Entities.VirtualFolderInfo</seealso>
    public partial class VirtualFolderInfo :  IEquatable<VirtualFolderInfo>
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="VirtualFolderInfo" /> class.
        /// </summary>
        public VirtualFolderInfo()
        {
        }
        
        /// <summary>
        /// The name.
        /// </summary>
        /// <value>The Name.</value>
        public string Name { get; set; }

        /// <summary>
        /// The locations.
        /// </summary>
        /// <value>The Locations.</value>
        public List<string> Locations { get; set; }

        /// <summary>
        /// The type of the collection.
        /// </summary>
        /// <value>The CollectionType.</value>
        public string CollectionType { get; set; }

        /// <summary>
        /// Gets or Sets LibraryOptions
        /// </summary>
        /// <value>The LibraryOptions.</value>
        public LibraryOptions LibraryOptions { get; set; }

        /// <summary>
        /// The item identifier.
        /// </summary>
        /// <value>The ItemId.</value>
        public string ItemId { get; set; }

        /// <summary>
        /// ItemId came first, so that is left for compatability purposes
        /// </summary>
        /// <value>The Id.</value>
        public string Id { get; set; }

        /// <summary>
        /// Gets or Sets Guid
        /// </summary>
        /// <value>The Guid.</value>
        public string Guid { get; set; }

        /// <summary>
        /// The primary image item identifier.
        /// </summary>
        /// <value>The PrimaryImageItemId.</value>
        public string PrimaryImageItemId { get; set; }

        /// <summary>
        /// Gets or Sets PrimaryImageTag
        /// </summary>
        /// <value>The PrimaryImageTag.</value>
        public string PrimaryImageTag { get; set; }

        /// <summary>
        /// Gets or Sets RefreshProgress
        /// </summary>
        /// <value>The RefreshProgress.</value>
        public double? RefreshProgress { get; set; }

        /// <summary>
        /// Gets or Sets RefreshStatus
        /// </summary>
        /// <value>The RefreshStatus.</value>
        public string RefreshStatus { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class VirtualFolderInfo {\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  Locations: ").Append(Locations).Append("\n");
            sb.Append("  CollectionType: ").Append(CollectionType).Append("\n");
            sb.Append("  LibraryOptions: ").Append(LibraryOptions).Append("\n");
            sb.Append("  ItemId: ").Append(ItemId).Append("\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  Guid: ").Append(Guid).Append("\n");
            sb.Append("  PrimaryImageItemId: ").Append(PrimaryImageItemId).Append("\n");
            sb.Append("  PrimaryImageTag: ").Append(PrimaryImageTag).Append("\n");
            sb.Append("  RefreshProgress: ").Append(RefreshProgress).Append("\n");
            sb.Append("  RefreshStatus: ").Append(RefreshStatus).Append("\n");
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
            return this.Equals(input as VirtualFolderInfo);
        }

        /// <summary>
        /// Returns true if VirtualFolderInfo instances are equal
        /// </summary>
        /// <param name="input">Instance of VirtualFolderInfo to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(VirtualFolderInfo input)
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
                    this.Locations == input.Locations ||
                    this.Locations != null &&
                    input.Locations != null &&
                    this.Locations.SequenceEqual(input.Locations)
                ) && 
                (
                    this.CollectionType == input.CollectionType ||
                    (this.CollectionType != null &&
                    this.CollectionType.Equals(input.CollectionType))
                ) && 
                (
                    this.LibraryOptions == input.LibraryOptions ||
                    (this.LibraryOptions != null &&
                    this.LibraryOptions.Equals(input.LibraryOptions))
                ) && 
                (
                    this.ItemId == input.ItemId ||
                    (this.ItemId != null &&
                    this.ItemId.Equals(input.ItemId))
                ) && 
                (
                    this.Id == input.Id ||
                    (this.Id != null &&
                    this.Id.Equals(input.Id))
                ) && 
                (
                    this.Guid == input.Guid ||
                    (this.Guid != null &&
                    this.Guid.Equals(input.Guid))
                ) && 
                (
                    this.PrimaryImageItemId == input.PrimaryImageItemId ||
                    (this.PrimaryImageItemId != null &&
                    this.PrimaryImageItemId.Equals(input.PrimaryImageItemId))
                ) && 
                (
                    this.PrimaryImageTag == input.PrimaryImageTag ||
                    (this.PrimaryImageTag != null &&
                    this.PrimaryImageTag.Equals(input.PrimaryImageTag))
                ) && 
                (
                    this.RefreshProgress == input.RefreshProgress ||
                    (this.RefreshProgress != null &&
                    this.RefreshProgress.Equals(input.RefreshProgress))
                ) && 
                (
                    this.RefreshStatus == input.RefreshStatus ||
                    (this.RefreshStatus != null &&
                    this.RefreshStatus.Equals(input.RefreshStatus))
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
                if (this.Locations != null)
                    hashCode = hashCode * 59 + this.Locations.GetHashCode();
                if (this.CollectionType != null)
                    hashCode = hashCode * 59 + this.CollectionType.GetHashCode();
                if (this.LibraryOptions != null)
                    hashCode = hashCode * 59 + this.LibraryOptions.GetHashCode();
                if (this.ItemId != null)
                    hashCode = hashCode * 59 + this.ItemId.GetHashCode();
                if (this.Id != null)
                    hashCode = hashCode * 59 + this.Id.GetHashCode();
                if (this.Guid != null)
                    hashCode = hashCode * 59 + this.Guid.GetHashCode();
                if (this.PrimaryImageItemId != null)
                    hashCode = hashCode * 59 + this.PrimaryImageItemId.GetHashCode();
                if (this.PrimaryImageTag != null)
                    hashCode = hashCode * 59 + this.PrimaryImageTag.GetHashCode();
                if (this.RefreshProgress != null)
                    hashCode = hashCode * 59 + this.RefreshProgress.GetHashCode();
                if (this.RefreshStatus != null)
                    hashCode = hashCode * 59 + this.RefreshStatus.GetHashCode();
                return hashCode;
            }
        }
    }
}