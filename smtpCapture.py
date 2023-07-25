#'/home/kali/Desktop/KeyLogger/packetCapture.pcap'
import pyshark


def capture_smtp_packets(interface, output_file, capture_duration):
    # Create a packet capture object with output file
    capture = pyshark.LiveCapture(interface=interface, output_file=output_file)

    # Set a capture filter for SMTP packets (port 25)
    capture.filter = 'tcp port 25'

    # Start capturing packets for the specified duration
    capture.sniff(timeout=capture_duration)

# Specify the network interface to capture packets from
interface = 'eth0'  # Change this to the appropriate interface

# Specify the output file path
output_file = '/home/kali/Desktop/KeyLogger/packetCapture.pcap'

	# Specify the capture duration in seconds
capture_duration = 100

	# Capture SMTP packets and save them to the output file, overwriting existing data
capture_smtp_packets(interface, output_file, capture_duration)
	
