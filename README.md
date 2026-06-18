# warp-headless-deps-dummy

Dummy RPM to satisfy GUI dependencies for Cloudflare WARP on headless systems (e.g., Amazon Linux 2023).

## Why this exists

`cloudflare-warp` depends on GUI libraries like:
- webkit2gtk3
- libappindicator-gtk3

These are not needed when running WARP in headless/server environments.

This package provides those dependencies virtually so `dnf` can proceed.

## Build
```bash

./build.sh
```

## Install
```bash
sudo dnf install -y ~/rpmbuild/RPMS/noarch/warp-headless-deps-dummy-*.rpm
```

## Example Usage
```
curl -L -o /tmp/dummy.rpm https://raw.githubusercontent.com/<user>/<repo>/main/warp-headless-deps-dummy-1.0-1.noarch.rpm
dnf install -y /tmp/dummy.rpm
dnf install -y cloudflare-warp
```

## Notes

Intended for headless systems only
Do not use on desktop environments
