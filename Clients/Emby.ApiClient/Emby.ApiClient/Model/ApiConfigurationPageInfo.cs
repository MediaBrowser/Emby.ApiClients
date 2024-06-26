// <copyright file="ApiConfigurationPageInfo.cs" company="Emby LLC">
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
    /// ApiConfigurationPageInfo.
    /// </summary>
    /// <seealso>Emby.Web.Api.ConfigurationPageInfo</seealso>
    public partial class ApiConfigurationPageInfo :  IEquatable<ApiConfigurationPageInfo>
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="ApiConfigurationPageInfo" /> class.
        /// </summary>
        public ApiConfigurationPageInfo()
        {
        }
        
        /// <summary>
        /// Gets or Sets Name
        /// </summary>
        /// <value>The Name.</value>
        public string Name { get; set; }

        /// <summary>
        /// Gets or Sets EnableInMainMenu
        /// </summary>
        /// <value>The EnableInMainMenu.</value>
        public bool? EnableInMainMenu { get; set; }

        /// <summary>
        /// Gets or Sets EnableInUserMenu
        /// </summary>
        /// <value>The EnableInUserMenu.</value>
        public bool? EnableInUserMenu { get; set; }

        /// <summary>
        /// Gets or Sets FeatureId
        /// </summary>
        /// <value>The FeatureId.</value>
        public string FeatureId { get; set; }

        /// <summary>
        /// Gets or Sets MenuSection
        /// </summary>
        /// <value>The MenuSection.</value>
        public string MenuSection { get; set; }

        /// <summary>
        /// Gets or Sets MenuIcon
        /// </summary>
        /// <value>The MenuIcon.</value>
        public string MenuIcon { get; set; }

        /// <summary>
        /// Gets or Sets DisplayName
        /// </summary>
        /// <value>The DisplayName.</value>
        public string DisplayName { get; set; }

        /// <summary>
        /// Gets or Sets ConfigurationPageType
        /// </summary>
        /// <value>The ConfigurationPageType.</value>
        public PluginsConfigurationPageType ConfigurationPageType { get; set; }

        /// <summary>
        /// Gets or Sets PluginId
        /// </summary>
        /// <value>The PluginId.</value>
        public string PluginId { get; set; }

        /// <summary>
        /// Gets or Sets Href
        /// </summary>
        /// <value>The Href.</value>
        public string Href { get; set; }

        /// <summary>
        /// Gets or Sets NavMenuId
        /// </summary>
        /// <value>The NavMenuId.</value>
        public string NavMenuId { get; set; }

        /// <summary>
        /// Gets or Sets Plugin
        /// </summary>
        /// <value>The Plugin.</value>
        public CommonPluginsIPlugin Plugin { get; set; }

        /// <summary>
        /// Gets or Sets Translations
        /// </summary>
        /// <value>The Translations.</value>
        public List<string> Translations { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class ApiConfigurationPageInfo {\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  EnableInMainMenu: ").Append(EnableInMainMenu).Append("\n");
            sb.Append("  EnableInUserMenu: ").Append(EnableInUserMenu).Append("\n");
            sb.Append("  FeatureId: ").Append(FeatureId).Append("\n");
            sb.Append("  MenuSection: ").Append(MenuSection).Append("\n");
            sb.Append("  MenuIcon: ").Append(MenuIcon).Append("\n");
            sb.Append("  DisplayName: ").Append(DisplayName).Append("\n");
            sb.Append("  ConfigurationPageType: ").Append(ConfigurationPageType).Append("\n");
            sb.Append("  PluginId: ").Append(PluginId).Append("\n");
            sb.Append("  Href: ").Append(Href).Append("\n");
            sb.Append("  NavMenuId: ").Append(NavMenuId).Append("\n");
            sb.Append("  Plugin: ").Append(Plugin).Append("\n");
            sb.Append("  Translations: ").Append(Translations).Append("\n");
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
            return this.Equals(input as ApiConfigurationPageInfo);
        }

        /// <summary>
        /// Returns true if ApiConfigurationPageInfo instances are equal
        /// </summary>
        /// <param name="input">Instance of ApiConfigurationPageInfo to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(ApiConfigurationPageInfo input)
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
                    this.EnableInMainMenu == input.EnableInMainMenu ||
                    (this.EnableInMainMenu != null &&
                    this.EnableInMainMenu.Equals(input.EnableInMainMenu))
                ) && 
                (
                    this.EnableInUserMenu == input.EnableInUserMenu ||
                    (this.EnableInUserMenu != null &&
                    this.EnableInUserMenu.Equals(input.EnableInUserMenu))
                ) && 
                (
                    this.FeatureId == input.FeatureId ||
                    (this.FeatureId != null &&
                    this.FeatureId.Equals(input.FeatureId))
                ) && 
                (
                    this.MenuSection == input.MenuSection ||
                    (this.MenuSection != null &&
                    this.MenuSection.Equals(input.MenuSection))
                ) && 
                (
                    this.MenuIcon == input.MenuIcon ||
                    (this.MenuIcon != null &&
                    this.MenuIcon.Equals(input.MenuIcon))
                ) && 
                (
                    this.DisplayName == input.DisplayName ||
                    (this.DisplayName != null &&
                    this.DisplayName.Equals(input.DisplayName))
                ) && 
                (
                    this.ConfigurationPageType == input.ConfigurationPageType ||
                    (this.ConfigurationPageType != null &&
                    this.ConfigurationPageType.Equals(input.ConfigurationPageType))
                ) && 
                (
                    this.PluginId == input.PluginId ||
                    (this.PluginId != null &&
                    this.PluginId.Equals(input.PluginId))
                ) && 
                (
                    this.Href == input.Href ||
                    (this.Href != null &&
                    this.Href.Equals(input.Href))
                ) && 
                (
                    this.NavMenuId == input.NavMenuId ||
                    (this.NavMenuId != null &&
                    this.NavMenuId.Equals(input.NavMenuId))
                ) && 
                (
                    this.Plugin == input.Plugin ||
                    (this.Plugin != null &&
                    this.Plugin.Equals(input.Plugin))
                ) && 
                (
                    this.Translations == input.Translations ||
                    this.Translations != null &&
                    input.Translations != null &&
                    this.Translations.SequenceEqual(input.Translations)
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
                if (this.EnableInMainMenu != null)
                    hashCode = hashCode * 59 + this.EnableInMainMenu.GetHashCode();
                if (this.EnableInUserMenu != null)
                    hashCode = hashCode * 59 + this.EnableInUserMenu.GetHashCode();
                if (this.FeatureId != null)
                    hashCode = hashCode * 59 + this.FeatureId.GetHashCode();
                if (this.MenuSection != null)
                    hashCode = hashCode * 59 + this.MenuSection.GetHashCode();
                if (this.MenuIcon != null)
                    hashCode = hashCode * 59 + this.MenuIcon.GetHashCode();
                if (this.DisplayName != null)
                    hashCode = hashCode * 59 + this.DisplayName.GetHashCode();
                if (this.ConfigurationPageType != null)
                    hashCode = hashCode * 59 + this.ConfigurationPageType.GetHashCode();
                if (this.PluginId != null)
                    hashCode = hashCode * 59 + this.PluginId.GetHashCode();
                if (this.Href != null)
                    hashCode = hashCode * 59 + this.Href.GetHashCode();
                if (this.NavMenuId != null)
                    hashCode = hashCode * 59 + this.NavMenuId.GetHashCode();
                if (this.Plugin != null)
                    hashCode = hashCode * 59 + this.Plugin.GetHashCode();
                if (this.Translations != null)
                    hashCode = hashCode * 59 + this.Translations.GetHashCode();
                return hashCode;
            }
        }
    }
}