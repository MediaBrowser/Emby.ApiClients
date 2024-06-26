// <copyright file="VideoHlsServiceApi.cs" company="Emby LLC">
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
	
    /// <summary>
    /// Provides a collection of service methods to interact with the API endpoints.
    /// </summary>
    public partial class VideoHlsServiceApi : IApiAccessor
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="VideoHlsServiceApi"/> class.
        /// </summary>
        /// <returns></returns>
        public VideoHlsServiceApi(ApiClient apiClient)
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
        /// 
        /// </summary>
        /// <remarks>
        /// Requires authentication as user
        /// </remarks>
        /// <param name="segmentContainer"></param>
        /// <param name="segmentId"></param>
        /// <param name="id"></param>
        /// <param name="playlistId"></param>
        /// <returns>Task of ApiResponse</returns>
        public async Task<RestResponse<Object>> GetAudioByIdHlsByPlaylistidBySegmentidBySegmentcontainer (string segmentContainer, string segmentId, string id, string playlistId)
        {
            // verify the required parameter 'segmentContainer' is set
            if (segmentContainer == null)
            {
                throw new ApiException("Missing required parameter 'segmentContainer' when calling VideoHlsServiceApi->GetAudioByIdHlsByPlaylistidBySegmentidBySegmentcontainer");
            }
            
            // verify the required parameter 'segmentId' is set
            if (segmentId == null)
            {
                throw new ApiException("Missing required parameter 'segmentId' when calling VideoHlsServiceApi->GetAudioByIdHlsByPlaylistidBySegmentidBySegmentcontainer");
            }
            
            // verify the required parameter 'id' is set
            if (id == null)
            {
                throw new ApiException("Missing required parameter 'id' when calling VideoHlsServiceApi->GetAudioByIdHlsByPlaylistidBySegmentidBySegmentcontainer");
            }
            
            // verify the required parameter 'playlistId' is set
            if (playlistId == null)
            {
                throw new ApiException("Missing required parameter 'playlistId' when calling VideoHlsServiceApi->GetAudioByIdHlsByPlaylistidBySegmentidBySegmentcontainer");
            }
            
            var request = new RestRequest("/Audio/{Id}/hls/{PlaylistId}/{SegmentId}.{SegmentContainer}", Method.Get);

            if (segmentContainer != null)
            {
                request.AddParameter("SegmentContainer", this.ApiClient.ParameterToString(segmentContainer), ParameterType.UrlSegment);
            }

            if (segmentId != null)
            {
                request.AddParameter("SegmentId", this.ApiClient.ParameterToString(segmentId), ParameterType.UrlSegment);
            }

            if (id != null)
            {
                request.AddParameter("Id", this.ApiClient.ParameterToString(id), ParameterType.UrlSegment);
            }

            if (playlistId != null)
            {
                request.AddParameter("PlaylistId", this.ApiClient.ParameterToString(playlistId), ParameterType.UrlSegment);
            }

            // make the HTTP request
            var localVarResponse = await this.ApiClient.RestClient.ExecuteAsync<Object>(request).ConfigureAwait(false);
            return localVarResponse;
        }

        /// <summary>
        /// 
        /// </summary>
        /// <remarks>
        /// Requires authentication as user
        /// </remarks>
        /// <param name="segmentContainer"></param>
        /// <param name="segmentId"></param>
        /// <param name="id"></param>
        /// <param name="playlistId"></param>
        /// <returns>Task of ApiResponse</returns>
        public async Task<RestResponse<Object>> GetVideosByIdHlsByPlaylistidBySegmentidBySegmentcontainer (string segmentContainer, string segmentId, string id, string playlistId)
        {
            // verify the required parameter 'segmentContainer' is set
            if (segmentContainer == null)
            {
                throw new ApiException("Missing required parameter 'segmentContainer' when calling VideoHlsServiceApi->GetVideosByIdHlsByPlaylistidBySegmentidBySegmentcontainer");
            }
            
            // verify the required parameter 'segmentId' is set
            if (segmentId == null)
            {
                throw new ApiException("Missing required parameter 'segmentId' when calling VideoHlsServiceApi->GetVideosByIdHlsByPlaylistidBySegmentidBySegmentcontainer");
            }
            
            // verify the required parameter 'id' is set
            if (id == null)
            {
                throw new ApiException("Missing required parameter 'id' when calling VideoHlsServiceApi->GetVideosByIdHlsByPlaylistidBySegmentidBySegmentcontainer");
            }
            
            // verify the required parameter 'playlistId' is set
            if (playlistId == null)
            {
                throw new ApiException("Missing required parameter 'playlistId' when calling VideoHlsServiceApi->GetVideosByIdHlsByPlaylistidBySegmentidBySegmentcontainer");
            }
            
            var request = new RestRequest("/Videos/{Id}/hls/{PlaylistId}/{SegmentId}.{SegmentContainer}", Method.Get);

            if (segmentContainer != null)
            {
                request.AddParameter("SegmentContainer", this.ApiClient.ParameterToString(segmentContainer), ParameterType.UrlSegment);
            }

            if (segmentId != null)
            {
                request.AddParameter("SegmentId", this.ApiClient.ParameterToString(segmentId), ParameterType.UrlSegment);
            }

            if (id != null)
            {
                request.AddParameter("Id", this.ApiClient.ParameterToString(id), ParameterType.UrlSegment);
            }

            if (playlistId != null)
            {
                request.AddParameter("PlaylistId", this.ApiClient.ParameterToString(playlistId), ParameterType.UrlSegment);
            }

            // make the HTTP request
            var localVarResponse = await this.ApiClient.RestClient.ExecuteAsync<Object>(request).ConfigureAwait(false);
            return localVarResponse;
        }

    }
}
