# patch_allure.py
import allure

if not hasattr(allure, 'severity_level'):
    class SeverityLevel:
        BLOCKER = 'blocker'
        CRITICAL = 'critical'
        NORMAL = 'normal'
        MINOR = 'minor'
        TRIVIAL = 'trivial'

    allure.severity_level = SeverityLevel

print("Patched allure module successfully.")
