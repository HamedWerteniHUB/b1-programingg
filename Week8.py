from datetime import datetime, timedelta


# ==================================================
# Lab Exercise 1: Secure User Authentication System
# ==================================================
class User:
    def __init__(self, username, password, privilege_level="standard"):
        self.__username = username
        self.__password_hash = self.__hash_password(password)
        self.__privilege_level = privilege_level
        self.__login_attempts = 0
        self.__account_status = "active"
        self.__activity_log = []

    # ---------- Private Methods ----------
    def __hash_password(self, password):
        # Simulate password hashing
        return f"hashed_{password}"

    def __log_activity(self, message):
        self.__activity_log.append(f"{datetime.now()}: {message}")

    # ---------- Authentication ----------
    def authenticate(self, password):
        if self.__account_status == "locked":
            self.__log_activity("Login attempt on locked account")
            return False

        if self.__hash_password(password) == self.__password_hash:
            self.__login_attempts = 0
            self.__log_activity("Successful login")
            return True
        else:
            self.__login_attempts += 1
            self.__log_activity(f"Failed login attempt {self.__login_attempts}")

            if self.__login_attempts >= 3:
                self.lock_account()

            return False

    def lock_account(self):
        self.__account_status = "locked"
        self.__log_activity("Account locked due to failed login attempts")

    def reset_login_attempts(self, admin_password):
        if self.__hash_password(admin_password) == "hashed_admin_secret":
            self.__account_status = "active"
            self.__login_attempts = 0
            self.__log_activity("Account unlocked by admin")
            return True
        return False

    # ---------- Access Control ----------
    def check_privileges(self, required_level):
        privilege_hierarchy = {
            "guest": 0,
            "standard": 1,
            "admin": 2
        }
        return (
            privilege_hierarchy.get(self.__privilege_level, 0)
            >= privilege_hierarchy.get(required_level, 0)
        )

    # ---------- Safe Access ----------
    def get_safe_info(self):
        return {
            "username": self.__username,
            "privilege_level": self.__privilege_level,
            "account_status": self.__account_status
        }

    def get_username(self):
        return self.__username

    def get_privilege_level(self):
        return self.__privilege_level


# ==================================================
# Lab Exercise 2: IoT Device Management System
# ==================================================
class Device:
    def __init__(self, device_id, device_type, owner, firmware_version="1.0.0"):
        self.__device_id = device_id
        self.__device_type = device_type
        self.__firmware_version = firmware_version
        self.__compliance_status = "unknown"
        self.__owner = owner
        self.__last_security_scan = None
        self.__is_active = True
        self.__access_log = []

    # ---------- Internal Logging ----------
    def __log_access(self, username, action):
        self.__access_log.append(
            f"{datetime.now()}: {username} - {action}"
        )

    # ---------- Access Control ----------
    def authorise_access(self, user):
        if not self.__is_active:
            self.__log_access(user.get_username(), "Denied - Device inactive")
            return False

        if self.__compliance_status != "compliant":
            if not user.check_privileges("admin"):
                self.__log_access(
                    user.get_username(),
                    "Denied - Non-compliant device"
                )
                return False

        if self.__owner != user.get_username() and not user.check_privileges("admin"):
            self.__log_access(user.get_username(), "Denied - Not owner")
            return False

        self.__log_access(user.get_username(), "Access granted")
        return True

    # ---------- Security & Compliance ----------
    def run_security_scan(self):
        self.__last_security_scan = datetime.now()
        self.__compliance_status = "compliant"
        self.__log_access("SYSTEM", "Security scan completed")

    def check_compliance(self):
        if self.__last_security_scan is None:
            self.__compliance_status = "unknown"
            return False

        days_since_scan = (datetime.now() - self.__last_security_scan).days
        if days_since_scan > 30:
            self.__compliance_status = "non-compliant"
            return False

        return self.__compliance_status == "compliant"

    def update_firmware(self, version, user):
        if not user.check_privileges("admin"):
            return False

        self.__firmware_version = version
        self.__log_access(
            user.get_username(),
            f"Firmware updated to {version}"
        )
        return True

    def quarantine(self, user):
        if not user.check_privileges("admin"):
            return False

        self.__is_active = False
        self.__log_access(user.get_username(), "Device quarantined")
        return True

    # ---------- Safe Access ----------
    def get_device_info(self):
        return {
            "device_id": self.__device_id,
            "device_type": self.__device_type,
            "firmware_version": self.__firmware_version,
            "compliance_status": self.__compliance_status,
            "owner": self.__owner,
            "is_active": self.__is_active
        }


class DeviceManager:
    def __init__(self):
        self.__devices = {}

    def add_device(self, device):
        device_info = device.get_device_info()
        self.__devices[device_info["device_id"]] = device

    def remove_device(self, device_id, user):
        if not user.check_privileges("admin"):
            return False

        if device_id in self.__devices:
            del self.__devices[device_id]
            return True

        return False

    def generate_security_report(self, user):
        if not user.check_privileges("admin"):
            return None

        report = []
        for device in self.__devices.values():
            device.check_compliance()
            report.append(device.get_device_info())

        return report
