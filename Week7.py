# LAB EXERCISE 1 – PRODUCT PRICING MANAGER

import logging
import re
from collections import defaultdict, Counter

# --------------------------------------------------
# Logging Configuration (shared)
# --------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("analysis_audit.log"),
        logging.StreamHandler()
    ]
)


# ==================================================
# EXERCISE 1 FUNCTIONS (UNCHANGED)
# ==================================================

def calculate_discount(category, tier):
    """
    Calculate total discount percentage based on
    product category and discount tier.
    """
    category_discounts = {
        "Electronics": 10,
        "Clothing": 15,
        "Books": 5,
        "Home": 12
    }

    tier_discounts = {
        "Premium": 5,
        "Standard": 0,
        "Budget": 2
    }

    return category_discounts.get(category, 0) + tier_discounts.get(tier, 0)


def process_products(input_file, output_file):
    """
    Read product data, calculate discounts,
    generate pricing report, and print summary.
    """
    try:
        products = []
        total_discount = 0

        with open(input_file, "r") as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    parts = line.strip().split(",")

                    if len(parts) != 4:
                        logging.warning(
                            f"Line {line_number}: Invalid format"
                        )
                        continue

                    name, price_str, category, tier = parts
                    base_price = float(price_str)

                    discount_pct = calculate_discount(category, tier)
                    discount_amount = base_price * (discount_pct / 100)
                    final_price = base_price - discount_amount

                    products.append({
                        "name": name,
                        "base_price": base_price,
                        "discount_pct": discount_pct,
                        "discount_amount": discount_amount,
                        "final_price": final_price
                    })

                    total_discount += discount_pct

                except ValueError as error:
                    logging.error(
                        f"Line {line_number}: Invalid price - {error}"
                    )

        with open(output_file, "w") as file:
            file.write("=" * 90 + "\n")
            file.write("PRICING REPORT\n")
            file.write("=" * 90 + "\n")
            file.write(
                f"{'Product Name':<30}"
                f"{'Base Price':>12}"
                f"{'Discount %':>12}"
                f"{'Discount $':>12}"
                f"{'Final Price':>12}\n"
            )
            file.write("-" * 90 + "\n")

            for product in products:
                file.write(
                    f"{product['name']:<30}"
                    f"${product['base_price']:>11.2f}"
                    f"{product['discount_pct']:>11.1f}%"
                    f"${product['discount_amount']:>11.2f}"
                    f"${product['final_price']:>11.2f}\n"
                )

            file.write("=" * 90 + "\n")

        average_discount = (
            total_discount / len(products) if products else 0
        )

        print("\nExercise 1 Complete")
        print(f"Products processed: {len(products)}")
        print(f"Average discount: {average_discount:.2f}%")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")

    except PermissionError:
        print(f"Error: Cannot write '{output_file}'")


# ==================================================
# LAB EXERCISE 2 – ADVANCED SERVER LOG ANALYZER
# (REWRITTEN – ONLY THIS PART CHANGED)
# ==================================================

class LogAnalyzer:
    """
    Analyze Apache-style server logs,
    detect security incidents, and
    generate multiple reports.
    """

    def __init__(self, log_file):
        self.log_file = log_file

        self.log_pattern = re.compile(
            r'(\S+) - - \[(.*?)\] "(\S+) (\S+) \S+" (\d+) (\d+)'
        )

        self.total_requests = 0
        self.unique_ips = set()
        self.http_methods = Counter()
        self.urls = Counter()
        self.status_codes = Counter()
        self.errors = []

        self.failed_logins = defaultdict(list)
        self.forbidden_access = []
        self.security_incidents = []


    def parse_log_line(self, line):
        match = self.log_pattern.match(line)
        if not match:
            return None

        ip, timestamp, method, url, status, size = match.groups()

        return {
            "ip": ip,
            "timestamp": timestamp,
            "method": method,
            "url": url,
            "status": int(status),
            "size": int(size)
        }


    def analyze_security(self, entry):
        if entry["url"] == "/login" and entry["status"] == 401:
            self.failed_logins[entry["ip"]].append(entry["timestamp"])
            attempts = len(self.failed_logins[entry["ip"]])

            if attempts >= 3:
                incident = (
                    f"Brute force attempt from {entry['ip']} - "
                    f"{attempts} failed attempts"
                )
                self.security_incidents.append(incident)
                logging.warning(incident)

        if entry["status"] == 403:
            incident = (
                f"Forbidden access attempt: "
                f"{entry['ip']} -> {entry['url']}"
            )
            self.forbidden_access.append(incident)
            self.security_incidents.append(incident)
            logging.warning(incident)

        sql_patterns = ["union", "select", "drop", "insert", "--", ";"]
        if any(p in entry["url"].lower() for p in sql_patterns):
            incident = (
                f"Potential SQL injection: "
                f"{entry['ip']} -> {entry['url']}"
            )
            self.security_incidents.append(incident)
            logging.warning(incident)


    def process_logs(self):
        try:
            logging.info(f"Starting analysis of {self.log_file}")

            with open(self.log_file, "r") as file:
                for line_number, line in enumerate(file, start=1):
                    try:
                        entry = self.parse_log_line(line.strip())
                        if not entry:
                            raise ValueError("Malformed log entry")

                        self.total_requests += 1
                        self.unique_ips.add(entry["ip"])
                        self.http_methods[entry["method"]] += 1
                        self.urls[entry["url"]] += 1
                        self.status_codes[entry["status"]] += 1

                        if entry["status"] >= 400:
                            self.errors.append(entry)

                        self.analyze_security(entry)

                    except Exception as error:
                        logging.error(
                            f"Line {line_number}: Error processing - {error}"
                        )

            logging.info(
                f"Analysis complete: {self.total_requests} requests processed"
            )

        except FileNotFoundError:
            print("Error: Log file not found")


    def generate_reports(self):

        with open("summary_report.txt", "w") as file:
            file.write("=" * 70 + "\n")
            file.write("SERVER LOG ANALYSIS SUMMARY\n")
            file.write("=" * 70 + "\n\n")
            file.write(f"Total Requests: {self.total_requests}\n")
            file.write(f"Unique Visitors: {len(self.unique_ips)}\n")

        with open("security_incidents.txt", "w") as file:
            file.write("=" * 70 + "\n")
            file.write("SECURITY INCIDENTS REPORT\n")
            file.write("=" * 70 + "\n\n")
            for incident in self.security_incidents:
                file.write(incident + "\n")

        with open("error_log.txt", "w") as file:
            file.write("=" * 70 + "\n")
            file.write("HTTP ERRORS LOG\n")
            file.write("=" * 70 + "\n\n")
            for error in self.errors:
                file.write(
                    f"[{error['timestamp']}] {error['ip']} - "
                    f"{error['method']} {error['url']} - "
                    f"Status: {error['status']}\n"
                )


# ==================================================
# PROGRAM ENTRY POINT
# ==================================================

if __name__ == "__main__":

    process_products("products.txt", "pricing_report.txt")

    analyzer = LogAnalyzer("server.log")
    analyzer.process_logs()
    analyzer.generate_reports()

    print("\nAll exercises completed successfully.")
