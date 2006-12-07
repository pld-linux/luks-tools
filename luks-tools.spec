Summary:	Utilities for working with LUKS-protected filesystems
Summary(pl):	Narzêdzia do pracy z systemami plików chronionymi przez LUKS
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
Pakiet luks-tools zawiera ró¿ne narzêdzia do pracy z systemami plików
chronionymi przez LUKS. HAL u¿ywa tych narzêdzi do automatycznego
montowania zaszyfrowanych wolumenów przy pod³±czaniu do systemu, pod
warunkiem, ¿e u¿ytkownik mo¿e podaæ poprawne has³o.

%package -n gnome-luks
Summary:	GNOME utilities for working with LUKS-protected filesystems
Summary(pl):	Narzêdzia GNOME do pracy z systemami plików chronionymi przez LUKS
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygtk-glade
Requires:	python-dbus >= 0.33

%description -n gnome-luks
GNOME utilities for working with LUKS-protected filesystems.

%description -n gnome-luks -l pl
Narzêdzia GNOME do pracy z systemami plików chronionymi przez LUKS.

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
