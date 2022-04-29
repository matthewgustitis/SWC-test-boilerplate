To run application and generate SWC-100 results:
   $ python SWC-100-audit.py


Results are currently output to results.txt


In order to add functionality for all SWC-100 vulnerabilities, new files just need to be added to local-web3-audit/copy_files/tests


The tests in the test_SWC_101 file are example tests just to show the general structure of the application. We can either change the pytest environment to output the results of the pytest tests to a file and do something with that to make test objects or we can essentially highjack the "asssert" function and use the results of those asserts to create TestResultObjects and return those somewhere.


###Fixes/Features:
   deploy.py and test_'s needs to dynamically find out the name of the contract in order to deploy it.
   this can be done in a few ways:
      - use a function to make the deploy script with the Contract name in it
      - update the Contract name in config
      - run deploy command from brownie console

   results need to be output as an object that can be pushed to the api

   need a method of creating tests that are customizable for each contract
   beyond tests that work for all projects universally (this is a big one)

   contracts need to be able to be processed either as a url to a raw file, a github repo, or a local directory
