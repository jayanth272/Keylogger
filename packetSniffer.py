from scapy.all import *
from collections import Counter

# Counter to keep track of email counts
email_counter = Counter()

def packet_callback(packet):
	print(packet)
	if packet.haslayer(TCP) and packet.haslayer(Raw):
        # Check if it's an SMTP packet
		if packet[TCP].dport == 25 or packet[TCP].sport == 25:
			payload = packet[Raw].load.decode('utf-8', errors='ignore')
			if 'MAIL FROM' in payload:
                # Extract the sender's email address
				sender_email = payload.split('MAIL FROM:<')[1].split('>')[0]
                # Count the email from the sender
				email_counter[sender_email] += 1
				if email_counter[sender_email] >= 1:
					print(f"Warning: Frequent emails detected from {sender_email}!")

# Start capturing SMTP packets
if __name__ == '__main__':
	sniff(filter="tcp port 25", prn=packet_callback, store=0)
