import pcapy
from impacket import ImpactDecoder

def capture_smtp_packets(interface):
    # Open the network interface in promiscuous mode with a 1MB buffer
    pcap = pcapy.open_live(interface, 1024, True, 100)

    # Set a filter to capture only SMTP packets (port 25)
    pcap.setfilter('tcp port 25')

    # Create a decoder for the captured packets
    decoder = ImpactDecoder.EthDecoder()

    # Start capturing packets
    while True:
        # Read the next packet from the interface
        (header, packet) = pcap.next()

        # Decode the packet
        ethernet_packet = decoder.decode(packet)

        # Check if the packet contains an IP layer
        if ethernet_packet.child() is not None:
            ip_packet = ethernet_packet.child()

            # Check if the IP packet contains a TCP layer
            if ip_packet.child() is not None and ip_packet.child().protocol == ip_packet.child().IP_PROTO_TCP:
                tcp_packet = ip_packet.child()

                # Check if the TCP packet contains an SMTP payload
                if tcp_packet.get_th_dport() == 25 and tcp_packet.get_payload():
                    print(tcp_packet.get_payload())

# Specify the network interface to capture packets from
interface = 'eth0'  # Change this to the appropriate interface

# Start capturing SMTP packets
capture_smtp_packets(interface)
