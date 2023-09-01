import library


def main():
    recipients = ['test_hillel_api_mailing@ukr.net']
    mail_body = 'Text from Odesa'
    mail_subject = "Hello"
    # attachment

    library.send_email(
        recipients=recipients,
        mail_body=mail_body,
        mail_subject=mail_subject,
    )


if __name__ == '__main__':
    main()
