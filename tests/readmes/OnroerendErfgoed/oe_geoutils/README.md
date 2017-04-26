# oe_geoutils

* Repository with general tools like OnoerendErfgoed/oe_utils
* Focus on Geo and localization (addresses)
* Modules like shapely and crapy are included, that is why the tools are not included in oe_utils
* Endpoints: `nearest_address`, `check_in_flanders`, `check_in_erfgoedgemeente`, `gemeente` and `provincie`
* Can  be used as validation module or as a pyramid extention 
* crab_pyramid is included to make use of Crab
* If Crab is not needed, update config: `crabpy.crab.include = False` 
  The crabid's will not be returned when asked for the nearest address.
