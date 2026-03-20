import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ai_hook_guard.analyzer import Analyzer

def main():

    # Get absolute path
    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_dir, "examples", "test_reentrancy.sol")

    with open(file_path, "r") as f:
        code = f.read()

    analyzer = Analyzer()
    result = analyzer.analyze(code)

    print("\n=== ANALYSIS RESULT ===\n")
    for key, value in result.items():
        print(f"{key}: {value}\n")


if __name__ == "__main__":
    main()
