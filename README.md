To run application and generate SWC-100 results:
   - specify url on line ~22
   $ python SWC-100-audit.py


Results are currently output to results.json


In order to add functionality for all SWC-100 vulnerabilities, new files just need to be added to $/copy_files/tests



### Fixes/Features:      
   ##### need a method of creating tests that are customizable for each contract beyond tests that work for all projects universally (this is a big one)

   ##### contracts need to be able to be processed either as a url to a raw file, a url to a github repo, or a local directory

   #### allow for dependencies and imports

   ##### allow for testing on multiple different testnets