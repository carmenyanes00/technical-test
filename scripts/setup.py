import subprocess

# Create a new user account
def create_user(username, home_directory):
    subprocess.run(["sudo", "useradd", "-m", "-s", "/bin/bash", username, "-d", home_directory])

# Add the user to the sudo group
def add_user_to_sudo(username):
    subprocess.run(["sudo", "usermod", "-aG", "sudo", username])

# Set a password for the user
def set_password(username):
    subprocess.run(["sudo", "passwd", username])

# Grant permission to restart services
def grant_permission_to_restart_services(username):
    input_string = "%s ALL=NOPASSWD:/bin/systemctl restart *" % username
    input_bytes = input_string.encode('utf-8')
    subprocess.run(["sudo", "visudo", "-f", "/etc/sudoers"], input=input_bytes)

# Grant permission to view, list, and stop network services
def grant_permission_to_network_services(username):
    input_string = "%s ALL=NOPASSWD:/bin/systemctl status network-*, /bin/systemctl list-units network-*, /bin/systemctl stop network-*" % username
    input_bytes = input_string.encode('utf-8')
    subprocess.run(["sudo", "visudo", "-f", "/etc/sudoers"], input=input_bytes)

# Grant permission to view, list, and stop system services
def grant_permission_to_system_services(username):
    input_string = "%s ALL=NOPASSWD:/bin/systemctl status system-*, /bin/systemctl list-units system-*, /bin/systemctl stop system-*" % username
    input_bytes = input_string.encode('utf-8')
    subprocess.run(["sudo", "visudo", "-f", "/etc/sudoers"], input=input_bytes)

# Grant permission to view, list, and stop logging services
def grant_permission_to_logging_services(username):
    input_string = "%s ALL=NOPASSWD:/bin/systemctl status journal-*, /bin/systemctl list-units journal-*, /bin/systemctl stop journal-*" % username
    input_bytes = input_string.encode('utf-8')
    subprocess.run(["sudo", "visudo", "-f", "/etc/sudoers"], input=input_bytes)

# Main function
def main():
    username = "testuser"
    home_directory = "/home/%s" % username

    create_user(username, home_directory)
    add_user_to_sudo(username)
    set_password(username)
    grant_permission_to_restart_services(username)
    grant_permission_to_network_services(username)
    grant_permission_to_system_services(username)
    grant_permission_to_logging_services(username)

if __name__ == "__main__":
    main()