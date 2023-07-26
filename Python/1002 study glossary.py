loop = 1
while loop == 1:
    print("Welcome to the Defininator!")
    lookup = input("What would you like to lookup? ")
    if lookup == "QOS" or "qos" or "quality of service":
        print(lookup)
        print('Quality of Service: used for bandwidth management')
    elif lookup == "preferred dns" or "preferred DNS":
        print(lookup)
        print('Domain Name System Server, translates domain names in IP addresses. Preferred Server is contacted first')
    elif lookup == "alternate dns" or "alternate DNS":
        print(lookup)
        print('Domain Name System Server, translates domain names into IP addresses, Alternate DNS is used when Preferred DNS Server is unavailable')
    elif lookup == "default gateway":
        print(lookup)
        print('Address used by a computer to find remote networks and hosts. When you go to a website, the gateway identifies the site as non-local, and routes the request to the internet')
    elif lookup == "subnet mask":
        print(lookup)
        print('A subnet mask is used to identify what network a computer belongs to The subnet mask works in conjunction with the system\'s IP address')
    elif lookup == "authentication methods" :
        print(lookup)
        print('WAP - Wireless Application Protocol - Legacy protocol by early mobile devices for mobile wireless connectivity ')
        print('WPA2 -Wi-Fi Protected Access 2 - security protocol in Wi-Fi standard, replaced WPA, included mandatory support for AES (advanced encryption standard) encryption mode ')
        print('WEP - Wired Equivalent Privacy - Older Security method, used CRC (Cyclic Redundancy Check) and had some big time flaws ')
        print('WPA - Wi-Fi Protected Access - secruity protocol in Wi-Fi standard, replaced WEP and uses message integrity check. WPA also uses TKIP (Temporal Key Integrity Protocol)')
    elif lookup == "heuristics" :
        print(lookup)
        print('Anti-virus protection technology uses knowledge of virus-like behavior as a means of defense')
    elif lookup == "definitions":
        print(lookup)
        print('Definitions are included in an anti-virus software\'s database of known threats to identify malicious activity and files')
    elif lookup == "patch management":
        print(lookup)
        print('a method of keeping operating systems and applications routinely up to date for operational and security purposes, also applies critical and security updates for OS and application software. Failing to keep OS and software applications up-to-date can cause complete system crashes and vulnerabilities to malware.')
    elif lookup == "network access control":
        print(lookup)
        print('a method of managing inbound and outbound traffic on a network, with a focus on security measures. The use of a firewall is a component of network access control.')
    elif lookup == "ifconfig":
        print(lookup)
        print('a system utility that is used for network configuration of a network interface. As an example, using ifconfig -a is used to view the configuration of all interfaces')
    elif lookup == "lwconfig":
        print(lookup)
        print('similar to the ifconfig command, however, it is directed as use with wireless networking.')
    elif lookup == "apt-get":
        print(lookup)
        print('(advanced package tool) command is used for handling packages within a Linux distribution. Using the update command along with apt-get will synchronize package index files')
    elif lookup == "remote disc entry":
        print(lookup)
        print('located in finder, a placeholder for systems that do not have an optical CD (Compact Disc) or DVD (Digital Versatile Disc) drive')
    elif lookup == "spotlight":
        print(lookup)
        print('Mac OS search tool that can find files, images, websites, applications, and more by using keywords and phrases.')
    elif lookup == "finder":
        print(lookup)
        print('File and Folder management application that is included with Mac OS. A simple search feature that is included searches only the local system.')
    elif lookup == "mission control":
        print(lookup)
        print('virtual desktop feature where users can create multiple spaces and switch between them using Mission Control')
    elif lookup == "windows search":
        print(lookup)
        print('A windows based search platform available only on windows, sorry Mac Daddy!')
    elif lookup == "anti-virus":
        print(lookup)
        print('software that can detect malware and prevent it from executing. The primary means of detection is to use a database of known virus patterns, called definitions, signatures, or patterns.')
    elif lookup == "patch management":
        print(lookup)
        print('applying critical and security updates for OS and application software. Failing to keep operating systems and software applications up-to-date can cause vulnerability to malware.')
    elif lookup == "firewalls":
        print(lookup)
        print('principally deployed to manage access between networks. They control communications by blocking packets based on access rules permitting or denying certain combinations of IP addresses and network ports.')
    elif lookup == "pnac":
        print(lookup)
        print('the switch (or router) in question performs some sort of authentication of the attached device before activating the port.')
    elif lookup == "asymmetric encryption":
        print(lookup)
        print('an important part of Public Key Infrastructure (PKI). Under PKI, users or server computers are validated by a Certificate Authority (CA), which issues the subject a digital certificate.')
    elif lookup == "execution control":
        print(lookup)
        print('logical security technologies designed to prevent malicious software from running on a host.')
    elif lookup == "cryptographic hashes":
        print(lookup)
        print('A hash is a short representation of data; a cryptographic hash makes it impossible to recover the original data from the hash. This technique can be used to prove data integrity.')
    elif lookup == "radius protocol" or "RADIUS":
        print(lookup)
        print('Remote Authentication Dial-in User Service (RADIUS) protocol, Authentication, Authorization, and Accounting are performed by a separate server (the AAA server). RADIUS is often used in VPN implementations.')
    elif lookup == "TACACS+" or "terminal access controller access control system":
        print(lookup)
        print('Developed by Cisco! Terminal Access Controller Access Control System (TACACS+) is a similar protocol to RADIUS but designed to be more flexible and reliable. TACACS+ is often used in authenticating administrative access to routers and switches.')
    elif lookup == "ACL" or "acl" or "access control list":
        print(lookup)
        print('An access control list (ACL) is basically a list of subjects (users or computers) and the privileges they have on the object or resource')
    elif lookup == "PNAC" or "pnac" or "port-based network access control":
        print(lookup)
        print('the switch ( or router) performs some sort of authentication of the attached device before activating the port.')
    elif lookup == "rootkit ":
        print(lookup)
        print('a set of tools designed to gain control of a computer and create a backdoor with root or system-level privileges without revealing its presence.')
    elif lookup == "trojan":
        print(lookup)
        print('a program (usually harmful) that is disguised and packaged as something else. Many Trojans function as backdoor applications.')
    elif lookup == "boot sector virus":
        print(lookup)
        print('a boot sector virus might be able to overwrite the existing boot sector, an application might be able to delete, corrupt, or install files, and a script might be able to change system settings or delete or install files.')
    elif lookup == "dns spoofing" or "DNS spoofing":
        print(lookup)
        print('DNS spoofing allows attackers to direct victims away from the legitimate sites they were intending to visit and towards fake sites. As part of preventing reinfection, you should inspect and re-secure the DNS configuration.')
    elif lookup == "Recovery Console" or "recovery console":
        print(lookup)
        print('a precursor to WinRE, used by the Windows 2000 and Windows XP versions. Recovery console presents a limited subset of the commands normally available at a Windows command prompt and does not provide as many tools as WinRE.')
    elif lookup == "termmmmmmm":
        print(lookup)
        print('definitionnnnnnnnnnnnn')
    elif lookup == "termmmmmmm":
        print(lookup)
        print('definitionnnnnnnnnnnnn')




    else:
        print('sorry dude!')
        #loop == 2
        #loop == 1
        pass 