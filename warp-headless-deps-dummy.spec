Name:        warp-headless-deps-dummy
Version:     1.0
Release:     1%{?dist}
Summary:     Dummy package to satisfy cloudflare-warp dependencies
License:     MIT
BuildArch:   noarch

Provides:    webkit2gtk3
Provides:    libwebkit2gtk-4.0.so.37()(64bit)
Provides:    libappindicator-gtk3
Provides:    libappindicator-gtk3.so.1()(64bit)

%description
Fake package to bypass GUI dependencies for headless Cloudflare WARP.

%files
%ghost /
