// <copyright file="ContainerProfile.cs" company="Emby LLC">
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
    /// ContainerProfile.
    /// </summary>
    /// <seealso>MediaBrowser.Model.Dlna.ContainerProfile</seealso>
    public partial class ContainerProfile :  IEquatable<ContainerProfile>
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="ContainerProfile" /> class.
        /// </summary>
        public ContainerProfile()
        {
        }
        
        /// <summary>
        /// Gets or Sets Type
        /// </summary>
        /// <value>The Type.</value>
        public DlnaProfileType Type { get; set; }

        /// <summary>
        /// Gets or Sets Conditions
        /// </summary>
        /// <value>The Conditions.</value>
        public List<ProfileCondition> Conditions { get; set; }

        /// <summary>
        /// Gets or Sets Container
        /// </summary>
        /// <value>The Container.</value>
        public string Container { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class ContainerProfile {\n");
            sb.Append("  Type: ").Append(Type).Append("\n");
            sb.Append("  Conditions: ").Append(Conditions).Append("\n");
            sb.Append("  Container: ").Append(Container).Append("\n");
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
            return this.Equals(input as ContainerProfile);
        }

        /// <summary>
        /// Returns true if ContainerProfile instances are equal
        /// </summary>
        /// <param name="input">Instance of ContainerProfile to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(ContainerProfile input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Type == input.Type ||
                    (this.Type != null &&
                    this.Type.Equals(input.Type))
                ) && 
                (
                    this.Conditions == input.Conditions ||
                    this.Conditions != null &&
                    input.Conditions != null &&
                    this.Conditions.SequenceEqual(input.Conditions)
                ) && 
                (
                    this.Container == input.Container ||
                    (this.Container != null &&
                    this.Container.Equals(input.Container))
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
                if (this.Type != null)
                    hashCode = hashCode * 59 + this.Type.GetHashCode();
                if (this.Conditions != null)
                    hashCode = hashCode * 59 + this.Conditions.GetHashCode();
                if (this.Container != null)
                    hashCode = hashCode * 59 + this.Container.GetHashCode();
                return hashCode;
            }
        }
    }
}