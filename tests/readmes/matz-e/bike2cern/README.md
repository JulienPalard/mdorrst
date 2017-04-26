# Bike2Work @ CERN

Sync Bike2Work rides from Strava to CERN Sharepoint.

## Configuration

Create the configuration file `~/.config/bike2cern/sync.cfg` with the
following contents (adjusted):

    [strava]
    client_id = 12345
    secret = deadbeef0123456789

    [cern]
    username = johndoe

Client ID and secret can be obtained on
[Strava](https://www.strava.com/settings/api).

Save the CERN password in the system keyring:

    keyring set bike2cern cern

Upon first usage, `bike2cern` will request a Strava access token.

## Fixing the Sharepoint Dependency

Unfortunately, the sharepoint library that *bike2cern* uses does not
support Python 3 completely.  If the sync crashes, add the following to top
of the last file printed in the stack trace (this should happen twice):

```python
unicode = str
```

## Usage

Use with a start and end date (rides on the day of the end date will not be
synced), e.g., for the first half of the year:

    bike2cern --dry-run 2017-01-01 2017-07-01

Remove `--dry-run` to actually do the sync.  **Use at your own risk, syncing
too much will require manual deletion!**  The python Sharepoint library
currenty does not return a list of calendar items currently, hence the
need to specify sync dates.
