//
// ItemCounts.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation


/** Class LibrarySummary   */

public struct ItemCounts: Codable {

    /** The movie count. */
    public var movieCount: Int?
    /** The series count. */
    public var seriesCount: Int?
    /** The episode count. */
    public var episodeCount: Int?
    /** The game count. */
    public var gameCount: Int?
    public var artistCount: Int?
    public var programCount: Int?
    /** The game system count. */
    public var gameSystemCount: Int?
    /** The trailer count. */
    public var trailerCount: Int?
    /** The song count. */
    public var songCount: Int?
    /** The album count. */
    public var albumCount: Int?
    /** The music video count. */
    public var musicVideoCount: Int?
    /** The box set count. */
    public var boxSetCount: Int?
    /** The book count. */
    public var bookCount: Int?
    public var itemCount: Int?

    public init(movieCount: Int? = nil, seriesCount: Int? = nil, episodeCount: Int? = nil, gameCount: Int? = nil, artistCount: Int? = nil, programCount: Int? = nil, gameSystemCount: Int? = nil, trailerCount: Int? = nil, songCount: Int? = nil, albumCount: Int? = nil, musicVideoCount: Int? = nil, boxSetCount: Int? = nil, bookCount: Int? = nil, itemCount: Int? = nil) {
        self.movieCount = movieCount
        self.seriesCount = seriesCount
        self.episodeCount = episodeCount
        self.gameCount = gameCount
        self.artistCount = artistCount
        self.programCount = programCount
        self.gameSystemCount = gameSystemCount
        self.trailerCount = trailerCount
        self.songCount = songCount
        self.albumCount = albumCount
        self.musicVideoCount = musicVideoCount
        self.boxSetCount = boxSetCount
        self.bookCount = bookCount
        self.itemCount = itemCount
    }

    public enum CodingKeys: String, CodingKey { 
        case movieCount = "MovieCount"
        case seriesCount = "SeriesCount"
        case episodeCount = "EpisodeCount"
        case gameCount = "GameCount"
        case artistCount = "ArtistCount"
        case programCount = "ProgramCount"
        case gameSystemCount = "GameSystemCount"
        case trailerCount = "TrailerCount"
        case songCount = "SongCount"
        case albumCount = "AlbumCount"
        case musicVideoCount = "MusicVideoCount"
        case boxSetCount = "BoxSetCount"
        case bookCount = "BookCount"
        case itemCount = "ItemCount"
    }

}