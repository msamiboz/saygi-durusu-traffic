#!/bin/zsh
# Retry the 2023 general-election neighbourhood download until all three Istanbul files exist.
cd "$(dirname "$0")/.."
for i in {1..10}; do
  n=$(find data/raw/elections/genel_bolge -name '*.xls*' 2>/dev/null | wc -l | tr -d ' ')
  echo "$(date '+%F %T') round $i: $n of 3 files"
  [ "$n" -ge 3 ] && break
  TUIK_WAIT_REPORT_MS=900000 python3 tools/tuik_genel_istanbul.py 2>&1 | grep -E "attempt|->|already"
  n=$(find data/raw/elections/genel_bolge -name '*.xls*' 2>/dev/null | wc -l | tr -d ' ')
  [ "$n" -ge 3 ] && break
  sleep 1800
done
echo "$(date '+%F %T') finished: $(find data/raw/elections/genel_bolge -name '*.xls*' | wc -l | tr -d ' ') files"
