## https://www.r-project.org/nosvn/pandoc/RSQLite.html
## https://rsqlite.r-dbi.org/reference/sqlite
## https://dbi.r-dbi.org

library("DBI")
library("RSQLite")

## FYI, use namespaces explicitly
con <- DBI::dbConnect(RSQLite::SQLite(), "../data/portal_mammals.sqlite")

## List tables
dbListTables(con)

## Get column names
dbListFields(con, "species")

## Get query results at once
df <- dbGetQuery(con, "SELECT * FROM surveys WHERE year = 2000")
head(df)

## Parameterized queries
df <- dbGetQuery(con, "SELECT * FROM surveys WHERE year = ? AND (month > ? AND month < ?)",
                 params = c(2000, 4, 10))
head(df)

## Disconnect
dbDisconnect(con)
