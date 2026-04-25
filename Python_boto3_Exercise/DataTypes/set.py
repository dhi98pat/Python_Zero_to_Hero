security_group = {
    "sg-001",
    "sg-002",
    "sg-003",
    "sg-001"  # Duplicate entry, sets will automatically handle this
}

print(f"Security Groups: {security_group}")