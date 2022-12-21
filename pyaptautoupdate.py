import subprocess
import getpass

def run_apt_commands():
    # Ask for the sudo password
    sudo_password = getpass.getpass(prompt="Enter your sudo password: ")

    # Run the apt update command
    update_command = ["sudo", "-S", "apt", "update"]
    update_process = subprocess.run(update_command, input=sudo_password, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    if update_process.returncode != 0:
        print("Error updating package list:")
        print(update_process.stderr)
        return

    # Run the apt upgrade command
    upgrade_command = ["sudo", "-S", "apt", "upgrade", "-y"]
    upgrade_process = subprocess.run(upgrade_command, input=sudo_password, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    if upgrade_process.returncode != 0:
        print("Error upgrading packages:")
        print(upgrade_process.stderr)
        return

    print("Packages updated and upgraded successfully!")

if __name__ == "__main__":
    run_apt_commands()
