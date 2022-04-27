import unittest
from testCases.test_cases_login import Test_Cases_Login
from testCases.test_cases_dashboard import Test_Cases_Dashboard
from testCases.test_cases_map import Test_Cases_Map

tc1 = unittest.TestLoader().loadTestsFromTestCase(Test_Cases_Login)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Test_Cases_Dashboard)
tc3 = unittest.TestLoader().loadTestsFromTestCase(Test_Cases_Map)

masterTestSuite = unittest.TestSuite([tc1, tc2, tc3])
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)