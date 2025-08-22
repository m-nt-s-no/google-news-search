import pytest
from pytest_mock import MockerFixture
from src import send_email

@pytest.fixture(autouse = True)
def fake_env(monkeypatch):
    #ensures tests use fake email credentials
    monkeypatch.setattr(send_email, "EMAIL_SENDER", "fake_email_sender")
    monkeypatch.setattr(send_email, "EMAIL_PASSWORD", "fake_email_password")
    monkeypatch.setattr(send_email, "EMAIL_RECIPIENT", "fake_email_recipient")

def test_send_email_no_results(mocker):
    # Mock the SMTP library to avoid sending real emails
    mock_smtp = mocker.patch("src.send_email.smtplib.SMTP")
    mock_smtp.return_value.sendmail.return_value = None

    # Call the function with an empty string
    send_email.send_email("")

    # Assert that sendmail was called with the correct parameters
    mock_smtp.return_value.sendmail.assert_called_once_with(
        "fake_email_sender",
        "fake_email_recipient",
        "No new results found."
    )
