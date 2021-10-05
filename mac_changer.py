import subprocess
import optparse

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i, "--interface". dest="interface", help="interface to change its MAC adress")
    parser.add_option("-m", "--mac", dest= "new_mac", help="New mac adress")
(options,arguments) = parser.parse_args()
if not options.interface:
    parser.error("[-] please specify an interface, use --help for more info")
elif not options.new_mac:
    parser.error("[-] please specify an new_mac, use --help for more info")
    return options

def change_mac(interface, new_mac):
    print("[+] changing Mac adress for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

    (options, arguments) = parser.parse_args()
    change_mac(options.interface, options.new mac)
