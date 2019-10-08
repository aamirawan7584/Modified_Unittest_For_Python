__author__ = 'Aamir Mumtaz'
from datetime import datetime
import json
import sys
import unittest
import mysqltest
from typing import List, Any, Callable
from unittest.suite import TestSuite
import loadtest
from TestResults import TestResult


class Runner(unittest.TestLoader):
    totaltestcases = 0
    numberofmodules = 0
    numberofclasses = 0
    numberoftestcases = 0
    dict = {}

    def extract_info_from_object(self, suitcaseobj):
        self.numberoftestcases = suitcaseobj.countTestCases()
        self.numberofmodules = len(suitcaseobj._tests)

    def makedic(self, module, class_name, test):
        """
        
10        :param module: module name
        :param class_name: class name
        :param test: testcases 
        :return: it return a dictionary containing discovered test cases info in this format
        {
            'moduleName':{
                            'ClassName':{
                            'TestCases':[testcases names]
                            }
                            'ClassName2':{
                            'TestCases':[TestCasesNames']
                            }
                            ...
                         }
        }
        """
        if module not in self.dict:
            self.dict[module] = {}
        self.dict[module].update({
            class_name: {
                "TestCases_Name": test
            }
        })
        return dict

    def gettestinfo(self, source):
        load = loadtest.Loader()

        """discover method look up for test methods in start directory, by default pattern is "test*.py' but
            any specific pattern can be added by using disvoer parameter e.g : Pattern = 'iamtest*.py' """

        testsuitecase: TestSuite = load.discover(start_dir=testdirectory)

        self.extract_info_from_object(testsuitecase)
        # discover return a test suite containing all test in that directory
        print(f"Found test in Source Directory {testdirectory} are :", testsuitecase)
        print(f"Number of test found in {testdirectory} Directory are:", self.numberoftestcases)

        tests = testsuitecase  # just for simplicity :P
        """
        in object returned by unittest.TestLoader.discover information of module, class and testmethod can be extracted like that:
        
        Number of Modules in TestSuite : len (tests._tests)
        Module Name: tests._tests[0]._tests[0]._tests[0].__class__.__module__
    
        Number of Classes in a specific module: len (tests._tests[Number of Module]._tests 
        TestSuite or class name :tests._tests[0]._tests[0]._tests[0].__class__.__name__
    
        Number of TestCases in a specific class: len(tests._tests[Number of Module]._tests[Number of Class]._tests
        Method Name : tests._tests[0]._tests[0]._tests[0]._testMethodName
    
        """
        """
        s = "------------------------------------------------------------------------------------"
        for i in range (0,4):
    
             print(tests._tests[1]._tests[0]._tests[i].__class__.__module__)
    
             print (tests._tests[0]._tests[0]._tests[i]._testMethodName)
    
             print (tests._tests[0]._tests[0]._tests[i].__class__.__name__)
    
             print (s)
        """
        sep = "------------------------------------------------------------------------------------"

        for module in range(self.numberofmodules):
            self.numberofclasses = len(tests._tests[module]._tests)
            for class_ in range(self.numberofclasses):
                modulename = tests._tests[module]._tests[class_]._tests[0].__class__.__module__
                # print(self.numberofclasses)
                class_name = tests._tests[module]._tests[class_]._tests[0].__class__.__name__
                # print("Class Name", class_name)
                self.numberoftestcases = len(tests._tests[module]._tests[class_]._tests)
                # print(self.numberoftestcases)
                test = []
                for testcase in range(self.numberoftestcases):
                    test_name = tests._tests[module]._tests[class_]._tests[testcase]._testMethodName
                    test.append(test_name)
                self.makedic(modulename, class_name, test)

        with open('testcases.json', 'w') as json_file:
            json.dump(self.dict, json_file, indent=2)
        # print(self.dict)

    def loadTests_FromModule(self, module):
        suite = unittest.TestSuite()
        __import__(module)
        mod = sys.modules[module]
        suite = unittest.TestLoader.loadTestsFromModule(self, module=mod)
        return suite

    def loadTests_FromClass(self, name, module):
        suite = unittest.TestSuite()
        __import__(module)
        mod = sys.modules[module]
        suite = unittest.TestLoader.loadTestsFromName(self, name, module=mod)
        return suite

    def loadTests_FromTestCases(self, names, class_, module):
        """
        Problem:
        my idea is that i pick names of testcases one by 0ne and load it using unittest.TestLoader.loadTestFromName but

        because this funciton does not have any info about class so it could not find those test


        :param names: a list of testcases name
        :param module: module name
        :return: testsuite
        """
        suite = unittest.TestSuite()
        __import__(module)
        mod = sys.modules[module]
        for name in names:
            suite.addTest(unittest.TestLoader.loadTestsFromName(self, class_ + "." + name, module=mod))
        return suite


if __name__ == '__main__':
    # test directory should be importable
    testdirectory = '/home/ebryx/Desktop/test_runner/hello/'
    runnerr = Runner()
    runnerr.gettestinfo(testdirectory)
    module_name = 'tests.test_1'
    class_name = 'Alpha'
    names = runnerr.dict[module_name][class_name]['TestCases_Name']
    # FOR running all testcases from a module
    # suite = runnerr.loadTests_FromModule('tests.test_1')
    # print (suite)

    # for running all testcases from a class
    # suite = runnerr.loadTests_FromClass('Alpha', 'tests.test_1')
    # print (suite)

    # for running selected test cases from a class
    suite = runnerr.loadTests_FromTestCases(names, class_name, module_name)
    # print(suite)
    start_time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    mysqltest.save_testruns_info_before(start_time, 'host@ALpha')
    result = unittest.TextTestRunner(verbosity=0, resultclass=TestResult).run(suite)
    end_time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    # resulttt = result.gettestsreport()
    runs = [end_time, result.testsRun, result.total_tests(), len(result.failures),
            len(result.errors), 'GoogleChrome', 'Link? UnderConstruction', mysqltest.get_runs_id()]
    mysqltest.save_testruns_info_after(runs)
