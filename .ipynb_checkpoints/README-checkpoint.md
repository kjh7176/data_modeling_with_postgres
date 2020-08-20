# Data Modeling with Postgres
This is the first project of Udacity's **Data Engineering Nanodegree**:mortar_board:.  
The purpose is to build an **ETL pipeline** transferring data from `JSON` to `Postgres database` Using `Python` and `SQL`

## Background
A startup called :musical_note:*Sparkify* wants to analyze the data they've been collecting on songs and user activity on their new music streaming app.  
The analytics team is particularly interested in understanding what songs users are listening to.  
Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.  

## ETL Pipeline
- Database Schema Diagram
![ERD](/images/db_schema.PNG "ERD from https://dbdiagram.io/")
- Click [here](https://github.com/kjh7176/data_modeling_with_postgres/wiki/ETL-Pipeline) for the details of **data transformation** process used in this project.

## Usage
1. Copy Repository to Local
```
$ git clone https://github.com/kjh7176/data_modeling_with_postgres
```

2. Create Database and Tables
```
$ python create_tables.py
```

3. Execute ETL process
```
$ python etl.py
```

4. Confirm records were sucessfully inserted in each table
   Open `test.ipynb` and run all code cells.

## Example
1. Table: songplays 
   - Query
   ```
   SELECT * FROM songplays LIMIT 5;
   ```
   - Result
   ![songplays](/images/songplays.PNG)
2. Table: users
   - Query
   ```
   SELECT * FROM users LIMIT 5;
   ```
   - Result
   ![users](/images/users.PNG)
3. Table: songs
   - Query
   ```
   SELECT * FROM songs LIMIT 5;
   ```
   - Result
   ![songs](/images/songs.PNG)
4. Table: artists
   - Query
   ```
   SELECT * FROM artists LIMIT 5;
   ```
   - Result
   ![Query](/images/artists.PNG)
5. Table: time
   - Query
   ```
   SELECT * FROM time LIMIT 5;
   ```
   - Result
   ![time](/images/time.PNG)