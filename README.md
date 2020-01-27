# Remedy Tools

This package leverages selenium to create tickets in the back-end gui of BMC Remedy.

## Getting Started

This package was created to programatically create tickets in BMC Remedy when an api is unavilable or access
to it is not possible. This project was made possible with the use of selenium which is used to simulate a
user submitting a ticket through the back-end gui. This is a semi-automated process for creating tickets,
because the Remedy system (depending on its configuration) requires user authentication, this means your
user token will be in use by the chromedriver and opening Remedy in another browser will cause the process
to fail.

### Prerequisites

To use this package is will require the chromedriver from chromium.

- [chromedriver.exe](http://chromedriver.chromium.org/) - Open Source Tool for Automated Testing

## Installation

This package is **not** available on [PyPi](https://pypi.org) at this time. Please use the following command to install from github:

```
$ pip install https://github.com/RackReaver/remedy-tools.git
```

## How to use

```
>>> from remedy-tools import RemedyTools
>>> client = Client(remedy_url, chromedriver_path)
>>>
>>> details = {
>>>     'customers': '',
>>>     'queue_name': '',
>>>     'summary': '',
>>>     'notes': '',
>>>     'service': '',
>>>     'work_details': '',
>>>     'operational_tier_1': '',
>>>     'operational_tier_2': '',
>>>     'operational_tier_3': ''
>>> }
>>>
>>> ticket_number = client.WorkOrder(**details)
```

## TO-DO

- Integrate selection of priority into details dictionary (currently auto selects Medium)

## Built With

- [Selenium](https://www.seleniumhq.org/) - Web Browser Automation
- [Requests](http://docs.python-requests.org/en/master/) - HTTP for Humans
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - HTML Parser

## Authors

- **Matt Ferreira** - _Developer_ - [RackReaver](https://github.com/RackReaver)

## License

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

- **Adam Sadovsky** - _[XPath Helper](https://github.com/google/xpaf)_ - XPath-based Parsing Framework (Chrome Extension)
