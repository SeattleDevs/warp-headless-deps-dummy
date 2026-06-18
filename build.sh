#!/bin/bash
set -e

# install tools if missing
sudo dnf install -y rpm-build rpmdevtools

# setup tree if not present
[ -d "$HOME/rpmbuild" ] || rpmdev-setuptree

# copy spec into place
cp warp-headless-deps-dummy.spec ~/rpmbuild/SPECS/

# build rpm
rpmbuild -bb ~/rpmbuild/SPECS/warp-headless-deps-dummy.spec

echo "RPM built at:"
ls -1 ~/rpmbuild/RPMS/noarch/
