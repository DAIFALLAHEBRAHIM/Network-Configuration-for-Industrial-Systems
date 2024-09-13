def enable_firewall(rules):
    for rule in rules:
        print(f"Applying rule: {rule}")

firewall_rules = ['ALLOW 192.168.1.0/24', 'DENY ALL']
enable_firewall(firewall_rules)
