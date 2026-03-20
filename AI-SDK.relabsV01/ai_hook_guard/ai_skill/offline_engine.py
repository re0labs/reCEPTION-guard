##local fallback version with no API key
def build_local_analysis(code: str, findings: list) -> str:
    if not findings:
        return (
            "No major issues were detected by the local analyzer. "
            "The hook appears to follow the currently implemented safety checks."
        )

    lines = []
    lines.append("Local security analysis summary:")
    lines.append("")

    for i, finding in enumerate(findings, start=1):
        lines.append(f"{i}. Issue: {finding.get('type', 'unknown')}")
        lines.append(f"   Description: {finding.get('description', '')}")
        lines.append(f"   Severity: {finding.get('severity', '')}")
        lines.append(f"   Details: {finding.get('details', '')}")

        recommendation = finding.get("recommendation", "")
        if recommendation:
            lines.append(f"   Recommendation: {recommendation}")

        patch = finding.get("patch", "")
        if patch:
            lines.append(f"   Patch: {patch}")

        lines.append("")

    lines.append(
        "This analysis was generated locally without requiring an external AI API key."
    )
    return "\n".join(lines)


def run_offline_ai_skill(code: str, findings: list) -> str:
    return build_local_analysis(code, findings)
