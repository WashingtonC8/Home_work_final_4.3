import pytest
import faker
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture
def generate_user_data():
    fake = faker.Faker()
    email = fake.email()
    password = fake.password()
    return email, password
