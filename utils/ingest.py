#!/usr/bin/env python
"""Script to ingest existing NetBox data"""

# (c) 2020, Larry Smith Jr. <mrlesmithjr@gmail.com>
#
# This file is a module for ingest existing NetBox data

#
# Module usage:
# python ingest.py --token yourusersapitoken \
# --url http(s)//:iporhostnameurl:port # noqa E501
# Example:
# python ingest.py --token 4f552cc2e8c3b76d9613a591e3adb58984a19a6f \
# --url http://127.0.0.1:8080 # noqa E501
#


import argparse
import json
import yaml
import pynetbox
from lib.netbox.ingest import NetBoxIngest
from lib.netbox.ansible import NetBoxToAnsible

# pylint: disable=too-many-public-methods


def get_args():
    """Get CLI command arguments"""

    parser = argparse.ArgumentParser()
    parser.add_argument('--output', help='Output type to display',
                        choices=['ansible', 'netbox'], default='netbox')
    parser.add_argument('--token', help='NetBox API token', required=True)
    parser.add_argument('--url', help='NetBox API host url',
                        default='http://127.0.0.1:8080')
    parser.add_argument('--format', help='Format to display',
                        choices=['json', 'yaml'], default='json')
    args = parser.parse_args()

    return args


def main():
    """Main module execution"""
    args = get_args()
    netbox_token = args.token
    netbox_url = args.url

    netbox = pynetbox.api(url=netbox_url, token=netbox_token)
    netbox_ingest = NetBoxIngest(netbox)
    netbox_data = netbox_ingest.data()

    if args.output == 'ansible':
        netbox_ansible = NetBoxToAnsible(netbox_data)
        netbox_ansible_data = netbox_ansible.data()

    if args.format == 'json':
        if args.output == 'netbox':
            print(json.dumps(netbox_data))
        else:
            print(json.dumps(netbox_ansible_data))
    else:
        if args.output == 'netbox':
            print(yaml.dump(netbox_data))
        else:
            print(yaml.dump(netbox_ansible_data))


if __name__ == '__main__':
    main()
