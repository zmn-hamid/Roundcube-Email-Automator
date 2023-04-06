# Roundcube Email Automator

Send bulk emails with roundcube automatically.

#### Features

- You can specify attachments as well
- Accepts user data as an `XLSX` file.

## Getting Started

#### Prerequisites

python 10+ must be installed and added to system path.

### Installation

1. Open terminal in the root directory and install requirement with this command:
   `pip install -r requirements.txt`
2. Make a `config.py` file in the root directory, and put this text inside it:

   ```
    LOGIN_URL = 'Your Login Page'  # end with slash
    USERNAME = 'Your Username'
    PASSWORD = 'Your Password'

    USERS_XLSX = 'path/to/users.xlsx'  # must be xlsx
    EMAIL_SUBJECT = 'path/to/email_subject.txt'  # must be txt
    EMAIL_BODY = 'path/to/email_body.txt'  # must be txt
    ATTACHMENTS = [ # put nothing here if no attachments needed
        # 'path/to/attachment.jpg',
    ]

    # don't change unless necessary
    COMPOSE_URL = LOGIN_URL + '?_task=mail&_action=compose'
   ```

   1. If your `LOGIN_URL` is not in this format: `http://mail.DOMAIN.com/webmail/`, do this:
      1. Open your email in the browser
      2. Click "Compose" from the left menu
      3. Copy the URL and remove the last part: `&_id=116063791642ea2b658946` (that number is different everytime)
      4. Replace the `COMPOSE_URL` line with this line:
         `COMPOSE_URL = 'rest of the URL from step 3'`
   2. After filling out the credentials and `LOGIN_URL`, replace the `USERS_XLSX` with the relative path to your users.xlsx file. <b>Important notes</b>:
      1. The path must be relative. For example, if you put the `users.xlsx` file in the [data](data/) folder, it would be like this:
         `USERS_XLSX = 'data/users.xlsx'`
      2. It must end with .xlsx
      3. Three headers/columns are required: `FIRST NAME`, `LAST NAME`, `EMAIL`. If email is empty or both first and last name are empty, that row wouldn't be detected.
   3. Email body and subject files are `txt` files that should be treated the same way as users xlsx file. Recommended to put them in [data](data/) folder, but not necessary.
   4. Put the relative path of every attachment you have, in the `ATTACHMENTS` list. Put nothing if you have no attachments.

#### Usage

Once you're in the root directory, run the app using `python -i email_automator.py`

- note: with this method if you choose `n` when prompted in the end, you can still access the driver using `driver`

## Important note

- Do not touch your PC while the app is being run. This app uses your keyboard keys to do some of the jobs. Doing anything can mess up the program's functioning.

## Contributing

Than you in advnace for your contribution to this project. As a new developer, I appreciate everyone who joins this project.

#### Motivation

This is a project I did for my work, but any contribution and improvements would be great.

#### Scope

The project has already reached its main goal, but improvements can still be done. have fun with your imagination.

#### How To Contribute

1. Fork this repository and clone it.
2. Make your desired changes to the project.
3. Commit your changes to the forked repository.
4. Submit a pull request to the main respoitory.

#### Guidelines for Contributions

- Consider to keep the same coding style and conventions.
- Write clear and precise commit messages.

## License

MIT License

This project is free and open-source. You can use, modify, and distribute it without any restrictions.

## Contact

If you have any questions or feedback about this project, feel free to get in touch with me:

- Email: zmn-hamid@proton.me
- [Telegram](https://t.me/hamid1780)
- [GitHub Issues](https://github.com/zmn-hamid/spotify-full-album/issues)
