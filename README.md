# MailGist

MailGist is a project designed to summarize your emails from Gmail and display them as a notification on your Windows Taskbar.

## Prerequisites

Before you begin, complete the following steps to authorize the application:
1. Complete the required steps on the [Google Cloud Documentation](https://developers.google.com/gmail/api/quickstart/python) under **Set up your environment**
2. Download the credentials json file and save it to `clients/credentials/gmail/XYZ.json`

> [!IMPORTANT]
> Ensure that you have your email added to the list of verified developers in the Google CLoud Oauth Page.

## Installation

To install MailGist, follow these steps:

```bash
git clone https://github.com/your-username/MailGist.git
cd MailGist
pip install -r requirements.txt
```

## Usage

To use MailGist, follow these steps:

1. Add a `GITHUB_TOKEN` or `OPENAI_API_KEY` environment variable
```bash
python main.py
```
> [!NOTE]
> On the first run, Google Oauth will ask you to verify that you wish to use MailGist.

## Contributing

To contribute to MailGist, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the original branch: `git push origin feature-branch`.
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.