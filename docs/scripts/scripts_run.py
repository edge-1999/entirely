import os
import sys

import django

# sys.path.insert(0, project)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'entirely.settings')
django.setup()


def run_main():
    from data_records.result import AuthorSystemMessages

    subscriber_id = 'dc2c1d98b9604f87a383f3e522ef53e2'
    a = AuthorSystemMessages(subscriber_id)
    a.def_get_system_messages()
    if a.display:
        print(a.data)


if __name__ == '__main__':
    run_main()
