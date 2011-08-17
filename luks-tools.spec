Summary:	Utilities for working with LUKS-protected filesystems
Summary(pl.UTF-8):	Narzędzia do pracy z systemami plików chronionymi przez LUKS
Name:		luks-tools
Version:	0.0.14
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://www.flyn.org/projects/luks-tools/%{name}-%{version}.tar.gz
# Source0-md5:	c9b5f19e2b601c8f776e98c4a8c2189d
URL:		http://www.flyn.org/projects/luks-tools/index.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	check-devel >= 0.8.2
BuildRequires:	cryptsetup-luks-devel >= 1.0.5
BuildRequires:	glib2-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The luks-tools package contains various utilities for working with
LUKS-protected filesystems. HAL uses these utilites to automatically
mount encrypted volumes when they are attached to a system, provided
the user can produce the correct passphrase.

%description -l pl.UTF-8
Pakiet luks-tools zawiera różne narzędzia do pracy z systemami plików
chronionymi przez LUKS. HAL używa tych narzędzi do automatycznego
montowania zaszyfrowanych wolumenów przy podłączaniu do systemu, pod
warunkiem, że użytkownik może podać poprawne hasło.

%package -n gnome-luks
Summary:	GNOME utilities for working with LUKS-protected filesystems
Summary(pl.UTF-8):	Narzędzia GNOME do pracy z systemami plików chronionymi przez LUKS
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	python-dbus >= 0.33
Requires:	python-pygtk-glade

%description -n gnome-luks
GNOME utilities for working with LUKS-protected filesystems.

%description -n gnome-luks -l pl.UTF-8
Narzędzia GNOME do pracy z systemami plików chronionymi przez LUKS.

%prep
%setup -q

# let rpm generate %{__python} dep
%{__sed} -i -e '1s,^#!.*python,#!%{__python},' src/gnome-luks-format.in

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# skip console.apps - redhat permission system
%{__make} install \
	SUBDIRS="src dry pam" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ README TODO
%attr(755,root,root) %{_sbindir}/luks-format
%attr(755,root,root) %{_sbindir}/luks-is-encrypted
%attr(755,root,root) %{_sbindir}/luks-setup
%{_mandir}/man1/luks-format.1*
%{_mandir}/man1/luks-is-encrypted.1*
%{_mandir}/man1/luks-setup.1*
%{_mandir}/man1/luks-tools.1*

%files -n gnome-luks
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-luks-format
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/gnome-luks-format
%{_datadir}/%{name}
%{_mandir}/man1/gnome-luks-format.1*
