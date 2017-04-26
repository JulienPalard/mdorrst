# sheetDB


[![PyPI Version](https://img.shields.io/pypi/v/sheetDB.png)](https://pypi.python.org/pypi/sheetDB)
[![Build Status](https://travis-ci.org/knyte/sheetDB.svg?branch=master)](https://travis-ci.org/knyte/sheetDB)
[![Code Climate](https://codeclimate.com/github/knyte/sheetDB/badges/gpa.svg)](https://codeclimate.com/github/knyte/sheetDB/code)
[![Test Coverage](https://codeclimate.com/github/knyte/sheetDB/badges/coverage.svg)](https://codeclimate.com/github/knyte/sheetDB/coverage)
[![Issue Count](https://codeclimate.com/github/knyte/sheetDB/badges/issue_count.svg)](https://codeclimate.com/github/knyte/sheetDB/issues)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e09f7a093ab24d02a2b0419f8108a365)](https://www.codacy.com/app/knyte/sheetDB?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=knyte/sheetDB&amp;utm_campaign=Badge_Grade)

Google Sheets as a back-end

sheetDB lets you treat Google Sheets spreadsheets as databases while still allowing them to be human-readable and human-usable.

## Installation
Latest release at https://github.com/knyte/sheetDB/tarball/0.1.10

Install via pip (recommended):

```python
pip install sheetDB
```

## Usage

### 1. Install dependencies
   Don't worry about this if you installed using pip

```python
pip install -r requirements.txt 
```

OR

```python
python setup.py install # installs the whole module
```

   (from the sheetDB parent directory)
   
### 2. Get OAuth credentials
   To use sheetDB and gspread, you need a Google Service Account and its corresponding credentials. 
   The Service Account you use must also have access to any pre-existing spreadsheets you want to use with sheetDB.
   
   Follow steps 1-3 under **Using Signed Credentials** [here](http://gspread.readthedocs.io/en/latest/oauth2.html).

### 3. Import

```python
from sheetDB import Credentials
```
    
### 4. Use
   Now you can use sheetDB to access, read, and modify existing Google Sheets spreadsheets as if they were databases.
   You can also create new spreadsheets and treat them as databases. See **Examples** below.

## Examples

### 1. Retrieving databases

```python
from sheetDB import Credentials
    
keyfile = "/path/to/keyfile"
 
creds = Credentials(keyfile)
    
# fetch an existing database
db = creds.fetchDatabase("Spreadsheet Title") # this works for a pre-formatted sheet
newDB = creds.fetchDatabase("Spreadsheet Title", checkFormat=False) 
# this will reformat an existing sheet to work as a database
 
# you can also fetch by key using creds.getDatabase
db3 = creds.getDatabase("spreadsheet_key", checkFormat=False)
  
# or by URL using creds.getDatabaseFromURL
db4 = creds.getDatabaseFromURL("spreadsheet_url", checkFormat=False)
    
# getDatabase and getDatabaseFromURL are recommended because titles are not necessarily unique
  
# oh, and you can also get all the databases you have access to
allDBs = creds.getAllDatabases(checkFormat=False) 
# if checkFormat is False, this will reformat all your sheets to work as databases
# this reformatting is fairly minor; just a new "Constants" worksheet gets added
# any reformatted sheets should still be human-readable and human-usable
```
    
### 2. Using databases

```python
db = creds.getDatabase("spreadsheet_key")
   
# database-wide constants - for tracking information
# you can get away with not using these yourself at all,
# since they're mostly just used automatically to track table constants
# but depending on what your database is supposed to store, directly using these
# might be useful, too
    
constant = db.fetchConstant("label") # returns a list (using comma separators)
# if constant is supposed to only have one value, just use constant[0]
db.setConstant("label", "value") # sets a constant
db.addToConstantList("label", "other value") # you can just have multiple values for a constant
db.setConstantList("other label", ["value", "other value", "a third value"])
db.removeFromConstantList("other label", "other value") # now just ["value", "a third value"]
db.removeConstant("other label") # permanently wiped now
# db.fetchConstant("other label") will return ["",]
    
# creating and retrieving tables
   
# retrieve tables by title
table = db.getTable("title")
    
# create a new table - remember that titles can't be re-used
newTable = db.createTable("new title", headerRow=["Name", "Birthday"])
# you can also give it a list of dictionaries as entities to populate the table with
# e.g., entities=[{"Name": "knyte", "Birthday": "01/01/1970"}, 
#                 {"Name": "vitriol", "Birthday": "01/02/1970"}]
    
# already have an existing worksheet you want to treat as a table?
existingTable = db.recognizeTable("existing title")
# you can also specify ignored rows and columns as parameters to recognizeTable

# if you're not sure whether a table exists already, try fetchTable
# it takes all the parameters of getTable, createTable, and recognizeTable
# alternatively, you could also use tableExists with the table title
    
# remove a table, too
db.removeTable("title")
    
# and finally, if you're **totally** done with the database **forever**, you can delete it
db.delete() # the spreadsheet goes away, too
```

### 3. Working with tables

```python
table = db.getTable("title")
    
# made some manual modifications and want to change the header #?
table.setHeader(5) # sets the header row to row 5
    
# ignore rows or columns
## ignored rows and columns are write-protected
## ignored rows are also read-protected and will not be mistaken for entities
## ignored cols are read-protected but that protection can be overriden by the user
table.ignoreRows(1, 2, 3)
table.unignoreRows(1, 2, 3)
table.ignoreCols(4, 5, 6)
table.unignoreCols(4, 5, 6)
    
table.setRefRow(6) # same principle as setHeader for the ref row
    
# the ref row lets you handle formulas and constraints on each column
# so you can force types- NUMERIC, INT, ALPHA, ALPHANUMERIC, ARRAY, BOOL, etc.
# constrain cells to be UNIQUE, POSITIVE, NONNEGATIVE
# or just put in formulas that will get populated to all new entities in that column
# unless overriden by another value, of course
    
# supported constraints right now:
## UNIQUE - forces cells to be unique within a column (ignoring ignored rows)
## POSITIVE - forces cells to be positive (NUMERIC/INT only)
## NONNEGATIVE/NONNEG - forces cells to be non-negative (NUMERIC/INT only)
## INT - forces cells to represent integers
## NUMERIC - forces cells to represent floating-point values
## STRING - only accepts Python string datatypes
## ALPHA - only accepts strings that contain values in [A-Z] and/or [a-z]
## ALPHANUMERIC/ALPHANUM - can contain values in [A-Z], [a-z], and/or [0-9]
## ARRAY/LIST - takes in arrays
## BOOL/BOOLEAN - only takes in "TRUE"/"FALSE" or True/False
## FORMULA - only takes in formulas (will accept malformed formulas, though)
## (if you're planning on using the same formula throughout a column,
##  just supply that formula *as* the constraint)
    
# these constraints will also cause column values to be returned as the proper datatype
# so an INT column will result in sheetDB retrieving 4, not "4"
    
# so let's use this a bit
    
table.constrain(5, "NUMERIC NONNEGATIVE ARRAY") # constrain by column number
table.updateConstraint("Name", "ALPHA") # or constrain by column label
# want to expand an existing constraint?
table.updateConstraint("Name", "UNIQUE", erase=False) # now both "ALPHA" and "UNIQUE"
# or to remove a constraint?
table.updateConstraint("Name", "", erase=True) # will erase and replace with nothing

# you can also use formulas as constraints
table.updateConstraint("Name", "=$A$1", erase=True)
# and for relative references...
table.updateConstraint("Name", "=R[4]C[-3]", erase=True)
# fetches the value from 4 columns below and 3 to the left
    
# now let's deal with entities stored in the database
entity = table.fetchEntity(20) # by row number
unignoredEntity = table.fetchEntity(20, unignore=True) # reads ignored columns now, too!
# these will be fetched as dictionaries with header labels as keys
# like {"Name": "knyte", "Birthday": "01/01/1970"}
   
# fetch a bunch at once, as a list (sorted by row number, in the order you provide)
entities = table.fetchEntities([1, 2, 3, 4, 5], unignore=False) # top 5 rows
    
# or even all of them
allEntities = table.getAllEntities()
# get them in a dictionary instead of a list, using the key of your choice
keyedEntities = table.getAllEntities(keyLabel="Name")
    
# add an entity
table.addEntity({"Name": "propulsion", "Birthday": "01/03/1970"})
# remove an entity by row number
table.removeEntity(6) # now row 6 is gone
# update an entity by row
table.updateEntity({"Birthday": "01/04/1970"}, 6) # now row 6's birthday is fixed!
    
# of course, you're note always going to have access to the row #'s
# in fact, you probably aren't going to be calling row-number based functions at all
   
# update entities that meet some constraints
matchDict = {"Name": {"value": "knyte", "type": POSITIVE}}
updates = {"Birthday": "01/01/1970"}
table.updateMatchingEntities(matchDict, updates)
# now all entities with their name set to "knyte" will have their birthday updated to "01/01/1970"
table.removeMatchingEntities(matchDict)
# and now all entities named "knyte" are gone...
# if you want to check for multiple values, use "values" instead of "value" and map that to a list of values
    
# finally, when you're absolutely, totally, never-gonna-use-it-ever-again-ever done
table.delete()
# it's gone now, forever
```

For quick, more extensive documentation, try:

```python
help(sheetDB.Credentials)
help(sheetDB.Database)
help(sheetDB.Table)
```

### Basic Best Practices

1. If you're interfering with a worksheet's header row #, reference row #, ignored row/col #'s- or, say, adding a row or 
 column to the middle of the worksheet, **do so programmatically** using the sheetDB library. Avoid interfering with these
 values in the first place.

2. If you want a worksheet to be modified by both humans and software using sheetDB:

    a. **Create a new worksheet** that uses QUERY, SORTED, or some similar formula to query the original sheet.

    b. Set up sheetDB to **modify the original** and leave it unaware of the copy.
    
    c. Let **humans modify the new sheet** that has access to the same values (and gets auto-updated).
    
    d. To keep things pretty, **hide the old sheet** since it'll mostly get accessed by a program at this point anyway.
    
3. **If your worksheet has a formula** that you want sheetDB to automatically add to any new rows, put that formula in the
 worksheet's reference row (its REFROW constant value). It will be automatically replicated in any new rows (unless 
 overriden). In general, it's viable to instead just have the formula in a self-populating duplicate worksheet (see 2. 
 above) but you might sometimes want a formula to be present in the sheet so that sheetDB can read that value.
 
4. **If humans are modifying a worksheet** that sheetDB also modifies, have a clear delineation between human-edited rows
 and sheetDB-edited rows. Constraint validation is not going to be performed automatically every time a human edits
 a value or adds to a column, so you might inadvertently violate column invariants.

## Sheet Constraints

(**Note**: You can ignore this section as long as you adhere to **Basic Best Practices**.)

To use a Google Sheets spreadsheet with sheetDB, make sure it **does not already have a worksheet named "Constants"** 
or some important invariants will likely be violated.

Any existing worksheets you want to manipulate with sheetDB **must also be using a row as a header**; you can't have 
entities listed column-by-column. Each row is considered to belong to a single entity/object in a table.

**Humans with access to a sheetDB Database sheet should be careful** when modifying the Constants sheet as well as
any header or constraint rows. If human editors add new columns or rows that they do not wish to be modified or
examined programmatically (i.e., rows/columns that aren't storing entities or are storing attributes of no interest
to any automated processes), they should add those row/column numbers to the IGNOREDROWS or IGNOREDCOLS constant for
that worksheet, adjusting any existing ignored row/col numbers if they were shifted by additions/deletions as well.

A worksheet's constants are stored as [worksheet ID]_[constant name]. Worksheet IDs cannot be extracted from the 
worksheet URL (a sheet's ID is not the same as the gid parameter in the URL), so the process of editing constants can 
get messy and involve guesswork.

For these reason, it's strongly recommended that **all modifications** that interfere with constants like a sheet's
header row #, reference row #, ignored row #'s, or ignored col #'s be **done programmatically if possible** and **any new
rows or columns added by humans be added strictly at the end of the sheet**. Also, it's strongly discouraged to perform
any major modifications to a worksheet that's simultaneously being modified by a program using sheetDB. Local records
are updated frequently enough to catch changes (like an added row) but can be easily thrown off if a human modifies
a sheet at the wrong time.
