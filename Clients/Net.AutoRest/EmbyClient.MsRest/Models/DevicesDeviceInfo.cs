// <auto-generated>
// Code generated by Microsoft (R) AutoRest Code Generator.
// Changes may cause incorrect behavior and will be lost if the code is
// regenerated.
// </auto-generated>

namespace EmbyClient.MsRest.Models
{
    using Newtonsoft.Json;
    using System.Linq;

    public partial class DevicesDeviceInfo
    {
        /// <summary>
        /// Initializes a new instance of the DevicesDeviceInfo class.
        /// </summary>
        public DevicesDeviceInfo()
        {
            CustomInit();
        }

        /// <summary>
        /// Initializes a new instance of the DevicesDeviceInfo class.
        /// </summary>
        public DevicesDeviceInfo(string name = default(string), string id = default(string), long? internalId = default(long?), string reportedDeviceId = default(string), string lastUserName = default(string), string appName = default(string), string appVersion = default(string), string lastUserId = default(string), System.DateTime? dateLastActivity = default(System.DateTime?), string iconUrl = default(string))
        {
            Name = name;
            Id = id;
            InternalId = internalId;
            ReportedDeviceId = reportedDeviceId;
            LastUserName = lastUserName;
            AppName = appName;
            AppVersion = appVersion;
            LastUserId = lastUserId;
            DateLastActivity = dateLastActivity;
            IconUrl = iconUrl;
            CustomInit();
        }

        /// <summary>
        /// An initialization method that performs custom operations like setting defaults
        /// </summary>
        partial void CustomInit();

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "Name")]
        public string Name { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "Id")]
        public string Id { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "InternalId")]
        public long? InternalId { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "ReportedDeviceId")]
        public string ReportedDeviceId { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "LastUserName")]
        public string LastUserName { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "AppName")]
        public string AppName { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "AppVersion")]
        public string AppVersion { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "LastUserId")]
        public string LastUserId { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "DateLastActivity")]
        public System.DateTime? DateLastActivity { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "IconUrl")]
        public string IconUrl { get; set; }

    }
}