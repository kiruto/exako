#!/usr/bin/env bash
find . -name "*sql" -type f -exec sql-protobuf {} \; > src/protobuf/database.proto
