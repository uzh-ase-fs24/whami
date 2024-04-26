import subprocess
import os


def run_coverage_tests():
    # Run coverage with unittest
    # Set the path for the .coverage data file
    subprocess.run(["python3", "-m", "coverage", "run", "--data-file=test_report/.coverage", "-m", "unittest"])


def generate_coverage_report():
    # Generate coverage report
    # Use the specified .coverage data file
    subprocess.run(["python3", "-m", "coverage", "report", "--data-file=test_report/.coverage"])


def generate_html_report():
    # Generate HTML coverage report
    # Specify output directory for HTML files and use the specified .coverage data file
    subprocess.run(["python3", "-m", "coverage", "html", "-d", "test_report", "--data-file=test_report/.coverage"])


if __name__ == "__main__":
    os.chdir("../backend")
    # Ensure the coverage directory exists before running tests
    if not os.path.exists("test_report"):
        os.makedirs("test_report")
    run_coverage_tests()
    generate_coverage_report()
    generate_html_report()
