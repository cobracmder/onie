
import re

OPTIONS = {'onie_installer': str,
           'onie_updater': str,
           'onie_arch': str,
           'onie_switch_asic': str,
           'onie_vendor': str,
           'onie_machine': str,
           'onie_machine_rev': str,
           'http_binary': str,
           'http_user': str,
           'http_group': str,
           'http_port': int,
           'tftp_binary': str,
           'tftp_user': str,
           'tftp_group': str,
           'dhcp_binary': str,
           'dhcp_user': str,
           'dhcp_group': str,
           'dhcp_lease_time': int,
           'dhcp_max_lease_time': int,
           'dhcp_domain_name': str,
           'dhcp_dns_server': str,
           'dhcp_gateway': str,
           'dhcp_next_server': str}
PRETTY_OPTIONS = sorted(OPTIONS.keys())
MAC_REGEX = re.compile('([a-fA-F0-9]{2}[:]?){6}')
