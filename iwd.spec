# TODO: system ell
Summary:	iwd - wireless daemon for Linux
Summary(pl.UTF-8):	iwd - demon sieci bezprzewodowej dla Linuksa
Name:		iwd
Version:	0.1
Release:	1
License:	LGPL v2.1+
Group:		Networking/Daemons
Source0:	https://www.kernel.org/pub/linux/network/wireless/%{name}-%{version}.tar.xz
# Source0-md5:	5dba7b3d20d6b5367ba4e55a9eaf6f95
URL:		https://git.kernel.org/pub/scm/network/wireless/iwd.git
BuildRequires:	asciidoc
BuildRequires:	dbus-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wireless daemon for Linux.

%description -l pl.UTF-8
Demon sieci bezprzewodowej dla Linuksa.

%prep
%setup -q

%build
%configure \
	--enable-docs \
	--disable-silent-rules \
	--with-systemd-unitdir=%{systemdunitdir}

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/iwctl
%attr(755,root,root) %{_bindir}/iwmon
%attr(755,root,root) %{_libexecdir}/iwd
%{systemdunitdir}/iwd.service
%{_datadir}/dbus-1/system.d/iwd-dbus.conf
%{_mandir}/man1/iwmon.1*
