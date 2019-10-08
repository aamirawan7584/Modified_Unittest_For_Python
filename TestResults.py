from datetime import datetime
from unittest import runner
import mysqltest

class TestResult(runner.TextTestResult):
    """A test result class that can print formatted test result and also save that result into database
    thats the plan
    """
    def __init__(self, stream, descriptions, verbosity):
        super(TestResult, self).__init__(stream, descriptions, verbosity)
        self.stream = stream
        self.showAll = verbosity > 1
        self.dots = verbosity == 1
        self.descriptions = descriptions
        # List containing all the test's name and class name with module name, their index, and status
        # (pass,fail,error).
        self.tests_run = []
        self.test_pass = 0  # new added for counting total number of tests pass

    def gettestsreport(self) -> list:
        """
        call this funciton to get information about test execution like name, suite name,
        status(pass,error,fail)
        :return: a list containing info of tests
        """
        return self.tests_run

    def total_tests(self):
        return self.test_pass

    def startTest(self, test) ->None:
        super(TestResult, self).startTest(test)
        if self.showAll:
            self.stream.write(self.getDescription(test))
            self.stream.write(" ... ")
            self.stream.flush()

    def stopTest(self, test) -> None:
        super(TestResult,self).stopTest(test)
        mysqltest.save_results(self.tests_run)
        self.tests_run = []

    def addSkip(self, test, reason):
        super(TestResult, self).addSkip(test, reason)
        self.tests_run.append(
            [self.getDescription(test), self.testsRun, "SKip!!", reason, self._exc_info_to_string(reason, test)])


    def addSuccess(self, test):
        super(TestResult, self).addSuccess(test)
        if self.showAll:
            self.stream.writeln("Pass :DDD")
        elif self.dots:
            self.stream.write('.')
            self.stream.flush()
        self._mirrorOutput = True
        self.test_pass += 1
        self.tests_run.append([self.getDescription(test), self.testsRun, "Pass!!",self._exc_info_to_string((None, None, None), test)])

    def addError(self, test, err):
        super(TestResult, self).addError(test, err)
        if self.showAll:
            self.stream.writeln("ERROR")
        elif self.dots:
            self.stream.write('E')
            self.stream.flush()
        self.tests_run.append([self.getDescription(test), self.testsRun, "Error!!", self._exc_info_to_string(err, test)])
        print(self.tests_run)

    def addFailure(self, test, err):
        super(TestResult, self).addFailure(test, err)
        if self.showAll:
            self.stream.writeln("FAIL")
        elif self.dots:
            self.stream.write('F')
            self.stream.flush()
        self.tests_run.append([self.getDescription(test), self.testsRun, "Fail!!", self._exc_info_to_string(err, test)])
        print(self.tests_run)
