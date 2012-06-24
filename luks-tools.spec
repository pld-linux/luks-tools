Summary:	Utilities for working with LUKS-protected filesystems
Summary(pl):	Narz�dzia do pracy z systemami plik�w chronionymi przez LUKS
Name:		luks-tools
Version:	0.0.9
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://www.flyn.org/projects/luks-tools/%{name}-%{version}.tar.gz
# Source0-md5:	be29c9090450c8efeafd3e8b81dccbb2
Patch0:		%{name}-ac_progs_paths_fix.patch
URL:		http://www.flyn.org/projects/luks-tools/index.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cryptsetup-luks-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The luks-tools package contains various utilities for working with
LUKS-protected filesystems. HAL uses these utilites to automatically
mount encrypted volumes when they are attached to a system, provided
the user can produce the correct passphrase.

%description -l pl
Pakiet luks-tools zawiera r�ne narz�dzia do pracy z systemami plik�w
chronionymi przez LUKS. HAL u�ywa tych narz�dzi do automatycznego
montowania zaszyfrowanych wolumen�w przy pod��czaniu do systemu, pod
warunkiem, �e u�ytkownik mo�e poda� poprawne has�o.

%package -n gnome-luks
Summary:	GNOME utilities for working with LUKS-protected filesystems
Summary(pl):	Narz�dzia GNOME do pracy z systemami plik�w chronionymi przez LUKS
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygtk-glade
Requires:	python-dbus >= 0.33

%description -n gnome-luks
GNOME utilities for working with LUKS-protected filesystems.

%description -n gnome-luks -l pl
Narz�dzia GNOME do pracy z systemami plik�w chronionymi przez LUKS.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
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
