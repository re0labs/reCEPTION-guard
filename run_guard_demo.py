from ai_hook_guard.guard import hook_guard


sample_code = """
function withdraw(uint amount) public {
    msg.sender.call{value:amount}("");
}
"""


def main():
    result = hook_guard.validate(sample_code)

    print("=" * 60)
    print("AI HOOK GUARD DEMO")
    print("=" * 60)
    print(f"Approved   : {result['approved']}")
    print(f"Risk Score : {result['risk_score']}")
    print(f"Confidence : {result['confidence']}")
    print(f"Issues     : {result['issues']}")
    print("\nFindings:")

    for finding in result["findings"]:
        print(f" - Type: {finding['type']}")
        print(f"   Description: {finding['description']}")
        print(f"   Severity: {finding['severity']}")
        print(f"   Details: {finding['details']}")
        print(f"   Recommendation: {finding.get('recommendation', '')}")
        print(f"   Patch: {finding.get('patch', '')}")
        print()

    print("AI Analysis:")
    print(result["ai_analysis"])


if __name__ == "__main__":
    main()
