# ConstChoices

ConstChoices is a enhance module using class-style define for const choices.

## Basic Uage

1 Inherit class `ConstChoices.ConstChoices`。

```python
from ConstChoices import ConstChoices


class YearInShoolChoices(ConstChoices):
    FRESHMAN = 'FR', 'Freshman'
    SOPHOMORE = 'SO', 'Sophomore'
    JUNIOR = 'JR', 'Junior'
    SENIOR = 'SR', 'Senior'

```

2 Get the members for this class.

```
>>> YearInShoolChoices.FRESHMAN
'FR'
>>> s.get_year_in_school_display()
'Junior'
>>> YearInShoolChoices.is_valid('SR')
True
>>> YearInShoolChoices.is_valid('Et')
False
```

## Advange Usege

You can replace two-element tuple with this class in the attr *choices* of model field for django.

Before:

```python
from django.db import models

class Student(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    UNKOWN = 'unkown'
    
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    
    GENDER_CHOICES = (
        (MALE, 'male'),
        (FEMALE, 'famale'),
        (UNKOWN, 'unkown')
    )
    
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )
    
    gender = models.IntergerFIeld(
        choices=GENDER_CHOICES,
        default=UNKOWN
    )

```

After using ConstChoices.

```
class Student(models.Model):
    class YearInShoolChoices(ConstChoices):
        FRESHMAN = 'FR', 'Freshman'
        SOPHOMORE = 'SO', 'Sophomore'
        JUNIOR = 'JR', 'Junior'
        SENIOR = 'SR', 'Senior'
    
    
    class GenderChoices(ConstChoices):
        MALE = 1, 'male'
        FEMALE = 2, 'female'
        UNKOWN 3, 'unkown'

    year_in_school = models.CharField(
        max_length=2,
        choices=YearInShoolChoices.choices,
        default=YearInShoolChoices.FRESHMAN,
    )
    gender = models.IntergerFIeld(
        choices=GenderChoices,
        default=GenderChoices.UNKOWN
    )
```
