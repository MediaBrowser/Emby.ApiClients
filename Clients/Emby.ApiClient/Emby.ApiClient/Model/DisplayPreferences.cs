// <copyright file="DisplayPreferences.cs" company="Emby LLC">
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
    /// DisplayPreferences.
    /// </summary>
    /// <seealso>Emby.Api.DisplayPreferences</seealso>
    public partial class DisplayPreferences :  IEquatable<DisplayPreferences>
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DisplayPreferences" /> class.
        /// </summary>
        public DisplayPreferences()
        {
        }
        
        /// <summary>
        /// Gets or Sets Id
        /// </summary>
        /// <value>The Id.</value>
        public string Id { get; set; }

        /// <summary>
        /// Gets or Sets SortBy
        /// </summary>
        /// <value>The SortBy.</value>
        public string SortBy { get; set; }

        /// <summary>
        /// Gets or Sets CustomPrefs
        /// </summary>
        /// <value>The CustomPrefs.</value>
        public Dictionary<string, string> CustomPrefs { get; set; }

        /// <summary>
        /// Gets or Sets SortOrder
        /// </summary>
        /// <value>The SortOrder.</value>
        public SortOrder SortOrder { get; set; }

        /// <summary>
        /// Gets or Sets _Client
        /// </summary>
        /// <value>The _Client.</value>
        public string _Client { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DisplayPreferences {\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  SortBy: ").Append(SortBy).Append("\n");
            sb.Append("  CustomPrefs: ").Append(CustomPrefs).Append("\n");
            sb.Append("  SortOrder: ").Append(SortOrder).Append("\n");
            sb.Append("  _Client: ").Append(_Client).Append("\n");
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
            return this.Equals(input as DisplayPreferences);
        }

        /// <summary>
        /// Returns true if DisplayPreferences instances are equal
        /// </summary>
        /// <param name="input">Instance of DisplayPreferences to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DisplayPreferences input)
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
                    this.SortBy == input.SortBy ||
                    (this.SortBy != null &&
                    this.SortBy.Equals(input.SortBy))
                ) && 
                (
                    this.CustomPrefs == input.CustomPrefs ||
                    this.CustomPrefs != null &&
                    input.CustomPrefs != null &&
                    this.CustomPrefs.SequenceEqual(input.CustomPrefs)
                ) && 
                (
                    this.SortOrder == input.SortOrder ||
                    (this.SortOrder != null &&
                    this.SortOrder.Equals(input.SortOrder))
                ) && 
                (
                    this._Client == input._Client ||
                    (this._Client != null &&
                    this._Client.Equals(input._Client))
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
                if (this.SortBy != null)
                    hashCode = hashCode * 59 + this.SortBy.GetHashCode();
                if (this.CustomPrefs != null)
                    hashCode = hashCode * 59 + this.CustomPrefs.GetHashCode();
                if (this.SortOrder != null)
                    hashCode = hashCode * 59 + this.SortOrder.GetHashCode();
                if (this._Client != null)
                    hashCode = hashCode * 59 + this._Client.GetHashCode();
                return hashCode;
            }
        }
    }
}