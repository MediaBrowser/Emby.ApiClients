﻿// <copyright file="DeserializationInterceptor.cs" company="Emby LLC">
// Emby.ApiClient. Autogenerated Code. No license applied. 
// </copyright>

namespace Emby.ApiClient.Client.Serialization
{
    using RestSharp;
    using RestSharp.Interceptors;
    using System.Threading;
    using System.Threading.Tasks;

    /// <summary>
    /// Interceptor for deserialization.
    /// </summary>
    public class DeserializationInterceptor : Interceptor
    {
        /// <summary>
        /// Intercepts the request before deserialization, won't be called if using non-generic ExecuteAsync
        /// </summary>
        /// <param name="response">HttpResponseMessage as received from the remote server</param>
        /// <param name="cancellationToken">Cancellation token</param>
        public override ValueTask BeforeDeserialization(RestResponse response, CancellationToken cancellationToken)
        {
            if (!response.IsSuccessStatusCode)
            {
                // This is to avoid deserialization of an error response; required due to a flaw in RestSharp
                response.Request.RequestFormat = DataFormat.None;
            }

            return base.BeforeDeserialization(response, cancellationToken);
        }
    }
}
