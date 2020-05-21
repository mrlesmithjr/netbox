"""lib/netbox/ansible.py"""


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
        self.inventory_items()

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

            # This is related to https://github.com/netbox-community/ansible_modules/issues/193
            form_factor = data.get('form_factor')
            int_type = data.get('type')
            if int_type is not None:
                data['type'] = data['type']['label']
            elif form_factor is not None:
                data['type'] = data['form_factor']['label']

            if data['mode'] is not None:
                data['mode'] = data['mode']['label']
            interface_info = {'data': {
                'description': data['description'],
                'device': data['device']['name'],
                'enabled': data['enabled'],
                'type': data['type'],
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

    def inventory_items(self):
        """Extract NetBox inventory items"""
        netbox_inventory_items = []
        for item in self.netbox_data['netbox_inventory_items']:
            data = item['data']
            if data['manufacturer'] is not None:
                data['manufacturer'] = data['manufacturer']['name']
            item_info = {
                'data': {'device': data['device']['name'],
                         'name': data['name'],
                         'part_id': data['part_id'],
                         'manufacturer': data['manufacturer'],
                         'serial': data['serial'],
                         'asset_tag': data['asset_tag'],
                         'description': data['description'],
                         'tags': data['tags']
                         }, 'state': item['state']}
            netbox_inventory_items.append(item_info)

        self.ansible_data['netbox_inventory_items'] = netbox_inventory_items

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
