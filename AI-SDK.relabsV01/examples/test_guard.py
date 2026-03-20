import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai_hook_guard.guard import hook_guard


def severity_label(severity):
    labels = {
        "high": "[HIGH]",
        "medium": "[MEDIUM]",
        "low": "[LOW]"
    }
    return labels.get(str(severity).lower(), "[UNKNOWN]")


def print_guard_result(result):
    print("\n" + "=" * 70)
    print("AI HOOK GUARD SECURITY REPORT")
    print("=" * 70)

    approved = result.get("approved", False)
    status = "APPROVED" if approved else "REJECTED"

    print(f"Status       : {status}")
    print(f"Risk Score   : {result.get('risk_score', 'N/A')}")
    print(f"Confidence   : {result.get('confidence', 'N/A')}")

    issues = result.get("issues", [])
    findings = result.get("findings", [])

    high_count = sum(1 for f in findings if str(f.get("severity", "")).lower() == "high")
    medium_count = sum(1 for f in findings if str(f.get("severity", "")).lower() == "medium")
    low_count = sum(1 for f in findings if str(f.get("severity", "")).lower() == "low")

    print(f"Issues Found : {len(issues)}")
    print(f"High         : {high_count}")
    print(f"Medium       : {medium_count}")
    print(f"Low          : {low_count}")

    if issues:
        print("\nDetected Issues:")
        for i, issue in enumerate(issues, 1):
            print(f"  {i}. {issue}")

    if findings:
        print("\n" + "-" * 70)
        print("DETAILED FINDINGS")
        print("-" * 70)

        for i, finding in enumerate(findings, 1):
            severity = finding.get("severity", "unknown")
            print(f"\n[{i}] {finding.get('type', 'unknown').upper()} {severity_label(severity)}")
            print(f"Description   : {finding.get('description', 'N/A')}")
            print(f"Details       : {finding.get('details', 'N/A')}")
            print(f"Recommendation: {finding.get('recommendation', 'N/A')}")
            print(f"Patch         : {finding.get('patch', 'N/A')}")

    fixed_code = result.get("fixed_code")
    if fixed_code:
        print("\n" + "-" * 70)
        print("CODE REVIEWED")
        print("-" * 70)
        print(fixed_code.strip())

    ai_analysis = result.get("ai_analysis")
    if ai_analysis:
        print("\n" + "-" * 70)
        print("AI ANALYSIS SUMMARY")
        print("-" * 70)
        print(ai_analysis)

    print("\n" + "-" * 70)
    print("FINAL DECISION")
    print("-" * 70)

    if approved:
        print("The contract passed the basic security checks.")
    else:
        print("The contract failed the security checks.")
        if high_count > 0:
            print(f"Reason: {high_count} high-severity issue(s) detected.")
        elif medium_count > 0:
            print(f"Reason: {medium_count} medium-severity issue(s) detected.")
        else:
            print("Reason: issues were detected and should be reviewed.")

    print("=" * 70 + "\n")


sample_contract = """
contract TestHook {
    mapping(address => uint256) public balances;

    function withdraw(uint256 amount) public {
        msg.sender.call{value:amount}("");
        balances[msg.sender] -= amount;
    }

    function beforeSwap(address caller, bytes calldata data) external returns (bytes4) {
        return this.beforeSwap.selector;
    }

    function updateDelta(int256 delta) external {
        int256 x = delta + 10;
    }
}
"""

result = hook_guard.validate(sample_contract)
print_guard_result(result)
