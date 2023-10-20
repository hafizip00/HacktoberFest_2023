# [dev]: s41r4j
# [usage]: just run the program to change mac address of current device (`python3 mac_changer.py`)
# [supported]: linux, rooted android

import subprocess, optparse, re

# Setting up: 'command line arguments' & 'help menu'
def get_arguments():

	parser = optparse.OptionParser()

	parser.add_option("-i", "--interface", dest='interface', help='Interface Name of which Mac Address to change')
	parser.add_option("-m", "--mac", dest='new_mac', help='New Mac Address to replace Old Mac Address')

	(options, arguments) = parser.parse_args()
	# return parser.parse_args()

	if not options.interface:
		parser.error('[-] Please specify an interface, use -h (or --help) for more info.')
	elif not options.new_mac:
		parser.error('[-] Please specify a new mac address, use -h (or --help) for more info.')
	return options
	

def change_mac(interface, new_mac):

	print('[+] Changing MAC Address for ' + interface + ' to ' + new_mac)
	
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
	subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):

	ifconfig_result = str(subprocess.check_output(['ifconfig', interface]))

	mac_addr_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

	if mac_addr_search_result:
		return mac_addr_search_result.group(0)
	else:
		print('[-] Could not read Mac Address')


def main():
	# (options, arguments) = get_arguments()
	(options) = get_arguments()

	current_mac = get_current_mac(options.interface)
	print("[+] Current MAC Address = " + str(current_mac))

	change_mac(options.interface, options.new_mac)

	current_mac = get_current_mac(options.interface)
	if current_mac == options.new_mac:
		print('[+] Mac Address was successfully changed to ' + current_mac)
	else:
		print('[-] Mac Address did not get changed')


main()
