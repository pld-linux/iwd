Summary:	iwd - wireless daemon for Linux
Summary(pl.UTF-8):	iwd - demon sieci bezprzewodowej dla Linuksa
Name:		iwd
Version:	1.1
Release:	1
License:	LGPL v2.1+
Group:		Networking/Daemons
Source0:	https://www.kernel.org/pub/linux/network/wireless/%{name}-%{version}.tar.xz
# Source0-md5:	158e2a7d813efbd5ee44171785789bd8
URL:		https://git.kernel.org/pub/scm/network/wireless/iwd.git
BuildRequires:	asciidoc
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	ell-devel >= 0.26
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,preun,postun):	systemd-units >= 38
Requires:	ell >= 0.26
Requires:	systemd-units >= 38
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wireless daemon for Linux.

%description -l pl.UTF-8
Demon sieci bezprzewodowej dla Linuksa.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-docs \
	--enable-external-ell \
	--disable-silent-rules \
	--with-systemd-unitdir=%{systemdunitdir}

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/iwd

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
%attr(755,root,root) %{_bindir}/iwctl
%attr(755,root,root) %{_bindir}/iwmon
%attr(755,root,root) %{_libexecdir}/iwd
/lib/systemd/network/80-iwd.link
%{systemdunitdir}/iwd.service
%{_datadir}/dbus-1/system.d/iwd-dbus.conf
%{_datadir}/dbus-1/system-services/net.connman.iwd.service
%{_mandir}/man1/iwctl.1*
%{_mandir}/man1/iwmon.1*
%{_mandir}/man5/iwd.config.5*
%{_mandir}/man5/iwd.network.5*
%{_mandir}/man7/iwd.debug.7*
%{_mandir}/man8/iwd.8*
/usr/lib/modules-load.d/pkcs8.conf
