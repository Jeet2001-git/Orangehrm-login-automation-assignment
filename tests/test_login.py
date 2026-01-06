
from pages.login_page import LoginPage

""" Test Case: Verify that a user can successfully log in with valid credentials and is redirected to the Dashboard page."""

def test_valid_login_redirects_to_dashboard(setup):

    # Arrange
    login_page = LoginPage(setup)

    # Act
    login_page.login("Admin", "admin123")

    # Assert
    assert login_page.is_login_successful(), (
        "Login failed: User was not redirected to the Dashboard page "
        "after entering valid credentials"
    )



