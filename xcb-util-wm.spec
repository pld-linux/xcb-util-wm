Summary:	XCB util-wm module
Summary(pl.UTF-8):	Moduł XCB util-wm
Name:		xcb-util-wm
Version:	0.4.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	87b19a1cd7bfcb65a24e36c300e03129
URL:		http://xcb.freedesktop.org/XcbUtil/
BuildRequires:	gperf
BuildRequires:	libxcb-devel >= 1.4
BuildRequires:	m4
BuildRequires:	pkgconfig
BuildRequires:	xcb-proto >= 1.6
BuildRequires:	xorg-util-util-macros >= 1.16.0
Requires:	libxcb >= 1.4
Conflicts:	xcb-util < 0.3.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

XCB util-wm module provides the following libraries:
- ewmh: Both client and window-manager helpers for EWMH.
- icccm: Both client and window-manager helpers for ICCCM.

%description -l pl.UTF-8
xcb-util udostępnia wiele bibliotek opartych powyżej libxcb (głównej
biblioteki protokołu X) oraz trochę bibliotek rozszerzeń. Te
eksperymentalne biblioteki udostępniają wygodne funkcje i interfejsy
czyniące surowy protokół X bardziej używalnym. Niektóre biblioteki
udostępniają także kod kliencki nie będący ściśle częścią protokołu X,
ale tradycyjnie dostarczany przez Xlib.

Moduł XCB util-wm udostępnia następującą biliotekę:
- ewmh: funkcje pomocnicze dla klientów i zarządców okien do EWMH.
- icccm: funkcje pomocnicze dla klientów i zarządców okien do ICCCM.

%package devel
Summary:	Header files for XCB util-wm libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek XCB util-wm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxcb-devel >= 1.4
Conflicts:	xcb-util < 0.3.8

%description devel
Header files for XCB util-wm libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek XCB util-wm.

%package static
Summary:	Static XCB util-wm libraries
Summary(pl.UTF-8):	Statyczne biblioteki XCB util-wm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XCB util-wm libraries.

%description static -l pl.UTF-8
Statyczne biblioteki XCB util-wm.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libxcb-icccm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-icccm.so.4
%attr(755,root,root) %{_libdir}/libxcb-ewmh.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-ewmh.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxcb-ewmh.so
%attr(755,root,root) %{_libdir}/libxcb-icccm.so
%{_libdir}/libxcb-ewmh.la
%{_libdir}/libxcb-icccm.la
%{_includedir}/xcb/xcb_ewmh.h
%{_includedir}/xcb/xcb_icccm.h
%{_pkgconfigdir}/xcb-ewmh.pc
%{_pkgconfigdir}/xcb-icccm.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxcb-ewmh.a
%{_libdir}/libxcb-icccm.a
