// <copyright file="SyncJobItem.cs" company="Emby LLC">
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
    /// SyncJobItem.
    /// </summary>
    /// <seealso>Emby.Server.Sync.Model.SyncJobItem</seealso>
    public partial class SyncJobItem :  IEquatable<SyncJobItem>
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="SyncJobItem" /> class.
        /// </summary>
        public SyncJobItem()
        {
        }
        
        /// <summary>
        /// Gets or Sets Id
        /// </summary>
        /// <value>The Id.</value>
        public long? Id { get; set; }

        /// <summary>
        /// Gets or Sets JobId
        /// </summary>
        /// <value>The JobId.</value>
        public long? JobId { get; set; }

        /// <summary>
        /// Gets or Sets ItemId
        /// </summary>
        /// <value>The ItemId.</value>
        public long? ItemId { get; set; }

        /// <summary>
        /// Gets or Sets ItemName
        /// </summary>
        /// <value>The ItemName.</value>
        public string ItemName { get; set; }

        /// <summary>
        /// Gets or Sets MediaSourceId
        /// </summary>
        /// <value>The MediaSourceId.</value>
        public string MediaSourceId { get; set; }

        /// <summary>
        /// Gets or Sets MediaSource
        /// </summary>
        /// <value>The MediaSource.</value>
        public MediaSourceInfo MediaSource { get; set; }

        /// <summary>
        /// Gets or Sets TargetId
        /// </summary>
        /// <value>The TargetId.</value>
        public string TargetId { get; set; }

        /// <summary>
        /// Gets or Sets InternalTargetId
        /// </summary>
        /// <value>The InternalTargetId.</value>
        public long? InternalTargetId { get; set; }

        /// <summary>
        /// Gets or Sets OutputPath
        /// </summary>
        /// <value>The OutputPath.</value>
        public string OutputPath { get; set; }

        /// <summary>
        /// Gets or Sets Status
        /// </summary>
        /// <value>The Status.</value>
        public SyncJobItemStatus Status { get; set; }

        /// <summary>
        /// Gets or Sets Progress
        /// </summary>
        /// <value>The Progress.</value>
        public double? Progress { get; set; }

        /// <summary>
        /// Gets or Sets DateCreated
        /// </summary>
        /// <value>The DateCreated.</value>
        public DateTimeOffset? DateCreated { get; set; }

        /// <summary>
        /// Gets or Sets PrimaryImageItemId
        /// </summary>
        /// <value>The PrimaryImageItemId.</value>
        public string PrimaryImageItemId { get; set; }

        /// <summary>
        /// Gets or Sets PrimaryImageTag
        /// </summary>
        /// <value>The PrimaryImageTag.</value>
        public string PrimaryImageTag { get; set; }

        /// <summary>
        /// Gets or Sets TemporaryPath
        /// </summary>
        /// <value>The TemporaryPath.</value>
        public string TemporaryPath { get; set; }

        /// <summary>
        /// Gets or Sets AdditionalFiles
        /// </summary>
        /// <value>The AdditionalFiles.</value>
        public List<ItemFileInfo> AdditionalFiles { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class SyncJobItem {\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  JobId: ").Append(JobId).Append("\n");
            sb.Append("  ItemId: ").Append(ItemId).Append("\n");
            sb.Append("  ItemName: ").Append(ItemName).Append("\n");
            sb.Append("  MediaSourceId: ").Append(MediaSourceId).Append("\n");
            sb.Append("  MediaSource: ").Append(MediaSource).Append("\n");
            sb.Append("  TargetId: ").Append(TargetId).Append("\n");
            sb.Append("  InternalTargetId: ").Append(InternalTargetId).Append("\n");
            sb.Append("  OutputPath: ").Append(OutputPath).Append("\n");
            sb.Append("  Status: ").Append(Status).Append("\n");
            sb.Append("  Progress: ").Append(Progress).Append("\n");
            sb.Append("  DateCreated: ").Append(DateCreated).Append("\n");
            sb.Append("  PrimaryImageItemId: ").Append(PrimaryImageItemId).Append("\n");
            sb.Append("  PrimaryImageTag: ").Append(PrimaryImageTag).Append("\n");
            sb.Append("  TemporaryPath: ").Append(TemporaryPath).Append("\n");
            sb.Append("  AdditionalFiles: ").Append(AdditionalFiles).Append("\n");
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
            return this.Equals(input as SyncJobItem);
        }

        /// <summary>
        /// Returns true if SyncJobItem instances are equal
        /// </summary>
        /// <param name="input">Instance of SyncJobItem to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(SyncJobItem input)
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
                    this.JobId == input.JobId ||
                    (this.JobId != null &&
                    this.JobId.Equals(input.JobId))
                ) && 
                (
                    this.ItemId == input.ItemId ||
                    (this.ItemId != null &&
                    this.ItemId.Equals(input.ItemId))
                ) && 
                (
                    this.ItemName == input.ItemName ||
                    (this.ItemName != null &&
                    this.ItemName.Equals(input.ItemName))
                ) && 
                (
                    this.MediaSourceId == input.MediaSourceId ||
                    (this.MediaSourceId != null &&
                    this.MediaSourceId.Equals(input.MediaSourceId))
                ) && 
                (
                    this.MediaSource == input.MediaSource ||
                    (this.MediaSource != null &&
                    this.MediaSource.Equals(input.MediaSource))
                ) && 
                (
                    this.TargetId == input.TargetId ||
                    (this.TargetId != null &&
                    this.TargetId.Equals(input.TargetId))
                ) && 
                (
                    this.InternalTargetId == input.InternalTargetId ||
                    (this.InternalTargetId != null &&
                    this.InternalTargetId.Equals(input.InternalTargetId))
                ) && 
                (
                    this.OutputPath == input.OutputPath ||
                    (this.OutputPath != null &&
                    this.OutputPath.Equals(input.OutputPath))
                ) && 
                (
                    this.Status == input.Status ||
                    (this.Status != null &&
                    this.Status.Equals(input.Status))
                ) && 
                (
                    this.Progress == input.Progress ||
                    (this.Progress != null &&
                    this.Progress.Equals(input.Progress))
                ) && 
                (
                    this.DateCreated == input.DateCreated ||
                    (this.DateCreated != null &&
                    this.DateCreated.Equals(input.DateCreated))
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
                    this.TemporaryPath == input.TemporaryPath ||
                    (this.TemporaryPath != null &&
                    this.TemporaryPath.Equals(input.TemporaryPath))
                ) && 
                (
                    this.AdditionalFiles == input.AdditionalFiles ||
                    this.AdditionalFiles != null &&
                    input.AdditionalFiles != null &&
                    this.AdditionalFiles.SequenceEqual(input.AdditionalFiles)
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
                if (this.JobId != null)
                    hashCode = hashCode * 59 + this.JobId.GetHashCode();
                if (this.ItemId != null)
                    hashCode = hashCode * 59 + this.ItemId.GetHashCode();
                if (this.ItemName != null)
                    hashCode = hashCode * 59 + this.ItemName.GetHashCode();
                if (this.MediaSourceId != null)
                    hashCode = hashCode * 59 + this.MediaSourceId.GetHashCode();
                if (this.MediaSource != null)
                    hashCode = hashCode * 59 + this.MediaSource.GetHashCode();
                if (this.TargetId != null)
                    hashCode = hashCode * 59 + this.TargetId.GetHashCode();
                if (this.InternalTargetId != null)
                    hashCode = hashCode * 59 + this.InternalTargetId.GetHashCode();
                if (this.OutputPath != null)
                    hashCode = hashCode * 59 + this.OutputPath.GetHashCode();
                if (this.Status != null)
                    hashCode = hashCode * 59 + this.Status.GetHashCode();
                if (this.Progress != null)
                    hashCode = hashCode * 59 + this.Progress.GetHashCode();
                if (this.DateCreated != null)
                    hashCode = hashCode * 59 + this.DateCreated.GetHashCode();
                if (this.PrimaryImageItemId != null)
                    hashCode = hashCode * 59 + this.PrimaryImageItemId.GetHashCode();
                if (this.PrimaryImageTag != null)
                    hashCode = hashCode * 59 + this.PrimaryImageTag.GetHashCode();
                if (this.TemporaryPath != null)
                    hashCode = hashCode * 59 + this.TemporaryPath.GetHashCode();
                if (this.AdditionalFiles != null)
                    hashCode = hashCode * 59 + this.AdditionalFiles.GetHashCode();
                return hashCode;
            }
        }
    }
}