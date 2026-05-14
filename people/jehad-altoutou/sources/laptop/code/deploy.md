---
type: source
source_type: laptop
title: deploy
slug: deploy
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/deploy.sh
original_size: 1902
original_ext: .sh
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# deploy

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/deploy.sh` on 2026-05-14._

```bash
#!/bin/bash

# Configuration
SERVER_IP="72.61.149.26"
SERVER_USER="root"
SERVER_PATH="/var/www/dubai-leads"
APP_NAME="dubai-leads"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Starting deployment for ${APP_NAME}...${NC}"

# 1. Package the project
echo -e "${BLUE}📦 Packaging project (excluding node_modules, .git, and update.tar.gz)...${NC}"
tar -czf update.tar.gz --exclude=node_modules --exclude=.git --exclude=update.tar.gz -C . .

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Packaging failed.${NC}"
    exit 1
fi

# 2. Upload to server
echo -e "${BLUE}📤 Uploading to ${SERVER_USER}@${SERVER_IP}...${NC}"
scp update.tar.gz ${SERVER_USER}@${SERVER_IP}:/root/

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Upload failed. Please check your SSH connection.${NC}"
    rm update.tar.gz
    exit 1
fi

# 3. Extract and rebuild remotely
echo -e "${BLUE}🏗️ Rebuilding on Hostinger...${NC}"
ssh ${SERVER_USER}@${SERVER_IP} << EOF
    # Ensure directory exists
    mkdir -p ${SERVER_PATH}
    
    # Extract
    echo "Extracting..."
    tar -xzf /root/update.tar.gz -C ${SERVER_PATH}
    
    # Navigate and rebuild
    cd ${SERVER_PATH}
    echo "Building Docker container..."
    docker compose build app
    
    echo "Starting container..."
    docker compose up -d --no-deps app
    
    # Clean up update file
    rm /root/update.tar.gz
    
    echo "Applying database schema changes..."
    docker compose exec -T app npx prisma db push --skip-generate

    echo "Checking status..."
    docker compose ps app
EOF

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Remote rebuild failed.${NC}"
    rm update.tar.gz
    exit 1
fi

# 4. Clean up local update file
rm update.tar.gz

echo -e "${GREEN}✅ Deployment successful!${NC}"
echo -e "${GREEN}🌍 Check your site at: https://dubaipropertyleads.ae/api/health${NC}"

```