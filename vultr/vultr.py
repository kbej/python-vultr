import requests
import json as json_module

API_ENDPOINT = 'https://api.vultr.com'


class VultrError(RuntimeError):
    pass


class Vultr(object):

    def __init__(self, api_key):
        self.endpoint = API_ENDPOINT
        self.api_key = api_key

    def snapshot_list(self):
        """
        /v1/snapshot/list
        GET - account
        List all snapshots on the current account

        Example Request:
        GET https://api.vultr.com/v1/snapshot/list?api_key=EXAMPLE
        Example Response:
        {
            "5359435d28b9a": {
                "SNAPSHOTID": "5359435d28b9a",
                "date_created": "2014-04-18 12:40:40",
                "description": "Test snapshot",
                "size": "42949672960",
                "status": "complete"
            },
            "5359435dc1df3": {
                "SNAPSHOTID": "5359435dc1df3",
                "date_created": "2014-04-22 16:11:46",
                "description": "",
                "size": "10000000",
                "status": "complete"
            }
        }
        Parameters:
        No Parameters
        """
        pass

    def snapshot_destroy(self, snapshot_id):
        """
        /v1/snapshot/destroy
        POST - account
        Destroy (delete) a snapshot. There is no going back from this call.

        Example Request:
        POST https://api.vultr.com/v1/snapshot/destroy?api_key=EXAMPLE
        Example Response:
        No response, check HTTP result code
        Parameters:
        SNAPSHOTID string Unique identifier for this snapshot.  These can be
        found using the v1/snapshot/list call.
        """
        pass

    def snapshot_create(self, sub_id):
        """
        /v1/snapshot/create
        POST - account
        Create a snapshot from an existing virtual machine. The virtual machine
        does not need to be stopped.

        Example Request:
        POST https://api.vultr.com/v1/snapshot/create?api_key=APIKEY
        SUBID=1312965
        Example Response:
        {
            "SNAPSHOTID": "544e52f31c706"
        }
        Parameters:
        SUBID integer Identifier of the virtual machine to create a snapshot
        from.  See v1/server/list
        description string (optional) Description of snapshot contents
        """
        pass

    def iso_list(self):
        """
        /v1/iso/list
        GET - account
        List all ISOs currently available on this account

        Example Request:
        GET https://api.vultr.com/v1/iso/list?api_key=EXAMPLE
        Example Response:
        {
            "24": {
                "ISOID": 24,
                "date_created": "2014-04-01 14:10:09",
                "filename": "CentOS-6.5-x86_64-minimal.iso",
                "size": 9342976,
                "md5sum": "ec0669895a250f803e1709d0402fc411"
            }
        }
        Parameters:
        No Parameters
        """
        pass

    def plans_list(self):
        """
        /v1/plans/list
        GET - public
        Retrieve a list of all active plans. Plans that are no longer available
        will not be shown. The 'windows' field is no longer in use, and will
        always be false. Windows licenses will be automatically added to any
        plan as necessary.

        Example Request:
        GET https://api.vultr.com/v1/plans/list
        Example Response:
        {
            "1": {
                "VPSPLANID": "1",
                "name": "Starter",
                "vcpu_count": "1",
                "ram": "512",
                "disk": "20",
                "bandwidth": "1",
                "price_per_month": "5.00",
                "windows": false
            },
            "2": {
                "VPSPLANID": "2",
                "name": "Basic",
                "vcpu_count": "1",
                "ram": "1024",
                "disk": "30",
                "bandwidth": "2",
                "price_per_month": "8.00",
                "windows": false
            }
        }
        Parameters:
        No Parameters
        """
        pass

    def regions_list(self):
        """
        /v1/regions/list
        GET - public
        Retrieve a list of all active regions. Note that just because a region
        is listed here, does not mean that there is room for new servers.

        Example Request:
        GET https://api.vultr.com/v1/regions/list
        Example Response:
        {
            "1": {
                "DCID": "1",
                "name": "New Jersey",
                "country": "US",
                "continent": "North America",
                "state": "NJ"
            },
            "2": {
                "DCID": "2",
                "name": "Chicago",
                "country": "US",
                "continent": "North America",
                "state": "IL"
            }
        }
        Parameters:
        No Parameters
        """

    def regions_availability(self, dc_id):
        """
        /v1/regions/availability
        GET - public
        Retrieve a list of the VPSPLANIDs currently available in this location.

        Example Request:
        GET https://api.vultr.com/v1/regions/availability?DCID=1
        Example Response:
        [
            40,
            11,
            45,
            29,
            41,
            61
        ]
        Parameters:
        DCID integer Location to check availability of
        """
        pass

    def startupscript_list(self):
        """
        /v1/startupscript/list
        GET - account
        List all startup scripts on the current account. 'boot' type scripts
        are executed by the server's operating system on the first boot. 'pxe'
        type scripts are executed by iPXE when the server itself starts up.

        Example Request:
        GET https://api.vultr.com/v1/startupscript/list?api_key=EXAMPLE
        Example Response:
        {
            "3": {
                "SCRIPTID": "3",
                "date_created": "2014-05-21 15:27:18",
                "date_modified": "2014-05-21 15:27:18",
                "name": "test ",
                "type": "boot",
                "script": "#!/bin/bash echo Hello World > /root/hello"
            },
            "5": {
                "SCRIPTID": "5",
                "date_created": "2014-08-22 15:27:18",
                "date_modified": "2014-09-22 15:27:18",
                "name": "test ",
                "type": "pxe",
                "script": "#!ipxe\necho Hello World\nshell"
            }
        }
        Parameters:
        No Parameters
        """

    def startupscript_destroy(self):
        """
        /v1/startupscript/destroy
        POST - account
        Remove a startup script

        Example Request:
        POST https://api.vultr.com/v1/startupscript/destroy?api_key=EXAMPLE
        Example Response:
        No response, check HTTP result code
        Parameters:
        SCRIPTID string Unique identifier for this startup script.  These can
        be found using the v1/startupscript/list call.
        """
        pass

    def startupscript_create(self):
        """
        /v1/startupscript/create
        POST - account
        Create a startup script

        Example Request:
        POST https://api.vultr.com/v1/startupscript/create?api_key=APIKEY
        name="my first script"
        script="#!/bin/bash\necho hello world > /root/hello"
        Example Response:
        {
            "SCRIPTID": 5
        }
        Parameters:
        name string Name of the newly created startup script
        script string Startup script contents
        type string boot|pxe Type of startup script.  Default is 'boot'
        """
        pass

    def startupscript_update(self):
        """
        /v1/startupscript/update
        POST - account
        Update an existing startup script

        Example Request:
        POST https://api.vultr.com/v1/startupscript/update?api_key=APIKEY
        SCRIPTID=5
        name="my first script"
        script="#!/bin/bash\necho hello world > /root/hello"
        Example Response:
        No response, check HTTP result code
        Parameters:
        SCRIPTID integer SCRIPTID of script to update (see
            /v1/startupscript/list)
        name string (optional) New name for the startup script
        script string (optional) New startup script contents
        """
        pass

    def dns_list(self):
        """
        /v1/dns/list
        GET - account
        List all domains associated with the current account

        Example Request:
        GET https://api.vultr.com/v1/dns/list?api_key=EXAMPLE
        Example Response:
        [
            {
                "domain": "example.com",
                "date_created": "2014-12-11 16:20:59"
            }
        ]
        Parameters:
        No Parameters
        """
        pass

    def dns_records(self):
        """
        /v1/dns/records
        GET - account
        List all the records associated with a particular domain

        Example Request:
        GET https://api.vultr.com/v1/dns/records?api_key=EXAMPLE
            &domain=example.com
        Example Response:
        [
            {
                "type": "A",
                "name": "",
                "data": "127.0.0.1",
                "priority": 0,
                "RECORDID": 1265276
            },
            {
                "type": "CNAME",
                "name": "*",
                "data": "example.com",
                "priority": 0,
                "RECORDID": 1265277
            }
        ]
        Parameters:
        domain string Domain to list records for
        """
        pass

    def dns_create_domain(self):
        """
        /v1/dns/create_domain
        POST - account
        Create a domain name in DNS

        Example Request:
        POST https://api.vultr.com/v1/dns/create_domain?api_key=EXAMPLE
        domain=example.com
        serverip=127.0.0.1
        Example Response:
        No response, check HTTP result code
        Parameters:
        domain string Domain name to create
        serverip string Server IP to use when creating default records (A and
            MX)
        """
        pass

    def dns_delete_domain(self):
        """
        /v1/dns/delete_domain
        POST - account
        Delete a domain name (and all associated records)

        Example Request:
        POST https://api.vultr.com/v1/dns/delete_domain?api_key=EXAMPLE
        domain=example.com
        Example Response:
        No response, check HTTP result code
        Parameters:
        domain string Domain name to delete
        """
        pass

    def dns_delete_record(self):
        """
        /v1/dns/delete_record
        POST - account
        Delete an individual DNS record

        Example Request:
        POST https://api.vultr.com/v1/dns/delete_record?api_key=EXAMPLE
        domain=example.com
        RECORDID=1265277
        Example Response:
        No response, check HTTP result code
        Parameters:
        domain string Domain name to delete record from
        RECORDID integer ID of record to delete (see /dns/records)
        """
        pass

    def dns_create_record(self):
        """
        /v1/dns/create_record
        POST - account
        Add a DNS record

        Example Request:
        POST https://api.vultr.com/v1/dns/create_record?api_key=EXAMPLE
        domain=example.com
        name=vultr
        type=A
        data=127.0.0.1
        Example Response:
        No response, check HTTP result code
        Parameters:
        domain string Domain name to add record to
        name string Name (subdomain) of record
        type string Type (A, AAAA, MX, etc) of record
        data string Data for this record
        ttl integer (optional) TTL of this record
        priority integer (only required for MX and SRV) Priority of this record
            (omit the priority from the data)
        """
        pass

    def sshkey_list(self):
        """
        /v1/sshkey/list
        GET - account
        List all the SSH keys on the current account

        Example Request:
        GET https://api.vultr.com/v1/sshkey/list?api_key=EXAMPLE
        Example Response:
        {
            "541b4960f23bd": {
                "SSHKEYID": "541b4960f23bd",
                "date_created": null,
                "name": "test",
                "ssh_key": "ssh-rsa AA... test@example.com"
            }
        }
        Parameters:
        No Parameters
        """
        pass

    def sshkey_destroy(self):
        """
        /v1/sshkey/destroy
        POST - account
        Remove a SSH key. Note that this will not remove the key from any
        machines that already have it.

        Example Request:
        POST https://api.vultr.com/v1/sshkey/destroy?api_key=EXAMPLE
        Example Response:
        No response, check HTTP result code
        Parameters:
        SSHKEYID string Unique identifier for this SSH key.  These can be found
            using the v1/sshkey/list call.
        """
        pass

    def sshkey_create(self):
        """
        /v1/sshkey/create
        POST - account
        Create a new SSH Key

        Example Request:
        POST https://api.vultr.com/v1/sshkey/create?api_key=APIKEY
        name="test SSH key"
        ssh_key="ssh-rsa AA... test@example.com"
        Example Response:
        {
            "SSHKEYID": "541b4960f23bd"
        }
        Parameters:
        name string Name of the SSH key
        ssh_key string SSH public key (in authorized_keys format)
        """
        pass

    def sshkey_update(self):
        """
        /v1/sshkey/update
        POST - account
        Update an existing SSH Key. Note that this will only update newly
        installed machines. The key will not be updated on any existing
        machines.

        Example Request:
        POST https://api.vultr.com/v1/sshkey/update?api_key=APIKEY
        SSHKEYID="541b4960f23bd"
        name="new key name"
        ssh_key="ssh-rsa AA... someother@example.com"
        Example Response:
        No response, check HTTP result code
        Parameters:
        SSHKEYID string SSHKEYID of key to update (see /v1/sshkey/list)
        name string (optional) New name for the SSH key
        ssh_key string (optional) New SSH key contents
        """
        pass

    def backup_list(self):
        """
        /v1/backup/list
        GET - account
        List all backups on the current account

        Example Request:
        GET https://api.vultr.com/v1/backup/list?api_key=EXAMPLE
        Example Response:
        {
            "543d34149403a": {
                "BACKUPID": "543d34149403a",
                "date_created": "2014-10-14 12:40:40",
                "description": "Automatic server backup",
                "size": "42949672960",
                "status": "complete"
            },
            "543d340f6dbce": {
                "BACKUPID": "543d340f6dbce",
                "date_created": "2014-10-13 16:11:46",
                "description": "",
                "size": "10000000",
                "status": "complete"
            }
        }
        Parameters:
        No Parameters
        """
        pass

    def server_list(self):
        """
        /v1/server/list
        GET - account
        List all active or pending virtual machines on the current account. The
        'status' field represents the status of the subscription and will be
        one of pending|active|suspended|closed. If the status is 'active', you
        can check 'power_status' to determine if the VPS is powered on or not.
        The API does not provide any way to determine if the initial
        installation has completed or not.

        Example Request:
        GET https://api.vultr.com/v1/server/list?api_key=EXAMPLE
        Example Response:
        {
            "576965": {
                "SUBID": "576965",
                "os": "CentOS 6 x64",
                "ram": "4096 MB",
                "disk": "Virtual 60 GB",
                "main_ip": "123.123.123.123",
                "vcpu_count": "2",
                "location": "New Jersey",
                "DCID": "1",
                "default_password": "nreqnusibni",
                "date_created": "2013-12-19 14:45:41",
                "pending_charges": "46.67",
                "status": "active",
                "cost_per_month": "10.05",
                "current_bandwidth_gb": 131.512,
                "allowed_bandwidth_gb": "1000",
                "netmask_v4": "255.255.255.248",
                "gateway_v4": "123.123.123.1",
                "power_status": "running",
                "VPSPLANID": "28",
                "v6_network": "2001:DB8:1000::",
                "v6_main_ip": "2001:DB8:1000::100",
                "v6_network_size": "64",
                "label": "my new server",
                "internal_ip": "10.99.0.10",
                "kvm_url": "https://my.vultr.com/subs/novnc/api.php
                    ?data=eawxFVZw2mXnhGUV",
                "auto_backups": "yes"
            }
        }
        Parameters:
        SUBID integer (optional) Unique identifier of a subscription. Only the
         subscription object will be returned.
        """
        pass

    def server_bandwidth(self):
        """
        /v1/server/bandwidth
        GET - account
        Get the bandwidth used by a virtual machine

        Example Request:
        GET https://api.vultr.com/v1/server/bandwidth?api_key=EXAMPLE
            &SUBID=576965
        Example Response:
        {
            "incoming_bytes": [
                [
                    "2014-06-10",
                    "81072581"
                ],
                [
                    "2014-06-11",
                    "222387466"
                ],
                [
                    "2014-06-12",
                    "216885232"
                ],
                [
                    "2014-06-13",
                    "117262318"
                ]
            ],
            "outgoing_bytes": [
                [
                    "2014-06-10",
                    "4059610"
                ],
                [
                    "2014-06-11",
                    "13432380"
                ],
                [
                    "2014-06-12",
                    "2455005"
                ],
                [
                    "2014-06-13",
                    "1106963"
                ]
            ]
        }
        Parameters:
        SUBID integer Unique identifier for this subscription.  These can be
            found using the v1/server/list call.
        """
        pass

    def server_reboot(self):
        """
        /v1/server/reboot
        POST - account
        Reboot a virtual machine. This is a hard reboot (basically, unplugging
            the machine).

        Example Request:
        POST https://api.vultr.com/v1/server/reboot?api_key=EXAMPLE
        Example Response:
        No response, check HTTP result code
        Parameters:
        SUBID integer Unique identifier for this subscription.  These can be
            found using the v1/server/list call.
        """
        pass

    def server_halt(self):
        """
        /v1/server/halt
        POST - account
        Halt a virtual machine. This is a hard power off (basically, unplugging
            the machine). The data on the machine will not be modified, and you
            will still be billed for the machine. To completely delete a
            machine, see v1/server/destroy

        Example Request:
        POST https://api.vultr.com/v1/server/halt?api_key=EXAMPLE
        Example Response:
        No response, check HTTP result code
        Parameters:
        SUBID integer Unique identifier for this subscription.  These can be
            found using the v1/server/list call.
        """
        pass

    def server_start(self):
        """
        /v1/server/start
        POST - account
        Start a virtual machine. If the machine is already running, it will be
        restarted.

        Example Request:
        POST https://api.vultr.com/v1/server/start?api_key=EXAMPLE
        Example Response:
        No response, check HTTP result code
        Parameters:
        SUBID integer Unique identifier for this subscription.  These can be
            found using the v1/server/list call.
        """
        pass

    def server_destroy(self):
        """
        /v1/server/destroy
        POST - account
        Destroy (delete) a virtual machine. All data will be permanently lost,
        and the IP address will be released. There is no going back from this
        call.

        Example Request:
        POST https://api.vultr.com/v1/server/destroy?api_key=EXAMPLE
        Example Response:
        No response, check HTTP result code
        Parameters:
        SUBID integer Unique identifier for this subscription.  These can be
            found using the v1/server/list call.
        """
        pass

    def server_reinstall(self):
        """
        /v1/server/reinstall
        POST - account
        Reinstall the operating system on a virtual machine. All data will be
        permanently lost, but the IP address will remain the same There is no
        going back from this call.

        Example Request:
        POST https://api.vultr.com/v1/server/reinstall?api_key=EXAMPLE
        Example Response:
        No response, check HTTP result code
        Parameters:
        SUBID integer Unique identifier for this subscription.  These can be
            found using the v1/server/list call.
        """
        pass

    def server_restore_snapshot(self):
        """
        /v1/server/restore_snapshot
        POST - account
        Restore the specificed snapshot to the virtual machine. Any data
        already on the virtual machine will be lost.

        Example Request:
        POST https://api.vultr.com/v1/server/restore_snapshot?api_key=EXAMPLE
        Example Response:
        No response, check HTTP result code
        Parameters:
        SUBID integer Unique identifier for this subscription.  These can be
            found using the v1/server/list call.
        SNAPSHOTID string SNAPSHOTID (see v1/snapshot/list) to restore to this
            instance
        """
        pass

    def server_restore_backup(self):
        """
        /v1/server/restore_backup
        POST - account
        Restore the specified backup to the virtual machine. Any data already
        on the virtual machine will be lost.

        Example Request:
        POST https://api.vultr.com/v1/server/restore_backup?api_key=EXAMPLE
        Example Response:
        No response, check HTTP result code
        Parameters:
        SUBID integer Unique identifier for this subscription.  These can be
            found using the v1/server/list call.
        BACKUPID string BACKUPID (see v1/backup/list) to restore to this
            instance
        """
        pass

    def server_create(self):
        """
        /v1/server/create
        POST - account
        Create a new virtual machine. You will start being billed for this
        immediately. The response only contains the SUBID for the new machine.
        You should use v1/server/list to poll and wait for the machine to be
        created (as this does not happen instantly).

        Example Request:
        POST https://api.vultr.com/v1/server/create?api_key=APIKEY
        DCID=1
        VPSPLANID=1
        OSID=127
        Example Response:
        {
            "SUBID": "1312965"
        }
        Parameters:
        DCID integer Location to create this virtual machine in.  See
            v1/regions/list
        VPSPLANID integer Plan to use when creating this virtual machine.  See
            v1/plans/list
        OSID integer Operating system to use.  See v1/os/list
        ipxe_chain_url string (optional) If you've selected the 'custom'
            operating system, this can be set to chainload the specified URL on
            bootup, via iPXE
        ISOID string (optional)  If you've selected the 'custom' operating
            system, this is the ID of a specific ISO to mount during the
            deployment
        SCRIPTID integer (optional) If you've not selected a 'custom' operating
            system, this can be the SCRIPTID of a startup script to execute on
            boot.  See v1/startupscript/list
        SNAPSHOTID string (optional) If you've selected the 'snapshot'
            operating system, this should be the SNAPSHOTID (see
            v1/snapshot/list) to restore for the initial installation
        enable_ipv6 string (optional) 'yes' or 'no'.  If yes, an IPv6 subnet
            will be assigned to the machine (where available)
        enable_private_network string (optional) 'yes' or 'no'. If yes, private
            networking support will be added to the new server.
        label string (optional) This is a text label that will be shown in the
            control panel
        SSHKEYID string (optional) List of SSH keys to apply to this server on
            install (only valid for Linux/FreeBSD).  See v1/sshkey/list.
            Seperate keys with commas
        auto_backups string (optional) 'yes' or 'no'.  If yes, automatic
            backups will be enabled for this server (these have an extra charge
            associated with them)
        APPID integer (optional) If launching an application (OSID 186), this
            is the APPID to launch. See v1/app/list.
        """
        pass

    def server_list_ipv4(self):
        """
        /v1/server/list_ipv4
        GET - account
        List the IPv4 information of a virtual machine. IP information is only
        available for virtual machines in the "active" state.

        Example Request:
        GET https://api.vultr.com/v1/server/list_ipv4?api_key=EXAMPLE
            &SUBID=576965
        Example Response:
        {
            "576965": [
                {
                    "ip": "123.123.123.123",
                    "netmask": "255.255.255.248",
                    "gateway": "123.123.123.1",
                    "type": "main_ip",
                    "reverse": "123.123.123.123.example.com"
                },
                {
                    "ip": "123.123.123.124",
                    "netmask": "255.255.255.248",
                    "gateway": "123.123.123.1",
                    "type": "secondary_ip",
                    "reverse": "123.123.123.124.example.com"
                },
                {
                    "ip": "10.99.0.10",
                    "netmask": "255.255.0.0",
                    "gateway": "",
                    "type": "private",
                    "reverse": ""
                }
            ]
        }
        Parameters:
        No Parameters
        """
        pass

    def server_reverse_set_ipv4(self):
        """
        /v1/server/reverse_set_ipv4
        POST - account
        Set a reverse DNS entry for an IPv4 address of a virtual machine. Upon
        success, DNS changes may take 6-12 hours to become active.

        Example Request:
        POST https://api.vultr.com/v1/server/reverse_set_ipv4?api_key=EXAMPLE
        Example Response:
        No response, check HTTP result code
        Parameters:
        SUBID integer Unique identifier for this subscription. These can be
            found using the v1/server/list call.
        ip string IPv4 address used in the reverse DNS update. These can be
            found with the v1/server/list_ipv4 call.
        entry string reverse DNS entry.
        """
        pass

    def server_reverse_default_ipv4(self):
        """
        /v1/server/reverse_default_ipv4
        POST - account
        Set a reverse DNS entry for an IPv4 address of a virtual machine to the
        original setting. Upon success, DNS changes may take 6-12 hours to
        become active.

        Example Request:
        POST https://api.vultr.com/v1/server/reverse_default_ipv4
            ?api_key=EXAMPLE
        Example Response:
        No response, check HTTP result code
        Parameters:
        SUBID integer Unique identifier for this subscription. These can be
            found using the v1/server/list call.
        ip string IPv4 address used in the reverse DNS update. These can be
            found with the v1/server/list_ipv4 call.
        """
        pass

    def server_list_ipv6(self):
        """
        /v1/server/list_ipv6
        GET - account
        List the IPv6 information of a virtual machine. IP information is only
        available for virtual machines in the "active" state. If the virtual
        machine does not have IPv6 enabled, then an empty array is returned.

        Example Request:
        GET https://api.vultr.com/v1/server/list_ipv6?api_key=EXAMPLE
            &SUBID=576965
        Example Response:
        {
            "576965": [
                {
                    "ip": "2001:DB8:1000::100",
                    "network": "2001:DB8:1000::",
                    "network_size": "64",
                    "type": "main_ip"
                }
            ]
        }
        Parameters:
        No Parameters
        """
        pass

    def server_reverse_list_ipv6(self):
        """
        /v1/server/reverse_list_ipv6
        GET - account
        List the IPv6 reverse DNS entries of a virtual machine. Reverse DNS
        entries are only available for virtual machines in the "active" state.
        If the virtual machine does not have IPv6 enabled, then an empty array
        is returned.

        Example Request:
        GET https://api.vultr.com/v1/server/reverse_list_ipv6?api_key=EXAMPLE
            &SUBID=576965
        Example Response:
        {
            "576965": [
                {
                    "ip": "2001:DB8:1000::101",
                    "reverse": "host1.example.com"
                },
                {
                    "ip": "2001:DB8:1000::102",
                    "reverse": "host2.example.com"
                }
            ]
        }
        Parameters:
        No Parameters
        """
        pass

    def server_reverse_set_ipv6(self):
        """
        /v1/server/reverse_set_ipv6
        POST - account
        Set a reverse DNS entry for an IPv6 address of a virtual machine. Upon
        success, DNS changes may take 6-12 hours to become active.

        Example Request:
        POST https://api.vultr.com/v1/server/reverse_set_ipv6?api_key=EXAMPLE
        Example Response:
        No response, check HTTP result code
        Parameters:
        SUBID integer Unique identifier for this subscription. These can be
            found using the v1/server/list call.
        ip string IPv6 address used in the reverse DNS update. These can be
            found with the v1/server/list_ipv6 or v1/server/reverse_list_ipv6
            calls.
        entry string reverse DNS entry.
        """
        pass

    def server_reverse_delete_ipv6(self):
        """
        /v1/server/reverse_delete_ipv6
        POST - account
        Remove a reverse DNS entry for an IPv6 address of a virtual machine.
        Upon success, DNS changes may take 6-12 hours to become active.

        Example Request:
        POST https://api.vultr.com/v1/server/reverse_delete_ipv6
            ?api_key=EXAMPLE
        Example Response:
        No response, check HTTP result code
        Parameters:
        SUBID integer Unique identifier for this subscription. These can be
            found using the v1/server/list call.
        ip string IPv6 address used in the reverse DNS update. These can be
            found with the v1/server/reverse_list_ipv6 call.
        """
        pass

    def server_label_set(self):
        """
        /v1/server/label_set
        POST - account
        Set the label of a virtual machine.

        Example Request:
        POST https://api.vultr.com/v1/server/label_set?api_key=EXAMPLE
        Example Response:
        No response, check HTTP result code
        Parameters:
        SUBID integer Unique identifier for this subscription. These can be
            found using the v1/server/list call.
        label string This is a text label that will be shown in the control
            panel.
        """
        pass

    def server_create_ipv4(self):
        """
        /v1/server/create_ipv4
        POST - account
        Add a new IPv4 address to a server. You will start being billed for
        this immediately. The server will be rebooted unless you specify
        otherwise. You must reboot the server before the IPv4 address can be
        configured.

        Example Request:
        POST https://api.vultr.com/v1/server/create_ipv4?api_key=EXAMPLE
        Example Response:
        No response, check HTTP result code
        Parameters:
        SUBID integer Unique identifier for this subscription. These can be
            found using the v1/server/list call.
        reboot string (optional, default 'yes') 'yes' or 'no'. If yes, the
            server is rebooted immediately.
        """
        pass

    def server_destroy_ipv4(self):
        """
        /v1/server/destroy_ipv4
        POST - account
        Removes a secondary IPv4 address from a server. Your server will be
        hard-restarted. We suggest halting the machine gracefully before
        removing IPs.

        Example Request:
        POST https://api.vultr.com/v1/server/destroy_ipv4?api_key=EXAMPLE
        Example Response:
        No response, check HTTP result code
        Parameters:
        SUBID integer Unique identifier for this subscription. These can be
        found using the v1/server/list call.
        ip string IPv4 address to remove.
        """
        pass

    def server_os_change_list(self):
        """
        /v1/server/os_change_list
        GET - account
        Retrieves a list of operating systems to which this server can be
        changed.

        Example Request:
        GET https://api.vultr.com/v1/server/os_change_list?api_key=EXAMPLE
            &SUBID=576965
        Example Response:
        {
            "127": {
                "OSID": "127",
                "name": "CentOS 6 x64",
                "arch": "x64",
                "family": "centos",
                "windows": false,
                "surcharge": "0.00"
            },
            "148": {
                "OSID": "148",
                "name": "Ubuntu 12.04 i386",
                "arch": "i386",
                "family": "ubuntu",
                "windows": false,
                "surcharge": "0.00"
            }
        }
        Parameters:
        SUBID integer Unique identifier for this subscription. These can be
            found using the v1/server/list call.
        """
        pass

    def server_os_change(self):
        """
        /v1/server/os_change
        POST - account
        Changes the operating system of a virtual machine. All data will be
        permanently lost.

        Example Request:
        POST https://api.vultr.com/v1/server/os_change?api_key=EXAMPLE
        Example Response:
        No response, check HTTP result code
        Parameters:
        SUBID integer Unique identifier for this subscription. These can be
            found using the v1/server/list call.
        OSID integer Operating system to use. See /v1/server/os_change_list.
        """
        pass

    def server_upgrade_plan_list(self):
        """
        /v1/server/upgrade_plan_list
        GET - account
        Retrieve a list of the VPSPLANIDs for which a virtual machine can be
        upgraded. An empty response array means that there are currently no
        upgrades available.

        Example Request:
        GET https://api.vultr.com/v1/server/upgrade_plan_list?api_key=EXAMPLE
        Example Response:
        [
            29,
            41,
            61
        ]
        Parameters:
        SUBID integer Unique identifier for this subscription. These can be
            found using the v1/server/list call.
        """
        pass

    def server_upgrade_plan(self):
        """
        /v1/server/upgrade_plan
        POST - account
        Upgrade the plan of a virtual machine. The virtual machine will be
        rebooted upon a successful upgrade.

        Example Request:
        POST https://api.vultr.com/v1/server/upgrade_plan?api_key=EXAMPLE
        Example Response:
        No response, check HTTP result code
        Parameters:
        SUBID integer Unique identifier for this subscription. These can be
            found using the v1/server/list call.
        VPSPLANID integer The new plan. See /v1/server/upgrade_plan_list.
        """
        pass

    def app_list(self):
        """
        /v1/app/list
        GET - public
        Retrieve a list of available applications. These refer to applications
        that can be launched when creating a Vultr VPS.

        Example Request:
        GET https://api.vultr.com/v1/app/list
        Example Response:
        {
            "1": {
                "APPID": "1",
                "name": "LEMP",
                "short_name": "lemp",
                "deploy_name": "LEMP on CentOS 6 x64"
            },
            "2": {
                "APPID": "2",
                "name": "WordPress",
                "short_name": "wordpress",
                "deploy_name": "WordPress on CentOS 6 x64"
            }
        }
        Parameters:
        No Parameters
        """
        pass

    def account_info(self):
        """
        /v1/account/info
        GET - account
        Retrieve information about the current account

        Example Request:
        GET https://api.vultr.com/v1/account/info?api_key=EXAMPLE
        Example Response:
        {
            "balance": "-5519.11",
            "pending_charges": "57.03",
            "last_payment_date": "2014-07-18 15:31:01",
            "last_payment_amount": "-1.00"
        }
        Parameters:
        No Parameters
        """
        pass

    def os_list(self):
        """
        /v1/os/list
        GET - public
        Retrieve a list of available operating systems. If the 'windows' flag
        is true, a Windows licenses will be included with the instance, which
        will increase the cost.

        Example Request:
        GET https://api.vultr.com/v1/os/list
        Example Response:
        {
            "127": {
                "OSID": "127",
                "name": "CentOS 6 x64",
                "arch": "x64",
                "family": "centos",
                "windows": false
            },
            "148": {
                "OSID": "148",
                "name": "Ubuntu 12.04 i386",
                "arch": "i386",
                "family": "ubuntu",
                "windows": false
            }
        }
        Parameters:
        No Parameters
        """
        pass

if __name__ == '__main__':
    print "Vultr API Python Libary"
    print "http://vultr.com"