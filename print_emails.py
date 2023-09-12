import os
import json

def print_emails():
    email_list=os.environ.get('EMAIL_LIST','').split(',')
    email_admin_fixed=os.environ.get('EMAIL_ADMIN','')
    
    print(email_list)
    print(f'The type of email_list is : {type(email_list)}')
    print(f'Emails in the list: {email_list}')
    print(f'First email in the list: {email_list[0]}')
    print(f'Fixed email in the workflow: {email_admin_fixed}')



print_emails()