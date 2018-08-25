# TODO: system ell
Summary:	iwd - wireless daemon for Linux
Summary(pl.UTF-8):	iwd - demon sieci bezprzewodowej dla Linuksa
Name:		iwd
Version:	0.7
Release:	1
License:	LGPL v2.1+
Group:		Networking/Daemons
Source0:	https://www.kernel.org/pub/linux/network/wireless/%{name}-%{version}.tar.xz
# Source0-md5:	dc26718ba7fb937864e70bbcd0b5843b
URL:		https://git.kernel.org/pub/scm/network/wireless/iwd.git
BuildRequires:	asciidoc
BuildRequires:	dbus-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,preun,postun):	systemd-units >= 38
Requires:	systemd-units >= 38
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

install -d $RPM_BUILD_ROOT%{_sysconfdir}/iwd
cp -p doc/main.conf $RPM_BUILD_ROOT%{_sysconfdir}/iwd/main.conf

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%systemd_post iwd.service

%preun
%systemd_preun iwd.service

%postun
%systemd_reload

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%dir %{_sysconfdir}/iwd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/iwd/main.conf
%attr(755,root,root) %{_bindir}/iwctl
%attr(755,root,root) %{_bindir}/iwmon
%attr(755,root,root) %{_libexecdir}/iwd
%{systemdunitdir}/iwd.service
%{_datadir}/dbus-1/system.d/iwd-dbus.conf
%{_datadir}/dbus-1/system-services/net.connman.iwd.service
%{_mandir}/man1/iwmon.1*
