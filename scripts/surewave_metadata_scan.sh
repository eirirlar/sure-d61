#!/bin/bash
# Scan all filed SUREWAVE deliverables and extract table-like metadata.
# One-off helper for T111 status.md preparation.
set -e
cd "$(dirname "$0")/../surewave/background"

# Skip the three grant-application docs; only walk the numbered deliverables and CFD note.
for f in [0-9]*.md; do
  base="${f%.md}"
  case "$base" in
    2022-02-23_surewave_proposal*|2022-06-24_surewave_annex1*|2022-09-20_surewave_grant*)
      continue ;;
  esac

  # Grab first ~80 lines for the deliverable details table
  head -80 "$f" > /tmp/scan_head.txt

  # Extract key fields with permissive regexes
  del_no=$(grep -oiE "Deliverable (No|number):[^|]*" /tmp/scan_head.txt | head -1 | sed 's/.*[Nn]umber:\s*//;s/.*[Nn]o:\s*//' | tr -d '\r\n' | head -c 40)
  title=$(grep -oiE "^Title:.*|^\s*Title:.*|D[0-9]\.[0-9]:?\s+[A-Z][^\n|]{5,120}" /tmp/scan_head.txt | head -1 | sed 's/^\s*Title:\s*//;s/[*_]//g' | head -c 120)
  wp=$(grep -oiE "\*\*WP\*\*\s+[0-9]+" /tmp/scan_head.txt | head -1 | grep -oE "[0-9]+" | head -1)
  task=$(grep -oiE "\*\*Task\*\*\s+D?[0-9]+\.?[0-9]*" /tmp/scan_head.txt | head -1 | sed 's/\*\*//g;s/Task\s*//i' | head -c 20)
  diss=$(grep -oiE "Dissemination level\**\s*\|?\s*\*?\*?[A-Z_-]+\*?\*?" /tmp/scan_head.txt | head -1 | grep -oE "PU|SEN|EU-Con|CI|CO|Public|Confidential|Sensitive" | head -1)
  dtype=$(grep -oiE "Deliverable type\**\s*\|?\s*\*?\*?[A-Z_-]+\*?\*?" /tmp/scan_head.txt | head -1 | grep -oE "R|DEM|DEC|DMP|OTHER|ORDP" | head -1)
  due=$(grep -oiE "Due (delivery date|date)[^|]*" /tmp/scan_head.txt | head -1 | grep -oE "[0-9]{1,2}[./-][0-9]{1,2}[./-][0-9]{2,4}" | head -1)
  actual=$(grep -oiE "Actual (delivery date|submission)[^|]*" /tmp/scan_head.txt | head -1 | grep -oE "[0-9]{1,2}[./-][0-9]{1,2}[./-][0-9]{2,4}" | head -1)
  lead=$(awk '/Lead beneficiary/{found=1;next} found && NF{print;exit}' /tmp/scan_head.txt | grep -oE "\*\*[A-Za-z_ ]+\*\*" | head -1 | tr -d '*' | head -c 40)
  contrib=$(awk '/Contributing beneficiaries/{found=1;next} found && NF{print;exit}' /tmp/scan_head.txt | tr -d '*|' | tr -s ' ' | head -c 120)
  size=$(wc -l < "$f")

  echo "===FILE==="
  echo "path|$f"
  echo "lines|$size"
  echo "del_no|$del_no"
  echo "title|$title"
  echo "wp|$wp"
  echo "task|$task"
  echo "type|$dtype"
  echo "diss|$diss"
  echo "due|$due"
  echo "actual|$actual"
  echo "lead|$lead"
  echo "contrib|$contrib"
done
