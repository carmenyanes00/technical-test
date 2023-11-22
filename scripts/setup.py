import subprocess


# Check if the user account `testuser` exists
def check_if_user_exists(username):
    subprocess.run(["sudo", "useradd", "-m", "-s", "/bin/bash", username, "-d", "/home/%s" % username])

# Create a new user account
def create_user(username, home_directory):
    if not check_if_user_exists(username):
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
    subprocess.run(["sudo", "visudo", "-f", "/etc/sudoers", "-c", input_string])

# Grant permission to view, list, and stop network services
def grant_permission_to_network_services(username):
    input_string = "%s ALL=NOPASSWD:/bin/systemctl status network-*, /bin/systemctl list-units network-*, /bin/systemctl stop network-*" % username
    subprocess.run(["sudo", "visudo", "-f", "/etc/sudoers", "-c", input_string])

# Grant permission to view, list, and stop system services
def grant_permission_to_system_services(username):
    input_string = "%s ALL=NOPASSWD:/bin/systemctl status system-*, /bin/systemctl list-units system-*, /bin/systemctl stop system-*" % username
    subprocess.run(["sudo", "visudo", "-f", "/etc/sudoers", "-c", input_string])

# Grant permission to view, list, and stop logging services
def grant_permission_to_logging_services(username):
    input_string = "%s ALL=NOPASSWD:/bin/systemctl status journal-*, /bin/systemctl list-units journal-*, /bin/systemctl stop journal-*" % username
    subprocess.run(["sudo", "visudo", "-f", "/etc/sudoers", "-c", input_string])

# Main function
def main():
    username = "testuser2"
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
