#!/usr/bin/env python3
"""Simple helper to fetch user info from Fireflies.ai using the API key."""
import json
import os
import sys
import urllib.request

API_URL = "https://api.fireflies.ai/v1/user"

def main() -> None:
    api_key = os.environ.get("FIREFLIES_API_KEY")
    if not api_key:
        raise SystemExit("FIREFLIES_API_KEY environment variable is not set")

    request = urllib.request.Request(
        API_URL,
        headers={"Authorization": f"Bearer {api_key}"},
    )

    with urllib.request.urlopen(request) as response:
        data = response.read()

    try:
        payload = json.loads(data)
    except json.JSONDecodeError:
        sys.stdout.buffer.write(data)
    else:
        print(json.dumps(payload, indent=2))

if __name__ == "__main__":
    main()
