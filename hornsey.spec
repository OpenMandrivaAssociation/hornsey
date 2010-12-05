%define version 0.5
%define rel 3
%define snapshot git20091030
%define release %mkrel 0.%{snapshot}.%{rel}

%define sversion %{version}%{snapshot}

Name: hornsey
Summary: The Moblin media player
Group: Graphical desktop/Other
Version: %{version}
License: LGPLv2.1
URL: http://www.moblin.org
Release: %{release}
Source0: %{name}-%{sversion}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

# patches commited after moblin-2.1 was tagged
Patch0: hornsey-0.5-fix-6876-crash.patch
Patch1: hornsey-0.5-fix-7358-scrollbar.patch
Patch2: hornsey-0.5-fix-7807-cpu.patch
Patch3: hornsey-0.5git20091030-new-clutter-gst.patch
BuildRequires: clutter-devel
BuildRequires: clutter-gst-devel
BuildRequires: clutter-gtk-devel
BuildRequires: bickley-devel
BuildRequires: nbtk-devel
BuildRequires: startup-notification-devel
BuildRequires: unique-devel
BuildRequires: bognor-regis-devel
BuildRequires: gnome-common
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: libnotify-devel
BuildRequires: libxtst-devel

%description
The Moblin media player

%prep
%setup -q -n %{name}-%{sversion}
%apply_patches

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root,-)
%doc COPYING AUTHORS NEWS README ChangeLog
%{_bindir}/hornsey
%{_datadir}/%{name}/*
%{_datadir}/icons/hicolor/64x64/apps/hornsey.png
%{_datadir}/applications/hornsey.desktop
%{_datadir}/dbus-1/services/org.moblin.Hornsey.service
%{_datadir}/locale/*
