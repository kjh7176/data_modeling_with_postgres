# Data Modeling with Postgres
This is the first project of Udacity's **Data Engineering Nanodegree**:mortar_board:.  
The purpose is to build an **ETL pipeline** transferring data from **JSON** to **Postgre database** Using **Python** and **SQL**

## Background
A startup called :musical_note:*Sparkify* wants to analyze the data they've been collecting on songs and user activity on their new music streaming app.  
The analytics team is particularly interested in understanding what songs users are listening to.  
Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.  

## ETL Pipeline
### 1. Extract from Dataset
- Song Dataset : **data/song_data**/A/B/C/TRABCEI128F424C983.json
```json
{
  "num_songs": 1, 
  "artist_id": "ARJIE2Y1187B994AB7", 
  "artist_latitude": null, 
  "artist_longitude": null, 
  "artist_location": "", 
  "artist_name": "Line Renaud", 
  "song_id": "SOUPIRU12A6D4FA1E1", 
  "title": "Der Kleine Dompfaff", 
  "duration": 152.92036, 
  "year": 0
}
```
- Log Dataset : **data/log_data**/2018/11/2018-11-12-events.json
```json
{
  "artist":"Barry Tuckwell\/Academy of St Martin-in-the-Fields\/Sir Neville Marriner",
  "auth":"Logged In",
  "firstName":"Celeste",
  "gender":"F",
  "itemInSession":1,
  "lastName":"Williams",
  "length":277.15873,
  "level":"free",
  "location":"Klamath Falls, OR",
  "method":"PUT",
  "page":"NextSong",
  "registration":1541077528796.0,
  "sessionId":438,
  "song":"Horn Concerto No. 4 in E flat K495: II. Romance (Andante cantabile)",
  "status":200,
  "ts":1541990264796,
  "userAgent":"\"Mozilla\/5.0 (Windows NT 6.1; WOW64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/37.0.2062.103 Safari\/537.36\"",
  "userId":"53"
 }
 ...
```
### 2. Transform Data and Load into Database
| Dataset(Song)      | Transformation | Table(songs) |
| :----: | :----: | :----: |
| song_id      | :x: | song_id       |
| title   |:x:| title        |
| artist_id   | :x:  | artist_id       |
| year   |:x:| year        |
| duration   | :x:|duration        |

| Dataset(Song)      | Transformation | Table(artists) |
| :----: | :----: | :----: |
| artist_id      | :x: | artist_id       |
| artist_name   |:x:| name        |
| artist_location   | :x:  | location       |
| artist_latitude   |:x:| latitude        |
| artist_longitude   | :x:|longitude        |

| Dataset(Log)      | Transformation | Table(time) |
| :----: | :----: | :----: |
| ts      | to_datetime | start_time       |
| ts.dt.hour   |:x:| hour        |
| ts.dt.day   | :x:  | day       |
| ts.dt.weekofyear   |:x:| week        |
| ts.dt.month   | :x:|month        |
| ts.dt.year   |:x:| year        |
| ts.dt.dayofweek   | :x:|weekday        |


| Dataset(Log)      | Transformation | Table(users) |
| :----: | :----: | :----: |
| userId      | :x: | user_id       |
| firstName   |:x:| first_name        |
| lastName   | :x:  | last_name       |
| gender   |:x:| gender        |
| level   | :x:|level        |

| Dataset(Log)      | Transformation | Table(songplays) |
| :----: | :----: | :----: |
| ts      | to_datetime | start_time       |
| userId   |:x:| user_id        |
| level   | :x:  | level       |
| :x:   | song_id FROM songs JOIN artists | song_id        |
| :x:   | artist_id FROM songs JOIN artists |artist_id        |
| song | column for SELECT WHERE | :x: |
| artist | column for SELECT WHERE | :x: |
| length | column for SELECT WHERE | :x: |
| sessionId   |:x:| session_id        |
| location   | :x:|location        |
| userAgent   | :x:|user_agent        |

### 3. Database Schema design
