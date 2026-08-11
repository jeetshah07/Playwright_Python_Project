from pages.testcases_page import CasesPage


def test_verify_test_cases(page):

    test_cases = CasesPage(page)

    test_cases.open_test_cases_page()