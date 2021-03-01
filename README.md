# selenium-ui-automation

[![CodeQL](https://github.com/mazlan/selenium-ui-automation/actions/workflows/codeql-analysis.yml/badge.svg?branch=master)](https://github.com/mazlan/selenium-ui-automation/actions/workflows/codeql-analysis.yml)

A simple test automation framework based on Selenium and Python using Chrome Web Driver.

The tests have been written using Python 3 as the programming language using the latest version of the Selenium library for Python 3. If you are using a virtual environment setup to run Python ensure, you this library installed. Below are the steps required on how the automated tests can be configured and run for a Windows machine (setup on a Mac can vary a bit):

*	Install latest version of Python 3
*	Ensure you have the latest version of Chrome browser installed
*	Download and put the latest version of Chrome driver in your PATH env variable
*	Install free version of IDEA’s Pycharm IDE
*	The project files can be opened up in the IDE which makes running the tests directly from the IDE  easier
*	Once project is setup in Pycharm, the tests can be run using python’s unittest framework by clicking on the test class name or test cases file in the IDE (ensure it is not py test but unites that is selected by default when running the tests)
*	Or tests can also be run via command line using the command: **python –m unittest tests.homepage.TestHomePageNavigation** by running the command from the root folder of the project
