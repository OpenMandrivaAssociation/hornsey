Name: hornsey
Summary: The Moblin media player
Group: Graphical desktop/Other
Version: 0.5git20091001
License: LGPLv2.1
URL: http://www.moblin.org
Release: %mkrel 1
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: clutter-devel
BuildRequires: clutter-gst-devel
BuildRequires: clutter-gtk-devel
BuildRequires: libbickley-devel
BuildRequires: libnbtk-devel
BuildRequires: startup-notification-devel
BuildRequires: libunique-devel
BuildRequires: bognor-regis-devel
BuildRequires: gnome-common
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: libnotify-devel
BuildRequires: libxtst-devel

Requires(post): /bin/touch

%description
The Moblin media player

%prep
%setup -q 

%build
./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post 
/bin/touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache \
  --quiet %{_datadir}/icons/hicolor 2> /dev/null|| :

%files 
%defattr(-,root,root,-)
%doc COPYING AUTHORS NEWS README ChangeLog
%{_bindir}/hornsey
%{_datadir}/%{name}/*
%{_datadir}/icons/hicolor/64x64/apps/hornsey.png
%{_datadir}/applications/hornsey.desktop
%{_datadir}/dbus-1/services/org.moblin.Hornsey.service
%{_datadir}/locale/*
