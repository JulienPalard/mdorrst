# exiffind
Find images by their exif tags'

# Install
```
$ pip3 install exiffind
```

# Usage
```bash
$ exiffind --param value /path/to/images
    
/path/to/images/a.jpg
/path/to/images/deeper/b.jpg
```

```python
from exiffind import check
check({
    "dir":"",
    "after":"2016-01-01"
})
```

## Parameters
- before: date to be digitized before in format YY-MM-DD (other date formats might work)
- after: date to be digitized after in format YY-MM-DD (other date formats might work)
- ext: search only for files with $EXT extensions
- orientation: horizontal, vertical
- author: 
- software:
- width: search by image with (supports ranges)
- height: search by image height (supports ranges)
- manufacturer: search by camera manufacturer
- model: search by camera model
- speed: search by speed (ISO value, supports ranges)
- exposure: search by exposure time (supports ranges)
- aperture: search by aperture value (supports ranges)
- fnumber: search by f-number (supports ranges)
- xresolution: search by resolution in x direction (supports ranges)
- yresolution: search by resolution in y direction (supports ranges)

Every parameter that supports searching by range can be used in the following ways:
- <X : smaller than X
- \>X : greater than X
- =X : equal to X (default)
- !X : not equal to X
- A:B : between A and B

Most parameters support fractional input, e.g. exposure can be 1/2.5