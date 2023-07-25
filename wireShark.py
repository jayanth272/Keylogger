import pyshark

def analyze_wireshark_data(pcap_file):
    # Open the pcap file
	cap = pyshark.FileCapture(pcap_file)
	#	dictionary to store report , ip -> count
	report = {}
    # Iterate over each packet
	for packet in cap:
        # Check if it's an SMTP packet
		if 'smtp' in packet:
            # Extract SMTP specific information
			from_ip = packet.ip.src
			to_ip = packet.ip.dst
            
			print("SMTP Packet:")
			print("Sender IP:", from_ip)
			print("Receiver IP:", to_ip)
			print("")
			if to_ip not in report:
				report[to_ip] = 0
			report[to_ip] += 1
			if report[to_ip] >= 3:
				print("\t----\t"+"Alert!"*3+"\t----")
				print("There might be keylogger installed in your system")
				print("Please check the running processes in 'TASK MANAGER'")
				return -1



	# Specify the path to the pcap file
pcap_file = '/home/kali/Desktop/KeyLogger/packetCapture.pcap'

	# Analyze the Wireshark data
analyze_wireshark_data(pcap_file)
