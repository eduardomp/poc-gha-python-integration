import os
import json

def print_emails():
    email_list=os.environ.get('EMAIL_LIST','').strip('][').split(',')
    email_admin_fixed=os.environ.get('EMAIL_ADMIN','')
    print(f'Emails in the list: {email_list}')
    print(f'First email in the list: {email_list[0]}')
    print(f'Fixed email in the workflow: {email_admin_fixed}')



print_emails()