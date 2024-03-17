Introduction
------------

This repository contains basic example of test automation framework using PyTest, Selenium and Allure. 
The framework corresponds to Layered Architecture Pattern and uses Page Objects for web pages.

For tests, the website [Artnow.ru](https://artnow.ru) was used.


How To Run
----------------

1) Install all requirements (specified in [requirements.txt](requirements.txt)):

    ```bash
    pip install -r requirements
    ```

2) Install all npm packages (specified in [package.json](package.json)):

    ```bash
    npm install
    ```

3) Run main.py

References
----------------

Smart Page Object for pytest: https://github.com/TimurNurlygayanov/ui-tests-example

Exception screenshots for pytest: https://github.com/jkaluzka/pytest-exception-interact/tree/main

Pytest+Allure article: https://www.programmersought.com/article/73684180086/

Pytest+Allure+Jenkins article: https://www.mo4tech.com/python-testing-framework-allure.html

Pytest+Allure+Gitlab article: https://habr.com/ru/articles/513432/

Allure for pytest official: https://allurereport.org/docs/pytest/

Pytest habr article: https://habr.com/ru/articles/269759/

Pytest documentation: https://pytest.org/en/latest/reference/reference.html#id147