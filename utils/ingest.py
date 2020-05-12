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


class NetBoxIngest:
    """Main NetBox ingestion class"""

    def __init__(self, netbox):
        self.netbox_data = {}
        self.netbox = netbox

    def data(self):
        """Collect all relevant NetBox data"""
        # DCIM
        self.dcim_collections()
        # Tenancy
        self.tenancy_collections()
        # IPAM
        self.ipam_collections()
        # Virtualization
        self.virtualization_collections()
        # Circuits
        self.circuits_collections()
        # Secrets
        self.secrets_collections()
        # Extras
        self.extras_collections()

        return self.netbox_data

    def dcim_collections(self):
        """Collect DCIM related info"""
        self.regions()
        self.sites()
        self.rack_roles()
        self.rack_groups()
        self.racks()
        self.manufacturers()
        self.platforms()
        self.device_types()
        self.device_roles()
        self.devices()
        self.interfaces()

    def tenancy_collections(self):
        """Collect tenancy related info"""
        self.tenant_groups()
        self.tenants()

    def ipam_collections(self):
        """Collect IPAM related info"""
        self.roles()
        self.vlan_groups()
        self.vlans()
        self.vrfs()
        self.rirs()
        self.aggs()
        self.prefixes()
        self.ip_addresses()

    def virtualization_collections(self):
        """Collect virtualization related info"""
        self.cluster_groups()
        self.cluster_types()
        self.clusters()
        self.virtual_machines()
        self.virtual_interfaces()

    def circuits_collections(self):
        """Collect circuit related info"""
        self.providers()
        self.circuit_types()
        self.circuits()

    def extras_collections(self):
        """Collect extras related info"""
        self.config_contexts()

    def secrets_collections(self):
        """Collect secrets related info"""
        self.secret_roles()
        self.secrets()

    def regions(self):
        """Returns all NetBox regions"""
        netbox_regions = []
        all_regions = self.netbox.dcim.regions.all()
        for region in all_regions:
            region_info = {'data': dict(region), 'state': 'present'}
            netbox_regions.append(region_info)

        self.netbox_data['netbox_regions'] = netbox_regions

    def sites(self):
        """Returns all NetBox sites"""
        netbox_sites = []
        all_sites = self.netbox.dcim.sites.all()
        for site in all_sites:
            site_info = {'data': dict(site), 'state': 'present'}
            netbox_sites.append(site_info)

        self.netbox_data['netbox_sites'] = netbox_sites

    def rack_roles(self):
        """Returns all NetBox rack roles"""
        netbox_rack_roles = []
        all_rack_roles = self.netbox.dcim.rack_roles.all()
        for role in all_rack_roles:
            role_info = {'data': dict(
                role), 'state': 'present'}
            netbox_rack_roles.append(role_info)

        self.netbox_data['netbox_rack_roles'] = netbox_rack_roles

    def rack_groups(self):
        """Returns all NetBox rack groups"""
        netbox_rack_groups = []
        all_rack_groups = self.netbox.dcim.rack_groups.all()
        for group in all_rack_groups:
            group_info = {'data': dict(
                group), 'state': 'present'}
            netbox_rack_groups.append(group_info)

        self.netbox_data['netbox_rack_groups'] = netbox_rack_groups

    def racks(self):
        """Returns all NetBox racks"""
        netbox_racks = []
        all_racks = self.netbox.dcim.racks.all()
        for rack in all_racks:
            rack_info = {'data': dict(
                rack), 'state': 'present'}
            netbox_racks.append(rack_info)

        self.netbox_data['netbox_racks'] = netbox_racks

    def manufacturers(self):
        """Returns all NetBox manufacturers"""
        netbox_manufacturers = []
        all_manufacturers = self.netbox.dcim.manufacturers.all()
        for manufacturer in all_manufacturers:
            manufacturer_info = {'data': dict(
                manufacturer), 'state': 'present'}
            netbox_manufacturers.append(manufacturer_info)

        self.netbox_data['netbox_manufacturers'] = netbox_manufacturers

    def platforms(self):
        """Returns all NetBox platforms"""
        netbox_platforms = []
        all_platforms = self.netbox.dcim.platforms.all()
        for platform in all_platforms:
            platform_info = {'data': dict(platform), 'state': 'present'}
            netbox_platforms.append(platform_info)

        self.netbox_data['netbox_platforms'] = netbox_platforms

    def device_types(self):
        """Returns all NetBox device types"""
        netbox_device_types = []
        all_netbox_device_types = self.netbox.dcim.device_types.all()
        for device_type in all_netbox_device_types:
            device_type_info = {'data': dict(device_type), 'state': 'present'}
            netbox_device_types.append(device_type_info)

        self.netbox_data['netbox_device_types'] = netbox_device_types

    def device_roles(self):
        """Returns all NetBox device roles"""
        netbox_device_roles = []
        all_device_roles = self.netbox.dcim.device_roles.all()
        for role in all_device_roles:
            role_info = {'data': dict(role), 'state': 'present'}
            netbox_device_roles.append(role_info)

        self.netbox_data['netbox_device_roles'] = netbox_device_roles

    def devices(self):
        """Returns all NetBox devices"""
        netbox_devices = []
        all_devices = self.netbox.dcim.devices.all()
        for device in all_devices:
            device_info = {'data': dict(device), 'state': 'present'}
            netbox_devices.append(device_info)

        self.netbox_data['netbox_devices'] = netbox_devices

    def interfaces(self):
        """Returns all NetBox interfaces"""
        netbox_device_interfaces = []
        all_interfaces = self.netbox.dcim.interfaces.all()
        for interface in all_interfaces:
            interface_info = {'data': dict(interface), 'state': 'present'}
            netbox_device_interfaces.append(interface_info)

        self.netbox_data['netbox_device_interfaces'] = netbox_device_interfaces

    def tenant_groups(self):
        """Returns all NetBox tenant groups"""
        netbox_tenant_groups = []
        all_tenant_groups = self.netbox.tenancy.tenant_groups.all()
        for group in all_tenant_groups:
            group_info = {'data': dict(group), 'state': 'present'}
            netbox_tenant_groups.append(group_info)

        self.netbox_data['netbox_tenant_groups'] = netbox_tenant_groups

    def tenants(self):
        """Returns all NetBox tenants"""
        netbox_tenants = []
        all_tenants = self.netbox.tenancy.tenants.all()
        for tenant in all_tenants:
            tenant_info = {'data': dict(tenant), 'state': 'present'}
            netbox_tenants.append(tenant_info)

        self.netbox_data['netbox_tenants'] = netbox_tenants

    def roles(self):
        """Returns all NetBox roles"""
        netbox_ipam_roles = []
        all_roles = self.netbox.ipam.roles.all()
        for role in all_roles:
            role_info = {'data': dict(role), 'state': 'present'}
            netbox_ipam_roles.append(role_info)

        self.netbox_data['netbox_ipam_roles'] = netbox_ipam_roles

    def vlan_groups(self):
        """Returns all NetBox VLAN groups"""
        netbox_vlan_groups = []
        all_vlan_groups = self.netbox.ipam.vlan_groups.all()
        for group in all_vlan_groups:
            group_info = {'data': dict(group), 'state': 'present'}
            netbox_vlan_groups.append(group_info)

        self.netbox_data['netbox_vlan_groups'] = netbox_vlan_groups

    def vlans(self):
        """Returns all NetBox VLANs"""
        netbox_vlans = []
        all_vlans = self.netbox.ipam.vlans.all()
        for vlan in all_vlans:
            vlan_info = {'data': dict(vlan), 'state': 'present'}
            netbox_vlans.append(vlan_info)

        self.netbox_data['netbox_vlans'] = netbox_vlans

    def vrfs(self):
        """Returns all NetBox VRFs"""
        netbox_vrfs = []
        all_vrfs = self.netbox.ipam.vrfs.all()
        for vrf in all_vrfs:
            vrf_info = {'data': dict(vrf), 'state': 'present'}
            netbox_vrfs.append(vrf_info)

        self.netbox_data['netbox_vrfs'] = netbox_vrfs

    def rirs(self):
        """Returns all NetBox RIRs"""
        netbox_rirs = []
        all_rirs = self.netbox.ipam.rirs.all()
        for rir in all_rirs:
            rir_info = {'data': dict(rir), 'state': 'present'}
            netbox_rirs.append(rir_info)

        self.netbox_data['netbox_rirs'] = netbox_rirs

    def aggs(self):
        """Returns all NetBox aggregates"""
        netbox_aggregates = []
        all_aggs = self.netbox.ipam.aggregates.all()
        for agg in all_aggs:
            agg_info = {'data': dict(agg), 'state': 'present'}
            netbox_aggregates.append(agg_info)

        self.netbox_data['netbox_aggregates'] = netbox_aggregates

    def prefixes(self):
        """Returns all NetBox prefixes"""
        netbox_prefixes = []
        all_prefixes = self.netbox.ipam.prefixes.all()
        for prefix in all_prefixes:
            prefix_info = {'data': dict(prefix), 'state': 'present'}
            netbox_prefixes.append(prefix_info)

        self.netbox_data['netbox_prefixes'] = netbox_prefixes

    def ip_addresses(self):
        """Returns all NetBox IP addresses"""
        netbox_ip_addresses = []
        all_ip_addresses = self.netbox.ipam.ip_addresses.all()
        for address in all_ip_addresses:
            address_info = {'data': dict(address), 'state': 'present'}
            netbox_ip_addresses.append(address_info)

        self.netbox_data['netbox_ip_addresses'] = netbox_ip_addresses

    def cluster_groups(self):
        """Returns all NetBox cluster groups"""
        netbox_cluster_groups = []
        all_cluster_groups = self.netbox.virtualization.cluster_groups.all()
        for group in all_cluster_groups:
            group_info = {'data': dict(group), 'state': 'present'}
            netbox_cluster_groups.append(group_info)

        self.netbox_data['netbox_cluster_groups'] = netbox_cluster_groups

    def cluster_types(self):
        """Returns all NetBox cluster types"""
        netbox_cluster_types = []
        all_cluster_types = self.netbox.virtualization.cluster_types.all()
        for cluster_type in all_cluster_types:
            cluster_info = {'data': dict(cluster_type), 'state': 'present'}
            netbox_cluster_types.append(cluster_info)

        self.netbox_data['netbox_cluster_types'] = netbox_cluster_types

    def clusters(self):
        """Returns all NetBox clusters"""
        netbox_clusters = []
        all_clusters = self.netbox.virtualization.clusters.all()
        for cluster in all_clusters:
            cluster_info = {'data': dict(cluster), 'state': 'present'}
            netbox_clusters.append(cluster_info)

        self.netbox_data['netbox_clusters'] = netbox_clusters

    def virtual_machines(self):
        """Returns all NetBox virtual machines"""
        netbox_virtual_machines = []
        all_vms = self.netbox.virtualization.virtual_machines.all()
        for virtual_machine in all_vms:
            virtual_machine_info = {'data': dict(
                virtual_machine), 'state': 'present'}
            netbox_virtual_machines.append(virtual_machine_info)

        self.netbox_data['netbox_virtual_machines'] = netbox_virtual_machines

    def virtual_interfaces(self):
        """Returns all NetBox virtual machines"""
        netbox_virtual_interfaces = []
        all_virtual_interfaces = self.netbox.virtualization.interfaces.all()
        for interface in all_virtual_interfaces:
            interface_info = {'data': dict(
                interface), 'state': 'present'}
            netbox_virtual_interfaces.append(interface_info)

        self.netbox_data['netbox_virtual_interfaces'] = netbox_virtual_interfaces

    def providers(self):
        """Returns all NetBox circuit providers"""
        netbox_providers = []
        all_providers = self.netbox.circuits.providers.all()
        for provider in all_providers:
            provider_info = {'data': dict(
                provider), 'state': 'present'}
            netbox_providers.append(provider_info)

        self.netbox_data['netbox_providers'] = netbox_providers

    def circuit_types(self):
        """Returns all NetBox circuit types"""
        netbox_circuit_types = []
        all_circuit_types = self.netbox.circuits.circuit_types.all()
        for circuit_type in all_circuit_types:
            circuit_type_info = {'data': dict(
                circuit_type), 'state': 'present'}
            netbox_circuit_types.append(circuit_type_info)

        self.netbox_data['netbox_circuit_types'] = netbox_circuit_types

    def circuits(self):
        """Returns all NetBox circuits"""
        netbox_circuits = []
        all_circuit = self.netbox.circuits.circuits.all()
        for circuit in all_circuit:
            circuit_info = {'data': dict(
                circuit), 'state': 'present'}
            netbox_circuits.append(circuit_info)

        self.netbox_data['netbox_circuits'] = netbox_circuits

    def secret_roles(self):
        """Returns all NetBox secret roles"""
        netbox_secret_roles = []
        all_secret_roles = self.netbox.secrets.secret_roles.all()
        for role in all_secret_roles:
            role_info = {'data': dict(
                role), 'state': 'present'}
            netbox_secret_roles.append(role_info)

        self.netbox_data['netbox_secret_roles'] = netbox_secret_roles

    def secrets(self):
        """Returns all NetBox secrets"""
        netbox_secrets = []
        all_secrets = self.netbox.secrets.secrets.all()
        for secret in all_secrets:
            secret_info = {'data': dict(
                secret), 'state': 'present'}
            netbox_secrets.append(secret_info)

        self.netbox_data['netbox_secrets'] = netbox_secrets

    def config_contexts(self):
        """Returns all NetBox config contexts"""
        netbox_config_contexts = []
        all_config_contexts = self.netbox.extras.config_contexts.all()
        for context in all_config_contexts:
            context_info = {'data': dict(context), 'state': 'present'}
            netbox_config_contexts.append(context_info)

        self.netbox_data['netbox_config_contexts'] = netbox_config_contexts


class NetBoxToAnsible:
    """Main NetBox to Ansible class"""

    def __init__(self, netbox_data):
        self.netbox_data = netbox_data
        self.ansible_data = {}

    def data(self):
        """Translate NetBox data to Ansible constructs"""
        # DCIM
        self.dcim_translations()
        # Tenancy
        self.tenancy_translations()
        # IPAM
        self.ipam_translations()
        # Virtualization
        self.virtualization_translations()
        # Circuits
        self.circuits_translations()
        # Secrets
        self.secrets_translations()
        # Extras
        self.extras_translations()

        return self.ansible_data

    def dcim_translations(self):
        """Translate DCIM related info"""
        self.regions()
        self.sites()
        self.rack_roles()
        self.rack_groups()
        self.racks()
        self.manufacturers()
        self.platforms()
        self.device_types()
        self.device_roles()
        self.devices()
        self.interfaces()

    def tenancy_translations(self):
        """Translate tenancy related info"""
        self.tenant_groups()
        self.tenants()

    def ipam_translations(self):
        """Translate IPAM related info"""
        self.roles()
        self.vlan_groups()
        self.vlans()
        self.vrfs()
        self.rirs()
        self.aggs()
        self.prefixes()
        self.ip_addresses()

    def virtualization_translations(self):
        """Translate virtualization related info"""
        self.cluster_groups()
        self.cluster_types()
        self.clusters()
        self.virtual_machines()
        self.virtual_interfaces()

    def circuits_translations(self):
        """Translate circuit related info"""
        # self.providers()
        # self.circuit_types()
        # self.circuits()

    def extras_translations(self):
        """Translate extras related info"""
        # self.config_contexts()

    def secrets_translations(self):
        """Translate secrets related info"""
        # self.secret_roles()
        # self.secrets()

    def roles(self):
        """Extract NetBox roles"""
        netbox_ipam_roles = []
        for role in self.netbox_data['netbox_ipam_roles']:
            data = role['data']
            role_info = {
                'data': {'name': data['name'], 'weight': data['weight']},
                'state': role['state']}
            netbox_ipam_roles.append(role_info)

        self.ansible_data['netbox_ipam_roles'] = netbox_ipam_roles

    def vlan_groups(self):
        """Extract NetBox VLAN groups"""
        netbox_vlan_groups = []
        for group in self.netbox_data['netbox_vlan_groups']:
            data = group['data']
            # Update site with name only if defined
            if data['site'] is not None:
                data['site'] = data['site']['name']
            group_info = {
                'data': {'name': data['name'], 'site': data['site']},
                'state': group['state']}
            netbox_vlan_groups.append(group_info)

        self.ansible_data['netbox_vlan_groups'] = netbox_vlan_groups

    def vlans(self):
        """Extract NetBox VLANs"""
        netbox_vlans = []
        for vlan in self.netbox_data['netbox_vlans']:
            data = vlan['data']
            # Update site with name only if defined
            if data['site'] is not None:
                data['site'] = data['site']['name']
            vlan_info = {
                'data': {'name': data['name'], 'site': data['site']},
                'state': vlan['state']}
            netbox_vlans.append(vlan_info)

        self.ansible_data['netbox_vlans'] = netbox_vlans

    def vrfs(self):
        """Extract NetBox VRFs"""
        netbox_vrfs = []
        for vrf in self.netbox_data['netbox_vrfs']:
            data = vrf['data']
            # Update tenant with name only if defined
            if data['tenant'] is not None:
                data['tenant'] = data['tenant']['name']
            vrf_info = {
                'data': {'name': data['name'], 'rd': data['rd'],
                         'enforce_unique': data['enforce_unique'],
                         'description': data['description'],
                         'tags': data['tags'],
                         'custom_fields': data['custom_fields'],
                         'tenant': data['tenant']},
                'state': vrf['state']}
            netbox_vrfs.append(vrf_info)

        self.ansible_data['netbox_vrfs'] = netbox_vrfs

    def rirs(self):
        """Extract NetBox RIRs"""
        netbox_rirs = []
        for rir in self.netbox_data['netbox_rirs']:
            data = rir['data']
            rir_info = {
                'data': {'name': data['name'],
                         'is_private': data['is_private']},
                'state': rir['state']}
            netbox_rirs.append(rir_info)

        self.ansible_data['netbox_rirs'] = netbox_rirs

    def aggs(self):
        """Extract NetBox aggregates"""
        netbox_aggregates = []
        for agg in self.netbox_data['netbox_aggregates']:
            data = agg['data']
            if data['rir'] is not None:
                data['rir'] = data['rir']['name']
            agg_info = {
                'data': {'custom_fields': data['custom_fields'],
                         'description': data['description'],
                         'prefix': data['prefix'],
                         'rir': data['rir'],
                         'tags': data['tags']},
                'state': agg['state']}
            netbox_aggregates.append(agg_info)

        self.ansible_data['netbox_aggregates'] = netbox_aggregates

    def prefixes(self):
        """Extract NetBox prefixes"""
        netbox_prefixes = []
        for prefix in self.netbox_data['netbox_prefixes']:
            data = prefix['data']
            # Update role with name only if defined
            if data['role'] is not None:
                data['role'] = data['role']['name']
            # Update site with name only if defined
            if data['site'] is not None:
                data['site'] = data['site']['name']
            # Update tenant with name only if defined
            if data['tenant'] is not None:
                data['tenant'] = data['tenant']['name']
            # Update vrf with name only if defined
            if data['vrf'] is not None:
                data['vrf'] = data['vrf']['name']
            prefix_info = {
                'data': {'custom_fields': data['custom_fields'],
                         'description': data['description'],
                         'family': data['family']['value'],
                         'is_pool': data['is_pool'],
                         'prefix': data['prefix'],
                         'site': data['site'],
                         'status': data['status']['label'],
                         'prefix_role': data['role'],
                         'tags': data['tags'],
                         'tenant': data['tenant'],
                         'vlan': data['vlan'],
                         'vrf': data['vrf']
                         }, 'state': prefix['state']}
            netbox_prefixes.append(prefix_info)

        self.ansible_data['netbox_prefixes'] = netbox_prefixes

    def ip_addresses(self):
        """Extract NetBox IP addresses"""
        netbox_ip_addresses = []
        for address in self.netbox_data['netbox_ip_addresses']:
            data = address['data']
            # Update interface with name and device
            if data['interface'] is not None:
                interface = data['interface']
                data['interface'] = {
                    'name': interface['name']
                }
                try:
                    data['interface']['device'] = interface['device']['name']
                except TypeError:
                    pass
                if interface['virtual_machine'] is not None:
                    data['interface']['virtual_machine'] = interface[
                        'virtual_machine']['name']
            # Update nat_inside
            if data['nat_inside'] is not None:
                data['nat_inside'] = {
                    'address': data['nat_inside']['address'],
                    'vrf': data['nat_inside']['vrf']
                }
            # Update tenant with name only if defined
            if data['tenant'] is not None:
                data['tenant'] = data['tenant']['name']
            # Update vrf with name only if defined
            if data['vrf'] is not None:
                data['vrf'] = data['vrf']['name']
            address_info = {'data': {'address': data['address'],
                                     'custom_fields': data['custom_fields'],
                                     'description': data['description'],
                                     'family': data['family']['value'],
                                     'interface': data['interface'],
                                     'nat_inside': data['nat_inside'],
                                     'status': data['status']['label'],
                                     'tags': data['tags'],
                                     'tenant': data['tenant'],
                                     'vrf': data['vrf']},
                            'state': address['state']}

            if data['role'] is not None:
                address_info['data']['role'] = data['role']['label']

            netbox_ip_addresses.append(address_info)

        self.ansible_data['netbox_ip_addresses'] = netbox_ip_addresses

    def tenant_groups(self):
        """Extract NetBox tenant groups"""
        netbox_tenant_groups = []
        for group in self.netbox_data['netbox_tenant_groups']:
            data = group['data']
            group_info = {
                'data': {'name': data['name']}, 'state': group['state']}
            netbox_tenant_groups.append(group_info)

        self.ansible_data['netbox_tenant_groups'] = netbox_tenant_groups

    def tenants(self):
        """Extract NetBox tenant groups"""
        netbox_tenants = []
        for tenant in self.netbox_data['netbox_tenants']:
            data = tenant['data']
            # Update group with name only if defined
            if data['group'] is not None:
                data['group'] = data['group']['name']
            tenant_info = {
                'data': {'description': data['description'],
                         'comments': data['comments'],
                         'custom_fields': data['custom_fields'],
                         'name': data['name'],
                         'slug': data['slug'],
                         'tenant_group': data['group'],
                         'tags': data['tags']},
                'state': tenant['state']}
            netbox_tenants.append(tenant_info)

        self.ansible_data['netbox_tenants'] = netbox_tenants

    def regions(self):
        """Extract NetBox regions"""
        netbox_regions = []
        for region in self.netbox_data['netbox_regions']:
            data = region['data']
            # Update parent region with name only if defined
            if data['parent'] is not None:
                data['parent'] = data['parent']['name']
            region_info = {
                'data': {'name': data['name'],
                         'parent_region': data['parent']},
                'state': region['state']}
            netbox_regions.append(region_info)

        self.ansible_data['netbox_regions'] = netbox_regions

    def sites(self):
        """Extract NetBox sites"""
        netbox_sites = []
        for site in self.netbox_data['netbox_sites']:
            data = site['data']
            # Update region with name only if defined
            if data['region'] is not None:
                data['region'] = data['region']['name']
            # Update tenant with name only if defined
            if data['tenant'] is not None:
                data['tenant'] = data['tenant']['name']
            site_info = {
                'data': {'asn': data['asn'],
                         'comments': data['comments'],
                         'contact_name': data['contact_name'],
                         'contact_phone': data['contact_phone'],
                         'contact_email': data['contact_email'],
                         'custom_fields': data['custom_fields'],
                         'description': data['description'],
                         'facility': data['facility'],
                         'latitude': data['latitude'],
                         'longitude': data['longitude'],
                         'name': data['name'],
                         'physical_address': data['physical_address'],
                         'shipping_address': data['shipping_address'],
                         'slug': data['slug'],
                         'region': data['region'],
                         'status': data['status']['label'],
                         'tags': data['tags'],
                         'tenant': data['tenant'],
                         'time_zone': data['time_zone'],
                         }, 'state': site['state']}
            netbox_sites.append(site_info)

        self.ansible_data['netbox_sites'] = netbox_sites

    def rack_roles(self):
        """Extract NetBox rack roles"""
        netbox_rack_roles = []
        for role in self.netbox_data['netbox_rack_roles']:
            data = role['data']
            role_info = {'data': {'name': data['name'],
                                  'color': data['color']},
                         'state': role['state']}
            netbox_rack_roles.append(role_info)

        self.ansible_data['netbox_rack_roles'] = netbox_rack_roles

    def rack_groups(self):
        """Extract NetBox rack groups"""
        netbox_rack_groups = []
        for group in self.netbox_data['netbox_rack_groups']:
            data = group['data']
            # Update site with name only if defined
            if data['site'] is not None:
                data['site'] = data['site']['name']
            group_info = {
                'data': {'name': data['name'], 'site': data['site']},
                'state': group['state']}
            netbox_rack_groups.append(group_info)

        self.ansible_data['netbox_rack_groups'] = netbox_rack_groups

    def racks(self):
        """Extract NetBox racks"""
        netbox_racks = []
        for rack in self.netbox_data['netbox_racks']:
            data = rack['data']
            # Update site with name only if defined
            if data['site'] is not None:
                data['site'] = data['site']['name']
            # Update rack group with name only if defined
            if data['group'] is not None:
                data['group'] = data['group']['name']
            # Update tenant with name only if defined
            if data['tenant'] is not None:
                data['tenant'] = data['tenant']['name']
            # Update type with label only if defined
            if data['type'] is not None:
                data['type'] = data['type']['label']
            # Update width with value only if defined
            if data['width'] is not None:
                data['width'] = data['width']['value']
            rack_info = {
                'data': {'asset_tag': data['asset_tag'],
                         'comments': data['comments'],
                         'custom_fields': data['custom_fields'],
                         'desc_units': data['desc_units'],
                         'name': data['name'],
                         'facility_id': data['facility_id'],
                         'outer_depth': data['outer_depth'],
                         'outer_width': data['outer_width'],
                         'rack_group': data['group'],
                         'rack_role': data['role'],
                         'serial': data['serial'],
                         'site': data['site'],
                         'status': data['status']['label'],
                         'tags': data['tags'],
                         'tenant': data['tenant'],
                         'type': data['type'],
                         'u_height': data['u_height'],
                         'width': data['width']
                         }, 'state': rack['state']}

            if data['outer_unit'] is not None:
                rack_info['data']['outer_unit'] = data['outer_unit']

            netbox_racks.append(rack_info)

        self.ansible_data['netbox_racks'] = netbox_racks

    def manufacturers(self):
        """Extract NetBox manufacturers"""
        netbox_manufacturers = []
        for manufacturer in self.netbox_data['netbox_manufacturers']:
            data = manufacturer['data']
            manufacturer_info = {'data': {'name': data['name']},
                                 'state': manufacturer['state']}
            netbox_manufacturers.append(manufacturer_info)

        self.ansible_data['netbox_manufacturers'] = netbox_manufacturers

    def platforms(self):
        """Extract NetBox platforms"""
        netbox_platforms = []
        for platform in self.netbox_data['netbox_platforms']:
            data = platform['data']
            # Update manufacturer with name only if defined
            if data['manufacturer'] is not None:
                data['manufacturer'] = data['manufacturer']['name']
            platform_info = {'data': {'manufacturer': data['manufacturer'],
                                      'name': data['name'],
                                      'napalm_driver': data['napalm_driver'],
                                      'napalm_args': data['napalm_args']},
                             'state': platform['state']}
            netbox_platforms.append(platform_info)

        self.ansible_data['netbox_platforms'] = netbox_platforms

    def device_types(self):
        """Extract NetBox device types"""
        netbox_device_types = []
        for device_type in self.netbox_data['netbox_device_types']:
            data = device_type['data']
            # Update manufacturer with name only if defined
            if data['manufacturer'] is not None:
                data['manufacturer'] = data['manufacturer']['name']
            device_type_info = {
                'data': {
                    'comments': data['comments'],
                    'custom_fields': data['custom_fields'],
                    'is_full_depth': data['is_full_depth'],
                    'manufacturer': data['manufacturer'],
                    'model': data['model'],
                    'part_number': data['part_number'],
                    'slug': data['slug'],
                    'tags': data['tags'],
                    'u_height': data['u_height']
                },
                'state': device_type['state']}

            if data['subdevice_role'] is not None:
                device_type_info['data']['subdevice_role'] = data[
                    'subdevice_role']['label']

            netbox_device_types.append(device_type_info)

        self.ansible_data['netbox_device_types'] = netbox_device_types

    def device_roles(self):
        """Extract NetBox device roles"""
        netbox_device_roles = []
        for role in self.netbox_data['netbox_device_roles']:
            data = role['data']
            role_info = {'data': {
                'name': data['name'],
                'color': data['color'],
                'vm_role': data['vm_role']
            }, 'state': role['state']}
            netbox_device_roles.append(role_info)

        self.ansible_data['netbox_device_roles'] = netbox_device_roles

    def devices(self):
        """Extract NetBox devices"""
        netbox_devices = []
        for device in self.netbox_data['netbox_devices']:
            data = device['data']
            device_info = {'data': {
                'name': data['name'],
                'platform': data['platform'],
                'serial': data['serial'],
                'asset_tag': data['asset_tag'],
                'position': data['position'],
                'status': data['status']['label'],
                'comments': data['comments'],
                'tags': data['tags'],
                'custom_fields': data['custom_fields']
            }, 'state': device['state']}

            # Update cluster with name only if defined
            if data['cluster'] is not None:
                device_info['data']['cluster'] = data['cluster']['name']
            # Update device_role with name only if defined
            if data['device_role'] is not None:
                device_info['data']['device_role'] = data['device_role'][
                    'name']
            # Update device_type with name only if defined
            if data['device_type'] is not None:
                device_info['data']['device_type'] = data['device_type'][
                    'model']
            # Update face with label only if defined
            if data['face'] is not None:
                device_info['data']['face'] = data['face']['label']
            # Update rack with name only if defined
            if data['rack'] is not None:
                device_info['data']['rack'] = data['rack']['name']
            # Update site with name only if defined
            if data['site'] is not None:
                device_info['data']['site'] = data['site']['name']
            # Update tenant with name only if defined
            if data['tenant'] is not None:
                device_info['data']['tenant'] = data['tenant']['name']

            netbox_devices.append(device_info)

        self.ansible_data['netbox_devices'] = netbox_devices

    def interfaces(self):
        """Extract NetBox interfaces"""
        netbox_device_interfaces = []
        for interface in self.netbox_data['netbox_device_interfaces']:
            data = interface['data']
            if data['form_factor'] is not None:
                data['form_factor'] = data['form_factor']['label']
            if data['mode'] is not None:
                data['mode'] = data['mode']['label']
            interface_info = {'data': {
                'description': data['description'],
                'device': data['device']['name'],
                'enabled': data['enabled'],
                'form_factor': data['form_factor'],
                'lag': data['lag'],
                'mac_address': data['mac_address'],
                'mgmt_only': data['mgmt_only'],
                'mode': data['mode'],
                'mtu': data['mtu'],
                'name': data['name'],
                'tagged_vlans': data['tagged_vlans'],
                'tags': data['tags'],
                'untagged_vlan': data['untagged_vlan']
            }, 'state': interface['state']}
            netbox_device_interfaces.append(interface_info)

        self.ansible_data[
            'netbox_device_interfaces'] = netbox_device_interfaces

    def cluster_groups(self):
        """Extract NetBox cluster groups"""
        netbox_cluster_groups = []
        for group in self.netbox_data['netbox_cluster_groups']:
            data = group['data']
            group_info = {'data': {'name': data['name']},
                          'state': group['state']}
            netbox_cluster_groups.append(group_info)

        self.ansible_data['netbox_cluster_groups'] = netbox_cluster_groups

    def cluster_types(self):
        """Extract NetBox cluster types"""
        netbox_cluster_types = []
        for cluster_type in self.netbox_data['netbox_cluster_types']:
            data = cluster_type['data']
            cluster_type_info = {'data': {'name': data['name']},
                                 'state': cluster_type['state']}
            netbox_cluster_types.append(cluster_type_info)

        self.ansible_data['netbox_cluster_types'] = netbox_cluster_types

    def clusters(self):
        """Extract NetBox clusters"""
        netbox_clusters = []
        for cluster in self.netbox_data['netbox_clusters']:
            data = cluster['data']
            # Update site with name only if defined
            if data['site'] is not None:
                data['site'] = data['site']['name']
            cluster_info = {'data': {'comments': data['comments'],
                                     'custom_fields': data['custom_fields'],
                                     'name': data['name'],
                                     'cluster_group': data['group']['name'],
                                     'cluster_type': data['type']['name'],
                                     'site': data['site'],
                                     'tags': data['tags']},
                            'state': cluster['state']}
            netbox_clusters.append(cluster_info)

        self.ansible_data['netbox_clusters'] = netbox_clusters

    def virtual_machines(self):
        """Extract NetBox virtual machines"""
        netbox_virtual_machines = []
        for virtual_machine in self.netbox_data['netbox_virtual_machines']:
            data = virtual_machine['data']
            vm_info = {'data': {'disk': data['disk'],
                                'memory': data['memory'],
                                'name': data['name'],
                                'platform': data['platform']['name'],
                                'site': data['site'],
                                'vcpus': data['vcpus'],
                                'status': data['status']['label'],
                                'tags': data['tags'],
                                'custom_fields': data['custom_fields']
                                },
                       'state': virtual_machine['state']}

            # Update cluster with name only if defined
            if data['cluster'] is not None:
                vm_info['data']['cluster'] = data['cluster']['name']
            # Update virtual_machine_role with name only if defined
            if data['role'] is not None:
                vm_info['data']['virtual_machine_role'] = data['role']['name']
            # Update site with name only if defined
            if data['site'] is not None:
                vm_info['data']['site'] = data['site']['name']
            # Update tenant with name only if defined
            if data['tenant'] is not None:
                vm_info['data']['tenant'] = data['tenant']['name']

            netbox_virtual_machines.append(vm_info)

        self.ansible_data['netbox_virtual_machines'] = netbox_virtual_machines

    def virtual_interfaces(self):
        """Extract NetBox virtual interfaces"""
        netbox_virtual_interfaces = []
        for interface in self.netbox_data['netbox_virtual_interfaces']:
            data = interface['data']
            if data['form_factor'] is not None:
                data['form_factor'] = data['form_factor']['label']
            if data['mode'] is not None:
                data['mode'] = data['mode']['label']
            interface_info = {'data': {
                'description': data['description'],
                'enabled': data['enabled'],
                'mac_address': data['mac_address'],
                'mode': data['mode'],
                'mtu': data['mtu'],
                'name': data['name'],
                'tagged_vlans': data['tagged_vlans'],
                'tags': data['tags'],
                'untagged_vlan': data['untagged_vlan'],
                'virtual_machine': data['virtual_machine']['name']
            }, 'state': interface['state']}
            netbox_virtual_interfaces.append(interface_info)

        self.ansible_data[
            'netbox_virtual_interfaces'] = netbox_virtual_interfaces


if __name__ == '__main__':
    main()
