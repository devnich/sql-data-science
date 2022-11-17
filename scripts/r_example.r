## https://www.r-project.org/nosvn/pandoc/RSQLite.html
## https://rsqlite.r-dbi.org/reference/sqlite
## https://dbi.r-dbi.org

## Access via dbplyr?
require("DBI")
require("RSQLite")

## library("dplyr")

con <- dbConnect(RSQLite::SQLite(), "../data/portal_mammals.sqlite")
