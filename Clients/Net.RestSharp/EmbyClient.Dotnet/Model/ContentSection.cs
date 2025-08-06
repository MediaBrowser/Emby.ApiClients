/*
 * EmbyClient.Dotnet
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using SwaggerDateConverter = EmbyClient.Dotnet.Client.SwaggerDateConverter;

namespace EmbyClient.Dotnet.Model
{
    /// <summary>
    /// ContentSection
    /// </summary>
    [DataContract]
        public partial class ContentSection :  IEquatable<ContentSection>
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="ContentSection" /> class.
        /// </summary>
        /// <param name="name">name.</param>
        /// <param name="id">id.</param>
        /// <param name="sectionType">sectionType.</param>
        /// <param name="collectionType">collectionType.</param>
        /// <param name="viewType">viewType.</param>
        /// <param name="monitor">monitor.</param>
        /// <param name="cardSizeOffset">cardSizeOffset.</param>
        /// <param name="scrollDirection">scrollDirection.</param>
        /// <param name="parentItem">parentItem.</param>
        public ContentSection(string name = default(string), string id = default(string), string sectionType = default(string), string collectionType = default(string), string viewType = default(string), List<string> monitor = default(List<string>), int? cardSizeOffset = default(int?), ScrollDirection scrollDirection = default(ScrollDirection), BaseItemDto parentItem = default(BaseItemDto))
        {
            this.Name = name;
            this.Id = id;
            this.SectionType = sectionType;
            this.CollectionType = collectionType;
            this.ViewType = viewType;
            this.Monitor = monitor;
            this.CardSizeOffset = cardSizeOffset;
            this.ScrollDirection = scrollDirection;
            this.ParentItem = parentItem;
        }
        
        /// <summary>
        /// Gets or Sets Name
        /// </summary>
        [DataMember(Name="Name", EmitDefaultValue=false)]
        public string Name { get; set; }

        /// <summary>
        /// Gets or Sets Id
        /// </summary>
        [DataMember(Name="Id", EmitDefaultValue=false)]
        public string Id { get; set; }

        /// <summary>
        /// Gets or Sets SectionType
        /// </summary>
        [DataMember(Name="SectionType", EmitDefaultValue=false)]
        public string SectionType { get; set; }

        /// <summary>
        /// Gets or Sets CollectionType
        /// </summary>
        [DataMember(Name="CollectionType", EmitDefaultValue=false)]
        public string CollectionType { get; set; }

        /// <summary>
        /// Gets or Sets ViewType
        /// </summary>
        [DataMember(Name="ViewType", EmitDefaultValue=false)]
        public string ViewType { get; set; }

        /// <summary>
        /// Gets or Sets Monitor
        /// </summary>
        [DataMember(Name="Monitor", EmitDefaultValue=false)]
        public List<string> Monitor { get; set; }

        /// <summary>
        /// Gets or Sets CardSizeOffset
        /// </summary>
        [DataMember(Name="CardSizeOffset", EmitDefaultValue=false)]
        public int? CardSizeOffset { get; set; }

        /// <summary>
        /// Gets or Sets ScrollDirection
        /// </summary>
        [DataMember(Name="ScrollDirection", EmitDefaultValue=false)]
        public ScrollDirection ScrollDirection { get; set; }

        /// <summary>
        /// Gets or Sets ParentItem
        /// </summary>
        [DataMember(Name="ParentItem", EmitDefaultValue=false)]
        public BaseItemDto ParentItem { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class ContentSection {\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  SectionType: ").Append(SectionType).Append("\n");
            sb.Append("  CollectionType: ").Append(CollectionType).Append("\n");
            sb.Append("  ViewType: ").Append(ViewType).Append("\n");
            sb.Append("  Monitor: ").Append(Monitor).Append("\n");
            sb.Append("  CardSizeOffset: ").Append(CardSizeOffset).Append("\n");
            sb.Append("  ScrollDirection: ").Append(ScrollDirection).Append("\n");
            sb.Append("  ParentItem: ").Append(ParentItem).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as ContentSection);
        }

        /// <summary>
        /// Returns true if ContentSection instances are equal
        /// </summary>
        /// <param name="input">Instance of ContentSection to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(ContentSection input)
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
                    this.Id == input.Id ||
                    (this.Id != null &&
                    this.Id.Equals(input.Id))
                ) && 
                (
                    this.SectionType == input.SectionType ||
                    (this.SectionType != null &&
                    this.SectionType.Equals(input.SectionType))
                ) && 
                (
                    this.CollectionType == input.CollectionType ||
                    (this.CollectionType != null &&
                    this.CollectionType.Equals(input.CollectionType))
                ) && 
                (
                    this.ViewType == input.ViewType ||
                    (this.ViewType != null &&
                    this.ViewType.Equals(input.ViewType))
                ) && 
                (
                    this.Monitor == input.Monitor ||
                    this.Monitor != null &&
                    input.Monitor != null &&
                    this.Monitor.SequenceEqual(input.Monitor)
                ) && 
                (
                    this.CardSizeOffset == input.CardSizeOffset ||
                    (this.CardSizeOffset != null &&
                    this.CardSizeOffset.Equals(input.CardSizeOffset))
                ) && 
                (
                    this.ScrollDirection == input.ScrollDirection ||
                    (this.ScrollDirection != null &&
                    this.ScrollDirection.Equals(input.ScrollDirection))
                ) && 
                (
                    this.ParentItem == input.ParentItem ||
                    (this.ParentItem != null &&
                    this.ParentItem.Equals(input.ParentItem))
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
                if (this.Id != null)
                    hashCode = hashCode * 59 + this.Id.GetHashCode();
                if (this.SectionType != null)
                    hashCode = hashCode * 59 + this.SectionType.GetHashCode();
                if (this.CollectionType != null)
                    hashCode = hashCode * 59 + this.CollectionType.GetHashCode();
                if (this.ViewType != null)
                    hashCode = hashCode * 59 + this.ViewType.GetHashCode();
                if (this.Monitor != null)
                    hashCode = hashCode * 59 + this.Monitor.GetHashCode();
                if (this.CardSizeOffset != null)
                    hashCode = hashCode * 59 + this.CardSizeOffset.GetHashCode();
                if (this.ScrollDirection != null)
                    hashCode = hashCode * 59 + this.ScrollDirection.GetHashCode();
                if (this.ParentItem != null)
                    hashCode = hashCode * 59 + this.ParentItem.GetHashCode();
                return hashCode;
            }
        }

    }
}
