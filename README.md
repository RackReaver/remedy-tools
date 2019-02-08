# Remedy Tools

This package leverages selenium to create tickets in the back-end gui of BMC Remedy.

## Getting Started

This package was created to programatically create tickets in BMC Remedy when an api is unavilable or access
to it is not possible. This project was made possible with the use of selenium which is used to simulate a 
user submitting a ticket through the back-end gui. This is a semi-automated process for creating tickets, 
because the Remedy system (depending on its configuration) requires user authentication, this means your
user token will be in use by the chromedriver and opening Remedy in another browser will cause the process
to fail.

## Installation

This package is available on [PyPi](https://pypi.org) and can be installed with the following command:

```
$ pip install remedy-tools
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

## Built With

* [Selenium](https://www.seleniumhq.org/) - Web Browser Automation
* [Requests](http://docs.python-requests.org/en/master/) - HTTP for Humans
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - HTML Parser

## Authors

* **Matt Ferreira** - *Developer* - [RackReaver](https://github.com/RackReaver)

## License

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* **Adam Sadovsky** - *[XPath Helper](https://github.com/google/xpaf)* - XPath-based Parsing Framework (Chrome Extension)