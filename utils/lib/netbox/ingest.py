"""lib/netbox/ingest.py"""


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
        self.cables()
        self.console_connections()
        self.inventory_items()

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

    def cables(self):
        """Returns all NetBox cables"""
        netbox_cables = []
        all_cables = self.netbox.dcim.cables.all()
        for cable in all_cables:
            cable_info = {'data': dict(cable), 'state': 'present'}
            netbox_cables.append(cable_info)

        self.netbox_data['netbox_cables'] = netbox_cables

    def console_connections(self):
        """Returns all NetBox console connections"""
        netbox_console_connections = []
        all_console_connections = self.netbox.dcim.console_connections.all()
        for connection in all_console_connections:
            connection_info = {'data': dict(connection), 'state': 'present'}
            netbox_console_connections.append(connection_info)

        self.netbox_data[
            'netbox_console_connections'] = netbox_console_connections

    def inventory_items(self):
        """Returns all NetBox inventory items"""
        netbox_inventory_items = []
        all_inventory_items = self.netbox.dcim.inventory_items.all()
        for item in all_inventory_items:
            item_info = {'data': dict(item), 'state': 'present'}
            netbox_inventory_items.append(item_info)

        self.netbox_data['netbox_inventory_items'] = netbox_inventory_items

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
