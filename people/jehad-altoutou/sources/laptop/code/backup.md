---
type: source
source_type: laptop
title: backup
slug: backup
created: 2026-04-14
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/scripts/backup.sh
original_size: 1258
original_ext: .sh
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# backup

_Extracted from `[[assessify|assessify]]/scripts/backup.sh` on 2026-05-14._

```bash
#!/bin/bash
# Assessify automated database backup script
# Usage: ./scripts/backup.sh
# Cron:  0 2 * * * /path/to/assessify/scripts/backup.sh
#
# Keeps the last 30 backups. Stores in ./backups/ directory.

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
BACKUP_DIR="$PROJECT_DIR/backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/assessify_$TIMESTAMP.db"
MAX_BACKUPS=30

# Create backup directory
mkdir -p "$BACKUP_DIR"

# Copy database from container
echo "[Backup] Starting backup at $(date)"
docker compose -f "$PROJECT_DIR/docker-compose.yml" cp app:/app/data/dev.db "$BACKUP_FILE"

if [ -f "$BACKUP_FILE" ]; then
  SIZE=$(du -h "$BACKUP_FILE" | cut -f1)
  echo "[Backup] Success: $BACKUP_FILE ($SIZE)"
else
  echo "[Backup] ERROR: backup file not created"
  exit 1
fi

# Rotate: remove oldest backups beyond MAX_BACKUPS
BACKUP_COUNT=$(ls -1 "$BACKUP_DIR"/assessify_*.db 2>/dev/null | wc -l)
if [ "$BACKUP_COUNT" -gt "$MAX_BACKUPS" ]; then
  REMOVE_COUNT=$((BACKUP_COUNT - MAX_BACKUPS))
  echo "[Backup] Rotating: removing $REMOVE_COUNT old backup(s)"
  ls -1t "$BACKUP_DIR"/assessify_*.db | tail -n "$REMOVE_COUNT" | xargs rm -f
fi

echo "[Backup] Done. $BACKUP_COUNT backup(s) in $BACKUP_DIR"

```