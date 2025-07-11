#!/bin/sh

if cp -r ../modules .; then
    if langgraph build -t langgraph-api-server --config langgraph-deployment.json; then
        rm -rf modules
    else
        echo "Error: langgraph build failed." >&2
        rm -rf modules
        exit 1
    fi
else
    echo "Error: Failed to copy ../modules directory." >&2
    exit 1
fi
