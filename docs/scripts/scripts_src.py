import os
import sys

import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'entirely.settings')
django.setup()


def run_main():
    # from data_records.result import AuthorSystemMessages
    # subscriber_id = 'dc2c1d98b9604f87a383f3e522ef53e2'
    # a = AuthorSystemMessages(subscriber_id)
    # a.def_get_system_messages()

    from develop_information.result import DevelopInformationNode
    a = DevelopInformationNode('117ca02eaef6408b9fb2967acdf79121')
    a.def_get_system_message()


if __name__ == '__main__':
    run_main()
