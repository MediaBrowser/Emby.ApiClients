// <auto-generated>
// Code generated by Microsoft (R) AutoRest Code Generator.
// Changes may cause incorrect behavior and will be lost if the code is
// regenerated.
// </auto-generated>

namespace EmbyClient.MsRest.Models
{
    using Newtonsoft.Json;
    using System.Linq;

    public partial class NameValuePair
    {
        /// <summary>
        /// Initializes a new instance of the NameValuePair class.
        /// </summary>
        public NameValuePair()
        {
            CustomInit();
        }

        /// <summary>
        /// Initializes a new instance of the NameValuePair class.
        /// </summary>
        public NameValuePair(string name = default(string), string value = default(string))
        {
            Name = name;
            Value = value;
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
        [JsonProperty(PropertyName = "Value")]
        public string Value { get; set; }

    }
}