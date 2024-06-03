# Kickstarter SQL Analysis

This project analyses Kickstarter data using SQL.

## Data & processing plan

The data is available as a zip from [Web Robots](webrobots.io). I am using the May 2024 csv version (renamed as `kickstarter.zip` for this project).

PostgreSQL will be used for database management because of the relatively large data size (~300MB). Data cleaning via staging table, due to columns with non-standard typecasting which by default convert to strings when imported directly.

Some SQL queries are then performed.

## Other tools used

pgAdmin4 (debugger extension)

