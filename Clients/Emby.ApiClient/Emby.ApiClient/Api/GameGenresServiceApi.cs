// <copyright file="GameGenresServiceApi.cs" company="Emby LLC">
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
    public partial class GameGenresServiceApi : IApiAccessor
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="GameGenresServiceApi"/> class.
        /// </summary>
        /// <returns></returns>
        public GameGenresServiceApi(ApiClient apiClient)
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
        /// Gets all Game genres from a given item, folder, or the entire library
        /// </summary>
        /// <remarks>
        /// Requires authentication as user
        /// </remarks>
        /// <param name="artistType">Artist or AlbumArtist (optional)</param>
        /// <param name="maxOfficialRating">Optional filter by maximum official rating (PG, PG-13, TV-MA, etc). (optional)</param>
        /// <param name="hasThemeSong">Optional filter by items with theme songs. (optional)</param>
        /// <param name="hasThemeVideo">Optional filter by items with theme videos. (optional)</param>
        /// <param name="hasSubtitles">Optional filter by items with subtitles. (optional)</param>
        /// <param name="hasSpecialFeature">Optional filter by items with special features. (optional)</param>
        /// <param name="hasTrailer">Optional filter by items with trailers. (optional)</param>
        /// <param name="isSpecialSeason">Optional. Filter by special season. (optional)</param>
        /// <param name="adjacentTo">Optional. Return items that are siblings of a supplied item. (optional)</param>
        /// <param name="startItemId">Optional. Skip through the list until a given item is found. (optional)</param>
        /// <param name="minIndexNumber">Optional filter by minimum index number. (optional)</param>
        /// <param name="minStartDate">Optional. The minimum premiere date. Format &#x3D; ISO (optional)</param>
        /// <param name="maxStartDate">Optional. The maximum premiere date. Format &#x3D; ISO (optional)</param>
        /// <param name="minEndDate">Optional. The minimum premiere date. Format &#x3D; ISO (optional)</param>
        /// <param name="maxEndDate">Optional. The maximum premiere date. Format &#x3D; ISO (optional)</param>
        /// <param name="minPlayers">Optional filter by minimum number of game players. (optional)</param>
        /// <param name="maxPlayers">Optional filter by maximum number of game players. (optional)</param>
        /// <param name="parentIndexNumber">Optional filter by parent index number. (optional)</param>
        /// <param name="hasParentalRating">Optional filter by items that have or do not have a parental rating (optional)</param>
        /// <param name="isHD">Optional filter by items that are HD or not. (optional)</param>
        /// <param name="isUnaired">Optional filter by items that are unaired episodes or not. (optional)</param>
        /// <param name="minCommunityRating">Optional filter by minimum community rating. (optional)</param>
        /// <param name="minCriticRating">Optional filter by minimum critic rating. (optional)</param>
        /// <param name="airedDuringSeason">Gets all episodes that aired during a season, including specials. (optional)</param>
        /// <param name="minPremiereDate">Optional. The minimum premiere date. Format &#x3D; ISO (optional)</param>
        /// <param name="minDateLastSaved">Optional. The minimum premiere date. Format &#x3D; ISO (optional)</param>
        /// <param name="minDateLastSavedForUser">Optional. The minimum premiere date. Format &#x3D; ISO (optional)</param>
        /// <param name="maxPremiereDate">Optional. The maximum premiere date. Format &#x3D; ISO (optional)</param>
        /// <param name="hasOverview">Optional filter by items that have an overview or not. (optional)</param>
        /// <param name="hasImdbId">Optional filter by items that have an imdb id or not. (optional)</param>
        /// <param name="hasTmdbId">Optional filter by items that have a tmdb id or not. (optional)</param>
        /// <param name="hasTvdbId">Optional filter by items that have a tvdb id or not. (optional)</param>
        /// <param name="excludeItemIds">Optional. If specified, results will be filtered by exxcluding item ids. This allows multiple, comma delimeted. (optional)</param>
        /// <param name="startIndex">Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)</param>
        /// <param name="limit">Optional. The maximum number of records to return (optional)</param>
        /// <param name="recursive">When searching within folders, this determines whether or not the search will be recursive. true/false (optional)</param>
        /// <param name="searchTerm">Enter a search term to perform a search request (optional)</param>
        /// <param name="sortOrder">Sort Order - Ascending,Descending (optional)</param>
        /// <param name="parentId">Specify this to localize the search to a specific item or folder. Omit to use the root (optional)</param>
        /// <param name="fields">Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines (optional)</param>
        /// <param name="excludeItemTypes">Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)</param>
        /// <param name="includeItemTypes">Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)</param>
        /// <param name="anyProviderIdEquals">Optional. If specified, result will be filtered to contain only items which match at least one of the specified IDs. Each provider ID must be in the form &#x27;prov.id&#x27;, e.g. &#x27;imdb.tt123456&#x27;. This allows multiple, comma delimeted value pairs. (optional)</param>
        /// <param name="filters">Optional. Specify additional filters to apply. This allows multiple, comma delimeted. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes (optional)</param>
        /// <param name="isFavorite">Optional filter by items that are marked as favorite, or not. (optional)</param>
        /// <param name="isMovie">Optional filter for movies. (optional)</param>
        /// <param name="isSeries">Optional filter for series. (optional)</param>
        /// <param name="isFolder">Optional filter for folders. (optional)</param>
        /// <param name="isNews">Optional filter for news. (optional)</param>
        /// <param name="isKids">Optional filter for kids. (optional)</param>
        /// <param name="isSports">Optional filter for sports. (optional)</param>
        /// <param name="isNew">Optional filter for IsNew. (optional)</param>
        /// <param name="isPremiere">Optional filter for IsPremiere. (optional)</param>
        /// <param name="isNewOrPremiere">Optional filter for IsNewOrPremiere. (optional)</param>
        /// <param name="isRepeat">Optional filter for IsRepeat. (optional)</param>
        /// <param name="projectToMedia">ProjectToMedia (optional)</param>
        /// <param name="mediaTypes">Optional filter by MediaType. Allows multiple, comma delimited. (optional)</param>
        /// <param name="imageTypes">Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited. (optional)</param>
        /// <param name="sortBy">Optional. Specify one or more sort orders, comma delimeted. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime (optional)</param>
        /// <param name="isPlayed">Optional filter by items that are played, or not. (optional)</param>
        /// <param name="genres">Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimeted. (optional)</param>
        /// <param name="officialRatings">Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimeted. (optional)</param>
        /// <param name="tags">Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. (optional)</param>
        /// <param name="excludeTags">Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. (optional)</param>
        /// <param name="years">Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimeted. (optional)</param>
        /// <param name="enableImages">Optional, include image information in output (optional)</param>
        /// <param name="enableUserData">Optional, include user data (optional)</param>
        /// <param name="imageTypeLimit">Optional, the max number of images to return, per image type (optional)</param>
        /// <param name="enableImageTypes">Optional. The image types to include in the output. (optional)</param>
        /// <param name="person">Optional. If specified, results will be filtered to include only those containing the specified person. (optional)</param>
        /// <param name="personIds">Optional. If specified, results will be filtered to include only those containing the specified person. (optional)</param>
        /// <param name="personTypes">Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited (optional)</param>
        /// <param name="studios">Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. (optional)</param>
        /// <param name="studioIds">Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. (optional)</param>
        /// <param name="artists">Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. (optional)</param>
        /// <param name="artistIds">Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. (optional)</param>
        /// <param name="albums">Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimeted. (optional)</param>
        /// <param name="ids">Optional. If specific items are needed, specify a list of item id&#x27;s to retrieve. This allows multiple, comma delimited. (optional)</param>
        /// <param name="videoTypes">Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimeted. (optional)</param>
        /// <param name="containers">Optional filter by Container. Allows multiple, comma delimeted. (optional)</param>
        /// <param name="audioCodecs">Optional filter by AudioCodec. Allows multiple, comma delimeted. (optional)</param>
        /// <param name="audioLayouts">Optional filter by AudioLayout. Allows multiple, comma delimeted. (optional)</param>
        /// <param name="videoCodecs">Optional filter by VideoCodec. Allows multiple, comma delimeted. (optional)</param>
        /// <param name="extendedVideoTypes">Optional filter by ExtendedVideoType. Allows multiple, comma delimeted. (optional)</param>
        /// <param name="subtitleCodecs">Optional filter by SubtitleCodec. Allows multiple, comma delimeted. (optional)</param>
        /// <param name="path">Optional filter by Path. (optional)</param>
        /// <param name="userId">User Id (optional)</param>
        /// <param name="minOfficialRating">Optional filter by minimum official rating (PG, PG-13, TV-MA, etc). (optional)</param>
        /// <param name="isLocked">Optional filter by items that are locked. (optional)</param>
        /// <param name="isPlaceHolder">Optional filter by items that are placeholders (optional)</param>
        /// <param name="hasOfficialRating">Optional filter by items that have official ratings (optional)</param>
        /// <param name="groupItemsIntoCollections">Whether or not to hide items behind their boxsets. (optional)</param>
        /// <param name="is3D">Optional filter by items that are 3D, or not. (optional)</param>
        /// <param name="seriesStatus">Optional filter by Series Status. Allows multiple, comma delimeted. (optional)</param>
        /// <param name="nameStartsWithOrGreater">Optional filter by items whose name is sorted equally or greater than a given input string. (optional)</param>
        /// <param name="artistStartsWithOrGreater">Optional filter by items whose name is sorted equally or greater than a given input string. (optional)</param>
        /// <param name="albumArtistStartsWithOrGreater">Optional filter by items whose name is sorted equally or greater than a given input string. (optional)</param>
        /// <param name="nameStartsWith">Optional filter by items whose name is sorted equally than a given input string. (optional)</param>
        /// <param name="nameLessThan">Optional filter by items whose name is equally or lesser than a given input string. (optional)</param>
        /// <returns>Task of ApiResponse (QueryResultBaseItemDto)</returns>
        public async Task<RestResponse<QueryResultBaseItemDto>> GetGamegenres (string artistType, string maxOfficialRating, bool? hasThemeSong, bool? hasThemeVideo, bool? hasSubtitles, bool? hasSpecialFeature, bool? hasTrailer, bool? isSpecialSeason, string adjacentTo, string startItemId, int? minIndexNumber, string minStartDate, string maxStartDate, string minEndDate, string maxEndDate, int? minPlayers, int? maxPlayers, int? parentIndexNumber, bool? hasParentalRating, bool? isHD, bool? isUnaired, double? minCommunityRating, double? minCriticRating, int? airedDuringSeason, string minPremiereDate, string minDateLastSaved, string minDateLastSavedForUser, string maxPremiereDate, bool? hasOverview, bool? hasImdbId, bool? hasTmdbId, bool? hasTvdbId, string excludeItemIds, int? startIndex, int? limit, bool? recursive, string searchTerm, string sortOrder, string parentId, string fields, string excludeItemTypes, string includeItemTypes, string anyProviderIdEquals, string filters, bool? isFavorite, bool? isMovie, bool? isSeries, bool? isFolder, bool? isNews, bool? isKids, bool? isSports, bool? isNew, bool? isPremiere, bool? isNewOrPremiere, bool? isRepeat, bool? projectToMedia, string mediaTypes, string imageTypes, string sortBy, bool? isPlayed, string genres, string officialRatings, string tags, string excludeTags, string years, bool? enableImages, bool? enableUserData, int? imageTypeLimit, string enableImageTypes, string person, string personIds, string personTypes, string studios, string studioIds, string artists, string artistIds, string albums, string ids, string videoTypes, string containers, string audioCodecs, string audioLayouts, string videoCodecs, string extendedVideoTypes, string subtitleCodecs, string path, string userId, string minOfficialRating, bool? isLocked, bool? isPlaceHolder, bool? hasOfficialRating, bool? groupItemsIntoCollections, bool? is3D, string seriesStatus, string nameStartsWithOrGreater, string artistStartsWithOrGreater, string albumArtistStartsWithOrGreater, string nameStartsWith, string nameLessThan)
        {
            var request = new RestRequest("/GameGenres", Method.Get);

            if (artistType != null)
            {
                request.AddQueryParameter("ArtistType", this.ApiClient.ParameterToString(artistType));
            }

            if (maxOfficialRating != null)
            {
                request.AddQueryParameter("MaxOfficialRating", this.ApiClient.ParameterToString(maxOfficialRating));
            }

            if (hasThemeSong != null)
            {
                request.AddQueryParameter("HasThemeSong", this.ApiClient.ParameterToString(hasThemeSong));
            }

            if (hasThemeVideo != null)
            {
                request.AddQueryParameter("HasThemeVideo", this.ApiClient.ParameterToString(hasThemeVideo));
            }

            if (hasSubtitles != null)
            {
                request.AddQueryParameter("HasSubtitles", this.ApiClient.ParameterToString(hasSubtitles));
            }

            if (hasSpecialFeature != null)
            {
                request.AddQueryParameter("HasSpecialFeature", this.ApiClient.ParameterToString(hasSpecialFeature));
            }

            if (hasTrailer != null)
            {
                request.AddQueryParameter("HasTrailer", this.ApiClient.ParameterToString(hasTrailer));
            }

            if (isSpecialSeason != null)
            {
                request.AddQueryParameter("IsSpecialSeason", this.ApiClient.ParameterToString(isSpecialSeason));
            }

            if (adjacentTo != null)
            {
                request.AddQueryParameter("AdjacentTo", this.ApiClient.ParameterToString(adjacentTo));
            }

            if (startItemId != null)
            {
                request.AddQueryParameter("StartItemId", this.ApiClient.ParameterToString(startItemId));
            }

            if (minIndexNumber != null)
            {
                request.AddQueryParameter("MinIndexNumber", this.ApiClient.ParameterToString(minIndexNumber));
            }

            if (minStartDate != null)
            {
                request.AddQueryParameter("MinStartDate", this.ApiClient.ParameterToString(minStartDate));
            }

            if (maxStartDate != null)
            {
                request.AddQueryParameter("MaxStartDate", this.ApiClient.ParameterToString(maxStartDate));
            }

            if (minEndDate != null)
            {
                request.AddQueryParameter("MinEndDate", this.ApiClient.ParameterToString(minEndDate));
            }

            if (maxEndDate != null)
            {
                request.AddQueryParameter("MaxEndDate", this.ApiClient.ParameterToString(maxEndDate));
            }

            if (minPlayers != null)
            {
                request.AddQueryParameter("MinPlayers", this.ApiClient.ParameterToString(minPlayers));
            }

            if (maxPlayers != null)
            {
                request.AddQueryParameter("MaxPlayers", this.ApiClient.ParameterToString(maxPlayers));
            }

            if (parentIndexNumber != null)
            {
                request.AddQueryParameter("ParentIndexNumber", this.ApiClient.ParameterToString(parentIndexNumber));
            }

            if (hasParentalRating != null)
            {
                request.AddQueryParameter("HasParentalRating", this.ApiClient.ParameterToString(hasParentalRating));
            }

            if (isHD != null)
            {
                request.AddQueryParameter("IsHD", this.ApiClient.ParameterToString(isHD));
            }

            if (isUnaired != null)
            {
                request.AddQueryParameter("IsUnaired", this.ApiClient.ParameterToString(isUnaired));
            }

            if (minCommunityRating != null)
            {
                request.AddQueryParameter("MinCommunityRating", this.ApiClient.ParameterToString(minCommunityRating));
            }

            if (minCriticRating != null)
            {
                request.AddQueryParameter("MinCriticRating", this.ApiClient.ParameterToString(minCriticRating));
            }

            if (airedDuringSeason != null)
            {
                request.AddQueryParameter("AiredDuringSeason", this.ApiClient.ParameterToString(airedDuringSeason));
            }

            if (minPremiereDate != null)
            {
                request.AddQueryParameter("MinPremiereDate", this.ApiClient.ParameterToString(minPremiereDate));
            }

            if (minDateLastSaved != null)
            {
                request.AddQueryParameter("MinDateLastSaved", this.ApiClient.ParameterToString(minDateLastSaved));
            }

            if (minDateLastSavedForUser != null)
            {
                request.AddQueryParameter("MinDateLastSavedForUser", this.ApiClient.ParameterToString(minDateLastSavedForUser));
            }

            if (maxPremiereDate != null)
            {
                request.AddQueryParameter("MaxPremiereDate", this.ApiClient.ParameterToString(maxPremiereDate));
            }

            if (hasOverview != null)
            {
                request.AddQueryParameter("HasOverview", this.ApiClient.ParameterToString(hasOverview));
            }

            if (hasImdbId != null)
            {
                request.AddQueryParameter("HasImdbId", this.ApiClient.ParameterToString(hasImdbId));
            }

            if (hasTmdbId != null)
            {
                request.AddQueryParameter("HasTmdbId", this.ApiClient.ParameterToString(hasTmdbId));
            }

            if (hasTvdbId != null)
            {
                request.AddQueryParameter("HasTvdbId", this.ApiClient.ParameterToString(hasTvdbId));
            }

            if (excludeItemIds != null)
            {
                request.AddQueryParameter("ExcludeItemIds", this.ApiClient.ParameterToString(excludeItemIds));
            }

            if (startIndex != null)
            {
                request.AddQueryParameter("StartIndex", this.ApiClient.ParameterToString(startIndex));
            }

            if (limit != null)
            {
                request.AddQueryParameter("Limit", this.ApiClient.ParameterToString(limit));
            }

            if (recursive != null)
            {
                request.AddQueryParameter("Recursive", this.ApiClient.ParameterToString(recursive));
            }

            if (searchTerm != null)
            {
                request.AddQueryParameter("SearchTerm", this.ApiClient.ParameterToString(searchTerm));
            }

            if (sortOrder != null)
            {
                request.AddQueryParameter("SortOrder", this.ApiClient.ParameterToString(sortOrder));
            }

            if (parentId != null)
            {
                request.AddQueryParameter("ParentId", this.ApiClient.ParameterToString(parentId));
            }

            if (fields != null)
            {
                request.AddQueryParameter("Fields", this.ApiClient.ParameterToString(fields));
            }

            if (excludeItemTypes != null)
            {
                request.AddQueryParameter("ExcludeItemTypes", this.ApiClient.ParameterToString(excludeItemTypes));
            }

            if (includeItemTypes != null)
            {
                request.AddQueryParameter("IncludeItemTypes", this.ApiClient.ParameterToString(includeItemTypes));
            }

            if (anyProviderIdEquals != null)
            {
                request.AddQueryParameter("AnyProviderIdEquals", this.ApiClient.ParameterToString(anyProviderIdEquals));
            }

            if (filters != null)
            {
                request.AddQueryParameter("Filters", this.ApiClient.ParameterToString(filters));
            }

            if (isFavorite != null)
            {
                request.AddQueryParameter("IsFavorite", this.ApiClient.ParameterToString(isFavorite));
            }

            if (isMovie != null)
            {
                request.AddQueryParameter("IsMovie", this.ApiClient.ParameterToString(isMovie));
            }

            if (isSeries != null)
            {
                request.AddQueryParameter("IsSeries", this.ApiClient.ParameterToString(isSeries));
            }

            if (isFolder != null)
            {
                request.AddQueryParameter("IsFolder", this.ApiClient.ParameterToString(isFolder));
            }

            if (isNews != null)
            {
                request.AddQueryParameter("IsNews", this.ApiClient.ParameterToString(isNews));
            }

            if (isKids != null)
            {
                request.AddQueryParameter("IsKids", this.ApiClient.ParameterToString(isKids));
            }

            if (isSports != null)
            {
                request.AddQueryParameter("IsSports", this.ApiClient.ParameterToString(isSports));
            }

            if (isNew != null)
            {
                request.AddQueryParameter("IsNew", this.ApiClient.ParameterToString(isNew));
            }

            if (isPremiere != null)
            {
                request.AddQueryParameter("IsPremiere", this.ApiClient.ParameterToString(isPremiere));
            }

            if (isNewOrPremiere != null)
            {
                request.AddQueryParameter("IsNewOrPremiere", this.ApiClient.ParameterToString(isNewOrPremiere));
            }

            if (isRepeat != null)
            {
                request.AddQueryParameter("IsRepeat", this.ApiClient.ParameterToString(isRepeat));
            }

            if (projectToMedia != null)
            {
                request.AddQueryParameter("ProjectToMedia", this.ApiClient.ParameterToString(projectToMedia));
            }

            if (mediaTypes != null)
            {
                request.AddQueryParameter("MediaTypes", this.ApiClient.ParameterToString(mediaTypes));
            }

            if (imageTypes != null)
            {
                request.AddQueryParameter("ImageTypes", this.ApiClient.ParameterToString(imageTypes));
            }

            if (sortBy != null)
            {
                request.AddQueryParameter("SortBy", this.ApiClient.ParameterToString(sortBy));
            }

            if (isPlayed != null)
            {
                request.AddQueryParameter("IsPlayed", this.ApiClient.ParameterToString(isPlayed));
            }

            if (genres != null)
            {
                request.AddQueryParameter("Genres", this.ApiClient.ParameterToString(genres));
            }

            if (officialRatings != null)
            {
                request.AddQueryParameter("OfficialRatings", this.ApiClient.ParameterToString(officialRatings));
            }

            if (tags != null)
            {
                request.AddQueryParameter("Tags", this.ApiClient.ParameterToString(tags));
            }

            if (excludeTags != null)
            {
                request.AddQueryParameter("ExcludeTags", this.ApiClient.ParameterToString(excludeTags));
            }

            if (years != null)
            {
                request.AddQueryParameter("Years", this.ApiClient.ParameterToString(years));
            }

            if (enableImages != null)
            {
                request.AddQueryParameter("EnableImages", this.ApiClient.ParameterToString(enableImages));
            }

            if (enableUserData != null)
            {
                request.AddQueryParameter("EnableUserData", this.ApiClient.ParameterToString(enableUserData));
            }

            if (imageTypeLimit != null)
            {
                request.AddQueryParameter("ImageTypeLimit", this.ApiClient.ParameterToString(imageTypeLimit));
            }

            if (enableImageTypes != null)
            {
                request.AddQueryParameter("EnableImageTypes", this.ApiClient.ParameterToString(enableImageTypes));
            }

            if (person != null)
            {
                request.AddQueryParameter("Person", this.ApiClient.ParameterToString(person));
            }

            if (personIds != null)
            {
                request.AddQueryParameter("PersonIds", this.ApiClient.ParameterToString(personIds));
            }

            if (personTypes != null)
            {
                request.AddQueryParameter("PersonTypes", this.ApiClient.ParameterToString(personTypes));
            }

            if (studios != null)
            {
                request.AddQueryParameter("Studios", this.ApiClient.ParameterToString(studios));
            }

            if (studioIds != null)
            {
                request.AddQueryParameter("StudioIds", this.ApiClient.ParameterToString(studioIds));
            }

            if (artists != null)
            {
                request.AddQueryParameter("Artists", this.ApiClient.ParameterToString(artists));
            }

            if (artistIds != null)
            {
                request.AddQueryParameter("ArtistIds", this.ApiClient.ParameterToString(artistIds));
            }

            if (albums != null)
            {
                request.AddQueryParameter("Albums", this.ApiClient.ParameterToString(albums));
            }

            if (ids != null)
            {
                request.AddQueryParameter("Ids", this.ApiClient.ParameterToString(ids));
            }

            if (videoTypes != null)
            {
                request.AddQueryParameter("VideoTypes", this.ApiClient.ParameterToString(videoTypes));
            }

            if (containers != null)
            {
                request.AddQueryParameter("Containers", this.ApiClient.ParameterToString(containers));
            }

            if (audioCodecs != null)
            {
                request.AddQueryParameter("AudioCodecs", this.ApiClient.ParameterToString(audioCodecs));
            }

            if (audioLayouts != null)
            {
                request.AddQueryParameter("AudioLayouts", this.ApiClient.ParameterToString(audioLayouts));
            }

            if (videoCodecs != null)
            {
                request.AddQueryParameter("VideoCodecs", this.ApiClient.ParameterToString(videoCodecs));
            }

            if (extendedVideoTypes != null)
            {
                request.AddQueryParameter("ExtendedVideoTypes", this.ApiClient.ParameterToString(extendedVideoTypes));
            }

            if (subtitleCodecs != null)
            {
                request.AddQueryParameter("SubtitleCodecs", this.ApiClient.ParameterToString(subtitleCodecs));
            }

            if (path != null)
            {
                request.AddQueryParameter("Path", this.ApiClient.ParameterToString(path));
            }

            if (userId != null)
            {
                request.AddQueryParameter("UserId", this.ApiClient.ParameterToString(userId));
            }

            if (minOfficialRating != null)
            {
                request.AddQueryParameter("MinOfficialRating", this.ApiClient.ParameterToString(minOfficialRating));
            }

            if (isLocked != null)
            {
                request.AddQueryParameter("IsLocked", this.ApiClient.ParameterToString(isLocked));
            }

            if (isPlaceHolder != null)
            {
                request.AddQueryParameter("IsPlaceHolder", this.ApiClient.ParameterToString(isPlaceHolder));
            }

            if (hasOfficialRating != null)
            {
                request.AddQueryParameter("HasOfficialRating", this.ApiClient.ParameterToString(hasOfficialRating));
            }

            if (groupItemsIntoCollections != null)
            {
                request.AddQueryParameter("GroupItemsIntoCollections", this.ApiClient.ParameterToString(groupItemsIntoCollections));
            }

            if (is3D != null)
            {
                request.AddQueryParameter("Is3D", this.ApiClient.ParameterToString(is3D));
            }

            if (seriesStatus != null)
            {
                request.AddQueryParameter("SeriesStatus", this.ApiClient.ParameterToString(seriesStatus));
            }

            if (nameStartsWithOrGreater != null)
            {
                request.AddQueryParameter("NameStartsWithOrGreater", this.ApiClient.ParameterToString(nameStartsWithOrGreater));
            }

            if (artistStartsWithOrGreater != null)
            {
                request.AddQueryParameter("ArtistStartsWithOrGreater", this.ApiClient.ParameterToString(artistStartsWithOrGreater));
            }

            if (albumArtistStartsWithOrGreater != null)
            {
                request.AddQueryParameter("AlbumArtistStartsWithOrGreater", this.ApiClient.ParameterToString(albumArtistStartsWithOrGreater));
            }

            if (nameStartsWith != null)
            {
                request.AddQueryParameter("NameStartsWith", this.ApiClient.ParameterToString(nameStartsWith));
            }

            if (nameLessThan != null)
            {
                request.AddQueryParameter("NameLessThan", this.ApiClient.ParameterToString(nameLessThan));
            }

            // make the HTTP request
            var localVarResponse = await this.ApiClient.RestClient.ExecuteAsync<QueryResultBaseItemDto>(request).ConfigureAwait(false);
            return localVarResponse;
        }

        /// <summary>
        /// Gets a Game genre, by name
        /// </summary>
        /// <remarks>
        /// Requires authentication as user
        /// </remarks>
        /// <param name="name">The genre name</param>
        /// <param name="userId">Optional. Filter by user id, and attach user data (optional)</param>
        /// <returns>Task of ApiResponse (BaseItemDto)</returns>
        public async Task<RestResponse<BaseItemDto>> GetGamegenresByName (string name, string userId)
        {
            // verify the required parameter 'name' is set
            if (name == null)
            {
                throw new ApiException("Missing required parameter 'name' when calling GameGenresServiceApi->GetGamegenresByName");
            }
            
            var request = new RestRequest("/GameGenres/{Name}", Method.Get);

            if (name != null)
            {
                request.AddParameter("Name", this.ApiClient.ParameterToString(name), ParameterType.UrlSegment);
            }

            if (userId != null)
            {
                request.AddQueryParameter("UserId", this.ApiClient.ParameterToString(userId));
            }

            // make the HTTP request
            var localVarResponse = await this.ApiClient.RestClient.ExecuteAsync<BaseItemDto>(request).ConfigureAwait(false);
            return localVarResponse;
        }

    }
}
