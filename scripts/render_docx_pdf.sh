#!/usr/bin/env bash
# Render a .docx to .pdf via LibreOffice, sandboxed so it does not touch
# %userprofile%\Documents and does not trip Windows Controlled Folder Access.
#
# Usage:
#   scripts/render_docx_pdf.sh <input.docx> [<input.docx> ...]
#
# Output: PDFs land in /tmp/sw_pdfs/<stem>.pdf (one per input).
#
# The -env:UserInstallation flag points LibreOffice at a disposable profile
# directory, so it does not read user templates, recent-documents list, or the
# default "My Documents" save path. --headless + --nolockcheck + --nologo
# further suppress interactive and shared-lock behaviour.
#
# Why this exists: a bare `soffice --headless --convert-to pdf` run triggers
# Windows "Protected folder access blocked" alerts for %userprofile%\Documents
# because LibreOffice's default user profile tries to initialise paths there.
# The sandboxed profile avoids those alerts.

set -euo pipefail

SOFFICE="${SOFFICE:-/c/Program Files/LibreOffice/program/soffice.exe}"
OUTDIR="${OUTDIR:-/tmp/sw_pdfs}"

if [[ $# -lt 1 ]]; then
    echo "usage: $0 <input.docx> [<input.docx> ...]" >&2
    exit 2
fi

if [[ ! -x "$SOFFICE" ]]; then
    echo "error: soffice not found at $SOFFICE" >&2
    echo "override with SOFFICE=<path> if LibreOffice is elsewhere" >&2
    exit 2
fi

mkdir -p "$OUTDIR"

PROFILE_DIR=$(mktemp -d -t sw_lo_profile.XXXXXX)
trap 'rm -rf "$PROFILE_DIR"' EXIT

# Convert the mktemp path (Git Bash /tmp/...) to a Windows path for the URI.
WIN_PROFILE=$(cygpath -w "$PROFILE_DIR" | sed 's|\\|/|g')

"$SOFFICE" \
    --headless \
    --nologo \
    --nolockcheck \
    --norestore \
    -env:UserInstallation="file:///${WIN_PROFILE}" \
    --convert-to pdf \
    --outdir "$OUTDIR" \
    "$@"

echo "---"
echo "outputs in $OUTDIR:"
for f in "$@"; do
    stem=$(basename "$f" .docx)
    out="$OUTDIR/${stem}.pdf"
    if [[ -f "$out" ]]; then
        size=$(stat -c '%s' "$out")
        printf '  %s (%d bytes)\n' "$out" "$size"
    else
        printf '  %s MISSING\n' "$out"
    fi
done
