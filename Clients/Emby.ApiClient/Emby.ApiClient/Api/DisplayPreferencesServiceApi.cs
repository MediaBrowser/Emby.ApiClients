// <copyright file="DisplayPreferencesServiceApi.cs" company="Emby LLC">
// Emby.ApiClient. Autogenerated Code. No license applied. 
// </copyright>
// <autogenerated />
namespace Emby.ApiClient.Api
{
	using System;
	using System.Collections.Generic;
	using System.Collections.ObjectModel;
	using System.Linq;
    using System.Threading.Tasks;
	using RestSharp;
	using Emby.ApiClient.Client;
	using Emby.ApiClient.Model;

    /// <summary>
    /// Provides a collection of service methods to interact with the API endpoints.
    /// </summary>
    public partial class DisplayPreferencesServiceApi : IApiAccessor
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DisplayPreferencesServiceApi"/> class.
        /// </summary>
        /// <returns></returns>
        public DisplayPreferencesServiceApi(ApiClient apiClient)
        {
            this.ApiClient = apiClient;
        }

        /// <summary>
        /// Gets the base path of the API client.
        /// </summary>
        /// <value>The base path</value>
        public String GetBasePath()
        {
            return this.ApiClient.RestClient.Options.BaseUrl?.ToString();
        }

        /// <summary>Gets the ApiClient object</summary>
        /// <value>An instance of the ApiClient</value>
        public ApiClient ApiClient {get; }

        /// <summary>
        /// Gets a user&#x27;s display preferences for an item
        /// </summary>
        /// <remarks>
        /// Requires authentication as user
        /// </remarks>
        /// <param name="id">Item Id</param>
        /// <param name="userId">User Id</param>
        /// <param name="_client">Client</param>
        /// <returns>Task of ApiResponse (DisplayPreferences)</returns>
        public async Task<RestResponse<DisplayPreferences>> GetDisplaypreferencesById (string id, string userId, string _client)
        {
            // verify the required parameter 'id' is set
            if (id == null)
            {
                throw new ApiException("Missing required parameter 'id' when calling DisplayPreferencesServiceApi->GetDisplaypreferencesById");
            }
            
            // verify the required parameter 'userId' is set
            if (userId == null)
            {
                throw new ApiException("Missing required parameter 'userId' when calling DisplayPreferencesServiceApi->GetDisplaypreferencesById");
            }
            
            // verify the required parameter '_client' is set
            if (_client == null)
            {
                throw new ApiException("Missing required parameter '_client' when calling DisplayPreferencesServiceApi->GetDisplaypreferencesById");
            }
            
            var request = new RestRequest("/DisplayPreferences/{Id}", Method.Get);

            if (id != null)
            {
                request.AddParameter("Id", this.ApiClient.ParameterToString(id), ParameterType.UrlSegment);
            }

            if (userId != null)
            {
                request.AddQueryParameter("UserId", this.ApiClient.ParameterToString(userId));
            }

            if (_client != null)
            {
                request.AddQueryParameter("Client", this.ApiClient.ParameterToString(_client));
            }

            // make the HTTP request
            var localVarResponse = await this.ApiClient.RestClient.ExecuteAsync<DisplayPreferences>(request).ConfigureAwait(false);
            return localVarResponse;
        }

        /// <summary>
        /// Gets user settings
        /// </summary>
        /// <remarks>
        /// Requires authentication as user
        /// </remarks>
        /// <param name="userId">User Id</param>
        /// <returns>Task of ApiResponse (Dictionary&lt;string, string&gt;)</returns>
        public async Task<RestResponse<Dictionary<string, string>>> GetUsersettingsByUserid (string userId)
        {
            // verify the required parameter 'userId' is set
            if (userId == null)
            {
                throw new ApiException("Missing required parameter 'userId' when calling DisplayPreferencesServiceApi->GetUsersettingsByUserid");
            }
            
            var request = new RestRequest("/UserSettings/{UserId}", Method.Get);

            if (userId != null)
            {
                request.AddParameter("UserId", this.ApiClient.ParameterToString(userId), ParameterType.UrlSegment);
            }

            // make the HTTP request
            var localVarResponse = await this.ApiClient.RestClient.ExecuteAsync<Dictionary<string, string>>(request).ConfigureAwait(false);
            return localVarResponse;
        }

        /// <summary>
        /// Updates a user&#x27;s display preferences for an item
        /// </summary>
        /// <remarks>
        /// Requires authentication as user
        /// </remarks>
        /// <param name="body">DisplayPreferences: </param>
        /// <param name="userId">User Id</param>
        /// <param name="displayPreferencesId">DisplayPreferences Id</param>
        /// <returns>Task of ApiResponse</returns>
        public async Task<RestResponse<Object>> PostDisplaypreferencesByDisplaypreferencesid (DisplayPreferences body, string userId, string displayPreferencesId)
        {
            // verify the required parameter 'body' is set
            if (body == null)
            {
                throw new ApiException("Missing required parameter 'body' when calling DisplayPreferencesServiceApi->PostDisplaypreferencesByDisplaypreferencesid");
            }
            
            // verify the required parameter 'userId' is set
            if (userId == null)
            {
                throw new ApiException("Missing required parameter 'userId' when calling DisplayPreferencesServiceApi->PostDisplaypreferencesByDisplaypreferencesid");
            }
            
            // verify the required parameter 'displayPreferencesId' is set
            if (displayPreferencesId == null)
            {
                throw new ApiException("Missing required parameter 'displayPreferencesId' when calling DisplayPreferencesServiceApi->PostDisplaypreferencesByDisplaypreferencesid");
            }
            
            var request = new RestRequest("/DisplayPreferences/{DisplayPreferencesId}", Method.Post);

            if (displayPreferencesId != null)
            {
                request.AddParameter("DisplayPreferencesId", this.ApiClient.ParameterToString(displayPreferencesId), ParameterType.UrlSegment);
            }

            if (userId != null)
            {
                request.AddQueryParameter("UserId", this.ApiClient.ParameterToString(userId));
            }

            if (body != null)
            {
                request.AddJsonBody(body);
            }
            
            // make the HTTP request
            var localVarResponse = await this.ApiClient.RestClient.ExecuteAsync<Object>(request).ConfigureAwait(false);
            return localVarResponse;
        }

        /// <summary>
        /// Updates a user&#x27;s display preferences for an item
        /// </summary>
        /// <remarks>
        /// Requires authentication as user
        /// </remarks>
        /// <param name="body">UserSettings: </param>
        /// <param name="userId">User Id</param>
        /// <returns>Task of ApiResponse</returns>
        public async Task<RestResponse<Object>> PostUsersettingsByUserid (List<string> body, string userId)
        {
            // verify the required parameter 'body' is set
            if (body == null)
            {
                throw new ApiException("Missing required parameter 'body' when calling DisplayPreferencesServiceApi->PostUsersettingsByUserid");
            }
            
            // verify the required parameter 'userId' is set
            if (userId == null)
            {
                throw new ApiException("Missing required parameter 'userId' when calling DisplayPreferencesServiceApi->PostUsersettingsByUserid");
            }
            
            var request = new RestRequest("/UserSettings/{UserId}", Method.Post);

            if (userId != null)
            {
                request.AddParameter("UserId", this.ApiClient.ParameterToString(userId), ParameterType.UrlSegment);
            }

            if (body != null)
            {
                request.AddJsonBody(body);
            }
            
            // make the HTTP request
            var localVarResponse = await this.ApiClient.RestClient.ExecuteAsync<Object>(request).ConfigureAwait(false);
            return localVarResponse;
        }

        /// <summary>
        /// Updates a user&#x27;s display preferences for an item
        /// </summary>
        /// <remarks>
        /// Requires authentication as user
        /// </remarks>
        /// <param name="body">Binary stream</param>
        /// <param name="userId">User Id</param>
        /// <returns>Task of ApiResponse</returns>
        public async Task<RestResponse<Object>> PostUsersettingsByUseridPartial (Object body, string userId)
        {
            // verify the required parameter 'body' is set
            if (body == null)
            {
                throw new ApiException("Missing required parameter 'body' when calling DisplayPreferencesServiceApi->PostUsersettingsByUseridPartial");
            }
            
            // verify the required parameter 'userId' is set
            if (userId == null)
            {
                throw new ApiException("Missing required parameter 'userId' when calling DisplayPreferencesServiceApi->PostUsersettingsByUseridPartial");
            }
            
            var request = new RestRequest("/UserSettings/{UserId}/Partial", Method.Post);

            if (userId != null)
            {
                request.AddParameter("UserId", this.ApiClient.ParameterToString(userId), ParameterType.UrlSegment);
            }

            if (body != null)
            {
                request.AddJsonBody(body);
            }
            
            // make the HTTP request
            var localVarResponse = await this.ApiClient.RestClient.ExecuteAsync<Object>(request).ConfigureAwait(false);
            return localVarResponse;
        }

    }
}
