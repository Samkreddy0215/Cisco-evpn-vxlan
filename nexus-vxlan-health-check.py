from netmiko import ConnectHandler
import csv

# Cisco Nexus Device Information
device = {
    "device_type": "cisco_nxos",
    "host": "10.1.1.10",
    "username": "admin",
    "password": "password"
}

try:
    connection = ConnectHandler(**device)

    # Collect BGP EVPN Neighbor Status
    bgp_output = connection.send_command("show bgp l2vpn evpn summary")

    # Verify NVE Interface
    nve_output = connection.send_command("show nve interface")

    # Check VTEP Information
    vtep_output = connection.send_command("show nve peers")

    # Verify VXLAN Tunnel Status
    tunnel_output = connection.send_command("show nve vni")

    # Export Results
    with open("vxlan_health_report.csv", "w", newline="") as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow(["Section", "Output"])

        writer.writerow(["BGP EVPN Neighbors", bgp_output])
        writer.writerow(["NVE Interface", nve_output])
        writer.writerow(["VTEP Peers", vtep_output])
        writer.writerow(["VXLAN VNIs", tunnel_output])

    print("VXLAN Health Report Generated Successfully.")

    connection.disconnect()

except Exception as error:
    print(f"Connection Failed: {error}")
