# RIT Jobzone Auto-Applier
Automatically apply to the 'easy-apply' jobs on RIT's Jobzone site. You could do the same thing manually, but this is more efficient and the results will be the same. You can see all jobs you have applied to using the other functions of the website.

## How it Works
1. Automatically race through all job postings in RIT's Symplicity JobZone system, with the following filters:
   > Only Jobs you qualify (screening only)
   > Jobs in your major 
   > Exclude jobs you have previously applied to
2. Find the jobs with easy apply button and apply.
   > Automatically make file selections to send to the employer.
   > Use either the default cover letter or you can opt to have the program open the url, and continue on with the other        
   applications while you work on a special cover letter for the employer (this may not be requested by every employer)
   > Use either the default writing sample or you can opt to have the program open the url, and continue on with the other       
   applications while you work on a special writing sample for the employer (this may not be requested by every employer)

## How To Install
#### Make sure Python 27 is installed
1. Download the zip file & unzip
2. Goto folder: rit_jobzone_auto_apply/rit_jobzone_auto_apply
3. Double-click "autorun" file
              or
   Hold shift key and right-click in the unzipped folder and open a command window
   Type in Command Window:
   ```
   python
   import rit_jobzone_auto_apply as rjaa
   rjaa.AutoApply()
   ```
  
## How to Use
1. Enter your username and password for RIT's Jobzone
2. Enter 'True' or 'False' to whether you want to use you default cover letter and your default writing sample
3. Leave the program to run & monitor the program's progress.

## Optional
1. Look on RIT's Jobzone for all Jobs you have applied for.
   
