import imaplib
from mail_account import user_name, pass_wd


def get_unseen_number():
    Mail = imaplib.IMAP4_SSL("mails.tsinghua.edu.cn")

    try:
        try:
            Mail.login(user_name, pass_wd)
        except Exception as e:
            print('login error: %s' % e)
            Mail.close()
        Mail.select("INBOX")
        tpy, data = Mail.search(None, 'UNSEEN')
        data = data[0].split()
        return len(data)
        Mail.logout()
    except Exception as e:
        print('imap error: %s' % e)
        Mail.close()


print(get_unseen_number())