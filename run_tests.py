import subprocess

def run_tests():
    # Run pytest with Allure reporting
    pytest_command = "pytest"
    subprocess.call(pytest_command, shell=True)

    # # Generate Allure report
    # generate_report_command = "allure generate ./allure-results -o ./allure-report --clean"
    # subprocess.call(generate_report_command, shell=True)

    # # Open Allure report in the default browser
    # open_report_command = "allure open ./allure-report"
    # subprocess.call(open_report_command, shell=True)

if __name__ == "__main__":
    run_tests()
