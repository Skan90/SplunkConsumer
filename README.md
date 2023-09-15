# SplunkConsumer

This project is a Proof of Concept (POC) and mentorship opportunity designed to demonstrate the use of Python packages for consuming data from external APIs. By leveraging Python's powerful libraries and best practices, this project serves as an educational resource for those looking to learn about API integration with Python.

Key Features:

- API Integration: Explore how to connect and retrieve data from external APIs using Python packages.
- Package Showcase: Demonstrate the usage of popular Python packages like requests or http.client for making API requests.
- Documentation: Provide clear documentation and code examples to help learners understand the process.
- Mentorship: Offer mentorship and guidance to those who want to expand their skills in API integration and Python programming.

The main goal with this project it's to implement a Prof of Concept with the following items:
- First Step
  - HTTP requests using python package [requests](https://requests.readthedocs.io/en/latest/) to collect data from [Splunk](https://www.splunk.com/).
  - Use of the python [JSON package](https://docs.python.org/3/library/json.html).
  - Unit Coverage test using [pytest](https://requests-mock.readthedocs.io/en/latest/pytest.html)
  - Use of external tools like Postman / Insomnia
  - Documentation following [Docstring](https://www.dataquest.io/blog/documenting-in-python-with-docstrings/) pattern
  - Focus in a more python code following [list and dictionary comprehension](https://www.netguru.com/blog/python-list-comprehension-dictionary).
- Second Step 
  - Data persistence using [PyMongo](https://pymongo.readthedocs.io/en/stable/).
  - Schema Validation
  - Integration and E2E test using [RobotFramework](https://robotframework.org/) or [Behave](https://behave.readthedocs.io/en/latest/)
- Third Step
  - All the CI infra needs to be inside a container [Dockerfile Doc](https://docs.docker.com/engine/reference/builder/).
    - Create a CI environmentto run the unit tests
    - Create a CI environmentto run the integration tests
    - Create a CI environmentto run the E2E test
- Last Step
  - Configure Grafana to consume data from MongoDB.

