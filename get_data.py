import pandas as pd
from pathlib import Path

import config as CONFIG


class Data:
    def get_users(self):
        users = []
        excel_data = pd.read_excel(CONFIG.USERS_XLSX)
        for idx, row in excel_data.iterrows():
            if '@' in (email := str(row['EMAIL'])):
                first_name = row['FIRST NAME']
                last_name = row['LAST NAME']
                name = ('%s %s' % (
                        first_name.strip() if type(first_name) == str else '',
                        last_name.strip() if type(last_name) == str else '',
                        )).strip()
                if name:
                    users.append({
                        'email': email,
                        'name': ('%s %s' % (
                            first_name.strip() if type(first_name) == str else '',
                            last_name.strip() if type(last_name) == str else '',
                        )).strip()
                    })
        return users

    def get_attachments(self):
        return [str(Path(item).absolute()) for item in CONFIG.ATTACHMENTS]

    def get_email_subject(self):
        return open(CONFIG.EMAIL_SUBJECT).read()

    def get_email_body(self):
        return open(CONFIG.EMAIL_BODY).read()


if __name__ == '__main__':
    import mein
    print(mein.dumps_en(Data().get_users()))
