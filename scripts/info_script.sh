#!/bin/bash

# File to store the information
output_file="system_info.txt"

# Function to gather package information
get_package_info() {
    echo "Getting installed package information..."
    dpkg-query -l > "$output_file"
    echo "Installed package information saved to $output_file"
    echo
}

# Function to gather service status
get_service_status() {
    echo "Getting service status..."
    systemctl list-units --type=service > "$output_file"
    echo "Service status saved to $output_file"
    echo
}

# Function to gather hardware configuration
get_hardware_info() {
    echo "Getting hardware configuration..."
    echo "Number of CPUs:" $(nproc) >> "$output_file"
    echo "CPU model:" $(cat /proc/cpuinfo | grep "model name" | uniq | cut -d ' ' -f 3-) >> "$output_file"
    echo "Total RAM:" $(free -h | awk '/^Mem/ {print $2}') >> "$output_file"
    echo "Free RAM:" $(free -h | awk '/^Mem/ {print $4}') >> "$output_file"
    echo "Disk information:" >> "$output_file"
    df -h >> "$output_file"
    echo "Hardware information saved to $output_file"
    echo
}

# Gather all information
get_package_info
get_service_status
get_hardware_info

echo "All information collected and saved to $output_file"
