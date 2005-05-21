Summary:	Utilities for working with LUKS-protected filesystems
Name:		luks-tools
Version:	0.0.4
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://www.flyn.org/projects/luks-tools/%{name}-%{version}.tar.gz
# Source0-md5:	6b2be4062878333a580d560f965a666a
URL:		http://www.flyn.org/projects/luks-tools/index.html
BuildRequires:	cryptsetup-luks-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The luks-tools package contains various utilities for working with
LUKS-protected filesystems. HAL uses these utilites to automatically mount
encrypted volumes when they are attached to a system, provided the user can
produce the correct passphrase.

%package -n gnome-luks
Summary:	GNOME utilities for working with LUKS-protected filesystems
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygtk-glade
Requires:	python-dbus >= 0.33

%description -n gnome-luks
GNOME utilities for working with LUKS-protected filesystems.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*

%files -n gnome-luks
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome*
%{_datadir}/%{name}
