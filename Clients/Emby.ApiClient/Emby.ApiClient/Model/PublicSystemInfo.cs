// <copyright file="PublicSystemInfo.cs" company="Emby LLC">
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
    /// PublicSystemInfo.
    /// </summary>
    /// <seealso>MediaBrowser.Model.System.PublicSystemInfo</seealso>
    public partial class PublicSystemInfo :  IEquatable<PublicSystemInfo>
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="PublicSystemInfo" /> class.
        /// </summary>
        public PublicSystemInfo()
        {
        }
        
        /// <summary>
        /// The local address.
        /// </summary>
        /// <value>The LocalAddress.</value>
        public string LocalAddress { get; set; }

        /// <summary>
        /// Gets or Sets LocalAddresses
        /// </summary>
        /// <value>The LocalAddresses.</value>
        public List<string> LocalAddresses { get; set; }

        /// <summary>
        /// The wan address.
        /// </summary>
        /// <value>The WanAddress.</value>
        public string WanAddress { get; set; }

        /// <summary>
        /// Gets or Sets RemoteAddresses
        /// </summary>
        /// <value>The RemoteAddresses.</value>
        public List<string> RemoteAddresses { get; set; }

        /// <summary>
        /// The name of the server.
        /// </summary>
        /// <value>The ServerName.</value>
        public string ServerName { get; set; }

        /// <summary>
        /// The version.
        /// </summary>
        /// <value>The Version.</value>
        public string Version { get; set; }

        /// <summary>
        /// The id.
        /// </summary>
        /// <value>The Id.</value>
        public string Id { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class PublicSystemInfo {\n");
            sb.Append("  LocalAddress: ").Append(LocalAddress).Append("\n");
            sb.Append("  LocalAddresses: ").Append(LocalAddresses).Append("\n");
            sb.Append("  WanAddress: ").Append(WanAddress).Append("\n");
            sb.Append("  RemoteAddresses: ").Append(RemoteAddresses).Append("\n");
            sb.Append("  ServerName: ").Append(ServerName).Append("\n");
            sb.Append("  Version: ").Append(Version).Append("\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
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
            return this.Equals(input as PublicSystemInfo);
        }

        /// <summary>
        /// Returns true if PublicSystemInfo instances are equal
        /// </summary>
        /// <param name="input">Instance of PublicSystemInfo to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(PublicSystemInfo input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.LocalAddress == input.LocalAddress ||
                    (this.LocalAddress != null &&
                    this.LocalAddress.Equals(input.LocalAddress))
                ) && 
                (
                    this.LocalAddresses == input.LocalAddresses ||
                    this.LocalAddresses != null &&
                    input.LocalAddresses != null &&
                    this.LocalAddresses.SequenceEqual(input.LocalAddresses)
                ) && 
                (
                    this.WanAddress == input.WanAddress ||
                    (this.WanAddress != null &&
                    this.WanAddress.Equals(input.WanAddress))
                ) && 
                (
                    this.RemoteAddresses == input.RemoteAddresses ||
                    this.RemoteAddresses != null &&
                    input.RemoteAddresses != null &&
                    this.RemoteAddresses.SequenceEqual(input.RemoteAddresses)
                ) && 
                (
                    this.ServerName == input.ServerName ||
                    (this.ServerName != null &&
                    this.ServerName.Equals(input.ServerName))
                ) && 
                (
                    this.Version == input.Version ||
                    (this.Version != null &&
                    this.Version.Equals(input.Version))
                ) && 
                (
                    this.Id == input.Id ||
                    (this.Id != null &&
                    this.Id.Equals(input.Id))
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
                if (this.LocalAddress != null)
                    hashCode = hashCode * 59 + this.LocalAddress.GetHashCode();
                if (this.LocalAddresses != null)
                    hashCode = hashCode * 59 + this.LocalAddresses.GetHashCode();
                if (this.WanAddress != null)
                    hashCode = hashCode * 59 + this.WanAddress.GetHashCode();
                if (this.RemoteAddresses != null)
                    hashCode = hashCode * 59 + this.RemoteAddresses.GetHashCode();
                if (this.ServerName != null)
                    hashCode = hashCode * 59 + this.ServerName.GetHashCode();
                if (this.Version != null)
                    hashCode = hashCode * 59 + this.Version.GetHashCode();
                if (this.Id != null)
                    hashCode = hashCode * 59 + this.Id.GetHashCode();
                return hashCode;
            }
        }
    }
}